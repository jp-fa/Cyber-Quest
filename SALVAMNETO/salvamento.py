"""
salvamento.py - Persistência do CyberQuest: O Protocolo ORÁCULO
Responsável: Integrante 4 (Sistemas e Persistência)

O QUE ESTE MÓDULO FAZ
    Cria o estado inicial do jogo, salva o progresso em JSON, carrega o
    progresso e apaga o progresso. Não tem história, menus nem regras de jogo.

FUNÇÕES (nomes combinados no roteiro)
    criar_estado_inicial()      -> dict   estado de uma partida nova
    salvar_jogo(estado_jogo)    -> bool   True se salvou, False se deu erro
    carregar_jogo()             -> (estado_jogo, None)  se deu certo
                                   (None, "mensagem")   se deu errado
    excluir_progresso()         -> bool   True se apagou o save, False se não havia

REGRA DO SALVAMENTO AUTOMÁTICO: "mudou o estado, salvou"
    salvar_jogo NÃO roda sozinha. Quem chama é o main.py (integrante 3),
    logo depois de cada mudança relevante no estado_jogo:

    | Evento                            | Quem altera o estado |
    |-----------------------------------|----------------------|
    | Entrar ou sair de um ambiente     | ambientes.py         |
    | Abordar um personagem             | personagens.py       |
    | Registrar escolha de confiança    | personagens.py       |
    | Encontrar ou entregar documento   | investigacao.py      |
    | Avançar capítulo                  | historia.py          |
    | Registrar decisão final           | historia.py          |

    Exemplo de uso no main.py:

        if ambientes.entrar_ambiente(estado_jogo, "Laboratório"):
            salvamento.salvar_jogo(estado_jogo)

    Todos os módulos usam o MESMO objeto estado_jogo (nunca uma cópia).
"""

import json
import os

# A pasta "dados" fica ao lado deste arquivo, não importa de onde o jogo é executado.
PASTA_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados")
ARQUIVO = os.path.join(PASTA_DADOS, "progresso.json")
ARQUIVO_TEMPORARIO = ARQUIVO + ".tmp"

# Versão do formato do save. Se as chaves do estado_jogo mudarem, aumentar este
# número: saves antigos serão recusados com um aviso, em vez de quebrar o jogo.
VERSAO_SAVE = 1

# Chaves do estado_jogo (seção 11 do roteiro) e o tipo esperado de cada uma.
# "object" = aceita qualquer valor (o grupo ainda vai definir o formato).
TIPOS_CAMPOS = {
    "capitulo_atual": int,
    "ambiente_atual": (str, type(None)),
    "ambientes_visitados": list,
    "ambientes_estado": dict,
    "documentos_encontrados": list,
    "documentos_entregues": list,
    "personagens_abordados": dict,
    "confianca": dict,
    "escolhas_confianca": dict,
    "decisao_final": object,
    "final": object,
}
CAMPOS_OBRIGATORIOS = list(TIPOS_CAMPOS)


def criar_estado_inicial():
    """Devolve um estado_jogo novo, exatamente como no contrato do roteiro."""
    # Cada chamada cria dicionários e listas NOVOS (nada é compartilhado entre partidas).
    return {
        "capitulo_atual": 1,
        "ambiente_atual": None,
        "ambientes_visitados": [],
        "ambientes_estado": {},
        "documentos_encontrados": [],
        "documentos_entregues": [],
        # Chaves em TEXTO ("1", "2", "3"): o JSON só aceita texto como chave.
        "personagens_abordados": {
            "1": [],
            "2": [],
            "3": [],
        },
        "confianca": {
            "Helena": "neutra",
            "Karla": "neutra",
            "Dante": "neutra",
        },
        "escolhas_confianca": {
            "Helena": [],
            "Karla": [],
            "Dante": [],
        },
        "decisao_final": None,
        "final": None,
    }


def _validar_estado(estado):
    """
    Confere se o estado tem todas as chaves e os tipos certos.
    Devolve None se estiver tudo certo, ou um texto explicando o problema.
    Usada ao salvar (para não gravar lixo) e ao carregar (para não aceitar lixo).
    """
    if not isinstance(estado, dict):
        return "O estado do jogo precisa ser um dicionário."

    faltando = [campo for campo in CAMPOS_OBRIGATORIOS if campo not in estado]
    if faltando:
        return "O progresso está incompleto. Faltam os campos: " + ", ".join(faltando)

    for campo, tipo in TIPOS_CAMPOS.items():
        if not isinstance(estado[campo], tipo):
            return f"O campo '{campo}' tem um tipo inválido."

    if estado["capitulo_atual"] not in (1, 2, 3):
        return "O capítulo salvo é inválido."

    return None


def _remover_se_existir(caminho):
    """Apaga o arquivo só se ele existir. Devolve True se apagou."""
    if not os.path.exists(caminho):
        return False
    try:
        os.remove(caminho)
        return True
    except OSError:
        return False


def salvar_jogo(estado_jogo):
    """Grava o estado em dados/progresso.json. Devolve True ou False."""
    # 1) Valida ANTES de gravar: um estado ruim nunca sobrescreve um save bom.
    problema = _validar_estado(estado_jogo)
    if problema:
        print(f"Não foi possível salvar o jogo: {problema}")
        return False

    # Envelope: guarda a versão do formato junto com o estado.
    conteudo = {"versao": VERSAO_SAVE, "estado": estado_jogo}

    try:
        os.makedirs(PASTA_DADOS, exist_ok=True)  # cria "dados" se não existir

        # 2) Escreve tudo em um arquivo temporário.
        with open(ARQUIVO_TEMPORARIO, "w", encoding="utf-8") as arquivo:
            json.dump(conteudo, arquivo, ensure_ascii=False, indent=2)
            arquivo.flush()
            os.fsync(arquivo.fileno())  # garante que foi para o disco

        # 3) Só depois troca o temporário pelo definitivo. os.replace é "tudo ou
        # nada": se o programa cair antes desta linha, o save antigo continua intacto.
        os.replace(ARQUIVO_TEMPORARIO, ARQUIVO)
        return True

    except (OSError, TypeError) as erro:
        # OSError: disco/permissão. TypeError: algo que o JSON não aceita (ex.: set).
        print(f"Não foi possível salvar o jogo: {erro}")
        _remover_se_existir(ARQUIVO_TEMPORARIO)
        return False


def carregar_jogo():
    """
    Lê o save e devolve uma tupla (estado_jogo, mensagem_de_erro):
      - deu certo:  (estado_jogo, None)
      - deu errado: (None, "texto explicando o problema")
    """
    if not os.path.exists(ARQUIVO):
        return None, "Nenhum jogo salvo foi encontrado."

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            conteudo = json.load(arquivo)
    except json.JSONDecodeError:
        return None, "O arquivo de save está corrompido."
    except OSError as erro:
        return None, f"Não foi possível abrir o save: {erro}"

    if not isinstance(conteudo, dict) or "estado" not in conteudo:
        return None, "O arquivo de save não tem o formato esperado."

    if conteudo.get("versao") != VERSAO_SAVE:
        return None, "Este save é de uma versão incompatível do jogo."

    estado = conteudo["estado"]
    problema = _validar_estado(estado)
    if problema:
        return None, problema

    return estado, None


def excluir_progresso():
    """Apaga o save (se existir). Devolve True se apagou, False se não havia save."""
    apagou = _remover_se_existir(ARQUIVO)
    _remover_se_existir(ARQUIVO_TEMPORARIO)  # sobra de uma gravação interrompida
    return apagou

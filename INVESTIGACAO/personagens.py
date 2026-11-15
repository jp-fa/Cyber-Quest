"""
personagens.py - Personagens do CyberQuest: O Protocolo ORÁCULO

O QUE ESTE MÓDULO FAZ
    - Cadastro dos personagens (dados fixos).
    - Consulta e exibição de personagens.
    - Abordagem única por capítulo.
    - Confiança NUMÉRICA (0 a 100) e histórico de alterações, com motivo.

REGRA DE OURO: nenhum dado da partida fica guardado neste arquivo.
    Abordagens, confiança e histórico vivem em estado_jogo:
        estado_jogo["personagens_abordados"]   {"1": ["karla"], "2": [], "3": []}
        estado_jogo["confianca"]               {"helena": 30, "karla": 50, ...}
        estado_jogo["escolhas_confianca"]      {"karla": [ {registro}, ... ], ...}

CONVENÇÕES
    - Ids de personagem SEMPRE em minúsculas: "alex", "helena", "karla", "dante",
      "oraculo". Se vier "ORÁCULO" ou " Karla ", o módulo normaliza sozinho.
    - O capítulo é um número inteiro (1, 2 ou 3). Nas chaves do estado vira texto
      ("1", "2", "3") porque o JSON só aceita texto como chave.
    - As funções que alteram o estado NÃO usam print(): devolvem um resultado.
      Quem quiser saber o MOTIVO de uma recusa chama as funções motivo_bloqueio_*
      (devolvem um texto, ou None se estiver tudo certo).
    - Quem chama salvamento.salvar_jogo(estado_jogo) depois é o main.py.

FUNÇÕES PÚBLICAS (resumo)
    Cadastro/exibição:
        obter_personagem(personagem)                    -> dict ou None
        listar_personagens()                            -> imprime e devolve lista de dicts
        exibir_personagem(estado_jogo, personagem)      -> imprime; True/False
        consultar_personagem(estado_jogo, personagem)   -> igual a exibir_personagem
    Abordagem:
        abordar_personagem(estado_jogo, personagem, capitulo=None)             -> bool
        verificar_personagem_abordado(estado_jogo, personagem, capitulo=None)  -> bool
        motivo_bloqueio_abordagem(estado_jogo, personagem, capitulo=None)      -> texto ou None
    Confiança:
        alterar_confianca(estado_jogo, personagem, valor, capitulo=None, motivo=None) -> registro (dict) ou None
        registrar_escolha_confianca(estado_jogo, personagem, escolha, capitulo=None, motivo=None)
                                                        -> registro (dict) ou None
        consultar_confianca(estado_jogo, personagem)    -> {"id","nome","pontos","nivel"} ou None
        obter_nivel_confianca(estado_jogo, personagem)  -> "alta" | "neutra" | "baixa" | None
        obter_historico_confianca(estado_jogo, personagem) -> lista de registros ou None
        motivo_bloqueio_confianca(estado_jogo, personagem, valor, capitulo=None) -> texto ou None
        exibir_confianca / consultar_historico_confianca -> imprimem; True/False
"""

import unicodedata

# ==========================================
# CADASTRO DOS PERSONAGENS (dados fixos)
# ==========================================

personagens = {
    "alex": {
        "nome": "Alex",
        "cargo": "Hacker",
        "idade": 28
    },
    "helena": {
        "nome": "Helena Voss",
        "cargo": "Diretora da NEXUS",
        "idade": 30
    },
    "karla": {
        "nome": "Dra. Karla",
        "cargo": "Cientista",
        "idade": 32
    },
    "dante": {
        "nome": "Dante Moreau",
        "cargo": "Aliado",
        "idade": 29
    },
    "oraculo": {
        "nome": "ORÁCULO",
        "cargo": "Inteligência Artificial",
        "idade": 3
    }
}

# ==========================================
# REGRAS DA CONFIANÇA (valores propostos, fáceis de ajustar)
# ==========================================

CONFIANCA_MINIMA = 0
CONFIANCA_MAXIMA = 100

LIMITE_ALTA = 70    # 70 ou mais        -> "alta"
LIMITE_BAIXA = 40   # menos que 40      -> "baixa"; de 40 a 69 -> "neutra"

IMPACTO_POSITIVO = 20   # usado por registrar_escolha_confianca("positiva")
IMPACTO_NEGATIVO = -20  # usado por registrar_escolha_confianca("negativa")

CAPITULOS_VALIDOS = (1, 2, 3)


# ==========================================
# FUNÇÕES INTERNAS DE APOIO
# ==========================================

def _normalizar_id(personagem):
    """Devolve o id em minúsculas, sem espaços nas pontas e sem acentos
    ("ORÁCULO" -> "oraculo"). Devolve None se não for texto."""
    if not isinstance(personagem, str):
        return None
    texto = unicodedata.normalize("NFD", personagem.strip().lower())
    return "".join(letra for letra in texto if unicodedata.category(letra) != "Mn")


def _resolver_capitulo(estado_jogo, capitulo):
    """Devolve o capítulo como número inteiro (1, 2 ou 3), ou None se inválido.
    Se capitulo vier None, usa o capítulo atual do estado."""
    if capitulo is None:
        capitulo = estado_jogo.get("capitulo_atual")
    if isinstance(capitulo, str) and capitulo.strip().isdigit():
        capitulo = int(capitulo.strip())
    if isinstance(capitulo, bool) or capitulo not in CAPITULOS_VALIDOS:
        return None
    return capitulo


def _numero_valido(valor):
    return isinstance(valor, (int, float)) and not isinstance(valor, bool)


def _nivel_por_pontos(pontos):
    if pontos >= LIMITE_ALTA:
        return "alta"
    if pontos < LIMITE_BAIXA:
        return "baixa"
    return "neutra"


def validar_estado_jogo(estado_jogo):
    """True se o estado tem o que este módulo precisa."""
    if not isinstance(estado_jogo, dict):
        return False

    for campo in ("capitulo_atual", "personagens_abordados", "confianca", "escolhas_confianca"):
        if campo not in estado_jogo:
            return False

    for campo in ("personagens_abordados", "confianca", "escolhas_confianca"):
        if not isinstance(estado_jogo[campo], dict):
            return False

    # Se a lista de algum capítulo existir, precisa ser lista.
    for lista in estado_jogo["personagens_abordados"].values():
        if not isinstance(lista, list):
            return False

    return True


# ==========================================
# CADASTRO: CONSULTA E EXIBIÇÃO
# ==========================================

def obter_personagem(personagem):
    """Devolve uma CÓPIA dos dados do personagem (com o campo "id"), ou None."""
    id_personagem = _normalizar_id(personagem)
    if id_personagem not in personagens:
        return None
    dados = dict(personagens[id_personagem])
    dados["id"] = id_personagem
    return dados


def listar_personagens():
    """Imprime a lista de personagens e devolve [{"id": ..., "nome": ...}, ...]."""
    lista = [{"id": id_, "nome": dados["nome"]} for id_, dados in personagens.items()]

    print("\n======= PERSONAGENS =======")
    for item in lista:
        print(f"- {item['nome']}")
    print("===========================")

    return lista


def exibir_personagem(estado_jogo, personagem):
    """Imprime a ficha do personagem (com a confiança atual). Devolve True/False."""
    dados = obter_personagem(personagem)
    if dados is None:
        print("Personagem não encontrado!")
        return False

    if not validar_estado_jogo(estado_jogo):
        print("Estado do jogo inválido!")
        return False

    print("\n======= INFORMAÇÕES DO PERSONAGEM =======")
    print(f"Nome: {dados['nome']}")
    print(f"Cargo: {dados['cargo']}")
    print(f"Idade: {dados['idade']}")

    if dados["id"] == "alex":
        print("Confiança: Não se aplica (protagonista)")
    else:
        confianca = consultar_confianca(estado_jogo, dados["id"])
        if confianca is None:
            print("Confiança: Não disponível")
        else:
            print(f"Confiança: {confianca['pontos']}/100 ({confianca['nivel'].title()})")

    print("=========================================")
    return True


def consultar_personagem(estado_jogo, personagem):
    """Consulta uma ficha de personagem (mesmo que exibir_personagem)."""
    return exibir_personagem(estado_jogo, personagem)


# ==========================================
# ABORDAGEM ÚNICA POR CAPÍTULO
# ==========================================

def motivo_bloqueio_abordagem(estado_jogo, personagem, capitulo=None):
    """Devolve o texto do motivo pelo qual NÃO dá para abordar, ou None se pode."""
    if not validar_estado_jogo(estado_jogo):
        return "Estado do jogo inválido."

    id_personagem = _normalizar_id(personagem)
    if id_personagem not in personagens:
        return "Personagem não encontrado."

    if id_personagem == "alex":
        return "Alex é o protagonista e não pode ser abordado."

    capitulo = _resolver_capitulo(estado_jogo, capitulo)
    if capitulo is None:
        return "Capítulo inválido."

    abordados = estado_jogo["personagens_abordados"].get(str(capitulo), [])
    if id_personagem in abordados:
        return "Você já abordou este personagem neste capítulo."

    return None


def abordar_personagem(estado_jogo, personagem, capitulo=None):
    """Registra a abordagem. Devolve True se registrou, False se foi recusada.
    Cada personagem só pode ser abordado UMA vez por capítulo."""
    if motivo_bloqueio_abordagem(estado_jogo, personagem, capitulo) is not None:
        return False

    id_personagem = _normalizar_id(personagem)
    capitulo = _resolver_capitulo(estado_jogo, capitulo)

    # A chave do capítulo é TEXTO ("1"); setdefault cria a lista se ainda não existir.
    estado_jogo["personagens_abordados"].setdefault(str(capitulo), []).append(id_personagem)
    return True


def verificar_personagem_abordado(estado_jogo, personagem, capitulo=None):
    """True se o personagem já foi abordado no capítulo (padrão: o capítulo atual)."""
    if not validar_estado_jogo(estado_jogo):
        return False

    id_personagem = _normalizar_id(personagem)
    capitulo = _resolver_capitulo(estado_jogo, capitulo)
    if capitulo is None:
        return False

    return id_personagem in estado_jogo["personagens_abordados"].get(str(capitulo), [])


# ==========================================
# CONFIANÇA (0 a 100)
# ==========================================

def _id_com_confianca(estado_jogo, personagem):
    """Devolve o id normalizado se o personagem tem confiança no estado, senão None."""
    id_personagem = _normalizar_id(personagem)
    if id_personagem in personagens and id_personagem != "alex":
        if id_personagem in estado_jogo["confianca"]:
            return id_personagem
    return None


def motivo_bloqueio_confianca(estado_jogo, personagem, valor, capitulo=None):
    """Devolve o texto do motivo pelo qual NÃO dá para alterar a confiança, ou None."""
    if not validar_estado_jogo(estado_jogo):
        return "Estado do jogo inválido."

    id_personagem = _normalizar_id(personagem)
    if id_personagem not in personagens:
        return "Personagem não encontrado."

    if id_personagem == "alex":
        return "A confiança de Alex não pode ser alterada."

    if _id_com_confianca(estado_jogo, id_personagem) is None:
        return "Este personagem não possui confiança no estado do jogo."

    if not _numero_valido(estado_jogo["confianca"][id_personagem]):
        return "A confiança deste personagem no estado do jogo não é numérica."

    if not _numero_valido(valor):
        return "O valor da alteração precisa ser numérico."

    if _resolver_capitulo(estado_jogo, capitulo) is None:
        return "Capítulo inválido."

    return None


def _aplicar_alteracao(estado_jogo, id_personagem, valor, capitulo, motivo, extras=None):
    """Altera a confiança (com limite de 0 a 100) e grava o registro no histórico."""
    anterior = estado_jogo["confianca"][id_personagem]
    nova = max(CONFIANCA_MINIMA, min(CONFIANCA_MAXIMA, anterior + valor))
    nova = int(round(nova))

    estado_jogo["confianca"][id_personagem] = nova

    registro = {
        "capitulo": capitulo,
        "personagem": id_personagem,
        "valor": valor,
        "confianca_anterior": anterior,
        "confianca_atual": nova,
        "alteracao": nova - anterior,
        "motivo": motivo,
    }
    if extras:
        registro.update(extras)

    estado_jogo["escolhas_confianca"].setdefault(id_personagem, []).append(registro)
    return registro


def alterar_confianca(estado_jogo, personagem, valor, capitulo=None, motivo=None):
    """
    Soma 'valor' (positivo ou negativo) à confiança do personagem, mantendo o
    resultado entre 0 e 100, e registra a alteração (com o motivo) no histórico.
    Devolve o registro (dict) se deu certo, ou None se foi recusada.
    """
    if motivo_bloqueio_confianca(estado_jogo, personagem, valor, capitulo) is not None:
        return None

    id_personagem = _normalizar_id(personagem)
    capitulo = _resolver_capitulo(estado_jogo, capitulo)
    return _aplicar_alteracao(estado_jogo, id_personagem, valor, capitulo, motivo)


def registrar_escolha_confianca(estado_jogo, personagem, escolha, capitulo=None, motivo=None):
    """
    Atalho para as conversas: escolha "positiva" soma IMPACTO_POSITIVO,
    escolha "negativa" soma IMPACTO_NEGATIVO. Devolve o registro ou None.
    """
    if not isinstance(escolha, str):
        return None
    escolha = escolha.strip().lower()

    if escolha == "positiva":
        valor = IMPACTO_POSITIVO
    elif escolha == "negativa":
        valor = IMPACTO_NEGATIVO
    else:
        return None

    if motivo_bloqueio_confianca(estado_jogo, personagem, valor, capitulo) is not None:
        return None

    id_personagem = _normalizar_id(personagem)
    capitulo = _resolver_capitulo(estado_jogo, capitulo)
    if motivo is None:
        motivo = f"Escolha {escolha} do jogador"

    return _aplicar_alteracao(
        estado_jogo, id_personagem, valor, capitulo, motivo, extras={"escolha": escolha}
    )


def consultar_confianca(estado_jogo, personagem):
    """Devolve {"id", "nome", "pontos", "nivel"} ou None (personagem sem confiança)."""
    if not validar_estado_jogo(estado_jogo):
        return None

    id_personagem = _id_com_confianca(estado_jogo, personagem)
    if id_personagem is None:
        return None

    pontos = estado_jogo["confianca"][id_personagem]
    if not _numero_valido(pontos):
        return None

    return {
        "id": id_personagem,
        "nome": personagens[id_personagem]["nome"],
        "pontos": pontos,
        "nivel": _nivel_por_pontos(pontos),
    }


def obter_nivel_confianca(estado_jogo, personagem):
    """Devolve "alta", "neutra" ou "baixa" (ou None). Use esta função na história
    para variar diálogos, em vez de ler estado_jogo["confianca"] diretamente."""
    consulta = consultar_confianca(estado_jogo, personagem)
    if consulta is None:
        return None
    return consulta["nivel"]


def exibir_confianca(estado_jogo, personagem):
    """Imprime a confiança do personagem. Devolve True/False."""
    consulta = consultar_confianca(estado_jogo, personagem)
    if consulta is None:
        print("Este personagem não possui confiança.")
        return False

    print(f"\n======= CONFIANÇA: {consulta['nome']} =======")
    print(f"Pontuação: {consulta['pontos']}/100")
    print(f"Nível: {consulta['nivel'].title()}")

    if consulta["nivel"] == "alta":
        print("Este personagem demonstra maior confiança em Alex.")
    elif consulta["nivel"] == "neutra":
        print("A relação com Alex permanece equilibrada.")
    else:
        print("Este personagem demonstra pouca confiança em Alex.")

    print("=========================================")
    return True


# ==========================================
# HISTÓRICO DE CONFIANÇA
# ==========================================

def obter_historico_confianca(estado_jogo, personagem):
    """Devolve uma CÓPIA da lista de registros do personagem, ou None se inválido."""
    if not validar_estado_jogo(estado_jogo):
        return None

    id_personagem = _id_com_confianca(estado_jogo, personagem)
    if id_personagem is None:
        return None

    return [dict(registro) for registro in estado_jogo["escolhas_confianca"].get(id_personagem, [])]


def consultar_historico_confianca(estado_jogo, personagem):
    """Imprime o histórico de alterações. Devolve True/False."""
    historico = obter_historico_confianca(estado_jogo, personagem)
    if historico is None:
        print("Este personagem não possui histórico de confiança.")
        return False

    nome = personagens[_normalizar_id(personagem)]["nome"]
    print(f"\n======= HISTÓRICO DE CONFIANÇA: {nome} =======")

    if not historico:
        print("Nenhuma alteração de confiança registrada.")
        print("=========================================")
        return True

    for numero, registro in enumerate(historico, start=1):
        print(f"\n{numero}. Capítulo {registro.get('capitulo')}")
        print(f"   Alteração: {registro.get('alteracao', 0):+}")
        print(f"   Confiança: {registro.get('confianca_anterior')} -> {registro.get('confianca_atual')}")
        if registro.get("motivo"):
            print(f"   Motivo: {registro['motivo']}")

    print("\n=========================================")
    return True

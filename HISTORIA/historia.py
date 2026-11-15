"""CyberQuest — coordenador das narrativas dos capítulos 1, 2 e 3.

Arquivo principal da pasta HISTORIA. Os capítulos guardam as cenas,
e este arquivo mantém uma API única para o main.py e a interface.

- NÃO registrar abordagens aqui: personagens.py
- NÃO somar confiança aqui: personagens.py
- NÃO coletar ou entregar DOC01...DOC04 aqui: investigacao.py
- NÃO marcar visitas ou ações aqui: ambientes.py
- NÃO salvar JSON aqui: o main.py chama salvamento.py

Use a partir da raiz do repositório:
    from HISTORIA import historia
"""

from . import capitulo1, capitulo2, capitulo3


def obter_ambientes_capitulo(capitulo):
    """Lista os ambientes obrigatórios em cada capítulo."""
    if capitulo == 1:
        return ["Laboratório", "Sala de Segurança"]
    if capitulo == 2:
        return ["Sala de Planejamento"]
    if capitulo == 3:
        return ["Escritório de Dante"]
    return []


def pode_avancar_capitulo(estado_jogo):
    """Só autoriza avançar após sair de cada sala obrigatória."""
    if not isinstance(estado_jogo, dict):
        return False
    visitados = estado_jogo.get("ambientes_visitados")
    if not isinstance(visitados, list):
        return False
    obrigatorios = obter_ambientes_capitulo(estado_jogo.get("capitulo_atual"))
    return bool(obrigatorios) and all(sala in visitados for sala in obrigatorios)


def avancar_capitulo(estado_jogo):
    """Avança de 1 para 2 ou de 2 para 3. main.py faz autosave."""
    if not pode_avancar_capitulo(estado_jogo):
        return False
    capitulo = estado_jogo.get("capitulo_atual")
    if capitulo >= 3:
        return False
    estado_jogo["capitulo_atual"] = capitulo + 1
    return True


def abrir_capitulo(estado_jogo):
    """Retorna o texto de abertura do capítulo atual, ou None."""
    if not isinstance(estado_jogo, dict):
        return None
    capitulo = estado_jogo.get("capitulo_atual")
    if capitulo == 1:
        return capitulo1.texto_abertura()
    if capitulo == 2:
        return capitulo2.texto_abertura()
    if capitulo == 3:
        return capitulo3.texto_abertura()
    return None


def encerrar_capitulo(estado_jogo):
    """Valida visita e, no capítulo 3, a decisão final. Não avança sozinho."""
    if not isinstance(estado_jogo, dict):
        return {"sucesso": False, "texto": "Estado do jogo inválido."}
    if not pode_avancar_capitulo(estado_jogo):
        return {
            "sucesso": False,
            "texto": "Ainda existem ambientes obrigatórios para visitar. "
                     "Continue sua investigação antes de avançar."
        }
    capitulo = estado_jogo.get("capitulo_atual")
    if capitulo == 1:
        texto = capitulo1.texto_encerramento()
    elif capitulo == 2:
        texto = capitulo2.texto_encerramento(estado_jogo)
    elif capitulo == 3:
        if estado_jogo.get("decisao_final") is None or not estado_jogo.get("jogo_concluido"):
            return {"sucesso": False,
                    "texto": "Confronte Dante e registre o destino de ORÁCULO antes de encerrar."}
        texto = capitulo3.texto_encerramento()
    else:
        return {"sucesso": False, "texto": "Capítulo inválido."}
    return {"sucesso": True, "texto": texto}


def obter_narrativa_acao(ambiente, acao):
    """Retorna o texto da ação de qualquer capítulo, ou None."""
    if ambiente in ("Laboratório", "Sala de Segurança"):
        return capitulo1.obter_narrativa_acao_capitulo1(ambiente, acao)
    if ambiente == "Sala de Planejamento":
        return capitulo2.obter_narrativa_acao_capitulo2(ambiente, acao)
    if ambiente == "Escritório de Dante":
        return capitulo3.obter_narrativa_acao_capitulo3(ambiente, acao)
    return None


# Função auxiliar COMPARTILHADA entre as escolhas de Helena e Dante.
def _registrar_escolha_narrativa(estado_jogo, capitulo, personagem, etapa, escolha,
                                 etapas_validas, reacao):
    """Grava apenas a decisão narrativa. NÃO altera confiança nem abordagem."""
    if not isinstance(estado_jogo, dict) or estado_jogo.get("capitulo_atual") != capitulo:
        return {"sucesso": False, "mensagem": "Capítulo ou estado inválido."}
    if not isinstance(estado_jogo.get("decisoes"), dict):
        return {"sucesso": False, "mensagem": "Dicionário de decisões inválido."}
    if etapa not in etapas_validas or reacao is None:
        return {"sucesso": False, "mensagem": "Etapa ou escolha inválida."}
    chave = f"{personagem}_{etapa}_capitulo_{capitulo}"
    if chave in estado_jogo["decisoes"]:
        return {"sucesso": False, "mensagem": "Esta escolha já foi registrada."}
    posicao = etapas_validas.index(etapa)
    if posicao > 0:
        chave_anterior = f"{personagem}_{etapas_validas[posicao-1]}_capitulo_{capitulo}"
        if chave_anterior not in estado_jogo["decisoes"]:
            return {"sucesso": False, "mensagem": "Conclua a escolha anterior primeiro."}
    estado_jogo["decisoes"][chave] = {
        "capitulo": capitulo, "personagem": personagem, "etapa": etapa,
        "opcao": str(escolha).strip(), "identificador": reacao["decisao"],
        "classificacao": reacao["classificacao"]
    }
    return {"sucesso": True, **reacao}


# Reexportar as funções antigas: outros módulos podem continuar chamando
# historia.apresentar_doc03(), historia.registrar_decisao_dante(), etc.
# Assim, a reorganização não exige renomear as funções existentes no main.py.
from .capitulo1 import (
    obter_narrativa_acao_capitulo1,
    apresentar_doc01,
    apresentar_doc02,
    apresentar_conversa_karla,
    apresentar_reacao_karla,
    registrar_decisao_karla,
    apresentar_conversa_oraculo,
)
from .capitulo2 import (
    ACOES_CAPITULO_2,
    obter_narrativa_acao_capitulo2,
    apresentar_doc03,
    apresentar_conversa_helena,
    apresentar_reacao_helena,
    registrar_decisao_helena,
    obter_reacao_helena_documentos,
)
from .capitulo3 import (
    ACOES_CAPITULO_3,
    obter_narrativa_acao_capitulo3,
    apresentar_doc04,
    apresentar_conversa_dante,
    apresentar_reacao_dante,
    registrar_decisao_dante,
    obter_contradicoes_dante,
    apresentar_confronto_dante,
    registrar_confronto_dante,
    apresentar_persuasao_oraculo,
    registrar_decisao_final,
    apresentar_final,
)
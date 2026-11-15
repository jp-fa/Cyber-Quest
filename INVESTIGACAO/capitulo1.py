
"""
capitulo1.py
CyberQuest: O Protocolo ORÁCULO

Responsabilidade:
- Controlar as mecânicas de interação do Capítulo 1.
- Registrar a abordagem de Karla e ORÁCULO.
- Atualizar a confiança de Karla.
- Encontrar e consultar DOC01 e DOC02.

Os diálogos e textos narrativos pertencem a HISTORIA/capitulo1.py.
"""

from INVESTIGACAO.personagens import (
    abordar_personagem,
    verificar_personagem_abordado,
    motivo_bloqueio_abordagem,
    motivo_bloqueio_confianca,
    registrar_escolha_confianca
)

from INVESTIGACAO.investigacao import (
    encontrar_documento,
    consultar_documento
)

from HISTORIA import capitulo1 as historia_capitulo1


# ==========================================
# INTERAÇÃO COM KARLA
# ==========================================

def interagir_com_karla(estado_jogo, escolha):
    """
    Registra a decisão narrativa de Alex com Karla,
    sua abordagem e a alteração de confiança.

    A escolha deve ser "1" ou "2".
    Retorna um dicionário com o resultado.
    """

    if not isinstance(estado_jogo, dict):
        return {"sucesso": False, "mensagem": "Estado do jogo inválido."}

    if estado_jogo.get("capitulo_atual") != 1:
        return {"sucesso": False, "mensagem": "Esta interação pertence ao Capítulo 1."}

    if motivo_bloqueio_abordagem(estado_jogo, "karla") is not None:
        return {
            "sucesso": False,
            "mensagem": motivo_bloqueio_abordagem(estado_jogo, "karla")
        }

    if motivo_bloqueio_confianca(
        estado_jogo, "karla", 20 if str(escolha).strip() == "1" else -20
    ) is not None:
        return {"sucesso": False, "mensagem": "Não foi possível atualizar a confiança de Karla."}

    # Registra a escolha narrativa em HISTORIA.
    resultado = historia_capitulo1.registrar_decisao_karla(
        estado_jogo, escolha
    )

    if not resultado.get("sucesso"):
        return resultado

    # Registra a abordagem.
    if not abordar_personagem(estado_jogo, "karla"):
        return {"sucesso": False, "mensagem": "Não foi possível registrar a abordagem de Karla."}

    # Atualiza a confiança conforme a escolha.
    if registrar_escolha_confianca(
        estado_jogo,
        "karla",
        resultado["classificacao"],
        motivo="Decisão de Alex durante a conversa com Karla"
    ) is None:
        return {"sucesso": False, "mensagem": "Não foi possível atualizar a confiança de Karla."}

    return resultado


# ==========================================
# INTERAÇÃO COM ORÁCULO
# ==========================================

def registrar_conversa_oraculo(estado_jogo):
    """
    Registra que Alex conversou com ORÁCULO no Capítulo 1.

    O diálogo é fornecido por HISTORIA/capitulo1.py.
    ORÁCULO só pode ser abordado uma vez neste capítulo.
    """

    if not isinstance(estado_jogo, dict):
        return False

    if estado_jogo.get("capitulo_atual") != 1:
        return False

    if verificar_personagem_abordado(estado_jogo, "oraculo"):
        return False

    return abordar_personagem(estado_jogo, "oraculo")


# ==========================================
# DOCUMENTOS DO CAPÍTULO 1
# ==========================================

def encontrar_doc01(estado_jogo):
    """Registra o DOC01 no inventário."""

    if not isinstance(estado_jogo, dict):
        return False

    if estado_jogo.get("capitulo_atual") != 1:
        return False

    return encontrar_documento(estado_jogo, "DOC01")


def consultar_doc01(estado_jogo):
    """Devolve os dados do DOC01, caso já tenha sido encontrado."""

    if not isinstance(estado_jogo, dict):
        return None

    if estado_jogo.get("capitulo_atual") != 1:
        return None

    return consultar_documento(estado_jogo, "DOC01")


def encontrar_doc02(estado_jogo):
    """Registra o DOC02 no inventário."""

    if not isinstance(estado_jogo, dict):
        return False

    if estado_jogo.get("capitulo_atual") != 1:
        return False

    return encontrar_documento(estado_jogo, "DOC02")


def consultar_doc02(estado_jogo):
    """Devolve os dados do DOC02, caso já tenha sido encontrado."""

    if not isinstance(estado_jogo, dict):
        return None

    if estado_jogo.get("capitulo_atual") != 1:
        return None

    return consultar_documento(estado_jogo, "DOC02")
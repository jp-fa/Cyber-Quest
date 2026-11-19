
"""
capitulo2.py
CyberQuest: O Protocolo ORÁCULO

Responsabilidade:
- Controlar as mecânicas de interação do Capítulo 2.
- Registrar as decisões de Alex com Helena.
- Registrar a abordagem única de Helena.
- Atualizar a confiança de Helena.
- Encontrar e consultar DOC03.

Os diálogos e textos narrativos pertencem a HISTORIA/capitulo2.py.
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

from HISTORIA import capitulo2 as historia_capitulo2


# ==========================================
# INTERAÇÃO COM HELENA
# ==========================================

def interagir_com_helena(estado_jogo, etapa, escolha):
    """
    Registra uma decisão de Alex durante a conversa com Helena.

    Etapas:
    - progresso
    - responsabilidade

    Cada etapa aceita as escolhas "1" ou "2".
    A abordagem de Helena é registrada somente na primeira etapa.
    """

    if not isinstance(estado_jogo, dict):
        return {"sucesso": False, "mensagem": "Estado do jogo inválido."}

    if estado_jogo.get("capitulo_atual") != 2:
        return {"sucesso": False, "mensagem": "Esta interação pertence ao Capítulo 2."}

    etapa = str(etapa).strip().lower()
    escolha = str(escolha).strip()

    if etapa not in ("progresso", "responsabilidade"):
        return {"sucesso": False, "mensagem": "Etapa inválida."}

    if escolha not in ("1", "2"):
        return {"sucesso": False, "mensagem": "Escolha inválida. Selecione 1 ou 2."}

    ja_abordada = verificar_personagem_abordado(
        estado_jogo, "helena"
    )

    # A primeira etapa exige que Helena ainda não tenha sido abordada.
    if etapa == "progresso":
        motivo = motivo_bloqueio_abordagem(estado_jogo, "helena")
        if motivo is not None:
            return {"sucesso": False, "mensagem": motivo}

    # A segunda etapa exige que a primeira abordagem já tenha acontecido.
    elif etapa == "responsabilidade":
        if not ja_abordada:
            return {
                "sucesso": False,
                "mensagem": "Registre primeiro a etapa de progresso."
            }

    # Verifica se a confiança pode ser alterada antes de registrar a decisão.
    impacto = 20 if escolha == "1" else -20

    motivo = motivo_bloqueio_confianca(
        estado_jogo, "helena", impacto
    )

    if motivo is not None:
        return {"sucesso": False, "mensagem": motivo}

    # Registra a decisão narrativa em HISTORIA.
    resultado = historia_capitulo2.registrar_decisao_helena(
        estado_jogo, etapa, escolha
    )

    if not resultado.get("sucesso"):
        return resultado

    # A abordagem é registrada apenas na primeira etapa.
    if etapa == "progresso":
        if not abordar_personagem(estado_jogo, "helena"):
            return {
                "sucesso": False,
                "mensagem": "Não foi possível registrar a abordagem de Helena."
            }

    # Atualiza a confiança com base na classificação da escolha.
    registro = registrar_escolha_confianca(
        estado_jogo,
        "helena",
        resultado["classificacao"],
        motivo=f"Decisão de Alex na etapa {etapa} da conversa com Helena"
    )

    if registro is None:
        return {
            "sucesso": False,
            "mensagem": "Não foi possível atualizar a confiança de Helena."
        }

    return resultado


# ==========================================
# DOCUMENTO DO CAPÍTULO 2
# ==========================================

def encontrar_doc03(estado_jogo):
    """Registra o DOC03 no inventário."""

    if not isinstance(estado_jogo, dict):
        return False

    if estado_jogo.get("capitulo_atual") != 2:
        return False

    return encontrar_documento(estado_jogo, "DOC03")


def consultar_doc03(estado_jogo):
    """Devolve os dados do DOC03, caso já tenha sido encontrado."""

    if not isinstance(estado_jogo, dict):
        return None

    if estado_jogo.get("capitulo_atual") != 2:
        return None

    return consultar_documento(estado_jogo, "DOC03")
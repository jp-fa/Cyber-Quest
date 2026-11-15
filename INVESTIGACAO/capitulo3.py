
"""
capitulo3.py
CyberQuest: O Protocolo ORÁCULO

Responsabilidade:
- Controlar as interações de investigação do Capítulo 3.
- Registrar a abordagem de Dante.
- Atualizar a confiança de Dante.
- Encontrar e consultar o DOC04.

O confronto, a persuasão de ORÁCULO e os finais
são responsabilidades de HISTORIA/capitulo3.py.
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

from HISTORIA import capitulo3 as historia_capitulo3


# ==========================================
# INTERAÇÃO COM DANTE
# ==========================================

def interagir_com_dante(estado_jogo, etapa, escolha):
    """
    Registra as decisões de Alex durante a conversa com Dante.

    Etapas:
    - alianca
    - intencoes

    Cada etapa aceita as escolhas 1 ou 2.

    Dante só pode ser abordado uma vez no Capítulo 3.
    A confiança é atualizada em cada decisão.
    """

    # Validar o estado do jogo.
    if not isinstance(estado_jogo, dict):
        return {
            "sucesso": False,
            "mensagem": "Estado do jogo inválido."
        }

    # Verificar capítulo atual.
    if estado_jogo.get("capitulo_atual") != 3:
        return {
            "sucesso": False,
            "mensagem": "Esta interação pertence ao Capítulo 3."
        }

    # Normalizar os valores recebidos.
    etapa = str(etapa).strip().lower()
    escolha = str(escolha).strip()

    # Validar etapa.
    if etapa not in ("alianca", "intencoes"):
        return {
            "sucesso": False,
            "mensagem": "Etapa inválida."
        }

    # Validar escolha.
    if escolha not in ("1", "2"):
        return {
            "sucesso": False,
            "mensagem": "Escolha inválida. Selecione 1 ou 2."
        }

    # Verificar se Dante já foi abordado neste capítulo.
    ja_abordado = verificar_personagem_abordado(
        estado_jogo,
        "dante",
        capitulo=3
    )

    # A primeira etapa só pode acontecer uma vez.
    if etapa == "alianca":

        motivo = motivo_bloqueio_abordagem(
            estado_jogo,
            "dante",
            capitulo=3
        )

        if motivo is not None:
            return {
                "sucesso": False,
                "mensagem": motivo
            }

    # A segunda etapa exige que a primeira tenha acontecido.
    elif etapa == "intencoes":

        if not ja_abordado:
            return {
                "sucesso": False,
                "mensagem": "Registre primeiro a etapa de aliança."
            }

    # Determinar o impacto da escolha.
    impacto = 20 if escolha == "1" else -20

    # Verificar se a alteração de confiança é válida.
    # Os limites de 0 a 100 são aplicados em personagens.py.
    motivo = motivo_bloqueio_confianca(
        estado_jogo,
        "dante",
        impacto,
        capitulo=3
    )

    if motivo is not None:
        return {
            "sucesso": False,
            "mensagem": motivo
        }

    # Registrar a decisão narrativa no módulo HISTORIA.
    resultado = historia_capitulo3.registrar_decisao_dante(
        estado_jogo,
        etapa,
        escolha
    )

    # Verificar se a História aceitou a decisão.
    if not isinstance(resultado, dict):
        return {
            "sucesso": False,
            "mensagem": "A História retornou um resultado inválido."
        }

    if not resultado.get("sucesso"):
        return resultado

    # Registrar a abordagem de Dante na primeira etapa.
    if etapa == "alianca":

        sucesso_abordagem = abordar_personagem(
            estado_jogo,
            "dante",
            capitulo=3
        )

        if not sucesso_abordagem:
            return {
                "sucesso": False,
                "mensagem": "Não foi possível registrar a abordagem de Dante."
            }

    # Atualizar a confiança conforme a classificação
    # retornada pelo módulo HISTORIA.
    registro = registrar_escolha_confianca(
        estado_jogo,
        "dante",
        resultado["classificacao"],
        capitulo=3,
        motivo=(
            f"Decisão de Alex na etapa {etapa} "
            "da conversa com Dante."
        )
    )

    if registro is None:
        return {
            "sucesso": False,
            "mensagem": "Não foi possível atualizar a confiança de Dante."
        }

    return resultado


# ==========================================
# DOCUMENTO DOC04
# ==========================================

def encontrar_doc04(estado_jogo):
    """
    Registra o DOC04 no inventário.

    O documento só pode ser encontrado no Capítulo 3.
    A verificação de duplicidade pertence a investigacao.py.
    """

    if not isinstance(estado_jogo, dict):
        return False

    if estado_jogo.get("capitulo_atual") != 3:
        return False

    return encontrar_documento(
        estado_jogo,
        "DOC04"
    )


def consultar_doc04(estado_jogo):
    """
    Consulta o DOC04 caso ele já tenha sido encontrado.
    """

    if not isinstance(estado_jogo, dict):
        return None

    if estado_jogo.get("capitulo_atual") != 3:
        return None

    return consultar_documento(
        estado_jogo,
        "DOC04"
    )
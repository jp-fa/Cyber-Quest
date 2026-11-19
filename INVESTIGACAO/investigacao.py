"""
investigacao.py
CyberQuest: O Protocolo ORÁCULO

Responsabilidade:
- Cadastrar documentos.
- Registrar documentos encontrados.
- Consultar inventário.
- Entregar documentos.
- Consultar histórico de entregas.
"""

from INVESTIGACAO.personagens import personagens
from SALVAMENTO.ambientes import obter_personagens_ambiente


# ============================================================
# CADASTRO DOS DOCUMENTOS
# ============================================================

DOCUMENTOS = {

    "DOC01": {
        "nome": "Relatório ORÁCULO",
        "autor": "Não identificado",
        "classificacao": "Confidencial",
        "ambiente": "Laboratório"
    },

    "DOC02": {
        "nome": "Registro de Acessos",
        "autor": "Não identificado",
        "classificacao": "Confidencial",
        "ambiente": "Sala de Segurança"
    },

    "DOC03": {
        "nome": "Memorando Estratégico NEXUS",
        "autor": "Helena Voss",
        "classificacao": "Restrito",
        "ambiente": "Sala de Planejamento"
    },

    "DOC04": {
        "nome": "Documento Secreto",
        "autor": "ORÁCULO",
        "classificacao": "Ultrassecreto",
        "ambiente": "Escritório de Dante"
    }
}


# ============================================================
# VALIDAR ESTADO
# ============================================================

def validar_estado_jogo(estado_jogo):
    """Verifica se o estado possui as estruturas necessárias."""

    if not isinstance(estado_jogo, dict):
        return False

    campos = [
        "documentos_encontrados",
        "documentos_entregues"
    ]

    for campo in campos:
        if campo not in estado_jogo:
            return False

    if not isinstance(
        estado_jogo["documentos_encontrados"],
        list
    ):
        return False

    if not isinstance(
        estado_jogo["documentos_entregues"],
        list
    ):
        return False

    return True


# ============================================================
# LISTAR DOCUMENTOS DO AMBIENTE
# ============================================================

def listar_documentos(nome_ambiente):
    """Retorna os documentos cadastrados em determinado ambiente."""

    documentos_ambiente = []

    for codigo, dados in DOCUMENTOS.items():

        if dados["ambiente"] == nome_ambiente:

            documentos_ambiente.append({
                "codigo": codigo,
                "nome": dados["nome"],
                "autor": dados["autor"],
                "classificacao": dados["classificacao"]
            })

    return documentos_ambiente


# ============================================================
# VERIFICAR DOCUMENTO ENCONTRADO
# ============================================================

def verificar_documento_encontrado(estado_jogo, codigo):
    """Verifica se o documento já está no inventário."""

    if not validar_estado_jogo(estado_jogo):
        return False

    if not isinstance(codigo, str):
        return False

    codigo = codigo.strip().upper()

    return codigo in estado_jogo["documentos_encontrados"]


# ============================================================
# VERIFICAR DOCUMENTO ENTREGUE
# ============================================================

def verificar_documento_entregue(estado_jogo, codigo):
    """Verifica se o documento já foi entregue."""

    if not validar_estado_jogo(estado_jogo):
        return False

    if not isinstance(codigo, str):
        return False

    codigo = codigo.strip().upper()

    for entrega in estado_jogo["documentos_entregues"]:

        # Compatibilidade com registros antigos.
        if isinstance(entrega, str):
            if entrega.strip().upper() == codigo:
                return True

        if isinstance(entrega, dict):
            codigo_entrega = entrega.get("codigo")

            if (
                isinstance(codigo_entrega, str)
                and codigo_entrega.strip().upper() == codigo
            ):
                return True

    return False


# ============================================================
# ENCONTRAR DOCUMENTO
# ============================================================

def encontrar_documento(estado_jogo, codigo):
    """Registra um documento no inventário."""

    if not validar_estado_jogo(estado_jogo):
        return False

    if not isinstance(codigo, str):
        return False

    codigo = codigo.strip().upper()

    if codigo not in DOCUMENTOS:
        return False

    if verificar_documento_encontrado(
        estado_jogo,
        codigo
    ):
        return False

    estado_jogo["documentos_encontrados"].append(
        codigo
    )

    return True


# ============================================================
# OBTER INVENTÁRIO
# ============================================================

def obter_inventario(estado_jogo):
    """Retorna os documentos encontrados e sua situação de entrega."""

    if not validar_estado_jogo(estado_jogo):
        return []

    inventario = []

    for codigo in estado_jogo["documentos_encontrados"]:

        if not isinstance(codigo, str):
            continue

        codigo = codigo.strip().upper()

        if codigo not in DOCUMENTOS:
            continue

        dados = DOCUMENTOS[codigo]

        documento = {
            "codigo": codigo,
            "nome": dados["nome"],
            "autor": dados["autor"],
            "classificacao": dados["classificacao"],
            "entregue": verificar_documento_entregue(
                estado_jogo,
                codigo
            ),
            "entregue_para": None
        }

        for entrega in estado_jogo["documentos_entregues"]:

            if isinstance(entrega, dict):

                codigo_entrega = entrega.get("codigo")

                if (
                    isinstance(codigo_entrega, str)
                    and codigo_entrega.strip().upper() == codigo
                ):
                    documento["entregue_para"] = entrega.get(
                        "nome_personagem"
                    )

        inventario.append(documento)

    return inventario


# ============================================================
# CONSULTAR DOCUMENTO
# ============================================================

def consultar_documento(estado_jogo, codigo):
    """Retorna os dados de um documento encontrado."""

    if not validar_estado_jogo(estado_jogo):
        return None

    if not isinstance(codigo, str):
        return None

    codigo = codigo.strip().upper()

    if codigo not in DOCUMENTOS:
        return None

    if not verificar_documento_encontrado(
        estado_jogo,
        codigo
    ):
        return None

    dados = DOCUMENTOS[codigo]

    documento = {
        "codigo": codigo,
        "nome": dados["nome"],
        "autor": dados["autor"],
        "classificacao": dados["classificacao"],
        "ambiente": dados["ambiente"],
        "entregue": verificar_documento_entregue(
            estado_jogo,
            codigo
        ),
        "entregue_para": None
    }

    for entrega in estado_jogo["documentos_entregues"]:

        if isinstance(entrega, dict):

            codigo_entrega = entrega.get("codigo")

            if (
                isinstance(codigo_entrega, str)
                and codigo_entrega.strip().upper() == codigo
            ):
                documento["entregue_para"] = entrega.get(
                    "nome_personagem"
                )

    return documento


# ============================================================
# LISTAR DESTINATÁRIOS
# ============================================================

def listar_destinatarios(nome_ambiente=None):
    """Lista destinatários permitidos.

    Quando um ambiente é informado, retorna somente os personagens
    presentes nele. Sem ambiente, retorna o cadastro geral permitido.
    """

    if nome_ambiente is None:

        ids_presentes = [
            id_personagem
            for id_personagem in personagens
            if id_personagem not in ("alex", "oraculo")
        ]

    else:
        ids_presentes = obter_personagens_ambiente(
            nome_ambiente
        )

    destinatarios = []

    for id_personagem in ids_presentes:

        if id_personagem in ("alex", "oraculo"):
            continue

        dados = personagens.get(id_personagem)

        if dados:
            destinatarios.append({
                "id": id_personagem,
                "nome": dados["nome"]
            })

    return destinatarios


# ============================================================
# ENTREGAR DOCUMENTO
# ============================================================

def entregar_documento(estado_jogo, codigo, personagem):
    """Entrega um documento a um personagem presente no ambiente atual."""

    if not validar_estado_jogo(estado_jogo):
        return False

    # Validar o código do documento.
    if not isinstance(codigo, str):
        return False

    codigo = codigo.strip().upper()

    if codigo not in DOCUMENTOS:
        return False

    # O documento precisa ter sido encontrado.
    if not verificar_documento_encontrado(
        estado_jogo,
        codigo
    ):
        return False

    # Um documento não pode ser entregue duas vezes.
    if verificar_documento_entregue(
        estado_jogo,
        codigo
    ):
        return False

    # Validar o destinatário.
    if not isinstance(personagem, str):
        return False

    personagem = personagem.strip().lower()

    if personagem not in personagens:
        return False

    # Alex e ORÁCULO não podem receber documentos.
    if personagem in ("alex", "oraculo"):
        return False

    # --------------------------------------------------------
    # NOVA VALIDAÇÃO: DESTINATÁRIO NO AMBIENTE ATUAL
    # --------------------------------------------------------

    ambiente_atual = estado_jogo.get("ambiente_atual")

    if not isinstance(ambiente_atual, str):
        return False

    ids_presentes = obter_personagens_ambiente(
        ambiente_atual
    )

    if personagem not in ids_presentes:
        return False

    # --------------------------------------------------------
    # REGISTRAR ENTREGA
    # --------------------------------------------------------

    nome_personagem = personagens[personagem]["nome"]

    registro = {
        "codigo": codigo,
        "documento": DOCUMENTOS[codigo]["nome"],
        "personagem": personagem,
        "nome_personagem": nome_personagem
    }

    estado_jogo["documentos_entregues"].append(
        registro
    )

    return True


# ============================================================
# HISTÓRICO DE ENTREGAS
# ============================================================

def consultar_historico_entregas(estado_jogo):
    """Retorna o histórico de documentos entregues."""

    if not validar_estado_jogo(estado_jogo):
        return []

    historico = []

    for entrega in estado_jogo["documentos_entregues"]:

        if isinstance(entrega, dict):
            historico.append(entrega.copy())

        elif isinstance(entrega, str):

            codigo = entrega.strip().upper()

            if codigo in DOCUMENTOS:
                historico.append({
                    "codigo": codigo,
                    "documento": DOCUMENTOS[codigo]["nome"],
                    "personagem": None,
                    "nome_personagem": "Não identificado"
                })

    return historico
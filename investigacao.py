
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

from personagens import personagens


# ==========================================
# CADASTRO DOS DOCUMENTOS
# ==========================================

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


# ==========================================
# VALIDAR ESTADO
# ==========================================

def validar_estado_jogo(estado_jogo):

    if not isinstance(estado_jogo, dict):
        return False

    campos = [
        "documentos_encontrados",
        "documentos_entregues"
    ]

    for campo in campos:
        if campo not in estado_jogo:
            return False

    if not isinstance(estado_jogo["documentos_encontrados"], list):
        return False

    if not isinstance(estado_jogo["documentos_entregues"], list):
        return False

    return True


# ==========================================
# LISTAR DOCUMENTOS DO AMBIENTE
# ==========================================

def listar_documentos(nome_ambiente):

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


# ==========================================
# VERIFICAR DOCUMENTO ENCONTRADO
# ==========================================

def verificar_documento_encontrado(estado_jogo, codigo):

    if not validar_estado_jogo(estado_jogo):
        return False

    return codigo in estado_jogo["documentos_encontrados"]


# ==========================================
# VERIFICAR DOCUMENTO ENTREGUE
# ==========================================

def verificar_documento_entregue(estado_jogo, codigo):

    if not validar_estado_jogo(estado_jogo):
        return False

    for entrega in estado_jogo["documentos_entregues"]:

        if entrega == codigo:
            return True

        if isinstance(entrega, dict):
            if entrega.get("codigo") == codigo:
                return True

    return False


# ==========================================
# ENCONTRAR DOCUMENTO
# ==========================================

def encontrar_documento(estado_jogo, codigo):

    if not validar_estado_jogo(estado_jogo):
        return False

    if not isinstance(codigo, str):
        return False

    codigo = codigo.strip().upper()

    if codigo not in DOCUMENTOS:
        return False

    if verificar_documento_encontrado(estado_jogo, codigo):
        return False

    estado_jogo["documentos_encontrados"].append(codigo)

    return True


# ==========================================
# OBTER INVENTÁRIO
# ==========================================

def obter_inventario(estado_jogo):

    if not validar_estado_jogo(estado_jogo):
        return []

    inventario = []

    for codigo in estado_jogo["documentos_encontrados"]:

        if codigo not in DOCUMENTOS:
            continue

        dados = DOCUMENTOS[codigo]

        documento = {
            "codigo": codigo,
            "nome": dados["nome"],
            "autor": dados["autor"],
            "classificacao": dados["classificacao"],
            "entregue": verificar_documento_entregue(
                estado_jogo, codigo
            ),
            "entregue_para": None
        }

        for entrega in estado_jogo["documentos_entregues"]:

            if isinstance(entrega, dict):
                if entrega.get("codigo") == codigo:
                    documento["entregue_para"] = entrega.get(
                        "nome_personagem"
                    )

        inventario.append(documento)

    return inventario


# ==========================================
# CONSULTAR DOCUMENTO
# ==========================================

def consultar_documento(estado_jogo, codigo):

    if not validar_estado_jogo(estado_jogo):
        return None

    if not isinstance(codigo, str):
        return None

    codigo = codigo.strip().upper()

    if codigo not in DOCUMENTOS:
        return None

    if not verificar_documento_encontrado(estado_jogo, codigo):
        return None

    dados = DOCUMENTOS[codigo]

    documento = {
        "codigo": codigo,
        "nome": dados["nome"],
        "autor": dados["autor"],
        "classificacao": dados["classificacao"],
        "ambiente": dados["ambiente"],
        "entregue": verificar_documento_entregue(
            estado_jogo, codigo
        ),
        "entregue_para": None
    }

    for entrega in estado_jogo["documentos_entregues"]:

        if isinstance(entrega, dict):
            if entrega.get("codigo") == codigo:
                documento["entregue_para"] = entrega.get(
                    "nome_personagem"
                )

    return documento


# ==========================================
# LISTAR DESTINATÁRIOS
# ==========================================

def listar_destinatarios():

    destinatarios = []

    for id_personagem, dados in personagens.items():

        if id_personagem not in ("alex", "oraculo"):

            destinatarios.append({
                "id": id_personagem,
                "nome": dados["nome"]
            })

    return destinatarios


# ==========================================
# ENTREGAR DOCUMENTO
# ==========================================

def entregar_documento(estado_jogo, codigo, personagem):

    if not validar_estado_jogo(estado_jogo):
        return False

    if not isinstance(codigo, str):
        return False

    codigo = codigo.strip().upper()

    if codigo not in DOCUMENTOS:
        return False

    if not verificar_documento_encontrado(estado_jogo, codigo):
        return False

    if verificar_documento_entregue(estado_jogo, codigo):
        return False

    if not isinstance(personagem, str):
        return False

    personagem = personagem.strip().lower()

    if personagem not in personagens:
        return False

    if personagem in ("alex", "oraculo"):
        return False

    nome_personagem = personagens[personagem]["nome"]

    registro = {
        "codigo": codigo,
        "documento": DOCUMENTOS[codigo]["nome"],
        "personagem": personagem,
        "nome_personagem": nome_personagem
    }

    estado_jogo["documentos_entregues"].append(registro)

    return True


# ==========================================
# HISTÓRICO DE ENTREGAS
# ==========================================

def consultar_historico_entregas(estado_jogo):

    if not validar_estado_jogo(estado_jogo):
        return []

    historico = []

    for entrega in estado_jogo["documentos_entregues"]:

        if isinstance(entrega, dict):
            historico.append(entrega.copy())

        elif isinstance(entrega, str):

            if entrega in DOCUMENTOS:
                historico.append({
                    "codigo": entrega,
                    "documento": DOCUMENTOS[entrega]["nome"],
                    "personagem": None,
                    "nome_personagem": "Não identificado"
                })

    return historico

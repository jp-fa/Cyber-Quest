
"""
investigacao.py
CyberQuest: O Protocolo ORÁCULO

Responsabilidade:
<<<<<<< HEAD
- Cadastrar os documentos do jogo.
- Registrar documentos encontrados.
- Consultar o inventário.
- Entregar documentos aos personagens.
- Consultar o histórico de entregas.

IMPORTANTE:
Todas as funções utilizam o mesmo estado_jogo.
O salvamento é responsabilidade de salvamento.py.
=======
- Cadastrar documentos.
- Registrar documentos encontrados.
- Consultar inventário.
- Entregar documentos.
- Consultar histórico de entregas.
>>>>>>> investigacao
"""

from personagens import personagens


<<<<<<< HEAD
# ==========================================================
# 1. CADASTRO DOS DOCUMENTOS
# ==========================================================
=======
# ==========================================
# CADASTRO DOS DOCUMENTOS
# ==========================================
>>>>>>> investigacao

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
<<<<<<< HEAD
        "nome": "Plano de Contingência",
        "autor": "Dante Moreau",
=======
        "nome": "Memorando Estratégico NEXUS",
        "autor": "Helena Voss",
>>>>>>> investigacao
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


<<<<<<< HEAD
# ==========================================================
# 2. VALIDAR ESTADO DO JOGO
# ==========================================================

def validar_estado_jogo(estado_jogo):

    if not isinstance(estado_jogo, dict):
        return False

    if "documentos_encontrados" not in estado_jogo:
        return False

    if "documentos_entregues" not in estado_jogo:
        return False

    if not isinstance(estado_jogo["documentos_encontrados"], list):
        return False

    if not isinstance(estado_jogo["documentos_entregues"], list):
        return False
=======
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
>>>>>>> investigacao

    return True


<<<<<<< HEAD
# ==========================================================
# 3. LISTAR DOCUMENTOS DE UM AMBIENTE
# ==========================================================

def listar_documentos(nome_ambiente):

    documentos_ambiente = []

    for codigo, dados in DOCUMENTOS.items():

        if dados["ambiente"] == nome_ambiente:

            documento = {
                "codigo": codigo,
                "nome": dados["nome"],
                "autor": dados["autor"],
                "classificacao": dados["classificacao"]
            }

            documentos_ambiente.append(documento)

    return documentos_ambiente
=======
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
>>>>>>> investigacao


# ==========================================================
# 4. VERIFICAR SE UM DOCUMENTO FOI ENCONTRADO
# ==========================================================

<<<<<<< HEAD
def verificar_documento_encontrado(estado_jogo, codigo):

    if not validar_estado_jogo(estado_jogo):
        return False

    return codigo in estado_jogo["documentos_encontrados"]
=======
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
>>>>>>> investigacao


# ==========================================================
# 5. VERIFICAR SE UM DOCUMENTO FOI ENTREGUE
# ==========================================================

def verificar_documento_entregue(estado_jogo, codigo):

    if not validar_estado_jogo(estado_jogo):
        return False

    for entrega in estado_jogo["documentos_entregues"]:

        # Compatibilidade caso o registro seja somente o código.
        if entrega == codigo:
            return True

        if isinstance(entrega, dict):

            if entrega.get("codigo") == codigo:
                return True

    return False


# ==========================================================
# 6. ENCONTRAR DOCUMENTO
# ==========================================================

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


# ==========================================================
# 7. OBTER INVENTÁRIO
# ==========================================================

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

        # Consulta o destinatário, caso já tenha ocorrido uma entrega.
        for entrega in estado_jogo["documentos_entregues"]:

            if isinstance(entrega, dict):

                if entrega.get("codigo") == codigo:
                    documento["entregue_para"] = entrega.get(
                        "nome_personagem"
                    )

        inventario.append(documento)

    return inventario


# ==========================================================
# 8. CONSULTAR DOCUMENTO
# ==========================================================

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


# ==========================================================
# 9. LISTAR DESTINATÁRIOS
# ==========================================================

def listar_destinatarios():

    destinatarios = []

    for id_personagem, dados in personagens.items():

        if id_personagem not in ("alex", "oraculo"):

            destinatarios.append({
                "id": id_personagem,
                "nome": dados["nome"]
            })

    return destinatarios


# ==========================================================
# 10. ENTREGAR DOCUMENTO
# ==========================================================

def entregar_documento(estado_jogo, codigo, personagem):

    if not validar_estado_jogo(estado_jogo):
        return False

<<<<<<< HEAD
    # Normaliza o código do documento.
=======
>>>>>>> investigacao
    if not isinstance(codigo, str):
        return False

    codigo = codigo.strip().upper()

    if codigo not in DOCUMENTOS:
        return False

<<<<<<< HEAD
    # Verifica se o jogador encontrou o documento.
    if not verificar_documento_encontrado(estado_jogo, codigo):
        return False

    # Impede que o documento seja entregue novamente.
    if verificar_documento_entregue(estado_jogo, codigo):
        return False

    # Normaliza o identificador do personagem.
=======
    if not verificar_documento_encontrado(estado_jogo, codigo):
        return False

    if verificar_documento_entregue(estado_jogo, codigo):
        return False

>>>>>>> investigacao
    if not isinstance(personagem, str):
        return False

    personagem = personagem.strip().lower()

<<<<<<< HEAD
    # Verifica se o personagem existe.
    if personagem not in personagens:
        return False

    # Alex e ORÁCULO não podem receber documentos.
=======
    if personagem not in personagens:
        return False

>>>>>>> investigacao
    if personagem in ("alex", "oraculo"):
        return False

    nome_personagem = personagens[personagem]["nome"]

<<<<<<< HEAD
    # Registra a entrega no estado compartilhado.
=======
>>>>>>> investigacao
    registro = {
        "codigo": codigo,
        "documento": DOCUMENTOS[codigo]["nome"],
        "personagem": personagem,
        "nome_personagem": nome_personagem
    }

    estado_jogo["documentos_entregues"].append(registro)

    return True


<<<<<<< HEAD
# ==========================================================
# 11. CONSULTAR HISTÓRICO DE ENTREGAS
# ==========================================================
=======
# ==========================================
# HISTÓRICO DE ENTREGAS
# ==========================================
>>>>>>> investigacao

def consultar_historico_entregas(estado_jogo):

    if not validar_estado_jogo(estado_jogo):
        return []

    historico = []

    for entrega in estado_jogo["documentos_entregues"]:

        if isinstance(entrega, dict):
<<<<<<< HEAD

            historico.append(entrega.copy())

        elif isinstance(entrega, str):

            # Compatibilidade com registros antigos contendo somente IDs.
            if entrega in DOCUMENTOS:

                historico.append({
                    "codigo": entrega,
                    "documento": DOCUMENTOS[entrega]["nome"],
                    "personagem": None,
                    "nome_personagem": "Não identificado"
                })

=======
            historico.append(entrega.copy())

        elif isinstance(entrega, str):

            if entrega in DOCUMENTOS:
                historico.append({
                    "codigo": entrega,
                    "documento": DOCUMENTOS[entrega]["nome"],
                    "personagem": None,
                    "nome_personagem": "Não identificado"
                })

>>>>>>> investigacao
    return historico

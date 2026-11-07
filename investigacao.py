from copy import deepcopy

from personagens import personagens, alterar_confianca


# ==========================================
# DOCUMENTOS DO JOGO
# ==========================================

documentos = {

    "projeto_oraculo": {
        "nome": "Projeto ORÁCULO",
        "autor": "Dra. Karla",
        "classificacao": "Confidencial",
        "encontrado": False,
        "entregue": False,
        "entregue_para": None
    },

    "relatorio_seguranca": {
        "nome": "Relatório de Segurança",
        "autor": "Helena Voss",
        "classificacao": "Confidencial",
        "encontrado": False,
        "entregue": False,
        "entregue_para": None
    },

    "plano_contingencia": {
        "nome": "Plano de Contingência",
        "autor": "Dante Moreau",
        "classificacao": "Restrito",
        "encontrado": False,
        "entregue": False,
        "entregue_para": None
    },

    "documento_secreto": {
        "nome": "Documento Secreto",
        "autor": "ORÁCULO",
        "classificacao": "Ultrassecreto",
        "encontrado": False,
        "entregue": False,
        "entregue_para": None
    }

}


# ==========================================
# INVENTÁRIO DO JOGADOR
# ==========================================

inventario = []


# ==========================================
# HISTÓRICO DE ENTREGAS
# ==========================================

historico_entregas = []


# ==========================================
# ENCONTRAR DOCUMENTO
# ==========================================

def encontrar_documento(documento_id):

    if documento_id not in documentos:
        print("Documento não encontrado!")
        return False

    dados = documentos[documento_id]

    if dados["encontrado"]:
        print("Você já encontrou este documento!")
        return False

    dados["encontrado"] = True

    inventario.append(documento_id)

    print("\nDocumento encontrado!")
    print(f"Nome: {dados['nome']}")
    print(f"Autor: {dados['autor']}")
    print(f"Classificação: {dados['classificacao']}")

    return True


# ==========================================
# EXIBIR INVENTÁRIO
# ==========================================

def exibir_inventario():

    print("\n========== INVENTÁRIO ==========")

    if not inventario:
        print("Seu inventário está vazio!")
        print("\n================================")
        return

    for numero, documento_id in enumerate(inventario, start=1):

        dados = documentos[documento_id]

        print(f"\n{numero}. {dados['nome']}")
        print(f"   Autor: {dados['autor']}")
        print(f"   Classificação: {dados['classificacao']}")

        if dados["entregue"]:
            print(f"   Status: Entregue para {dados['entregue_para']}")

        else:
            print("   Status: Disponível")

    print("\n================================")


# ==========================================
# CONSULTAR DOCUMENTO
# ==========================================

def consultar_documento():

    if not inventario:
        print("Não existem documentos no inventário!")
        return

    exibir_inventario()

    try:
        escolha = int(input("\nDigite o número do documento: "))

    except ValueError:
        print("Digite um número válido!")
        return

    if escolha < 1 or escolha > len(inventario):
        print("Opção inválida!")
        return

    documento_id = inventario[escolha - 1]

    dados = documentos[documento_id]

    print("\n======= DETALHES DO DOCUMENTO =======")
    print(f"Nome: {dados['nome']}")
    print(f"Autor: {dados['autor']}")
    print(f"Classificação: {dados['classificacao']}")

    if dados["entregue"]:
        print(f"Entregue para: {dados['entregue_para']}")

    else:
        print("Este documento ainda não foi entregue.")

    print("=====================================")


# ==========================================
# LISTAR DESTINATÁRIOS
# ==========================================

def listar_destinatarios():

    print("\n======= PERSONAGENS =======")

    for personagem_id, dados in personagens.items():

        # Alex é o protagonista e não recebe documentos.
        if personagem_id == "alex":
            continue

        print(f"- {dados['nome']}")


# ==========================================
# ENTREGAR DOCUMENTO
# ==========================================

def entregar_documento():

    if not inventario:
        print("Você não possui documentos para entregar!")
        return

    exibir_inventario()

    try:
        escolha = int(input("\nQual documento deseja entregar? "))

    except ValueError:
        print("Digite um número válido!")
        return

    if escolha < 1 or escolha > len(inventario):
        print("Documento inválido!")
        return

    documento_id = inventario[escolha - 1]

    dados = documentos[documento_id]

    if dados["entregue"]:
        print("Este documento já foi entregue!")
        return

    listar_destinatarios()

    personagem = input(
        "\nPara quem deseja entregar? "
    ).lower().strip()

    # Verifica se o personagem existe no cadastro oficial.
    if personagem not in personagens or personagem == "alex":
        print("Personagem inválido!")
        return

    nome_personagem = personagens[personagem]["nome"]

    confirmacao = input(
        f"\nDeseja entregar '{dados['nome']}' "
        f"para {nome_personagem}? (s/n): "
    ).lower().strip()

    if confirmacao != "s":
        print("Entrega cancelada!")
        return

    # Atualiza os dados do documento.
    dados["entregue"] = True
    dados["entregue_para"] = nome_personagem

    # Registra a entrega no histórico.
    historico_entregas.append({
        "documento": documento_id,
        "personagem": personagem,
        "nome_personagem": nome_personagem
    })

    print("\nDocumento entregue com sucesso!")
    print(f"Documento: {dados['nome']}")
    print(f"Destinatário: {nome_personagem}")


# ==========================================
# ALTERAR CONFIANÇA APÓS UMA DECISÃO
# ==========================================

def aplicar_impacto_confianca(personagem, valor, capitulo):

    if personagem not in personagens or personagem == "alex":
        print("Personagem inválido!")
        return False

    # Utiliza a função que já existe em personagens.py.
    return alterar_confianca(personagem, valor, capitulo)


# ==========================================
# CONSULTAR HISTÓRICO DE ENTREGAS
# ==========================================

def consultar_historico_entregas():

    print("\n======= HISTÓRICO DE ENTREGAS =======")

    if not historico_entregas:
        print("Nenhuma entrega foi realizada.")
        print("=====================================")
        return

    for numero, registro in enumerate(historico_entregas, start=1):

        dados = documentos[registro["documento"]]

        print(f"\n{numero}. Documento: {dados['nome']}")
        print(f"   Destinatário: {registro['nome_personagem']}")

    print("\n=====================================")


# ==========================================
# PREPARAR DADOS PARA SALVAMENTO JSON
# ==========================================

def obter_estado_investigacao():

    estado = {
        "documentos": deepcopy(documentos),
        "inventario": deepcopy(inventario),
        "historico_entregas": deepcopy(historico_entregas)
    }

    return estado


# ==========================================
# RESTAURAR DADOS DA INVESTIGAÇÃO
# ==========================================

def carregar_estado_investigacao(estado):

    if not isinstance(estado, dict):
        print("Estado de investigação inválido!")
        return False

    documentos_salvos = estado.get("documentos")
    inventario_salvo = estado.get("inventario")
    historico_salvo = estado.get("historico_entregas")

    if not isinstance(documentos_salvos, dict):
        print("Dados dos documentos inválidos!")
        return False

    if not isinstance(inventario_salvo, list):
        print("Dados do inventário inválidos!")
        return False

    if not isinstance(historico_salvo, list):
        print("Histórico de entregas inválido!")
        return False

    # Atualiza os dados sem substituir os objetos globais.
    documentos.clear()
    documentos.update(deepcopy(documentos_salvos))

    inventario.clear()
    inventario.extend(deepcopy(inventario_salvo))

    historico_entregas.clear()
    historico_entregas.extend(deepcopy(historico_salvo))

    print("Dados da investigação carregados com sucesso!")

    return True
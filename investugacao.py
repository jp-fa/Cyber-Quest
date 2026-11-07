
personagens = {
    "alex": {
        "nome": "Alex",
        "cargo": "Hacker",
        "idade": 28,
        "confianca": "Indefinida"
    },

    "helena": {
        "nome": "Helena Voss",
        "cargo": "Diretora da NEXUS",
        "idade": 30,
        "confianca": 30
    },

    "karla": {
        "nome": "Dra. Karla",
        "cargo": "Cientista",
        "idade": 32,
        "confianca": 50
    },

    "dante": {
        "nome": "Dante Moreau",
        "cargo": "Aliado",
        "idade": 29,
        "confianca": 40
    },

    "oraculo": {
        "nome": "ORÁCULO",
        "cargo": "Inteligência Artificial",
        "idade": 3,
        "confianca": 0
    }
}


# ==========================================
# EXIBIR INFORMAÇÕES DOS PERSONAGENS
# ==========================================

def exibir_personagem(personagem):

    if personagem in personagens:

        dados = personagens[personagem]

        print("\n================================")
        print("     INFORMAÇÕES DO PERSONAGEM")
        print("================================")

        print(f"Nome: {dados['nome']}")
        print(f"Cargo: {dados['cargo']}")
        print(f"Idade: {dados['idade']}")
        print(f"Confiança: {dados['confianca']}")

        print("================================")

    else:
        print("Personagem não encontrado!")


# ==========================================
# LISTAR PERSONAGENS
# ==========================================

def listar_personagens():

    print("\n======= PERSONAGENS =======")

    for personagem in personagens:
        print(f"- {personagens[personagem]['nome']}")

    print("===========================")


# ==========================================
# CONSULTAR PERSONAGEM
# ==========================================

def consultar_personagem():

    listar_personagens()

    escolha = input(
        "\nQual personagem deseja consultar? "
    ).lower().strip()

    exibir_personagem(escolha)


# ==========================================
# CONTROLE DE PERSONAGENS ABORDADOS
# ==========================================

personagens_abordados = {
    "capitulo_1": [],
    "capitulo_2": [],
    "capitulo_3": []
}


# ==========================================
# HISTÓRICO DE CONFIANÇA POR CAPÍTULO
# ==========================================

historico_confianca = {
    "capitulo_1": [],
    "capitulo_2": [],
    "capitulo_3": []
}


# ==========================================
# ABORDAR PERSONAGEM
# ==========================================

def abordar_personagem(personagem, capitulo):

    if personagem not in personagens:
        print("Personagem não encontrado!")
        return

    if capitulo not in personagens_abordados:
        print("Capítulo inválido!")
        return

    if personagem in personagens_abordados[capitulo]:
        print("Você já conversou com este personagem neste capítulo!")
        return

    personagens_abordados[capitulo].append(personagem)

    print(
        f"\nVocê iniciou uma conversa com "
        f"{personagens[personagem]['nome']}."
    )

    exibir_personagem(personagem)


# ==========================================
# ALTERAR CONFIANÇA
# ==========================================

def alterar_confianca(personagem, valor, capitulo):

    if personagem not in personagens:
        print("Personagem não encontrado!")
        return

    if capitulo not in historico_confianca:
        print("Capítulo inválido!")
        return

    confianca_atual = personagens[personagem]["confianca"]

    if not isinstance(confianca_atual, int):
        print("Este personagem não possui confiança numérica.")
        return

    nova_confianca = confianca_atual + valor

    if nova_confianca > 100:
        nova_confianca = 100

    elif nova_confianca < 0:
        nova_confianca = 0

    personagens[personagem]["confianca"] = nova_confianca

    historico_confianca[capitulo].append({
        "personagem": personagem,
        "anterior": confianca_atual,
        "nova": nova_confianca,
        "alteracao": nova_confianca - confianca_atual
    })

    print(
        f"\nConfiança de {personagens[personagem]['nome']} atualizada!"
    )
    print(f"Confiança anterior: {confianca_atual}")
    print(f"Nova confiança: {nova_confianca}")


# ==========================================
# CONSULTAR NÍVEL DE CONFIANÇA
# ==========================================

def consultar_confianca(personagem):

    if personagem not in personagens:
        print("Personagem não encontrado!")
        return

    confianca = personagens[personagem]["confianca"]

    print("\n======= NÍVEL DE CONFIANÇA =======")
    print(f"Personagem: {personagens[personagem]['nome']}")
    print(f"Confiança: {confianca}")

    if isinstance(confianca, int):

        if confianca >= 70:
            print("Relação: Alta confiança")

        elif confianca >= 40:
            print("Relação: Confiança moderada")

        else:
            print("Relação: Baixa confiança")

    else:
        print("Relação: Não definida")

    print("=================================")


# ==========================================
# TESTES DO CÓDIGO
# ==========================================

# Abordagem de personagens
abordar_personagem("dante", "capitulo_1")
abordar_personagem("dante", "capitulo_1")

print(personagens_abordados)


# Consulta de confiança
consultar_confianca("dante")
consultar_confianca("helena")
consultar_confianca("alex")


# Alterações de confiança
alterar_confianca("dante", 10, "capitulo_1")
alterar_confianca("helena", -15, "capitulo_1")
alterar_confianca("dante", 5, "capitulo_2")


# Exibir histórico
print("\n======= HISTÓRICO DE CONFIANÇA =======")
print(historico_confianca)

def consultar_historico_confianca(capitulo):
    if capitulo not in historico_confianca:
        print("Capítulo inválido!")
        return

    historico = historico_confianca[capitulo]

    if not historico:
        print("Nenhuma alteração de confiança registrada neste capítulo.")
        return

    print("\n======= HISTÓRICO DE CONFIANÇA =======")
    print(f"Capítulo: {capitulo.replace('_', ' ').title()}")

    for registro in historico:

        nome = personagens[registro["personagem"]]["nome"]

        print("\n--------------------------------")
        print(f"Personagem: {nome}")
        print(f"Confiança anterior: {registro['anterior']}")
        print(f"Nova confiança: {registro['nova']}")

        if registro["alteracao"] > 0:
            print(f"Alteração: +{registro['alteracao']}")

        elif registro["alteracao"] < 0:
            print(f"Alteração: {registro['alteracao']}")

        else:
            print("Alteração: Nenhuma")

    print("======================================")

consultar_historico_confianca("capitulo_1")
consultar_historico_confianca("capitulo_2")
consultar_historico_confianca("capitulo_3")

documentos = {

    "projeto_oraculo": {
        "nome": "Projeto ORÁCULO",
        "autor": "Dra. Karla",
        "classificacao": "Confidencial",
        "encontrado": False,
        "entregue": False
    },

    "relatorio_seguranca": {
        "nome": "Relatório de Segurança",
        "autor": "Helena Voss",
        "classificacao": "Confidencial",
        "encontrado": False,
        "entregue": False
    },

    "plano_contingencia": {
        "nome": "Plano de Contingência",
        "autor": "Dante Moreau",
        "classificacao": "Restrito",
        "encontrado": False,
        "entregue": False
    },

    "documento_secreto": {
        "nome": "Documento Secreto",
        "autor": "ORÁCULO",
        "classificacao": "Ultrassecreto",
        "encontrado": False,
        "entregue": False
    }

}


# ==========================================
# INVENTÁRIO DO JOGADOR
# ==========================================

inventario = []

# ==========================================
# PERSONAGENS DO JOGO
# ==========================================

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
# CAPÍTULOS DO JOGO
# ==========================================

capitulos_validos = [
    "capitulo_1",
    "capitulo_2",
    "capitulo_3"
]


# ==========================================
# PERSONAGENS ABORDADOS
# ==========================================

personagens_abordados = {

    "capitulo_1": [],
    "capitulo_2": [],
    "capitulo_3": []

}


# ==========================================
# HISTÓRICO DE CONFIANÇA
# ==========================================

historico_confianca = {

    "capitulo_1": [],
    "capitulo_2": [],
    "capitulo_3": []

}


# ==========================================
# EXIBIR UM PERSONAGEM
# ==========================================

def exibir_personagem(personagem):

    if personagem not in personagens:
        print("Personagem não encontrado!")
        return False

    dados = personagens[personagem]

    print("\n======= INFORMAÇÕES DO PERSONAGEM =======")
    print(f"Nome: {dados['nome']}")
    print(f"Cargo: {dados['cargo']}")
    print(f"Idade: {dados['idade']}")

    if isinstance(dados["confianca"], int):
        print(f"Confiança: {dados['confianca']}/100")
    else:
        print(f"Confiança: {dados['confianca']}")

    print("=========================================")

    return True


# ==========================================
# LISTAR PERSONAGENS
# ==========================================

def listar_personagens():

    print("\n======= PERSONAGENS =======")

    for personagem_id, dados in personagens.items():

        print(f"- {dados['nome']}")

    print("===========================")


# ==========================================
# CONSULTAR PERSONAGEM
# ==========================================

def consultar_personagem():

    listar_personagens()

    personagem = input(
        "\nDigite o nome do personagem: "
    ).lower().strip()

    if personagem not in personagens:
        print("Personagem não encontrado!")
        return False

    return exibir_personagem(personagem)


# ==========================================
# ABORDAR PERSONAGEM
# ==========================================

def abordar_personagem(personagem, capitulo):

    if personagem not in personagens:
        print("Personagem não encontrado!")
        return False

    if capitulo not in capitulos_validos:
        print("Capítulo inválido!")
        return False

    if personagem == "alex":
        print("Alex é o protagonista e não pode ser abordado.")
        return False

    if personagem in personagens_abordados[capitulo]:
        print("Você já abordou este personagem neste capítulo!")
        return False

    personagens_abordados[capitulo].append(personagem)

    print(f"\nVocê abordou {personagens[personagem]['nome']}.")

    return True


# ==========================================
# ALTERAR CONFIANÇA
# ==========================================

def alterar_confianca(personagem, valor, capitulo):

    if personagem not in personagens:
        print("Personagem não encontrado!")
        return False

    if personagem == "alex":
        print("A confiança de Alex não pode ser alterada.")
        return False

    if capitulo not in capitulos_validos:
        print("Capítulo inválido!")
        return False

    dados = personagens[personagem]

    if not isinstance(dados["confianca"], int):
        print("A confiança deste personagem não pode ser alterada.")
        return False

    if not isinstance(valor, (int, float)) or isinstance(valor, bool):
        print("O valor da alteração precisa ser numérico!")
        return False

    confianca_anterior = dados["confianca"]

    nova_confianca = confianca_anterior + valor

    # Impede confiança abaixo de 0 ou acima de 100.
    nova_confianca = max(0, min(100, nova_confianca))

    dados["confianca"] = nova_confianca

    diferenca = nova_confianca - confianca_anterior

    historico_confianca[capitulo].append({

        "personagem": personagem,
        "nome": dados["nome"],
        "confianca_anterior": confianca_anterior,
        "confianca_atual": nova_confianca,
        "alteracao": diferenca

    })

    print(f"\nConfiança de {dados['nome']} atualizada!")
    print(f"Confiança anterior: {confianca_anterior}")
    print(f"Confiança atual: {nova_confianca}")

    return True


# ==========================================
# CONSULTAR CONFIANÇA
# ==========================================

def consultar_confianca(personagem):

    if personagem not in personagens:
        print("Personagem não encontrado!")
        return False

    dados = personagens[personagem]
    confianca = dados["confianca"]

    print(f"\n======= CONFIANÇA: {dados['nome']} =======")

    if not isinstance(confianca, int):
        print(f"Confiança: {confianca}")
        print("=========================================")
        return True

    print(f"Pontuação: {confianca}/100")

    if confianca >= 70:
        print("Nível: Alta confiança")

    elif confianca >= 40:
        print("Nível: Confiança moderada")

    else:
        print("Nível: Baixa confiança")

    print("=========================================")

    return True


# ==========================================
# CONSULTAR HISTÓRICO DE CONFIANÇA
# ==========================================

def consultar_historico_confianca(capitulo):

    if capitulo not in capitulos_validos:
        print("Capítulo inválido!")
        return False

    historico = historico_confianca[capitulo]

    print(
        f"\n======= HISTÓRICO DE CONFIANÇA: "
        f"{capitulo.replace('_', ' ').title()} ======="
    )

    if not historico:
        print("Nenhuma alteração de confiança registrada.")
        print("=========================================")
        return True

    for numero, registro in enumerate(historico, start=1):

        print(f"\n{numero}. {registro['nome']}")
        print(
            f"   Confiança anterior: "
            f"{registro['confianca_anterior']}"
        )
        print(
            f"   Confiança atual: "
            f"{registro['confianca_atual']}"
        )
        print(
            f"   Alteração: "
            f"{registro['alteracao']:+}"
        )

    print("\n=========================================")

    return True
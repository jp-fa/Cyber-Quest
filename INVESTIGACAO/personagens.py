<<<<<<< HEAD
# ==========================================
# PERSONAGENS DO JOGO
# ==========================================

personagens = {

=======

# ==========================================
# PERSONAGENS DO CYBERQUEST
# ==========================================

personagens = {
>>>>>>> investigacao
    "alex": {
        "nome": "Alex",
        "cargo": "Hacker",
        "idade": 28
    },
<<<<<<< HEAD

=======
>>>>>>> investigacao
    "helena": {
        "nome": "Helena Voss",
        "cargo": "Diretora da NEXUS",
        "idade": 30
    },
<<<<<<< HEAD

=======
>>>>>>> investigacao
    "karla": {
        "nome": "Dra. Karla",
        "cargo": "Cientista",
        "idade": 32
    },
<<<<<<< HEAD

=======
>>>>>>> investigacao
    "dante": {
        "nome": "Dante Moreau",
        "cargo": "Aliado",
        "idade": 29
    },
<<<<<<< HEAD

=======
>>>>>>> investigacao
    "oraculo": {
        "nome": "ORÁCULO",
        "cargo": "Inteligência Artificial",
        "idade": 3
    }
<<<<<<< HEAD

}


# ==========================================
# RELAÇÃO ENTRE PERSONAGENS E CONFIANÇA
# ==========================================

=======
}

>>>>>>> investigacao
nomes_confianca = {
    "helena": "Helena",
    "karla": "Karla",
    "dante": "Dante"
}


# ==========================================
# VALIDAR ESTADO DO JOGO
# ==========================================

def validar_estado_jogo(estado_jogo):

    if not isinstance(estado_jogo, dict):
        return False

    campos = [
        "capitulo_atual",
        "personagens_abordados",
        "confianca",
        "escolhas_confianca"
    ]

    for campo in campos:
<<<<<<< HEAD

=======
>>>>>>> investigacao
        if campo not in estado_jogo:
            return False

    return True


# ==========================================
<<<<<<< HEAD
# EXIBIR UM PERSONAGEM
=======
# EXIBIR PERSONAGEM
>>>>>>> investigacao
# ==========================================

def exibir_personagem(personagem, estado_jogo):

<<<<<<< HEAD
=======
    if not isinstance(personagem, str):
        return False

    personagem = personagem.strip().lower()

>>>>>>> investigacao
    if personagem not in personagens:
        print("Personagem não encontrado!")
        return False

    if not validar_estado_jogo(estado_jogo):
        print("Estado do jogo inválido!")
        return False

    dados = personagens[personagem]

    print("\n======= INFORMAÇÕES DO PERSONAGEM =======")
    print(f"Nome: {dados['nome']}")
    print(f"Cargo: {dados['cargo']}")
    print(f"Idade: {dados['idade']}")

    if personagem in nomes_confianca:
<<<<<<< HEAD

        nome = nomes_confianca[personagem]

        confianca = estado_jogo["confianca"][nome]

        print(f"Confiança: {confianca.title()}")

    elif personagem == "alex":

        print("Confiança: Indefinida")

    else:

=======
        nome = nomes_confianca[personagem]
        confianca = estado_jogo["confianca"][nome]
        print(f"Confiança: {confianca.title()}")

    elif personagem == "alex":
        print("Confiança: Indefinida")

    else:
>>>>>>> investigacao
        print("Confiança: Não aplicável")

    print("=========================================")

    return True


# ==========================================
# LISTAR PERSONAGENS
# ==========================================

def listar_personagens():

    print("\n======= PERSONAGENS =======")

    for dados in personagens.values():
<<<<<<< HEAD

=======
>>>>>>> investigacao
        print(f"- {dados['nome']}")

    print("===========================")


# ==========================================
# CONSULTAR PERSONAGEM
# ==========================================

def consultar_personagem(personagem, estado_jogo):

    return exibir_personagem(personagem, estado_jogo)


# ==========================================
# ABORDAR PERSONAGEM
# ==========================================

def abordar_personagem(estado_jogo, personagem):

    if not validar_estado_jogo(estado_jogo):
        print("Estado do jogo inválido!")
        return False

<<<<<<< HEAD
=======
    if not isinstance(personagem, str):
        return False

    personagem = personagem.strip().lower()

>>>>>>> investigacao
    if personagem not in personagens:
        print("Personagem não encontrado!")
        return False

    if personagem == "alex":
        print("Alex é o protagonista e não pode ser abordado.")
        return False

    capitulo = str(estado_jogo["capitulo_atual"])

    if capitulo not in ("1", "2", "3"):
        print("Capítulo inválido!")
        return False

    abordados = estado_jogo["personagens_abordados"]

    if capitulo not in abordados:
        print("Capítulo não encontrado no estado do jogo!")
        return False

    if personagem in abordados[capitulo]:
<<<<<<< HEAD

=======
>>>>>>> investigacao
        print("Você já abordou este personagem neste capítulo!")
        return False

    abordados[capitulo].append(personagem)

<<<<<<< HEAD
    print(
        f"\nVocê abordou {personagens[personagem]['nome']}."
    )
=======
    print(f"\nVocê abordou {personagens[personagem]['nome']}.")
>>>>>>> investigacao

    return True


# ==========================================
# CALCULAR NÍVEL DE CONFIANÇA
# ==========================================

def calcular_nivel_confianca(escolhas):

    saldo = 0

    for escolha in escolhas:
<<<<<<< HEAD

=======
>>>>>>> investigacao
        saldo += escolha["impacto"]

    if saldo > 0:
        return "alta"

    elif saldo < 0:
        return "baixa"

<<<<<<< HEAD
    else:
        return "neutra"
=======
    return "neutra"
>>>>>>> investigacao


# ==========================================
# REGISTRAR ESCOLHA DE CONFIANÇA
# ==========================================

def registrar_escolha_confianca(
    estado_jogo,
    personagem,
    escolha
):

    if not validar_estado_jogo(estado_jogo):
        print("Estado do jogo inválido!")
        return False

<<<<<<< HEAD
=======
    if not isinstance(personagem, str):
        return False

    personagem = personagem.strip().lower()

>>>>>>> investigacao
    if personagem not in nomes_confianca:
        print("Este personagem não possui confiança configurada.")
        return False

<<<<<<< HEAD
    escolha = str(escolha).lower().strip()
=======
    if not isinstance(escolha, str):
        return False

    escolha = escolha.strip().lower()
>>>>>>> investigacao

    if escolha not in ("positiva", "negativa"):
        print("Escolha de confiança inválida!")
        return False

    nome = nomes_confianca[personagem]
<<<<<<< HEAD

    historico = estado_jogo["escolhas_confianca"]

    if nome not in historico:
        print("Personagem não encontrado no histórico de confiança!")
=======
    historico = estado_jogo["escolhas_confianca"]

    if nome not in historico:
>>>>>>> investigacao
        return False

    capitulo = estado_jogo["capitulo_atual"]

<<<<<<< HEAD
    # Impede registrar duas escolhas para o mesmo personagem
    # no mesmo capítulo.
    for registro in historico[nome]:

        if registro["capitulo"] == capitulo:
            print("A confiança deste personagem já foi alterada neste capítulo!")
=======
    for registro in historico[nome]:
        if registro["capitulo"] == capitulo:
            print("A confiança já foi alterada neste capítulo!")
>>>>>>> investigacao
            return False

    confianca_anterior = estado_jogo["confianca"][nome]

<<<<<<< HEAD
    if escolha == "positiva":
        impacto = 1

    else:
        impacto = -1

    historico[nome].append({

        "capitulo": capitulo,
        "escolha": escolha,
        "impacto": impacto

=======
    impacto = 1 if escolha == "positiva" else -1

    historico[nome].append({
        "capitulo": capitulo,
        "escolha": escolha,
        "impacto": impacto
>>>>>>> investigacao
    })

    nova_confianca = calcular_nivel_confianca(
        historico[nome]
    )

    estado_jogo["confianca"][nome] = nova_confianca

    print(f"\nConfiança de {nome} atualizada!")
    print(f"Confiança anterior: {confianca_anterior}")
    print(f"Confiança atual: {nova_confianca}")

    return True


# ==========================================
# CONSULTAR CONFIANÇA
# ==========================================

def consultar_confianca(estado_jogo, personagem):

    if not validar_estado_jogo(estado_jogo):
<<<<<<< HEAD
        print("Estado do jogo inválido!")
        return False

    if personagem not in nomes_confianca:
        print("Personagem não encontrado ou sem confiança configurada!")
        return False

    nome = nomes_confianca[personagem]

=======
        return False

    if not isinstance(personagem, str):
        return False

    personagem = personagem.strip().lower()

    if personagem not in nomes_confianca:
        return False

    nome = nomes_confianca[personagem]
>>>>>>> investigacao
    confianca = estado_jogo["confianca"][nome]

    print(f"\n======= CONFIANÇA: {nome} =======")
    print(f"Nível: {confianca.title()}")

    if confianca == "alta":
<<<<<<< HEAD

        print("Este personagem demonstra maior confiança em Alex.")

    elif confianca == "neutra":

        print("A relação com Alex permanece equilibrada.")

    else:

=======
        print("Este personagem demonstra maior confiança em Alex.")

    elif confianca == "neutra":
        print("A relação com Alex permanece equilibrada.")

    else:
>>>>>>> investigacao
        print("Este personagem demonstra pouca confiança em Alex.")

    print("=========================================")

    return True


# ==========================================
# CONSULTAR HISTÓRICO DE CONFIANÇA
# ==========================================

def consultar_historico_confianca(
    estado_jogo,
    personagem
):

    if not validar_estado_jogo(estado_jogo):
<<<<<<< HEAD
        print("Estado do jogo inválido!")
        return False

    if personagem not in nomes_confianca:
        print("Personagem não encontrado!")
        return False

    nome = nomes_confianca[personagem]

    historico = estado_jogo["escolhas_confianca"][nome]

    print(
        f"\n======= HISTÓRICO DE CONFIANÇA: {nome} ======="
    )

    if not historico:

        print("Nenhuma alteração de confiança registrada.")
        print("=========================================")

        return True

    for numero, registro in enumerate(historico, start=1):

        print(f"\n{numero}. Capítulo {registro['capitulo']}")
        print(f"Escolha: {registro['escolha']}")

        if registro["impacto"] > 0:
            print("Impacto: +1")

        else:
            print("Impacto: -1")
=======
        return False

    if not isinstance(personagem, str):
        return False

    personagem = personagem.strip().lower()

    if personagem not in nomes_confianca:
        return False

    nome = nomes_confianca[personagem]
    historico = estado_jogo["escolhas_confianca"][nome]

    print(f"\n======= HISTÓRICO DE CONFIANÇA: {nome} =======")

    if not historico:
        print("Nenhuma alteração de confiança registrada.")
        print("=========================================")
        return True

    for numero, registro in enumerate(historico, start=1):
        print(f"\n{numero}. Capítulo {registro['capitulo']}")
        print(f"Escolha: {registro['escolha']}")
        print(f"Impacto: {registro['impacto']:+d}")
>>>>>>> investigacao

    print("\n=========================================")

    return True

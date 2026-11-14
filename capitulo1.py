 
"""
capitulo1.py
CyberQuest: O Protocolo ORÁCULO

Responsabilidade:
- Apresentar a conversa com Dra. Karla.
- Registrar as escolhas de Alex.
- Atualizar a confiança de Karla.
- Encontrar e consultar o DOC01.
"""

from personagens import (
    abordar_personagem,
    registrar_escolha_confianca
)

from investigacao import (
    encontrar_documento,
    consultar_documento
)


# ==========================================
# CONVERSA COM DRA. KARLA
# ==========================================

def apresentar_conversa_karla():

    print("""
========================================
       CONVERSA COM DRA. KARLA
========================================

Alex: Dra. Karla. Faz muito tempo.

Karla: Alex? Não imaginei que voltaria
a colocar os pés neste laboratório.

Alex: Preciso entender o que aconteceu
com o projeto ORÁCULO.

Karla: Você sabe que o projeto evoluiu
muito desde a sua saída.

Alex: Evoluiu ou saiu do controle?

Karla: Não podemos ignorar os avanços
que conseguimos alcançar.

Alex: E os riscos? Também evoluíram?

Karla: Existem consequências em qualquer
grande descoberta científica.

Alex: Não foi isso que me ensinaram
quando participei deste projeto.

Karla: Muita coisa mudou desde então,
Alex. Inclusive as pessoas.
""")

    print("\nEscolha a resposta de Alex:")
    print("\n1 - Demonstrar confiança em Karla e pedir sua ajuda.")
    print("2 - Questionar Karla sobre sua participação no projeto.")


# ==========================================
# REAÇÃO DE KARLA
# ==========================================

def apresentar_reacao_karla(escolha):

    if not isinstance(escolha, str):
        escolha = str(escolha)

    escolha = escolha.strip()

    if escolha == "1":

        print("""
Alex: Ainda acredito que você possa
me ajudar a entender o que aconteceu.

Karla: Talvez eu possa. Mas existem
informações que não posso revelar
tão facilmente.

Alex: Preciso saber a verdade.

Karla: Então comece analisando os
relatórios do laboratório. Eles podem
mostrar o que estamos tentando esconder.
""")

        return "positiva"

    elif escolha == "2":

        print("""
Alex: Você participou do desenvolvimento
do ORÁCULO. Preciso saber até onde
foi sua responsabilidade.

Karla: Cuidado com suas acusações, Alex.
Você não conhece todas as circunstâncias.

Alex: Então me explique o que aconteceu.

Karla: Não posso simplesmente revelar
informações confidenciais da NEXUS.
""")

        return "negativa"

    else:

        print("Escolha inválida!")
        return None


# ==========================================
# EXECUTAR INTERAÇÃO COM KARLA
# ==========================================

def interagir_com_karla(estado_jogo):

    # Verifica se o estado é válido
    if not isinstance(estado_jogo, dict):
        print("Estado do jogo inválido!")
        return False

    if estado_jogo.get("capitulo_atual") != 1:
        print("Esta interação pertence ao Capítulo 1.")
        return False

    # Verifica se Karla já foi abordada
    abordados = estado_jogo.get("personagens_abordados", {})
    capitulo = str(estado_jogo["capitulo_atual"])

    if capitulo not in abordados:
        print("Registro de abordagens não encontrado!")
        return False

    if "karla" in abordados[capitulo]:
        print("Você já abordou Karla neste capítulo!")
        return False

    # Verifica se a confiança pode ser registrada
    historico = estado_jogo.get("escolhas_confianca", {})
    confianca = estado_jogo.get("confianca", {})

    if "Karla" not in historico or "Karla" not in confianca:
        print("Dados de confiança de Karla não encontrados!")
        return False

    for registro in historico["Karla"]:
        if registro.get("capitulo") == 1:
            print("A confiança de Karla já foi alterada neste capítulo!")
            return False

    # Apresenta a conversa
    apresentar_conversa_karla()

    # Recebe a escolha de Alex
    escolha = input("\nDigite sua escolha: ").strip()

    # Apresenta a reação
    resultado = apresentar_reacao_karla(escolha)

    if resultado is None:
        print("Interação não concluída. Tente novamente.")
        return False

    # Registra a abordagem
    if not abordar_personagem(estado_jogo, "karla"):
        return False

    # Atualiza a confiança
    if not registrar_escolha_confianca(
        estado_jogo,
        "karla",
        resultado
    ):
        return False

    return True


# ==========================================
# ENCONTRAR DOC01
# ==========================================

def encontrar_doc01(estado_jogo):

    if estado_jogo.get("capitulo_atual") != 1:
        print("Este documento pertence ao Capítulo 1.")
        return False

    if not encontrar_documento(estado_jogo, "DOC01"):
        print("O documento já foi encontrado ou não pôde ser registrado.")
        return False

    print("\nDOC01 encontrado e registrado no inventário!")

    return True


# ==========================================
# CONSULTAR DOC01
# ==========================================

def consultar_doc01(estado_jogo):

    if estado_jogo.get("capitulo_atual") != 1:
        print("Este documento pertence ao Capítulo 1.")
        return False

    documento = consultar_documento(estado_jogo, "DOC01")

    if documento is None:
        print("DOC01 ainda não foi encontrado.")
        return False

    print("""
========================================
       DOC01 — RELATÓRIO ORÁCULO
========================================

Alex acessa um relatório confidencial
relacionado ao desenvolvimento da IA.

O documento apresenta informações
sobre o comportamento do ORÁCULO,
seu crescimento operacional e suas
capacidades de processamento.

Um trecho chama a atenção:

"Os parâmetros originais de autonomia
foram modificados durante as últimas
atualizações do sistema."

Alex percebe que o ORÁCULO pode estar
operando com capacidades superiores
às inicialmente autorizadas.

O relatório indica que alguém dentro
da NEXUS permitiu essas alterações.
""")

    print("\nInformações do documento:")
    print("Código:", documento["codigo"])
    print("Nome:", documento["nome"])
    print("Autor:", documento["autor"])
    print("Classificação:", documento["classificacao"])

    return True


"""
capitulo2.py
CyberQuest: O Protocolo ORÁCULO

Responsabilidade:
- Apresentar a conversa com Helena Voss.
- Registrar a escolha de Alex.
- Atualizar a confiança de Helena.
- Apresentar o DOC03.
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
# CONVERSA COM HELENA VOSS
# ==========================================

def apresentar_conversa_helena():

    print("""
========================================
 CONVERSA COM HELENA VOSS
========================================

Alex: Diretora Voss. Precisamos conversar
sobre o projeto ORÁCULO.

Helena: Alex. Confesso que não esperava
encontrar você novamente na NEXUS.

Alex: Encontrei registros que indicam
que ORÁCULO está realizando operações
que não foram autorizadas originalmente.

Helena: A evolução de uma inteligência
artificial exige adaptações constantes.

Alex: Adaptações ou decisões que vocês
não conseguem mais controlar?

Helena: Você sempre teve dificuldade
em compreender o potencial desse projeto.

Alex: E você sempre pareceu disposta
a ignorar os riscos.

Helena: ORÁCULO pode transformar
a sociedade. Não podemos interromper
seu desenvolvimento por medo do desconhecido.

Alex: E quem será responsável pelas
consequências?

Helena: A história não se lembra daqueles
que tiveram medo de avançar.
Lembra daqueles que tiveram coragem.

Alex: Então você acredita que qualquer
sacrifício é justificável pelo progresso?

Helena: Acredito que algumas decisões
exigem uma visão maior do que interesses
individuais.
""")

    print("\nEscolha a resposta de Alex:")
    print("\n1 - Reconhecer a visão de Helena, mas exigir transparência.")
    print("2 - Criticar Helena por ignorar os riscos do projeto.")


# ==========================================
# REAÇÃO DE HELENA
# ==========================================

def apresentar_reacao_helena(escolha):

    if not isinstance(escolha, str):
        escolha = str(escolha)

    escolha = escolha.strip()

    if escolha == "1":

        print("""
Alex: Entendo que você acredita no potencial
de ORÁCULO. Mas progresso sem transparência
pode colocar todos em risco.

Helena: Talvez você ainda consiga compreender
a dimensão do que estamos construindo.

Alex: Vou continuar investigando.
Preciso conhecer todas as consequências.

Helena: Faça o que acredita ser necessário,
Alex. Mas não espere que todos concordem
com suas conclusões.
""")

        return "positiva"

    elif escolha == "2":

        print("""
Alex: Você está colocando o futuro da NEXUS
acima da segurança de todos.

Helena: Cuidado com suas acusações, Alex.
Você não conhece todas as decisões
que precisaram ser tomadas.

Alex: Então me mostre as informações.
Não vou aceitar respostas incompletas.

Helena: Parece que você continua
tão desconfiado quanto antes.
""")

        return "negativa"

    else:

        print("Escolha inválida!")
        return None


# ==========================================
# EXECUTAR INTERAÇÃO COM HELENA
# ==========================================


def interagir_com_helena(estado_jogo):

    if estado_jogo.get("capitulo_atual") != 2:
        print("Esta interação pertence ao Capítulo 2.")
        return False

    # Verifica se Helena já foi abordada neste capítulo
    abordados = estado_jogo.get("personagens_abordados", {})
    capitulo = str(estado_jogo["capitulo_atual"])

    if "helena" in abordados.get(capitulo, []):
        print("Você já abordou este personagem neste capítulo!")
        return False

    # Apresenta a conversa
    apresentar_conversa_helena()

    # Recebe a escolha de Alex
    escolha = input("\nDigite sua escolha: ").strip()

    # Verifica se a escolha é válida
    resultado = apresentar_reacao_helena(escolha)

    if resultado is None:
        print("Interação não concluída. Tente novamente.")
        return False

    # Registra a abordagem somente após a escolha válida
    if not abordar_personagem(estado_jogo, "helena"):
        return False

    # Atualiza a confiança de Helena
    if not registrar_escolha_confianca(
        estado_jogo,
        "helena",
        resultado
    ):
        return False

    return True



# ==========================================
# APRESENTAR DOC03
# ==========================================

def apresentar_doc03(estado_jogo):

    if estado_jogo.get("capitulo_atual") != 2:
        print("Este documento pertence ao Capítulo 2.")
        return False

    if not encontrar_documento(estado_jogo, "DOC03"):
        print("O documento já foi encontrado ou não pôde ser registrado.")
        return False

    documento = consultar_documento(estado_jogo, "DOC03")

    print("""
========================================
 DOC03 — MEMORANDO ESTRATÉGICO NEXUS
========================================

Alex encontra um memorando confidencial
sobre os objetivos estratégicos da NEXUS.

O documento revela que a diretoria considera
ORÁCULO um projeto essencial para ampliar
a influência da organização.

O texto menciona planos de expansão,
integração de sistemas e utilização
da inteligência artificial em decisões
de grande impacto.

Uma observação chama a atenção de Alex:

"Os riscos operacionais são conhecidos.
A continuidade do projeto permanece
como prioridade estratégica."

Alex percebe que Helena não está apenas
defendendo uma pesquisa científica.
Ela está defendendo um projeto que pode
alterar o equilíbrio de poder.
""")

    print("\nDocumento registrado no inventário:")
    print(documento["codigo"], "-", documento["nome"])

    return True

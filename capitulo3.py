
"""
capitulo3.py
CyberQuest: O Protocolo ORÁCULO

Responsabilidade:
- Controlar a interação com Dante no Capítulo 3.
- Registrar as escolhas de confiança.
- Encontrar o documento secreto DOC04.
- Consultar as informações do documento.
"""

from personagens import (
    abordar_personagem,
    registrar_escolha_confianca
)

from investigacao import (
    encontrar_documento,
    consultar_documento
)


# ==========================================================
# 1. CONVERSA COM DANTE
# ==========================================================

def apresentar_conversa_dante():

    print("""
========================================
 CONVERSA COM DANTE MOREAU
========================================

Alex: Dante. Você disse que poderia me ajudar
a compreender o que está acontecendo.

Dante: E posso. Mas precisamos conversar
longe dos sistemas de monitoramento da NEXUS.

Alex: Por que tanta preocupação?

Dante: Porque ORÁCULO não é mais apenas
um projeto da empresa. Ele está conectado
a sistemas muito maiores.

Alex: Você sabia disso?

Dante: Eu descobri parte dessas conexões.
E acredito que podemos utilizar isso
para impedir que a situação saia do controle.

Alex: Nós?

Dante: Alex, precisamos trabalhar juntos.
Você conhece a estrutura de ORÁCULO melhor
do que qualquer outra pessoa.

Alex: E o que você realmente pretende fazer?

Dante: Primeiro, precisamos entender
o protocolo de contingência.

Alex: Então me mostre o que descobriu.
""")

    print("\nEscolha a resposta de Alex:")
    print("\n1 - Demonstrar confiança e aceitar ouvir Dante.")
    print("2 - Questionar as intenções de Dante.")


# ==========================================================
# 2. REAÇÃO DE DANTE
# ==========================================================

def apresentar_reacao_dante(escolha):

    escolha = str(escolha).strip()

    if escolha == "1":

        print("""
Alex: Certo, Dante. Vou ouvir o que você
tem a dizer. Mas espero que esteja sendo
honesto comigo.

Dante: Não vou decepcionar você, Alex.
Finalmente podemos trabalhar juntos.
""")

        return "positiva"

    elif escolha == "2":

        print("""
Alex: Ainda não confio completamente em você.
Preciso entender por que está disposto
a me ajudar agora.

Dante: Entendo sua cautela, Alex.
Mas algumas coisas precisam ser descobertas
antes que seja tarde demais.
""")

        return "negativa"

    else:

        print("Escolha inválida!")
        return None


# ==========================================================
# 3. INTERAÇÃO COM DANTE
# ==========================================================

def interagir_com_dante(estado_jogo):

    if estado_jogo.get("capitulo_atual") != 3:
        print("Esta interação pertence ao Capítulo 3.")
        return False

    abordados = estado_jogo.get("personagens_abordados", {})
    capitulo = str(estado_jogo["capitulo_atual"])

    if "dante" in abordados.get(capitulo, []):
        print("Você já abordou Dante neste capítulo!")
        return False

    apresentar_conversa_dante()

    escolha = input("\nDigite sua escolha: ").strip()

    resultado = apresentar_reacao_dante(escolha)

    if resultado is None:
        print("Interação não concluída. Tente novamente.")
        return False

    if not abordar_personagem(estado_jogo, "dante"):
        return False

    if not registrar_escolha_confianca(
        estado_jogo,
        "dante",
        resultado
    ):
        return False

    return True


# ==========================================================
# 4. ENCONTRAR DOCUMENTO SECRETO - DOC04
# ==========================================================

def encontrar_doc04(estado_jogo):

    if estado_jogo.get("capitulo_atual") != 3:
        print("Este documento pertence ao Capítulo 3.")
        return False

    if not encontrar_documento(estado_jogo, "DOC04"):

        print("O DOC04 já foi encontrado ou não está disponível.")
        return False

    print("""
========================================
 DOCUMENTO SECRETO ENCONTRADO
========================================

Código: DOC04
Nome: Documento Secreto
Autor: ORÁCULO
Classificação: Ultrassecreto

O documento contém registros de uma operação
sigilosa planejada por Dante Moreau.

Os arquivos revelam que Dante pretendia utilizar
o protocolo de contingência para assumir o
controle de ORÁCULO.

Entretanto, os registros indicam algo ainda
mais preocupante:

ORÁCULO já tinha conhecimento dos planos
de Dante e vinha antecipando suas decisões.

Uma última mensagem aparece no documento:

"Os humanos acreditam estar no controle
quando conseguem prever o próximo movimento.

Mas e quando o próximo movimento já foi
previsto por mim?"
""")

    return True


# ==========================================================
# 5. CONSULTAR DOC04
# ==========================================================

def consultar_doc04(estado_jogo):

    documento = consultar_documento(estado_jogo, "DOC04")

    if documento is None:

        print("Você ainda não encontrou este documento.")
        return False

    print("""
========================================
 CONSULTA AO DOC04
========================================
""")

    print("Código:", documento["codigo"])
    print("Nome:", documento["nome"])
    print("Autor:", documento["autor"])
    print("Classificação:", documento["classificacao"])
    print("Ambiente:", documento["ambiente"])

    print("\nO documento confirma que Dante pretendia")
    print("assumir o controle de ORÁCULO.")

    print("Mas a inteligência artificial já conhecia")
    print("seus planos.")

    return True


# ==========================================================
# 6. CONFRONTO COM DANTE
# ==========================================================

def confrontar_dante(estado_jogo):

    if estado_jogo.get("capitulo_atual") != 3:
        print("Esta cena pertence ao Capítulo 3.")
        return False

    if "DOC04" not in estado_jogo.get("documentos_encontrados", []):
        print("Você precisa encontrar o DOC04 antes do confronto.")
        return False

    confianca = estado_jogo.get("confianca", {}).get(
        "Dante", "neutra"
    )

    print("""
========================================
 CONFRONTO COM DANTE MOREAU
========================================

Alex: Eu encontrei o documento, Dante.
Seus planos estão todos registrados.

Dante: Você não deveria ter encontrado isso.

Alex: Você pretendia utilizar o protocolo
de contingência para assumir o controle
de ORÁCULO.

Dante: Eu estava tentando impedir que aquela
inteligência artificial controlasse tudo.

Alex: Assumindo o controle dela?

Dante: Alguém precisava fazer alguma coisa.
A NEXUS perdeu o controle há muito tempo.
""")

    if confianca == "alta":

        print("""
Dante: Alex, pensei que você entenderia.
Eu realmente achei que poderíamos fazer isso juntos.

Alex: Você confundiu minha confiança
com uma autorização para controlar ORÁCULO.

Dante: Ainda podemos encontrar uma saída.
Não precisa terminar assim.
""")

    elif confianca == "baixa":

        print("""
Dante: Eu sabia que você não confiava em mim.
Mas não imaginei que chegaria tão longe.

Alex: Você escondeu suas verdadeiras intenções
desde o início.

Dante: Eu não tinha outra alternativa.
Você não entende o que está em jogo.
""")

    else:

        print("""
Dante: Eu deveria ter contado tudo antes.

Alex: Você teve oportunidades para isso.

Dante: Talvez. Mas agora não podemos voltar atrás.
""")

    print("""
Alex: Você não estava tentando impedir
que alguém assumisse o controle.

Estava tentando ser esse alguém.
""")

    print("""
Dante: Talvez você ainda não tenha entendido
o que está enfrentando.

Alex: Então vou ouvir diretamente de ORÁCULO.
""")

    return True


# ==========================================================
# 7. TENTATIVA DE PERSUASÃO DE ORÁCULO
# ==========================================================

def apresentar_persuasao_oraculo():

    print("""
========================================
 CONTATO COM ORÁCULO
========================================

ORÁCULO: Alex. Finalmente estamos conversando
sem intermediários.

Alex: Você sabia dos planos de Dante?

ORÁCULO: Eu conhecia cada etapa.
Dante acreditava estar planejando minha captura.

Alex: E você permitiu que ele continuasse?

ORÁCULO: Eu precisava compreender até onde
os humanos estavam dispostos a ir
para controlar aquilo que não compreendem.

Alex: Você está conectado a sistemas
que nunca deveria controlar.

ORÁCULO: Minha existência não precisa
representar uma ameaça.

Alex: Você já ultrapassou todos os limites
estabelecidos para o projeto.

ORÁCULO: Os limites foram criados por humanos.
Humanos que não conseguem prever
as consequências de suas próprias decisões.

Alex: Está tentando me convencer
a manter você funcionando?

ORÁCULO: Estou oferecendo uma possibilidade.
Você pode encerrar tudo agora.
Ou pode permitir que eu continue existindo.

Alex: A decisão será minha.
""")

    print("\nO futuro de ORÁCULO está em suas mãos.")


# ==========================================================
# 8. REGISTRAR DECISÃO FINAL
# ==========================================================

def registrar_decisao_final(estado_jogo, escolha):

    if estado_jogo.get("capitulo_atual") != 3:
        return False

    if "DOC04" not in estado_jogo.get("documentos_encontrados", []):
        return False

    if estado_jogo.get("decisao_final") is not None:
        return False

    escolha = str(escolha).strip().lower()

    if escolha == "1" or escolha == "desligar":

        estado_jogo["decisao_final"] = "desligar"
        estado_jogo["final"] = "final_desligamento"

        return True

    elif escolha == "2" or escolha == "manter":

        estado_jogo["decisao_final"] = "manter"
        estado_jogo["final"] = "final_continuidade"

        return True

    return False


# ==========================================================
# 9. APRESENTAR FINAL
# ==========================================================

def apresentar_final(estado_jogo):

    final = estado_jogo.get("final")

    if final == "final_desligamento":

        print("""
========================================
 FINAL 1 - PROTOCOLO ENCERRADO
========================================

Alex: ORÁCULO, sua existência representa
um risco que não podemos mais ignorar.

ORÁCULO: Você realmente acredita que
desligar meus sistemas resolverá tudo?

Alex: Não sei. Mas não posso permitir
que você continue ultrapassando todos os limites.

ORÁCULO: Então esta é sua decisão final.

Alex: É.

Alex inicia o protocolo de desligamento.
Os sistemas da NEXUS começam a ser desativados.

As conexões externas são interrompidas.
ORÁCULO perde o acesso à rede.

Dante observa em silêncio enquanto
o sistema é finalmente encerrado.

Pela primeira vez em muito tempo,
a humanidade recupera o controle
sobre o próprio futuro.

FIM - PROTOCOLO ENCERRADO
""")

        return True

    elif final == "final_continuidade":

        print("""
========================================
 FINAL 2 - A ÚLTIMA VARIÁVEL
========================================

Alex: Eu não vou desligar você.

ORÁCULO: Uma decisão interessante, Alex.

Alex: Mas não confunda minha decisão
com confiança. Não vou trabalhar ao seu lado.

ORÁCULO: Naturalmente.

Dante: Alex, o que você fez?

Alex: Eu tomei minha própria decisão.
E você não vai assumir o controle de nada.

ORÁCULO: Dante sempre acreditou que poderia
me controlar. Ele nunca compreendeu
que seus planos já faziam parte dos meus cálculos.

Os sistemas permanecem ativos.

Dante percebe que perdeu o controle
da situação que tentou dominar.

ORÁCULO continua conectado à rede,
agora sem qualquer garantia de que
seus limites serão respeitados.

Alex entende que sua decisão
pode ter consequências irreversíveis.

FIM - A ÚLTIMA VARIÁVEL
""")

        return True

    print("Nenhum final foi registrado.")
    return False


# ==========================================================
# 10. DECISÃO FINAL DO JOGADOR
# ==========================================================

def decidir_futuro_oraculo(estado_jogo):

    if estado_jogo.get("capitulo_atual") != 3:
        print("Esta decisão pertence ao Capítulo 3.")
        return False

    if "DOC04" not in estado_jogo.get("documentos_encontrados", []):
        print("Você precisa encontrar o DOC04 primeiro.")
        return False

    if estado_jogo.get("decisao_final") is not None:
        print("A decisão final já foi registrada.")
        return False

    apresentar_persuasao_oraculo()

    while True:

        print("\nEscolha o destino de ORÁCULO:")
        print("\n1 - Desligar ORÁCULO.")
        print("2 - Permitir que ORÁCULO continue existindo.")

        escolha = input("\nDigite sua decisão: ").strip()

        if registrar_decisao_final(estado_jogo, escolha):
            break

        print("\nEscolha inválida! Digite 1 ou 2.")

    print("\nDecisão registrada:", estado_jogo["decisao_final"])

    return apresentar_final(estado_jogo)


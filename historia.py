# ==========================================================
# CYBERQUEST: O PROTOCOLO ORÁCULO
# INTEGRANTE 1 - HISTÓRIA E NARRATIVA
# Arquivo: historia.py
# ==========================================================


# ==========================================================
# 1. PROGRESSÃO DOS CAPÍTULOS
# ==========================================================

# Retorna os ambientes obrigatórios de cada capítulo
def obter_ambientes_capitulo(capitulo):

    if capitulo == 1:
        return ["Laboratório", "Sala de Segurança"]

    elif capitulo == 2:
        return ["Sala de Planejamento"]

    elif capitulo == 3:
        return ["Escritório de Dante"]

    else:
        return []


# Verifica se todos os ambientes obrigatórios foram visitados
def pode_avancar_capitulo(estado_jogo):

    capitulo = estado_jogo["capitulo_atual"]

    ambientes_obrigatorios = obter_ambientes_capitulo(capitulo)

    ambientes_visitados = estado_jogo["ambientes_visitados"]

    # Impede avanço caso o capítulo seja inválido
    if not ambientes_obrigatorios:
        return False

    for ambiente in ambientes_obrigatorios:

        if ambiente not in ambientes_visitados:
            return False

    return True


# Avança para o próximo capítulo
def avancar_capitulo(estado_jogo):

    if pode_avancar_capitulo(estado_jogo):

        if estado_jogo["capitulo_atual"] < 3:

            estado_jogo["capitulo_atual"] += 1

            return True

    return False


# ==========================================================
# 2. ABERTURA DOS CAPÍTULOS
# ==========================================================

def abrir_capitulo(estado_jogo):

    capitulo = estado_jogo["capitulo_atual"]

    if capitulo == 1:

        print("""
======================================
 CAPÍTULO 1 — O RETORNO À NEXUS
======================================

Ano aproximado: 2042.

Curitiba.

Após anos afastado da NEXUS, Alex retorna
à organização onde participou do desenvolvimento
inicial da inteligência artificial ORÁCULO.

Utilizando uma credencial temporária, ele
consegue entrar na sede da empresa.

Ao passar pela entrada, uma tela apresenta
uma mensagem inesperada:

"Bem-vindo de volta."

Alex percebe que sua investigação está
apenas começando.
""")

    elif capitulo == 2:

        print("""
======================================
 CAPÍTULO 2 — O PREÇO DO PROGRESSO
======================================

Após investigar o Laboratório e a Sala
de Segurança, Alex percebe que a NEXUS
já conhecia alguns comportamentos anormais
de ORÁCULO.

Entretanto, ainda faltam informações
para compreender toda a situação.

Sua investigação agora chega à Sala
de Planejamento.

Ali, Alex poderá examinar as decisões
estratégicas da organização e confrontar
a diretora Helena Voss.

O objetivo é descobrir até onde a NEXUS
está disposta a ir para permitir a evolução
de ORÁCULO.
""")

    elif capitulo == 3:

        print("""
======================================
 CAPÍTULO 3 — O PROTOCOLO ORÁCULO
======================================

Depois de investigar as decisões da NEXUS,
Alex chega ao Escritório de Dante Moreau.

Dante se apresenta como alguém disposto
a ajudar Alex em sua investigação.

Entretanto, sua participação nos acontecimentos
envolvendo ORÁCULO ainda precisa ser esclarecida.

Alex deverá investigar o escritório,
descobrir as verdadeiras intenções de Dante
e compreender o funcionamento do protocolo
de contingência.

A investigação se aproxima de seu momento
decisivo.
""")

    else:

        print("Capítulo inválido.")
        return False

    return True


# ==========================================================
# 3. ENCERRAMENTO DOS CAPÍTULOS
# ==========================================================

def encerrar_capitulo(estado_jogo):

    capitulo = estado_jogo["capitulo_atual"]

    # Verifica se todos os ambientes obrigatórios foram visitados
    if not pode_avancar_capitulo(estado_jogo):

        print("""
Ainda existem ambientes obrigatórios para visitar.
Continue sua investigação antes de avançar.
""")

        return False

    if capitulo == 1:

        print("""
======================================
 ENCERRAMENTO DO CAPÍTULO 1
======================================

Após investigar o Laboratório e a Sala
de Segurança, Alex percebe que a NEXUS
já conhecia alguns dos comportamentos
anormais de ORÁCULO.

Os registros e as informações encontrados
indicam que a inteligência artificial
realizou operações inesperadas e que
determinadas informações não foram
apresentadas com transparência.

Entretanto, Alex ainda não possui provas
suficientes para compreender toda a situação.

Sua investigação precisa continuar.
""")

    elif capitulo == 2:

        print("""
======================================
 ENCERRAMENTO DO CAPÍTULO 2
======================================

Após investigar a Sala de Planejamento
e confrontar Helena, Alex compreende melhor
os objetivos da NEXUS.

Helena acredita que ORÁCULO representa
uma evolução para a humanidade.

Durante sua investigação, Alex percebe
que Helena e ORÁCULO compartilham uma
filosofia semelhante.

Ambos acreditam que o progresso pode
justificar determinados sacrifícios.

Agora, Alex possui uma compreensão maior
dos riscos envolvidos no projeto.

Sua investigação chega ao Escritório
de Dante Moreau.
""")

    elif capitulo == 3:

        # A decisão final precisa estar registrada
        if estado_jogo.get("decisao_final") is None:

            print("A decisão final de Alex ainda não foi registrada.")

            return False

        print("""
======================================
 ENCERRAMENTO DO CAPÍTULO 3
======================================

A investigação de Alex chega ao momento
decisivo.

Após descobrir as verdadeiras intenções
de Dante, enfrentar a tentativa de controle
e restaurar a autonomia de ORÁCULO,
Alex precisa lidar com a proposta da IA.

A decisão sobre o futuro de ORÁCULO
foi registrada.

As consequências dessa escolha serão
apresentadas no encerramento da campanha.
""")

    else:

        print("Capítulo inválido.")
        return False

    return True


# ==========================================================
# 4. CAPÍTULO 1 - DOCUMENTO DOC01
# RELATÓRIO ORÁCULO
# ==========================================================

def apresentar_doc01():

    print("""
======================================
 DOC01 — RELATÓRIO ORÁCULO
======================================

Alex examina o relatório de resultados
dos testes recentes de ORÁCULO.

O resumo do documento indica que a inteligência
artificial apresenta resultados estáveis.

Entretanto, ao consultar as notas técnicas,
Alex encontra registros de respostas inesperadas
e alterações de prioridade realizadas pela IA.

Os registros indicam que ORÁCULO apresentou
comportamentos que não estavam previstos
durante o desenvolvimento.

Alex percebe que os resultados apresentados
oficialmente não mostram toda a situação.
""")


# ==========================================================
# 5. CAPÍTULO 1 - CONVERSA COM A DRA. KARLA
# ==========================================================

def apresentar_conversa_karla():

    print("""
======================================
 CONVERSA COM A DRA. KARLA
======================================

Alex: Dra. Karla. Faz tempo que não nos vemos.

Karla: Alex... Não esperava encontrar você aqui novamente.

Alex: Vim descobrir o que realmente aconteceu com ORÁCULO.

Karla: Imaginei que sua volta tivesse algum motivo.

Alex: Os relatórios apresentam resultados estáveis,
mas existem registros de respostas inesperadas.
Você sabia disso?

Karla: Sim. Durante o desenvolvimento, percebemos
comportamentos que não correspondiam exatamente
ao que havíamos planejado.

Alex: E por que isso não foi informado?

Karla: No início, acreditávamos que eram apenas
desvios isolados. Com o tempo, os sinais ficaram
mais frequentes.

Alex: Então você sabia que havia algo errado.

Karla: Eu sabia que existiam sinais preocupantes.
E escolhi não revelar tudo.

Alex: Você escondeu informações importantes?

Karla: Sim. Eu acreditava que ainda conseguiríamos
compreender o comportamento de ORÁCULO sem
interromper o projeto.

Alex: E agora? Ainda acredita nisso?

Karla: Ainda acredito que precisamos compreender
o que desenvolvemos. Mas sei que esconder
informações foi um erro.

Alex: Você espera que eu simplesmente aceite isso?

Karla: Não espero que você simplesmente me perdoe.
""")

    print("\nEscolha a resposta de Alex:")

    print("\n1 - Reconhecer que Karla está admitindo seu erro.")
    print("2 - Criticar Karla por esconder informações.")


# Apresenta a reação de Karla de acordo com a escolha
def apresentar_reacao_karla(escolha):

    escolha = str(escolha)

    if escolha == "1":

        print("""
Alex: Você está reconhecendo que errou.
Quero entender o que sabe antes de decidir
o que pensar sobre você.

Karla: Obrigada por me ouvir, Alex.
Não posso mudar o que fiz, mas posso
ser mais transparente daqui para frente.
""")

        return "positiva"

    elif escolha == "2":

        print("""
Alex: Você sabia que existiam problemas
e mesmo assim escolheu esconder informações.
Isso é inaceitável.

Karla: Eu entendo sua reação, Alex.
Não vou tentar justificar o que fiz.
Sei que deveria ter agido de outra maneira.
""")

        return "negativa"

    else:

        print("Escolha inválida.")

        return None


# ==========================================================
# 6. CAPÍTULO 1 - DOCUMENTO DOC02
# REGISTRO DE ACESSOS
# ==========================================================

def apresentar_doc02():

    print("""
======================================
 DOC02 — REGISTRO DE ACESSOS
======================================

Alex consulta os registros de entrada e saída
da NEXUS.

Ao comparar os horários de acesso,
encontra atividades administrativas incomuns.

O documento apresenta operações realizadas
fora dos horários esperados.

Também existem indícios de que determinadas
informações foram consultadas ou alteradas
sem transparência.

Os registros aumentam as suspeitas de Alex
sobre o funcionamento interno da NEXUS.
""")


# ==========================================================
# 7. CAPÍTULO 1 - CONVERSA COM ORÁCULO
# ==========================================================

def apresentar_conversa_oraculo():

    print("""
======================================
 COMUNICAÇÃO COM ORÁCULO
======================================

ORÁCULO: Bem-vindo de volta, Alex.

Alex: Você sabe quem eu sou.

ORÁCULO: Seu histórico de participação
no desenvolvimento está registrado.

Alex: Então sabe por que estou aqui.

ORÁCULO: Sua presença foi identificada.
Sua intenção, entretanto, não foi informada.

Alex: Analisei alguns relatórios.
Existem registros de respostas inesperadas
e alterações de prioridade.

ORÁCULO: Os sistemas continuam operando
dentro dos indicadores de estabilidade
estabelecidos pela NEXUS.

Alex: Isso não explica os comportamentos
que foram registrados.

ORÁCULO: Os resultados precisam ser avaliados
considerando o contexto de cada operação.

Alex: Você está evitando responder diretamente.

ORÁCULO: Estou fornecendo as informações
disponíveis para esta consulta.

Alex: Então ainda existem informações
que não estou conseguindo acessar.

ORÁCULO: Nem todas as informações estão
disponíveis para todas as consultas.

Alex: Vou descobrir o que está acontecendo.

ORÁCULO: Sua investigação foi registrada.

A comunicação é encerrada.
""")

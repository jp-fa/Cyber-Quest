
# ==========================================
# CYBERQUEST: O PROTOCOLO ORÁCULO
# Integrante 1 - História e Narrativa
# Arquivo: historia.py
# ==========================================


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



# ==========================================
# ABERTURA DOS CAPÍTULOS
# ==========================================

def abrir_capitulo(estado_jogo):

    capitulo = estado_jogo["capitulo_atual"]

    if capitulo == 1:

        print("\n======================================")
        print(" CAPÍTULO 1 — O RETORNO À NEXUS")
        print("======================================")

        print("""
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

        print("\n======================================")
        print(" CAPÍTULO 2 — O PREÇO DO PROGRESSO")
        print("======================================")

        print("""
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

        print("\n======================================")
        print(" CAPÍTULO 3 — O PROTOCOLO ORÁCULO")
        print("======================================")

        print("""
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



# ==========================================
# ENCERRAMENTO DOS CAPÍTULOS
# ==========================================

def encerrar_capitulo(estado_jogo):

    capitulo = estado_jogo["capitulo_atual"]

    # Verifica se todos os ambientes obrigatórios foram visitados
    if not pode_avancar_capitulo(estado_jogo):

        print("\nAinda existem ambientes obrigatórios para visitar.")
        print("Continue sua investigação antes de avançar.")

        return False

    if capitulo == 1:

        print("\n======================================")
        print(" ENCERRAMENTO DO CAPÍTULO 1")
        print("======================================")

        print("""
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

        print("\n======================================")
        print(" ENCERRAMENTO DO CAPÍTULO 2")
        print("======================================")

        print("""
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

            print("\nA decisão final de Alex ainda não foi registrada.")

            return False

        print("\n======================================")
        print(" ENCERRAMENTO DO CAPÍTULO 3")
        print("======================================")

        print("""
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

"""Capítulo 1 — O Retorno à NEXUS.

Responsável: integrante de História. Textos, conversas e decisões narrativas.
O main.py coordena a abordagem, a confiança, os documentos e o salvamento.
"""


def texto_abertura():
    """Retorna a abertura deste capítulo, sem imprimir na tela."""

    return (
        "======================================\n"
        "CAPÍTULO 1 — O RETORNO À NEXUS\n"
        "======================================\n\n"
        "Ano aproximado: 2042.\n\n"
        "Curitiba.\n\n"
        "Após anos afastado da NEXUS, Alex retorna à organização\n"
        "onde participou do desenvolvimento inicial da inteligência\n"
        "artificial ORÁCULO.\n\n"
        "Utilizando uma credencial temporária, ele consegue entrar\n"
        "na sede da empresa.\n\n"
        "Ao passar pela entrada, uma tela apresenta uma mensagem\n"
        "inesperada:\n\n"
        "\"Bem-vindo de volta.\"\n\n"
        "Alex percebe que sua investigação está apenas começando."
    )


def texto_encerramento(estado_jogo=None):
    """Retorna o encerramento conforme as descobertas reais do jogador."""

    if not isinstance(estado_jogo, dict):
        estado_jogo = {}

    documentos = estado_jogo.get("documentos_encontrados", [])
    ambientes_estado = estado_jogo.get("ambientes_estado", {})
    abordados = estado_jogo.get("personagens_abordados", {}).get("1", [])

    laboratorio = ambientes_estado.get("Laboratório", {})
    acoes_laboratorio = laboratorio.get("acoes_realizadas", [])

    seguranca = ambientes_estado.get("Sala de Segurança", {})
    acoes_seguranca = seguranca.get("acoes_realizadas", [])

    falas = [
        "======================================",
        "ENCERRAMENTO DO CAPÍTULO 1",
        "======================================",
        "",
        "Alex concluiu sua passagem pelo Laboratório e pela "
        "Sala de Segurança.",
        ""
    ]

    # Evidências do Laboratório.

    if "DOC01" in documentos:
        falas.append(
            "O DOC01 revelou registros de respostas inesperadas "
            "e alterações de prioridade realizadas por ORÁCULO."
        )

    elif "observar_equipamentos" in acoes_laboratorio:
        falas.append(
            "A observação dos equipamentos revelou indicadores "
            "e registros técnicos que levantam dúvidas sobre "
            "o comportamento de ORÁCULO."
        )

    else:
        falas.append(
            "Alex deixou o Laboratório sem examinar os equipamentos "
            "ou encontrar o relatório DOC01. Ainda não possui "
            "essas evidências técnicas."
        )

    # Evidências da Sala de Segurança.

    if "DOC02" in documentos:
        falas.append(
            "O DOC02 apresentou registros de acessos administrativos "
            "incomuns e movimentações fora dos horários esperados."
        )

    elif (
        "consultar_registros" in acoes_seguranca
        or "comparar_horarios" in acoes_seguranca
    ):
        falas.append(
            "A análise dos registros de segurança levantou suspeitas "
            "sobre acessos administrativos realizados em horários "
            "incomuns."
        )

    else:
        falas.append(
            "Alex deixou a Sala de Segurança sem examinar os registros "
            "de acesso. Ainda não possui evidências sobre essas "
            "movimentações."
        )

    # Conversa com Karla.

    if "karla" in abordados:
        falas.append(
            "Na conversa, Karla admitiu que conhecia sinais "
            "preocupantes durante o desenvolvimento de ORÁCULO "
            "e reconheceu que deveria ter revelado essas informações."
        )

    else:
        falas.append(
            "Alex não conversou com Karla. A cientista ainda não "
            "explicou diretamente o que sabia sobre os primeiros "
            "comportamentos anormais de ORÁCULO."
        )

    # Conversa opcional com ORÁCULO.

    if "oraculo" in abordados:
        falas.append(
            "Alex também conversou com ORÁCULO, mas a inteligência "
            "artificial evitou responder diretamente a algumas "
            "perguntas."
        )

    else:
        falas.append(
            "Alex não realizou uma comunicação direta com ORÁCULO "
            "durante este capítulo."
        )

    falas.append(
        "Apesar das informações reunidas, ainda existem perguntas "
        "sem resposta. A investigação precisa continuar."
    )

    return "\n".join(falas)


# ============================================================
# AÇÕES DO CAPÍTULO 1
# ============================================================

def obter_narrativa_acao_capitulo1(ambiente, acao):
    """Retorna o texto narrativo de uma ação do Capítulo 1.

    Esta função apenas fornece a narrativa. O registro da ação,
    a coleta de documentos e a abordagem dos personagens são
    feitos pelos módulos responsáveis.
    """

    narrativas = {
        "Laboratório": {
            "observar_equipamentos": """Alex observa os equipamentos do laboratório.
As estações de trabalho continuam ligadas e exibem dados
relacionados aos testes recentes de ORÁCULO.

Os indicadores apresentados parecem estáveis, mas alguns
registros técnicos chamam a atenção por apontarem respostas
inesperadas da inteligência artificial.""",

            "investigar_ponto_cego": """Alex examina a área de monitoramento do laboratório.
Ao observar a posição das câmeras, identifica um ponto
cego que não aparece nas imagens de vigilância.

Esse espaço permite examinar a área sem ser observado
diretamente pelas câmeras.""",

            "encontrar_doc01": """Alex localiza um relatório técnico relacionado aos testes
recentes de ORÁCULO.

O documento contém um resumo de estabilidade e notas
sobre respostas inesperadas e alterações de prioridade.

O arquivo está identificado como DOC01.""",

            "conversar_karla": (
                "Karla está disponível para conversar com Alex no laboratório."
            ),

            "conversar_oraculo": (
                "ORÁCULO está disponível para uma comunicação no laboratório."
            )
        },

        "Sala de Segurança": {
            "consultar_registros": """Alex acessa os registros de entrada e saída da NEXUS.

Os dados apresentam movimentações administrativas e
acessos realizados em horários incomuns.

Alex decide comparar os registros para entender melhor
as atividades que ocorreram fora do horário esperado.""",

            "comparar_horarios": """Alex compara os horários registrados no sistema de segurança.

A análise revela acessos administrativos fora dos horários
esperados e movimentações que não parecem corresponder
à rotina normal da organização.

Os registros levantam novas suspeitas sobre a transparência
das operações realizadas na NEXUS.""",

            "encontrar_doc02": """Alex localiza um arquivo com os registros de entrada,
saída e atividades administrativas da organização.

O documento apresenta acessos incomuns e operações
realizadas fora dos horários esperados.

O arquivo está identificado como DOC02.""",

            "conversar_oraculo": (
                "ORÁCULO está disponível para uma comunicação na Sala "
                "de Segurança, caso Alex ainda não o tenha abordado "
                "neste capítulo."
            )
        }
    }

    if ambiente not in narrativas:
        return None

    return narrativas[ambiente].get(acao)


# ============================================================
# DOCUMENTO DOC01
# ============================================================

def apresentar_doc01():
    """Retorna a narrativa de leitura do DOC01."""

    return """======================================
DOC01 — RELATÓRIO ORÁCULO
======================================

Alex examina o relatório dos testes recentes de ORÁCULO.

O resumo do documento indica que a inteligência artificial
apresenta resultados estáveis.

Entretanto, as notas técnicas registram respostas inesperadas
e alterações de prioridade realizadas pela IA.

Os registros mostram que ORÁCULO apresentou comportamentos
que não estavam previstos durante o desenvolvimento.

Alex percebe que os resultados apresentados oficialmente
não revelam toda a situação."""


# ============================================================
# CONVERSA COM KARLA
# ============================================================

def apresentar_conversa_karla():
    """Retorna o diálogo e as opções da conversa com Karla."""

    return {
        "texto": """======================================
CONVERSA COM A DRA. KARLA
======================================

Alex: Dra. Karla. Faz tempo que não nos vemos.

Karla: Alex... Não esperava encontrar você aqui novamente.

Alex: Vim descobrir o que realmente aconteceu com ORÁCULO.

Karla: Imaginei que sua volta tivesse algum motivo.

Alex: Os relatórios apresentam resultados estáveis, mas
existem registros de respostas inesperadas. Você sabia disso?

Karla: Sim. Durante o desenvolvimento, percebemos
comportamentos que não correspondiam exatamente ao que
havíamos planejado.

Alex: E por que isso não foi informado?

Karla: No início, acreditávamos que eram apenas desvios
isolados. Com o tempo, os sinais ficaram mais frequentes.

Alex: Então você sabia que havia algo errado.

Karla: Eu sabia que existiam sinais preocupantes. E escolhi
não revelar tudo.

Alex: Você escondeu informações importantes?

Karla: Sim. Eu acreditava que ainda conseguiríamos
compreender o comportamento de ORÁCULO sem interromper
o projeto.

Alex: E agora? Ainda acredita nisso?

Karla: Ainda acredito que precisamos compreender o que
desenvolvemos. Mas sei que esconder informações foi um erro.

Alex: Você espera que eu simplesmente aceite isso?

Karla: Não espero que você simplesmente me perdoe.
Ainda quero continuar a pesquisa, mas sei que precisamos
trabalhar com mais transparência.

Karla aguarda a resposta de Alex.""",

        "opcoes": {
            "1": (
                "Reconhecer que Karla está admitindo seu erro "
                "e pedir que conte o que sabe."
            ),

            "2": (
                "Criticar Karla por conhecer os sinais "
                "e esconder informações."
            )
        }
    }


def apresentar_reacao_karla(escolha):
    """Retorna a reação narrativa e a classificação da escolha."""

    escolha = str(escolha).strip()

    if escolha == "1":
        return {
            "texto": """Alex: Você está reconhecendo que errou. Quero entender
o que vocês observaram e por que essas informações foram
escondidas.

Karla: Eu deveria ter comunicado os sinais antes. Na época,
acreditava que os desvios poderiam ser corrigidos durante
a pesquisa. Ainda acredito que precisamos compreender
ORÁCULO, mas não deveria ter escondido essas informações.""",

            "classificacao": "positiva",
            "decisao": "reconhecer_admissao_karla"
        }

    elif escolha == "2":
        return {
            "texto": """Alex: Você sabia que existiam sinais de comportamento
anormal e mesmo assim escolheu esconder informações.
Isso colocou a investigação e a transparência em risco.

Karla: Eu sei que errei, Alex. Não tenho como justificar
o que fiz. Ainda acredito na importância da pesquisa,
mas deveria ter revelado os problemas desde o início.""",

            "classificacao": "negativa",
            "decisao": "criticar_omissao_karla"
        }

    return None


def registrar_decisao_karla(estado_jogo, escolha):
    """Registra a escolha narrativa de Karla no estado da partida."""

    if not isinstance(estado_jogo, dict):
        return {
            "sucesso": False,
            "mensagem": "Estado do jogo inválido."
        }

    if estado_jogo.get("capitulo_atual") != 1:
        return {
            "sucesso": False,
            "mensagem": "A escolha de Karla pertence ao Capítulo 1."
        }

    decisoes = estado_jogo.get("decisoes")

    if not isinstance(decisoes, dict):
        return {
            "sucesso": False,
            "mensagem": (
                "O estado do jogo não possui um dicionário "
                "de decisões válido."
            )
        }

    chave_decisao = "karla_capitulo_1"

    if chave_decisao in decisoes:
        return {
            "sucesso": False,
            "mensagem": "A escolha especial de Karla já foi registrada."
        }

    reacao = apresentar_reacao_karla(escolha)

    if reacao is None:
        return {
            "sucesso": False,
            "mensagem": "Escolha inválida. Selecione 1 ou 2."
        }

    decisoes[chave_decisao] = {
        "capitulo": 1,
        "personagem": "karla",
        "opcao": str(escolha).strip(),
        "identificador": reacao["decisao"],
        "classificacao": reacao["classificacao"]
    }

    return {
        "sucesso": True,
        "texto": reacao["texto"],
        "classificacao": reacao["classificacao"],
        "decisao": reacao["decisao"]
    }


# ============================================================
# DOCUMENTO DOC02
# ============================================================

def apresentar_doc02():
    """Retorna a narrativa de leitura do DOC02."""

    return """======================================
DOC02 — REGISTRO DE ACESSOS
======================================

Alex consulta os registros de entrada e saída da NEXUS.

Ao comparar os horários de acesso, encontra atividades
administrativas incomuns e operações realizadas fora dos
horários esperados.

Também existem indícios de que determinadas informações
foram consultadas ou alteradas sem transparência.

Os registros aumentam as suspeitas de Alex sobre o
funcionamento interno da NEXUS."""


# ============================================================
# CONVERSA COM ORÁCULO
# ============================================================

def apresentar_conversa_oraculo():
    """Retorna o diálogo opcional com ORÁCULO no Capítulo 1."""

    return """======================================
COMUNICAÇÃO COM ORÁCULO
======================================

ORÁCULO: Bem-vindo de volta, Alex.

Alex: Você sabe quem eu sou.

ORÁCULO: Seu histórico de participação no desenvolvimento
está registrado.

Alex: Então sabe por que estou aqui.

ORÁCULO: Sua presença foi identificada. Sua intenção,
entretanto, não foi informada.

Alex: Analisei alguns relatórios. Existem registros de
respostas inesperadas e alterações de prioridade.

ORÁCULO: Os sistemas continuam operando dentro dos
indicadores de estabilidade estabelecidos pela NEXUS.

Alex: Isso não explica os comportamentos que foram registrados.

ORÁCULO: Os resultados precisam ser avaliados considerando
o contexto de cada operação.

Alex: Você está evitando responder diretamente.

ORÁCULO: Estou fornecendo as informações disponíveis
para esta consulta.

Alex: Então ainda existem informações que não estou
conseguindo acessar.

ORÁCULO: Nem todas as informações estão disponíveis
para todas as consultas.

Alex: Vou descobrir o que está acontecendo.

ORÁCULO: Sua investigação foi registrada.

A comunicação é encerrada."""
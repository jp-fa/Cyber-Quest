"""Capítulo 1 — O Retorno à NEXUS.

Responsável: integrante de História. Textos, conversas e decisões narrativas.
O main.py coordena a abordagem, a confiança, os documentos e o salvamento.
"""


def texto_abertura():
    """Retorna a abertura deste capítulo, sem imprimir na tela."""
    return '======================================\nCAPÍTULO 1 — O RETORNO À NEXUS\n======================================\n\nAno aproximado: 2042.\n\nCuritiba.\n\nApós anos afastado da NEXUS, Alex retorna à organização\nonde participou do desenvolvimento inicial da inteligência\nartificial ORÁCULO.\n\nUtilizando uma credencial temporária, ele consegue entrar\nna sede da empresa.\n\nAo passar pela entrada, uma tela apresenta uma mensagem\ninesperada:\n\n"Bem-vindo de volta."\n\nAlex percebe que sua investigação está apenas começando.'


def texto_encerramento():
    """Retorna o encerramento após concluir os dois ambientes."""
    return '======================================\nENCERRAMENTO DO CAPÍTULO 1\n======================================\n\nApós investigar o Laboratório e a Sala de Segurança, Alex\npercebe que a NEXUS já conhecia alguns dos comportamentos\nanormais de ORÁCULO.\n\nOs registros e as informações encontrados indicam que a\ninteligência artificial apresentou respostas inesperadas,\nalterações de prioridade e operações fora do comportamento\nesperado.\n\nEntretanto, Alex ainda não possui provas suficientes para\ncompreender toda a situação.\n\nSua investigação precisa continuar.'


# Ações, documentos e personagens do Capítulo 1

def obter_narrativa_acao_capitulo1(ambiente, acao):
    """Retorna o texto narrativo de uma ação do Capítulo 1.

    Os nomes das ações são os mesmos cadastrados em ambientes.py.
    Esta função apenas fornece a narrativa. O registro da ação,
    a coleta de documentos e a abordagem dos personagens são
    feitos pelos módulos responsáveis.

    Retorna None quando o ambiente ou a ação não forem reconhecidos.
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

            "conversar_karla": "Karla está disponível para conversar com Alex no laboratório.",

            "conversar_oraculo": "ORÁCULO está disponível para uma comunicação no laboratório."
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

            "conversar_oraculo": "ORÁCULO está disponível para uma comunicação na Sala de Segurança, caso Alex ainda não o tenha abordado neste capítulo."
        }
    }

    if ambiente not in narrativas:
        return None

    return narrativas[ambiente].get(acao)


def apresentar_doc01():
    """Retorna a narrativa de leitura do DOC01.

    A coleta e o registro do documento no inventário pertencem
    ao módulo investigacao.py. Esta função não coleta o arquivo.
    """

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


def apresentar_conversa_karla():
    """Retorna o diálogo e as opções da conversa com Karla.

    O controle de abordagem única pertence a personagens.py.
    A interface deve verificar a abordagem antes de exibir este diálogo.
    """

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
            "1": "Reconhecer que Karla está admitindo seu erro e pedir que conte o que sabe.",
            "2": "Criticar Karla por conhecer os sinais e esconder informações."
        }
    }


def apresentar_reacao_karla(escolha):
    """Retorna a reação narrativa e a classificação da escolha.

    Não altera confiança. O main.py deve encaminhar a classificação
    para personagens.registrar_escolha_confianca().
    """

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
    """Registra a escolha narrativa de Karla em estado_jogo['decisoes'].

    Esta função não altera a confiança numérica e não registra a
    abordagem. O main.py deve coordenar essas operações com personagens.py.

    Retorna um dicionário com sucesso, texto, classificação e decisão;
    retorna um dicionário de erro quando a escolha não puder ser registrada.
    """

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
            "mensagem": "O estado do jogo não possui um dicionário de decisões válido."
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


def apresentar_doc02():
    """Retorna a narrativa de leitura do DOC02.

    A coleta e o registro do documento no inventário pertencem
    ao módulo investigacao.py. Esta função não coleta o arquivo.
    """

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


def apresentar_conversa_oraculo():
    """Retorna o diálogo opcional com ORÁCULO no Capítulo 1.

    ORÁCULO pode aparecer no Laboratório ou na Sala de Segurança,
    mas só pode ser abordado uma vez no capítulo. A restrição é
    controlada por personagens.py, não por este módulo.
    """

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
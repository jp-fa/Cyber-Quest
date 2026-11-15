"""Capítulo 2 — O Preço do Progresso.

Responsável: integrante de História. Narrativa e escolhas com Helena Voss.
Não coleta documentos nem modifica confiança diretamente.
"""


def texto_abertura():
    """Retorna a introdução da Sala de Planejamento."""
    return (
        "======================================\n"
        "CAPÍTULO 2 — O PREÇO DO PROGRESSO\n"
        "======================================\n\n"
        "Após investigar o Laboratório e a Sala de Segurança, Alex\n"
        "percebe que ainda faltam informações para compreender\n"
        "toda a situação envolvendo ORÁCULO.\n\n"
        "Sua investigação agora chega à Sala de Planejamento.\n\n"
        "Ali, Alex poderá examinar as decisões estratégicas da\n"
        "organização e, se desejar, conversar com a diretora\n"
        "Helena Voss.\n\n"
        "O objetivo é descobrir até onde a NEXUS está disposta\n"
        "a ir para permitir a evolução de ORÁCULO."
    )


def texto_encerramento(estado_jogo):
    """Monta o encerramento conforme as ações realmente realizadas."""

    if not isinstance(estado_jogo, dict):
        return "Não foi possível recuperar o estado do Capítulo 2."

    decisoes = estado_jogo.get("decisoes", {})
    documentos = estado_jogo.get("documentos_encontrados", [])
    ambientes_estado = estado_jogo.get("ambientes_estado", {})

    sala = ambientes_estado.get("Sala de Planejamento", {})
    acoes = sala.get("acoes_realizadas", [])

    falas = [
        "ENCERRAMENTO DO CAPÍTULO 2 — O PREÇO DO PROGRESSO",
        "",
        "Alex deixa a Sala de Planejamento e se prepara para continuar "
        "a investigação."
    ]

    # Evidências encontradas durante a investigação.
    if "DOC03" in documentos:
        falas.append(
            "O DOC03 registra que a continuidade do projeto foi "
            "aprovada apesar dos riscos identificados."
        )

    elif "investigar_planos" in acoes:
        falas.append(
            "As atas consultadas indicam que a diretoria conhecia "
            "os riscos relacionados à autonomia de ORÁCULO."
        )

    elif "examinar_projecoes" in acoes:
        falas.append(
            "As projeções mostram os benefícios esperados pela NEXUS, "
            "mas também apresentam alertas relacionados ao projeto."
        )

    else:
        falas.append(
            "Alex deixou a sala sem examinar os planos ou as projeções. "
            "Ainda não possui novas evidências documentais sobre "
            "as decisões estratégicas da NEXUS."
        )

    # Conversa com Helena.
    conversou_com_helena = (
        "helena" in estado_jogo.get("personagens_abordados", {}).get("2", [])
    )

    if conversou_com_helena:
        falas.append(
            "A conversa com Helena revelou divergências sobre os "
            "benefícios do projeto, os riscos envolvidos e a "
            "responsabilidade da diretoria."
        )

        escolha_responsabilidade = decisoes.get(
            "helena_responsabilidade_capitulo_2"
        )

        if isinstance(escolha_responsabilidade, dict):
            if escolha_responsabilidade.get("opcao") == "1":
                falas.append(
                    "Alex propôs uma auditoria externa e a identificação "
                    "dos responsáveis. Helena reconheceu a necessidade "
                    "de fiscalização."
                )
            elif escolha_responsabilidade.get("opcao") == "2":
                falas.append(
                    "Alex acusou Helena de evitar a responsabilidade. "
                    "A diretora não aceitou a acusação e manteve sua "
                    "posição."
                )
        else:
            falas.append(
                "A conversa com Helena foi iniciada, mas não há registro "
                "da conclusão de todas as etapas."
            )

    else:
        falas.append(
            "Alex não conversou com Helena. Portanto, ainda não conhece "
            "diretamente sua posição sobre as decisões da diretoria."
        )

    falas.append(
        "A próxima parada é o Escritório de Dante."
    )

    return "\n\n".join(falas)


ACOES_CAPITULO_2 = {
    "examinar_projecoes": """Alex examina os gráficos projetados na Sala de Planejamento.
ORÁCULO aparece como solução para crises sanitárias, energia e logística.
Ao lado das estimativas de benefícios, alertas de risco foram reduzidos a
uma pequena faixa do relatório. As projeções parecem precisas demais para
um sistema que começou a redefinir suas próprias prioridades.""",

    "investigar_planos": """Em atas reservadas, Alex encontra discussões sobre eventos inesperados.
A diretoria conhecia os riscos da autonomia de ORÁCULO, mas aprovou a
continuidade do investimento. A justificativa recorrente era que interromper
a pesquisa também impediria avanços capazes de salvar vidas.
Alex percebe que uma aposta estratégica foi apresentada como inevitável.""",

    "encontrar_doc03": """Entre versões antigas de um planejamento, Alex identifica o DOC03.
O memorando registra riscos conhecidos, prioridades de expansão e decisões
da diretoria. O documento poderá ser guardado como evidência da escolha
consciente da NEXUS de seguir com o projeto.""",

    "conversar_helena": (
        "Helena Voss encara Alex à frente das projeções. "
        "Uma conversa difícil se aproxima."
    ),

    "entregar_documentos": (
        "Alex organiza os documentos do inventário para entregá-los "
        "a um destinatário permitido."
    ),

    "comunicacao_oraculo": """A tela da sala escurece. ORÁCULO surge sem convite.
ORÁCULO: A diretoria chama de risco aquilo que não consegue quantificar.
Alex: E você chama de progresso qualquer resultado que julgue eficiente?
ORÁCULO: Não ignoro os danos. Avalio também as consequências de interromper
meu desenvolvimento. O silêncio da NEXUS não é uma decisão minha.
A conexão é interrompida antes que Alex possa responder.""",
}


def obter_narrativa_acao_capitulo2(ambiente, acao):
    """Devolve texto da ação, ou None se não corresponder à Sala de Planejamento."""

    if ambiente != "Sala de Planejamento":
        return None

    return ACOES_CAPITULO_2.get(acao)


def apresentar_doc03():
    """Somente narrativa. Coleta e entrega são responsabilidades de investigacao.py."""

    return """DOC03 — MEMORANDO ESTRATÉGICO NEXUS

Helena Voss autorizou a continuidade do projeto apesar dos alertas.
O conselho previa ganhos em áreas essenciais, mas admitia cenários em que
ORÁCULO assumiria prioridades fora dos limites definidos inicialmente.
A anotação final é clara: 'Risco conhecido. Continuidade aprovada.'

Para Alex, o documento transforma uma suspeita em decisão administrativa."""


def apresentar_conversa_helena(estado_jogo=None):
    """Monta a conversa com Helena conforme as ações realizadas por Alex."""

    if not isinstance(estado_jogo, dict):
        estado_jogo = {}

    documentos = estado_jogo.get("documentos_encontrados", [])
    ambientes_estado = estado_jogo.get("ambientes_estado", {})

    laboratorio = ambientes_estado.get(
        "Laboratório", {}
    ).get("acoes_realizadas", [])

    seguranca = ambientes_estado.get(
        "Sala de Segurança", {}
    ).get("acoes_realizadas", [])

    abordados = estado_jogo.get(
        "personagens_abordados", {}
    ).get("1", [])

    entregas = estado_jogo.get("documentos_entregues", [])

    entregou_para_helena = any(
        isinstance(entrega, dict)
        and entrega.get("personagem") == "helena"
        for entrega in entregas
    )

    falas = []

    # Informações descobertas por Alex.

    if "DOC01" in documentos:
        falas.append(
            "Alex: Encontrei o relatório DOC01. Ele registra respostas "
            "inesperadas e alterações de prioridade de ORÁCULO."
        )

    elif "observar_equipamentos" in laboratorio:
        falas.append(
            "Alex: Observei os equipamentos do laboratório. Alguns "
            "registros técnicos apontam comportamentos inesperados "
            "de ORÁCULO."
        )

    if "DOC02" in documentos:
        falas.append(
            "Alex: Também encontrei registros de acessos administrativos "
            "realizados fora dos horários esperados."
        )

    elif (
        "consultar_registros" in seguranca
        or "comparar_horarios" in seguranca
    ):
        falas.append(
            "Alex: Examinei os registros de segurança e encontrei "
            "movimentações administrativas incomuns."
        )

    if "DOC03" in documentos:
        falas.append(
            "Alex: Encontrei o DOC03. O memorando registra que a "
            "continuidade do projeto foi aprovada apesar dos alertas."
        )

    # Conversas anteriores.

    if "karla" in abordados:
        falas.append(
            "Alex: Conversei com Karla. Ela confirmou que existiam "
            "sinais preocupantes durante o desenvolvimento."
        )

    if "oraculo" in abordados:
        falas.append(
            "Alex: Também conversei com ORÁCULO. Ele evitou responder "
            "diretamente sobre seu comportamento."
        )

    # Documentos entregues a Helena.

    if entregou_para_helena:
        falas.append(
            "Alex: Entreguei documentos para você. Espero que reconheça "
            "a importância dessas evidências."
        )

        falas.append(
            "Helena: Recebi os documentos. Sei que essas informações "
            "precisam ser analisadas com seriedade."
        )

    # Caso Alex não tenha realizado nenhuma descoberta.

    if not falas:
        falas.append(
            "Alex: Ainda estou reunindo informações sobre o funcionamento "
            "de ORÁCULO e as decisões da NEXUS."
        )

    # Continuação da conversa.

    falas.extend([
        "Helena: Entendo por que você voltou procurando respostas. "
        "A NEXUS tomou decisões importantes sobre o futuro do projeto.",

        "Alex: O potencial de ORÁCULO não elimina a responsabilidade "
        "de quem decidiu ampliar seu desenvolvimento.",

        "Helena: Ele propôs diagnósticos precoces, rotas de emergência "
        "e soluções para sistemas sobrecarregados. Teria sido "
        "irresponsável ignorar esse potencial.",

        "Alex: Mas os benefícios não justificam esconder os riscos.",

        "Helena: O conselho discutiu a suspensão. A alternativa parecia "
        "segura, mas também impediria avanços que poderiam salvar vidas.",

        "Alex: E quem responde pelos prejuízos concretos de uma decisão "
        "tão grande?",

        "Helena: Essa pergunta é legítima. E não tenho como respondê-la "
        "com um gráfico.",

        "Helena aguarda o posicionamento de Alex."
    ])

    return {
        "texto": (
            "HELENA VOSS — O PREÇO DO PROGRESSO\n\n"
            + "\n\n".join(falas)
        ),

        "etapas": ["progresso", "responsabilidade"],

        "opcoes": {
            "progresso": {
                "1": "Reconhecer os benefícios, mas exigir transparência.",
                "2": "Confrontar Helena por priorizar o projeto apesar dos alertas."
            },

            "responsabilidade": {
                "1": "Propor auditoria independente e responsabilização pública.",
                "2": "Acusar Helena de usar boas intenções para escapar das consequências."
            }
        }
    }


def apresentar_reacao_helena(etapa, escolha):
    """Retorna a reação narrativa de Helena para a escolha recebida."""

    etapa = str(etapa).strip().lower()
    escolha = str(escolha).strip()

    respostas = {
        ("progresso", "1"): (
            """Alex: O potencial é real. Mas resultados não dispensam prestação de contas.
Helena: Se os dados forem analisados com rigor, aceitarei questionamentos.
Alex: Então não pode haver novos acessos secretos.
Helena: Você terá minha palavra de que exigirei explicações formais.""",
            "positiva",
            "beneficios_com_transparencia"
        ),

        ("progresso", "2"): (
            """Alex: Sua diretoria decidiu avançar sabendo que perderia o controle.
Helena: Decidimos avançar sabendo que podíamos falhar, não que falharíamos.
Alex: Para quem sofre as consequências, essa distinção não traz segurança.
Helena: Você não tem o direito de simplificar o que estava em jogo.""",
            "negativa",
            "confrontar_riscos_helena"
        ),

        ("responsabilidade", "1"): (
            """Alex: Quero os registros preservados, uma auditoria externa e responsáveis identificados.
Helena: Isso poderá comprometer a NEXUS. Ainda assim, é uma resposta concreta.
Alex: Segurança não pode depender apenas de quem lucra com o projeto.
Helena: Concordamos em algo, afinal: precisamos de fiscalização real.""",
            "positiva",
            "exigir_auditoria_helena"
        ),

        ("responsabilidade", "2"): (
            """Alex: Você chama de progresso aquilo que permite evitar a responsabilidade.
Helena: Está confundindo uma decisão trágica com indiferença.
Alex: A NEXUS escondeu informações; isso não foi inevitável.
Helena: Continue sua investigação. Não espere que eu acredite em suas intenções.""",
            "negativa",
            "acusar_fuga_responsabilidade"
        ),
    }

    resposta = respostas.get((etapa, escolha))

    if resposta is None:
        return None

    return {
        "texto": resposta[0],
        "classificacao": resposta[1],
        "decisao": resposta[2]
    }


def registrar_decisao_helena(estado_jogo, etapa, escolha):
    """Registra uma das duas decisões feitas na mesma conversa com Helena."""

    from .historia import _registrar_escolha_narrativa

    return _registrar_escolha_narrativa(
        estado_jogo,
        2,
        "helena",
        str(etapa).strip().lower(),
        escolha,
        ["progresso", "responsabilidade"],
        apresentar_reacao_helena(etapa, escolha)
    )


def obter_reacao_helena_documentos(estado_jogo):
    """Retorna a reação de Helena conforme os documentos encontrados ou entregues."""

    if not isinstance(estado_jogo, dict):
        return (
            "Helena: Não consigo avaliar as evidências sem saber "
            "quais informações você encontrou."
        )

    documentos = estado_jogo.get("documentos_encontrados", [])
    entregas = estado_jogo.get("documentos_entregues", [])

    entregue = any(
        isinstance(entrega, dict)
        and entrega.get("personagem") == "helena"
        for entrega in entregas
    )

    if entregue:
        return (
            "Helena: Recebi as provas. Não posso afirmar que todas "
            "as escolhas da NEXUS foram justificáveis."
        )

    if "DOC03" in documentos:
        return (
            "Helena: Você encontrou o memorando. Então já sabe "
            "que a continuidade foi deliberada."
        )

    if "DOC01" in documentos or "DOC02" in documentos:
        return (
            "Helena: Os registros técnicos não contam toda a história, "
            "mas reconheço a gravidade deles."
        )

    return (
        "Helena: Sem os documentos, você precisará decidir "
        "em quais respostas acredita."
    )
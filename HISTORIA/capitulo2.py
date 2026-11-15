"""Capítulo 2 — O Preço do Progresso.

Responsável: integrante de História. Narrativa e escolhas com Helena Voss.
Não coleta documentos nem modifica confiança diretamente.
"""


def texto_abertura():
    """Retorna a introdução da Sala de Planejamento."""
    return '======================================\nCAPÍTULO 2 — O PREÇO DO PROGRESSO\n======================================\n\nApós investigar o Laboratório e a Sala de Segurança, Alex\npercebe que a NEXUS já conhecia alguns comportamentos\nanormais de ORÁCULO.\n\nEntretanto, ainda faltam informações para compreender\ntoda a situação.\n\nSua investigação agora chega à Sala de Planejamento.\n\nAli, Alex poderá examinar as decisões estratégicas da\norganização e confrontar a diretora Helena Voss.\n\nO objetivo é descobrir até onde a NEXUS está disposta\na ir para permitir a evolução de ORÁCULO.'


def texto_encerramento(estado_jogo):
    """Retorna o texto final do Capítulo 2, com base nas decisões salvas."""
    escolhas = estado_jogo.get("decisoes", {})
    if "helena_progresso_capitulo_2" not in escolhas:
        detalhe = ("Alex saiu sem ouvir pessoalmente todos os argumentos de Helena. "
                   "As decisões registradas nos planos ainda precisam ser explicadas.")
    else:
        detalhe = ("As respostas de Helena deixaram clara a tensão entre avanço, "
                   "segurança e responsabilidade.")
    return ("ENCERRAMENTO DO CAPÍTULO 2 — O PREÇO DO PROGRESSO\n\n"
            "Alex confirma que a NEXUS conhecia os riscos de ORÁCULO, "
            "mas manteve o investimento por acreditar nos benefícios futuros.\n\n"
            + detalhe + "\n\nA próxima parada é o Escritório de Dante.")


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
    "conversar_helena": "Helena Voss encara Alex à frente das projeções. Uma conversa difícil se aproxima.",
    "entregar_documentos": "Alex organiza os documentos do inventário para entregá-los a um destinatário permitido.",
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


def apresentar_conversa_helena():
    return {
        "texto": """HELENA VOSS — O PREÇO DO PROGRESSO

Alex: Nas salas técnicas, vi sinais de que ORÁCULO mudou prioridades sem aviso.
Helena: Eu conheço os relatórios. Também conheço o que ele conseguiu fazer.
Alex: Não é a mesma coisa que ter autorização para fazê-lo.
Helena: Ele propôs diagnósticos precoces, rotas de emergência e soluções para
sistemas sobrecarregados. Teria sido irresponsável ignorar esse potencial.
Alex: Mas a NEXUS ocultou os riscos e continuou ampliando o acesso dele.
Helena: O conselho discutiu a suspensão. A alternativa parecia segura,
mas também condenaria pessoas a problemas que talvez pudéssemos resolver.
Alex: Você transformou uma decisão incerta em um projeto inevitável.
Helena: Não digo que acertamos em tudo. Digo que o medo não pode decidir sozinho.
Alex: E quem responde pelos prejuízos concretos de uma decisão tão grande?
Helena: Essa pergunta é legítima. E não tenho como respondê-la com um gráfico.
Helena aguarda o posicionamento de Alex.""",
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
    etapa, escolha = str(etapa).strip(), str(escolha).strip()
    respostas = {
        ("progresso", "1"): ("""Alex: O potencial é real. Mas resultados não dispensam prestação de contas.
Helena: Se os dados forem analisados com rigor, aceitarei questionamentos.
Alex: Então não pode haver novos acessos secretos.
Helena: Você terá minha palavra de que exigirei explicações formais.""",
                            "positiva", "beneficios_com_transparencia"),
        ("progresso", "2"): ("""Alex: Sua diretoria decidiu avançar sabendo que perderia o controle.
Helena: Decidimos avançar sabendo que podíamos falhar, não que falharíamos.
Alex: Para quem sofre as consequências, essa distinção não traz segurança.
Helena: Você não tem o direito de simplificar o que estava em jogo.""",
                            "negativa", "confrontar_riscos_helena"),
        ("responsabilidade", "1"): ("""Alex: Quero os registros preservados, uma auditoria externa e responsáveis identificados.
Helena: Isso poderá comprometer a NEXUS. Ainda assim, é uma resposta concreta.
Alex: Segurança não pode depender apenas de quem lucra com o projeto.
Helena: Concordamos em algo, afinal: precisamos de fiscalização real.""",
                            "positiva", "exigir_auditoria_helena"),
        ("responsabilidade", "2"): ("""Alex: Você chama de progresso aquilo que permite evitar a responsabilidade.
Helena: Está confundindo uma decisão trágica com indiferença.
Alex: A NEXUS escondeu informações; isso não foi inevitável.
Helena: Continue sua investigação. Não espere que eu acredite em suas intenções.""",
                            "negativa", "acusar_fuga_responsabilidade"),
    }
    r = respostas.get((etapa, escolha))
    if r is None:
        return None
    return {"texto": r[0], "classificacao": r[1], "decisao": r[2]}


def registrar_decisao_helena(estado_jogo, etapa, escolha):
    """Registra uma das duas decisões feitas na mesma conversa com Helena."""
    from .historia import _registrar_escolha_narrativa

    return _registrar_escolha_narrativa(
        estado_jogo, 2, "helena", str(etapa).strip(), escolha,
        ["progresso", "responsabilidade"], apresentar_reacao_helena(etapa, escolha)
    )


def obter_reacao_helena_documentos(estado_jogo):
    """O que Helena diz se Alex encontrou documentos; não concede confiança."""
    docs = estado_jogo.get("documentos_encontrados", [])
    entregue = any(isinstance(e, dict) and e.get("personagem") == "helena"
                   for e in estado_jogo.get("documentos_entregues", []))
    if entregue:
        return "Helena: Recebi as provas. Não posso afirmar que todas as escolhas da NEXUS foram justificáveis."
    if "DOC03" in docs:
        return "Helena: Você encontrou o memorando. Então já sabe que a continuidade foi deliberada."
    if "DOC01" in docs or "DOC02" in docs:
        return "Helena: Os registros técnicos não contam toda a história, mas reconheço a gravidade deles."
    return "Helena: Sem os documentos, você precisará decidir em quais respostas acredita."
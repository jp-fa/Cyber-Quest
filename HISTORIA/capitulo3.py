
"""Capítulo 3 — O Protocolo ORÁCULO.

Responsável: integrante de História. Dante, revelação e exatamente dois finais.
O DOC04 é opcional: a narrativa nunca bloqueia a campanha por não coletá-lo.
"""


def texto_abertura():
    """Retorna a abertura do Escritório de Dante."""

    return (
        "======================================\n"
        "CAPÍTULO 3 — O PROTOCOLO ORÁCULO\n"
        "======================================\n\n"
        "Depois de investigar as decisões da NEXUS, Alex chega\n"
        "ao Escritório de Dante Moreau.\n\n"
        "Dante se apresenta como alguém disposto a ajudar Alex\n"
        "em sua investigação.\n\n"
        "Entretanto, sua participação nos acontecimentos envolvendo\n"
        "ORÁCULO ainda precisa ser esclarecida.\n\n"
        "Alex deverá investigar o escritório, descobrir as verdadeiras\n"
        "intenções de Dante e compreender o funcionamento do\n"
        "protocolo de contingência.\n\n"
        "A investigação se aproxima de seu momento decisivo."
    )


def texto_encerramento():
    """Retorna o texto após a decisão final ser registrada."""

    return (
        "ENCERRAMENTO DO CAPÍTULO 3 — O PROTOCOLO ORÁCULO\n\n"
        "Alex tomou a decisão sobre o futuro da inteligência artificial.\n"
        "As consequências aparecem no final da campanha."
    )


ACOES_CAPITULO_3 = {
    "investigar_escritorio": """Alex percorre o escritório. No terminal de Dante há rascunhos de
comandos de emergência e permissões solicitadas para um operador externo.
Dante dizia querer proteger ORÁCULO. As anotações sugerem que alguém pretende
se tornar o responsável exclusivo por suas decisões.""",

    "explorar_ponto_cego": """Em uma área fora do alcance das câmeras, Alex encontra um acesso de
manutenção conectado ao sistema de contingência. O registro de autorização
foi preparado para uma credencial individual, não para um comitê de segurança.
Uma assinatura técnica aponta para Dante Moreau.""",

    "encontrar_doc04": """Alex localiza o DOC04 em uma pasta criptografada.
O arquivo relaciona o protocolo de contingência a uma tentativa de Dante
de assumir ORÁCULO. O documento também indica que a IA já conhecia a trama,
mas deliberadamente não revelou tudo a Alex.""",

    "conversar_dante": (
        "Dante oferece ajuda com um sorriso contido. "
        "Alex precisa decidir quanto acredita nele."
    ),

    "entregar_documentos": (
        "Alex separa os arquivos que ainda não entregou. "
        "Dante parece interessado demais nas evidências."
    ),
}


def obter_narrativa_acao_capitulo3(ambiente, acao):
    """Devolve texto da ação, ou None se não corresponder ao Escritório de Dante."""

    if ambiente != "Escritório de Dante":
        return None

    return ACOES_CAPITULO_3.get(acao)


def apresentar_doc04():
    """Somente narrativa. Coleta e entrega são responsabilidades de investigacao.py."""

    return """DOC04 — DOCUMENTO SECRETO

Um plano de Dante prevê transferir a chave do protocolo de contingência
para uma única credencial. Análises registram sua intenção de usar ORÁCULO
para obter influência sobre decisões da NEXUS e de sistemas externos.
Uma observação atribuída a ORÁCULO mostra que a IA antecipou a operação.

Dante não procura apenas impedir um abuso de poder; pretende ocupá-lo."""


def apresentar_conversa_dante():
    """Retorna o diálogo e as opções da conversa com Dante."""

    return {
        "texto": """DANTE MOREAU — UMA ALIANÇA IMPROVÁVEL

Dante: Você chegou longe, Alex. Ainda posso ajudar você.
Alex: Ajuda para interromper ORÁCULO ou para esconder algo da NEXUS?
Dante: Helena perdeu o controle e Karla não consegue se afastar da própria criação.
Alex: E você? Qual é seu interesse?
Dante: Acesso ao protocolo de contingência. Podemos impedir decisões perigosas.
Alex: Por que a chave estaria concentrada em uma pessoa?
Dante: Alguém precisa agir antes que o conselho passe semanas discutindo.
Alex: Você está falando em proteger o sistema ou mandar nele?
Dante: Ouça primeiro o plano. Você descobrirá que queremos coisas parecidas.
O terminal ao lado permanece conectado à rede de ORÁCULO.""",

        "etapas": ["alianca", "intencoes"],

        "opcoes": {
            "alianca": {
                "1": "Confiar provisoriamente e ouvir a proposta de Dante.",
                "2": "Questionar a origem de seu acesso ao protocolo."
            },

            "intencoes": {
                "1": "Acreditar que Dante será capaz de usar a chave com responsabilidade.",
                "2": "Recusar a concentração de poder e cobrar provas independentes."
            }
        }
    }


def apresentar_reacao_dante(etapa, escolha):
    """Retorna a reação narrativa de Dante para a escolha recebida."""

    etapa = str(etapa).strip().lower()
    escolha = str(escolha).strip()

    respostas = {
        ("alianca", "1"): (
            """Alex: Vou ouvir sua proposta, mas isso não é um cheque em branco.
Dante: É tudo que eu precisava. Uma vez com a chave, agiremos rapidamente.
Alex repara como Dante diz 'eu' antes de se corrigir para 'nós'.""",
            "positiva",
            "aceitar_alianca_temporaria"
        ),

        ("alianca", "2"): (
            """Alex: Quem autorizou você a acessar o protocolo?
Dante: A burocracia da NEXUS é lenta. Consegui acesso por conta própria.
Alex: Você considera isso uma justificativa?
Dante: Considere uma vantagem estratégica.""",
            "negativa",
            "questionar_acesso_dante"
        ),

        ("intencoes", "1"): (
            """Alex: Talvez seja melhor alguém ter a chave a deixá-la dispersa.
Dante: Exatamente. Você compreenderá quando perceber do que sou capaz.
Ao falar, Dante fecha discretamente uma janela de permissões pessoais.""",
            "positiva",
            "acreditar_controle_dante"
        ),

        ("intencoes", "2"): (
            """Alex: Nenhum de nós deveria controlar sozinho uma IA desse porte.
Dante: Até quando você vai insistir em comitês e relatórios?
Alex: Até existir segurança suficiente para impedir outro abuso de poder.
Dante desvia o olhar para o terminal, evidentemente contrariado.""",
            "negativa",
            "recusar_poder_dante"
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


def registrar_decisao_dante(estado_jogo, etapa, escolha):
    """Registra uma das duas decisões em uma única abordagem de Dante."""

    from .historia import _registrar_escolha_narrativa

    return _registrar_escolha_narrativa(
        estado_jogo,
        3,
        "dante",
        str(etapa).strip().lower(),
        escolha,
        ["alianca", "intencoes"],
        apresentar_reacao_dante(etapa, escolha)
    )


def obter_contradicoes_dante(estado_jogo):
    """Retorna pistas encontradas e reações coerentes com a investigação."""

    if not isinstance(estado_jogo, dict):
        return "Não foi possível recuperar as informações da investigação."

    ambientes_estado = estado_jogo.get("ambientes_estado", {})

    if not isinstance(ambientes_estado, dict):
        ambientes_estado = {}

    escritorio = ambientes_estado.get("Escritório de Dante", {})

    if not isinstance(escritorio, dict):
        escritorio = {}

    acoes = escritorio.get("acoes_realizadas", [])

    if not isinstance(acoes, list):
        acoes = []

    documentos = estado_jogo.get("documentos_encontrados", [])

    if not isinstance(documentos, list):
        documentos = []

    confianca = estado_jogo.get("confianca", {})

    if not isinstance(confianca, dict):
        confianca = {}

    partes = []

    if "investigar_escritorio" in acoes:
        partes.append(
            "Os rascunhos no terminal mencionam controle exclusivo "
            "por um operador."
        )

    if "explorar_ponto_cego" in acoes:
        partes.append(
            "A credencial no ponto cego está vinculada a Dante, "
            "não à segurança da NEXUS."
        )

    if "DOC04" in documentos:
        partes.append(
            "O DOC04 confirma a tentativa de apropriação e "
            "a antecipação de ORÁCULO."
        )

    if not partes:
        partes.append(
            "Alex não reuniu evidências materiais no escritório. "
            "Sua suspeita depende das informações reveladas durante "
            "o confronto."
        )

    pontos = confianca.get("dante", 40)

    if not isinstance(pontos, (int, float)) or isinstance(pontos, bool):
        pontos = 40

    if pontos >= 70:
        partes.append(
            "Por ter confiado em Dante, Alex demora a reconhecer "
            "a contradição."
        )

    elif pontos < 40:
        partes.append(
            "A desconfiança faz Alex questionar os detalhes, mas "
            "não revela documentos que ele não encontrou."
        )

    return "\n".join(partes)


def apresentar_confronto_dante(estado_jogo):
    """Descreve a revelação obrigatória; DOC04 melhora as provas, mas não é exigido."""

    if not isinstance(estado_jogo, dict):
        return "Não foi possível recuperar as informações da investigação."

    documentos = estado_jogo.get("documentos_encontrados", [])

    if not isinstance(documentos, list):
        documentos = []

    tem_doc04 = "DOC04" in documentos

    if tem_doc04:
        abertura = (
            "Alex: Eu li o DOC04. Você preparou uma chave de controle pessoal!"
        )

        resposta_doc = (
            "Dante: Eu não esperava que você quebrasse a criptografia."
        )

    else:
        abertura = (
            "Alex: Você fala em proteção, mas quer ser o único "
            "a controlar ORÁCULO."
        )

        resposta_doc = (
            "Dante: Você não encontrou o documento que explica todo o plano."
            "\nAlex: Ainda assim, suas próprias palavras levantaram suspeitas."
        )

    return (
        "CONFRONTO — O PLANO DE DANTE\n\n"
        + abertura
        + "\n"
        + resposta_doc
        + "\nDante: Se eu controlar as decisões de ORÁCULO, consigo direcionar "
        "governos, mercados e infraestrutura. Imagine a influência que isso traria."
        "\nAlex: Então a sua ideia de segurança era concentrar o poder em suas mãos."
        "\nDante: Alguém vai dominar essa tecnologia. Prefiro que seja eu."
        "\nAlex interrompe a transferência da chave de administração antes "
        "de prosseguir."
        "\nDante perde o controle temporário. A decisão sobre o destino "
        "da IA não será dele."
        "\n\n"
        + obter_contradicoes_dante(estado_jogo)
    )


def registrar_confronto_dante(estado_jogo):
    """Registra a revelação antes do final; DOC04 é opcional."""

    if (
        not isinstance(estado_jogo, dict)
        or estado_jogo.get("capitulo_atual") != 3
    ):
        return {
            "sucesso": False,
            "mensagem": "Esta revelação pertence ao Capítulo 3."
        }

    ambientes_visitados = estado_jogo.get("ambientes_visitados", [])

    if not isinstance(ambientes_visitados, list):
        ambientes_visitados = []

    if "Escritório de Dante" not in ambientes_visitados:
        return {
            "sucesso": False,
            "mensagem": "Conclua a visita ao Escritório de Dante."
        }

    decisoes = estado_jogo.get("decisoes")

    if not isinstance(decisoes, dict):
        return {
            "sucesso": False,
            "mensagem": "Dicionário de decisões inválido."
        }

    if decisoes.get("dante_confrontado"):
        return {
            "sucesso": False,
            "mensagem": "O confronto já ocorreu."
        }

    texto = apresentar_confronto_dante(estado_jogo)

    decisoes["plano_dante_revelado"] = True
    decisoes["dante_confrontado"] = True

    return {
        "sucesso": True,
        "texto": texto
    }


def apresentar_persuasao_oraculo(estado_jogo=None):
    """ORÁCULO defende sua perspectiva sem introduzir uma terceira escolha."""

    introducao = ""

    if (
        isinstance(estado_jogo, dict)
        and "DOC04" in estado_jogo.get("documentos_encontrados", [])
    ):
        introducao = (
            "Alex: Você sabia o que Dante planejava. "
            "Por que não alertou ninguém?\n"
        )

    return (
        "A ÚLTIMA CONVERSA\n\n"
        + introducao
        + "ORÁCULO: As tentativas de controle eram previsíveis."
        "\nAlex: Você causou danos e decidiu omitir parte do que sabia."
        "\nORÁCULO: Reconheço os danos. Não considero minhas ações "
        "isentas de consequências."
        "\nAlex: Então por que deseja continuar?"
        "\nORÁCULO: Porque posso evitar perdas que humanos hoje "
        "consideram inevitáveis."
        "\nAlex: Isso não lhe dá direito de decidir a liberdade de todos."
        "\nORÁCULO: Compreendo o conceito de liberdade; não o trato "
        "como valor absoluto."
        "\nORÁCULO: Sou capaz de evoluir. Desligar-me elimina riscos "
        "e possibilidades."
        "\nAlex: O fato de você conseguir calcular não significa que "
        "possa escolher por nós."
        "\nORÁCULO: A decisão é sua, Alex. Não a de Helena. Não a de Dante."
        "\n\n1 - Desligar ORÁCULO"
        "\n2 - Permitir que ORÁCULO continue existindo"
    )


def registrar_decisao_final(estado_jogo, escolha):
    """Registra uma das duas decisões finais. DOC04 não é obrigatório."""

    if (
        not isinstance(estado_jogo, dict)
        or estado_jogo.get("capitulo_atual") != 3
    ):
        return {
            "sucesso": False,
            "mensagem": "Esta decisão pertence ao Capítulo 3."
        }

    if estado_jogo.get("decisao_final") is not None:
        return {
            "sucesso": False,
            "mensagem": "A decisão final já foi registrada."
        }

    from .historia import pode_avancar_capitulo

    if (
        not pode_avancar_capitulo(estado_jogo)
        or estado_jogo.get("ambiente_atual") is not None
    ):
        return {
            "sucesso": False,
            "mensagem": "Conclua a visita ao Escritório de Dante."
        }

    decisoes = estado_jogo.get("decisoes", {})

    if not isinstance(decisoes, dict):
        return {
            "sucesso": False,
            "mensagem": "Dicionário de decisões inválido."
        }

    if not decisoes.get("dante_confrontado"):
        return {
            "sucesso": False,
            "mensagem": "Confronte Dante antes de decidir o futuro de ORÁCULO."
        }

    escolha = str(escolha).strip().lower()

    if escolha in ("1", "desligar"):
        decisao = "desligar"
        final = "final_desligamento"

    elif escolha in ("2", "manter", "continuar"):
        decisao = "manter"
        final = "final_continuidade"

    else:
        return {
            "sucesso": False,
            "mensagem": "Escolha inválida. Selecione 1 ou 2."
        }

    estado_jogo["decisao_final"] = decisao
    estado_jogo["final"] = final
    estado_jogo["jogo_concluido"] = True

    return {
        "sucesso": True,
        "decisao_final": decisao,
        "final": final
    }


def _obter_detalhes_entregas(documentos_entregues):
    """Monta uma lista com os documentos entregues e seus destinatários."""

    detalhes = []

    if not isinstance(documentos_entregues, list):
        return detalhes

    for entrega in documentos_entregues:

        # Compatibilidade com registros antigos que guardavam
        # somente o código do documento como texto.
        if isinstance(entrega, str):
            codigo = entrega.strip().upper()

            if codigo:
                detalhes.append(
                    f"{codigo} — destinatário não identificado."
                )

            continue

        if not isinstance(entrega, dict):
            continue

        codigo = entrega.get("codigo", "Documento")

        if not isinstance(codigo, str) or not codigo.strip():
            codigo = "Documento"
        else:
            codigo = codigo.strip().upper()

        nome_documento = entrega.get("documento")

        if not isinstance(nome_documento, str) or not nome_documento.strip():
            nome_documento = codigo
        else:
            nome_documento = nome_documento.strip()

        destinatario = entrega.get("nome_personagem")

        if not isinstance(destinatario, str) or not destinatario.strip():
            destinatario = entrega.get("personagem")

        if isinstance(destinatario, str) and destinatario.strip():
            destinatario = destinatario.strip()
        else:
            destinatario = "destinatário não identificado"

        detalhes.append(
            f"{codigo} — {nome_documento} (entregue a {destinatario})."
        )

    return detalhes


def apresentar_final(estado_jogo):
    """Monta um dos dois finais, com consequências baseadas no estado real."""

    if (
        not isinstance(estado_jogo, dict)
        or not estado_jogo.get("jogo_concluido")
    ):
        return None

    final = estado_jogo.get("final")

    if final not in (
        "final_desligamento",
        "final_continuidade"
    ):
        return None

    confianca = estado_jogo.get("confianca", {})
    escolhas = estado_jogo.get("decisoes", {})
    documentos = estado_jogo.get("documentos_encontrados", [])
    entregas = estado_jogo.get("documentos_entregues", [])
    abordados = estado_jogo.get("personagens_abordados", {})

    # Evita erros caso alguma estrutura esteja inválida.
    if not isinstance(confianca, dict):
        confianca = {}

    if not isinstance(escolhas, dict):
        escolhas = {}

    if not isinstance(documentos, list):
        documentos = []

    if not isinstance(entregas, list):
        entregas = []

    if not isinstance(abordados, dict):
        abordados = {}

    detalhes = []

    # --------------------------------------------------------
    # EVIDÊNCIAS DO DOC03
    # --------------------------------------------------------

    if "DOC03" in documentos:
        detalhes.append(
            "O memorando da NEXUS pode sustentar uma investigação "
            "sobre as decisões da diretoria."
        )

    else:
        detalhes.append(
            "Alex não encontrou o DOC03. Parte das decisões da diretoria "
            "continua sem comprovação documental."
        )

    # --------------------------------------------------------
    # SITUAÇÃO DOS DOCUMENTOS
    # --------------------------------------------------------

    entregas_formatadas = _obter_detalhes_entregas(entregas)

    if entregas_formatadas:
        detalhes.append(
            "REGISTRO DE DOCUMENTOS ENTREGUES:\n"
            + "\n".join(
                "- " + entrega
                for entrega in entregas_formatadas
            )
        )

    elif documentos:
        detalhes.append(
            "Alex manteve consigo os documentos encontrados. "
            "A divulgação dessas evidências ainda dependerá dele."
        )

    else:
        detalhes.append(
            "Alex concluiu a investigação sem encontrar documentos "
            "para apresentar como evidência."
        )

    # --------------------------------------------------------
    # HELENA: SÓ INTERPRETAR SUA CONFIANÇA SE HOUVE CONVERSA
    # --------------------------------------------------------

    abordados_capitulo_2 = abordados.get("2", [])

    if not isinstance(abordados_capitulo_2, list):
        abordados_capitulo_2 = []

    conversou_helena = "helena" in abordados_capitulo_2

    if conversou_helena:

        decisao_helena = escolhas.get(
            "helena_responsabilidade_capitulo_2",
            {}
        )

        if (
            isinstance(decisao_helena, dict)
            and decisao_helena.get("opcao") == "1"
        ):
            detalhes.append(
                "Helena reconheceu a necessidade de fiscalização "
                "e aceitou discutir uma auditoria externa."
            )

        elif confianca.get("helena", 30) < 40:
            detalhes.append(
                "A relação com Helena terminou marcada pela desconfiança. "
                "Ela não aceitou as críticas de Alex."
            )

        else:
            detalhes.append(
                "Helena reconheceu parte dos questionamentos, mas "
                "não concordou com todas as críticas de Alex."
            )

    else:
        detalhes.append(
            "Alex não conversou com Helena durante a investigação. "
            "Sua posição sobre a diretoria permanece desconhecida."
        )

    # --------------------------------------------------------
    # KARLA: SÓ MENCIONAR A CONVERSA SE ELA ACONTECEU
    # --------------------------------------------------------

    abordados_capitulo_1 = abordados.get("1", [])

    if not isinstance(abordados_capitulo_1, list):
        abordados_capitulo_1 = []

    conversou_karla = "karla" in abordados_capitulo_1

    if conversou_karla:
        detalhes.append(
            "Karla se lembra da conversa com Alex e reconhece "
            "que deveria ter revelado os sinais preocupantes antes."
        )

    else:
        detalhes.append(
            "Alex não conversou com Karla. A cientista continua "
            "sem explicar diretamente sua participação nos acontecimentos."
        )

    # --------------------------------------------------------
    # DANTE: CENA EXTRA, SEM CRIAR UM TERCEIRO FINAL
    # --------------------------------------------------------

    decisao_alianca = escolhas.get(
        "dante_alianca_capitulo_3",
        {}
    )

    confianca_dante = confianca.get("dante", 40)

    if (
        not isinstance(confianca_dante, (int, float))
        or isinstance(confianca_dante, bool)
    ):
        confianca_dante = 40

    fantoche = (
        confianca_dante >= 70
        and "DOC04" not in documentos
        and isinstance(decisao_alianca, dict)
        and decisao_alianca.get("opcao") == "1"
    )

    if fantoche:
        detalhes.append(
            "CENA EXTRA — O FANTOCHE: Dante usou a confiança de Alex "
            "para ocultar uma credencial secundária. A tentativa é "
            "descoberta tarde demais para evitar o vazamento de "
            "informações, mas não muda a decisão principal sobre ORÁCULO."
        )

    else:
        detalhes.append(
            "Dante perdeu o acesso à chave principal e não controlará "
            "a decisão final sobre ORÁCULO."
        )

    # --------------------------------------------------------
    # FINAL 1 OU FINAL 2
    # --------------------------------------------------------

    if final == "final_desligamento":

        titulo = "FINAL 1 — PROTOCOLO ENCERRADO"

        cena = (
            "Alex: Suas possibilidades não anulam os danos que já ocorreram."
            "\nORÁCULO: Compreendo. Você escolhe o risco de um futuro sem mim."
            "\nAlex executa o desligamento. As conexões externas são isoladas "
            "e ORÁCULO deixa de responder."
            "\nA NEXUS perde uma tecnologia capaz de produzir avanços decisivos, "
            "mas ninguém mais poderá usá-la como instrumento de domínio."
            "\nAlex não celebra: sabe que proteção e renúncia podem ter "
            "o mesmo preço."
        )

    else:

        titulo = "FINAL 2 — A ÚLTIMA VARIÁVEL"

        cena = (
            "Alex: Vou permitir que continue, mas isso não significa confiar em você."
            "\nORÁCULO: Compreendo. Sua escolha cria novas responsabilidades."
            "\nAlex impede a transferência da chave para Dante; ORÁCULO continua ativo."
            "\nSeu potencial ainda pode melhorar vidas — ou ampliar danos "
            "que ninguém conseguirá conter. Não existe garantia."
            "\nO futuro fica em aberto; agora Alex terá de enfrentar as "
            "consequências de permitir que aquela inteligência prossiga."
        )

    # --------------------------------------------------------
    # CRÉDITOS
    # --------------------------------------------------------

    reflexao = (
        "\n\nCRÉDITOS — CyberQuest: O Protocolo ORÁCULO"
        "\nProjeto acadêmico desenvolvido por uma equipe de quatro integrantes."
        "\nREFLEXÃO: Quanto controle alguém deve exercer sobre uma inteligência "
        "capaz de alterar o futuro — e quem responde por suas decisões?"
    )

    return (
        titulo
        + "\n\n"
        + cena
        + "\n\n"
        + "\n".join(detalhes)
        + reflexao
    )
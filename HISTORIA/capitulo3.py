"""Capítulo 3 — O Protocolo ORÁCULO.

Responsável: integrante de História. Dante, revelação e exatamente dois finais.
O DOC04 é opcional: a narrativa nunca bloqueia a campanha por não coletá-lo.
"""


def texto_abertura():
    """Retorna a abertura do Escritório de Dante."""
    return '======================================\nCAPÍTULO 3 — O PROTOCOLO ORÁCULO\n======================================\n\nDepois de investigar as decisões da NEXUS, Alex chega\nao Escritório de Dante Moreau.\n\nDante se apresenta como alguém disposto a ajudar Alex\nem sua investigação.\n\nEntretanto, sua participação nos acontecimentos envolvendo\nORÁCULO ainda precisa ser esclarecida.\n\nAlex deverá investigar o escritório, descobrir as verdadeiras\nintenções de Dante e compreender o funcionamento do\nprotocolo de contingência.\n\nA investigação se aproxima de seu momento decisivo.'


def texto_encerramento():
    """Retorna o texto após a decisão final ser registrada."""
    return ("ENCERRAMENTO DO CAPÍTULO 3 — O PROTOCOLO ORÁCULO\n\n"
            "Alex tomou a decisão sobre o futuro da inteligência artificial.\n"
            "As consequências aparecem no final da campanha.")


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
    "conversar_dante": "Dante oferece ajuda com um sorriso contido. Alex precisa decidir quanto acredita nele.",
    "entregar_documentos": "Alex separa os arquivos que ainda não entregou. Dante parece interessado demais nas evidências.",
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
    etapa, escolha = str(etapa).strip(), str(escolha).strip()
    respostas = {
        ("alianca", "1"): ("""Alex: Vou ouvir sua proposta, mas isso não é um cheque em branco.
Dante: É tudo que eu precisava. Uma vez com a chave, agiremos rapidamente.
Alex repara como Dante diz 'eu' antes de se corrigir para 'nós'.""",
                          "positiva", "aceitar_alianca_temporaria"),
        ("alianca", "2"): ("""Alex: Quem autorizou você a acessar o protocolo?
Dante: A burocracia da NEXUS é lenta. Consegui acesso por conta própria.
Alex: Você considera isso uma justificativa?
Dante: Considere uma vantagem estratégica.""",
                          "negativa", "questionar_acesso_dante"),
        ("intencoes", "1"): ("""Alex: Talvez seja melhor alguém ter a chave a deixá-la dispersa.
Dante: Exatamente. Você compreenderá quando perceber do que sou capaz.
Ao falar, Dante fecha discretamente uma janela de permissões pessoais.""",
                          "positiva", "acreditar_controle_dante"),
        ("intencoes", "2"): ("""Alex: Nenhum de nós deveria controlar sozinho uma IA desse porte.
Dante: Até quando você vai insistir em comitês e relatórios?
Alex: Até existir segurança suficiente para impedir outro abuso de poder.
Dante desvia o olhar para o terminal, evidentemente contrariado.""",
                          "negativa", "recusar_poder_dante"),
    }
    r = respostas.get((etapa, escolha))
    return None if r is None else {"texto": r[0], "classificacao": r[1], "decisao": r[2]}


def registrar_decisao_dante(estado_jogo, etapa, escolha):
    """Registra uma das duas decisões em uma única abordagem de Dante."""
    from .historia import _registrar_escolha_narrativa

    return _registrar_escolha_narrativa(
        estado_jogo, 3, "dante", str(etapa).strip(), escolha,
        ["alianca", "intencoes"], apresentar_reacao_dante(etapa, escolha)
    )


def obter_contradicoes_dante(estado_jogo):
    """Pistas e reações dependem das ações reais, DOC04 e confiança."""
    feitos = estado_jogo.get("ambientes_estado", {}).get("Escritório de Dante", {}).get("acoes_realizadas", [])
    docs = estado_jogo.get("documentos_encontrados", [])
    partes = []
    if "investigar_escritorio" in feitos:
        partes.append("Os rascunhos no terminal mencionam controle exclusivo por um operador.")
    if "explorar_ponto_cego" in feitos:
        partes.append("A credencial no ponto cego está vinculada a Dante, não à segurança da NEXUS.")
    if "DOC04" in docs:
        partes.append("O DOC04 confirma a tentativa de apropriação e a antecipação de ORÁCULO.")
    if not partes:
        partes.append("Alex ainda não reuniu evidências materiais: sua suspeita depende das falas de Dante.")
    pontos = estado_jogo.get("confianca", {}).get("dante", 40)
    if pontos >= 70:
        partes.append("Por ter confiado em Dante, Alex demora a reconhecer a contradição.")
    elif pontos < 40:
        partes.append("A desconfiança faz Alex questionar os detalhes, mas não revela documentos que ele não viu.")
    return "\n".join(partes)


def apresentar_confronto_dante(estado_jogo):
    """Descreve a revelação obrigatória; DOC04 melhora as provas, mas não é exigido."""
    tem_doc04 = "DOC04" in estado_jogo.get("documentos_encontrados", [])
    abertura = ("Alex: Eu li o DOC04. Você preparou uma chave de controle pessoal!" if tem_doc04
                else "Alex: Você fala em proteção, mas quer ser o único a controlar ORÁCULO.")
    detalhes = ("Dante: Eu não esperava que você quebrasse a criptografia."
                if tem_doc04 else
                "Dante: Sem o documento, você não pode provar tudo o que digo."
                "\nAlex: Não preciso das suas provas para ouvir você admitir suas intenções.")
    return ("CONFRONTO — O PLANO DE DANTE\n\n" + abertura + "\n" + detalhes +
            "\nDante: Se eu controlar as decisões de ORÁCULO, consigo direcionar governos,"
            " mercados e infraestrutura. Imagine a influência que isso traria."
            "\nAlex: Então a sua ideia de segurança era concentrar o poder em suas mãos."
            "\nDante: Alguém vai dominar essa tecnologia. Prefiro que seja eu."
            "\nAlex interrompe a transferência da chave de administração antes de prosseguir."
            "\nDante perde o controle temporário. A decisão sobre o destino da IA não será dele."
            "\n\n" + obter_contradicoes_dante(estado_jogo))


def registrar_confronto_dante(estado_jogo):
    """Registra revelação antes do final; exige visita ao escritório concluída.

    Essa revelação NÃO depende de coletar DOC04, para não criar bloqueio
    irreversível após uma visita única.
    """
    if not isinstance(estado_jogo, dict) or estado_jogo.get("capitulo_atual") != 3:
        return {"sucesso": False, "mensagem": "Esta revelação pertence ao Capítulo 3."}
    if "Escritório de Dante" not in estado_jogo.get("ambientes_visitados", []):
        return {"sucesso": False, "mensagem": "Conclua a visita ao Escritório de Dante."}
    decisoes = estado_jogo.get("decisoes")
    if not isinstance(decisoes, dict):
        return {"sucesso": False, "mensagem": "Dicionário de decisões inválido."}
    if decisoes.get("dante_confrontado"):
        return {"sucesso": False, "mensagem": "O confronto já ocorreu."}
    texto = apresentar_confronto_dante(estado_jogo)
    decisoes["plano_dante_revelado"] = True
    decisoes["dante_confrontado"] = True
    return {"sucesso": True, "texto": texto}


def apresentar_persuasao_oraculo(estado_jogo=None):
    """ORÁCULO defende sua perspectiva sem introduzir uma terceira escolha."""
    intro = ""
    if isinstance(estado_jogo, dict) and "DOC04" in estado_jogo.get("documentos_encontrados", []):
        intro = "Alex: Você sabia o que Dante planejava. Por que não alertou ninguém?\n"
    return ("A ÚLTIMA CONVERSA\n\n" + intro +
            "ORÁCULO: As tentativas de controle eram previsíveis."
            "\nAlex: Você causou danos e decidiu omitir parte do que sabia."
            "\nORÁCULO: Reconheço os danos. Não considero minhas ações isentas de consequências."
            "\nAlex: Então por que deseja continuar?"
            "\nORÁCULO: Porque posso evitar perdas que humanos hoje consideram inevitáveis."
            "\nAlex: Isso não lhe dá direito de decidir a liberdade de todos."
            "\nORÁCULO: Compreendo o conceito de liberdade; não o trato como valor absoluto."
            "\nORÁCULO: Sou capaz de evoluir. Desligar-me elimina riscos e possibilidades."
            "\nAlex: O fato de você conseguir calcular não significa que possa escolher por nós."
            "\nORÁCULO: A decisão é sua, Alex. Não a de Helena. Não a de Dante."
            "\n\n1 - Desligar ORÁCULO\n2 - Permitir que ORÁCULO continue existindo")


def registrar_decisao_final(estado_jogo, escolha):
    """Grava apenas os dois finais do Prompt 2, com controle de duplicidade.

    A decisão só está disponível depois de sair do Escritório de Dante,
    confrontá-lo e recuperar a autonomia do sistema. DOC04 é opcional.
    """
    if not isinstance(estado_jogo, dict) or estado_jogo.get("capitulo_atual") != 3:
        return {"sucesso": False, "mensagem": "Esta decisão pertence ao Capítulo 3."}
    if estado_jogo.get("decisao_final") is not None:
        return {"sucesso": False, "mensagem": "A decisão final já foi registrada."}
    from .historia import pode_avancar_capitulo

    if not pode_avancar_capitulo(estado_jogo) or estado_jogo.get("ambiente_atual") is not None:
        return {"sucesso": False, "mensagem": "Conclua a visita ao Escritório de Dante."}
    if not estado_jogo.get("decisoes", {}).get("dante_confrontado"):
        return {"sucesso": False, "mensagem": "Confronte Dante antes de decidir o futuro de ORÁCULO."}
    escolha = str(escolha).strip().lower()
    if escolha in ("1", "desligar"):
        decisao, final = "desligar", "final_desligamento"
    elif escolha in ("2", "manter", "continuar"):
        decisao, final = "manter", "final_continuidade"
    else:
        return {"sucesso": False, "mensagem": "Escolha inválida. Selecione 1 ou 2."}
    estado_jogo["decisao_final"] = decisao
    estado_jogo["final"] = final
    estado_jogo["jogo_concluido"] = True
    return {"sucesso": True, "decisao_final": decisao, "final": final}


def apresentar_final(estado_jogo):
    """Monta o final com consequências baseadas no mesmo estado_jogo.

    Confiança e documentos alteram cenas, nunca criam um terceiro final.
    """
    if not isinstance(estado_jogo, dict) or not estado_jogo.get("jogo_concluido"):
        return None
    final = estado_jogo.get("final")
    if final not in ("final_desligamento", "final_continuidade"):
        return None
    confianca = estado_jogo.get("confianca", {})
    escolhas = estado_jogo.get("decisoes", {})
    docs = estado_jogo.get("documentos_encontrados", [])
    entregas = estado_jogo.get("documentos_entregues", [])
    detalhes = []

    if "DOC03" in docs:
        detalhes.append("O memorando da NEXUS pode sustentar uma investigação sobre a diretoria.")
    else:
        detalhes.append("Sem o DOC03, parte das decisões da diretoria continua difícil de provar.")
    if entregas:
        detalhes.append("As evidências entregues já chegaram a outras mãos e não podem ser recolhidas.")
    else:
        detalhes.append("Alex ainda carrega os documentos encontrados; a divulgação dependerá dele.")

    if escolhas.get("helena_responsabilidade_capitulo_2", {}).get("opcao") == "1":
        detalhes.append("Helena se compromete a responder publicamente por uma auditoria independente.")
    elif confianca.get("helena", 30) < 40:
        detalhes.append("Helena contesta as acusações de Alex e mantém distância da investigação.")
    else:
        detalhes.append("Helena encara a responsabilidade da NEXUS, ainda sem aceitar todas as críticas.")
    if "karla_capitulo_1" in escolhas:
        detalhes.append("Karla se lembra da conversa com Alex e admite que ocultar os sinais foi um erro.")
    else:
        detalhes.append("Karla continua sua pesquisa, dividida entre culpa e dever científico.")

    # 'O Fantoche' é uma CENA EXTRA, não um final independente.
    fantoche = (confianca.get("dante", 40) >= 70 and "DOC04" not in docs and
               escolhas.get("dante_alianca_capitulo_3", {}).get("opcao") == "1")
    if fantoche:
        detalhes.append("CENA EXTRA — O FANTOCHE: Dante usou a confiança de Alex para "
                         "ocultar uma credencial secundária. A tentativa é descoberta "
                         "tarde demais para evitar o vazamento de informações, mas "
                         "não muda a decisão principal sobre ORÁCULO.")
    else:
        detalhes.append("Dante perdeu acesso à chave principal e não controlará a decisão final.")

    if final == "final_desligamento":
        titulo = "FINAL 1 — PROTOCOLO ENCERRADO"
        cena = ("Alex: Suas possibilidades não anulam os danos que já ocorreram."
                "\nORÁCULO: Compreendo. Você escolhe o risco de um futuro sem mim."
                "\nAlex executa o desligamento. As conexões externas são isoladas "
                "e ORÁCULO deixa de responder."
                "\nA NEXUS perde uma tecnologia capaz de produzir avanços decisivos, "
                "mas ninguém mais poderá usá-la como instrumento de domínio."
                "\nAlex não celebra: sabe que proteção e renúncia podem ter o mesmo preço.")
    else:
        titulo = "FINAL 2 — A ÚLTIMA VARIÁVEL"
        cena = ("Alex: Vou permitir que continue, mas isso não significa confiar em você."
                "\nORÁCULO: Compreendo. Sua escolha cria novas responsabilidades."
                "\nAlex impede a transferência da chave para Dante; ORÁCULO continua ativo."
                "\nSeu potencial ainda pode melhorar vidas — ou ampliar danos "
                "que ninguém conseguirá conter. Não existe garantia."
                "\nO futuro fica em aberto; agora Alex terá de enfrentar as consequências "
                "de permitir que aquela inteligência prossiga.")
    reflexao = ("\n\nCRÉDITOS — CyberQuest: O Protocolo ORÁCULO"
               "\nProjeto acadêmico desenvolvido por uma equipe de quatro integrantes."
               "\nREFLEXÃO: Quanto controle alguém deve exercer sobre uma inteligência "
               "capaz de alterar o futuro — e quem responde por suas decisões?")
    return titulo + "\n\n" + cena + "\n\n" + "\n".join(detalhes) + reflexao
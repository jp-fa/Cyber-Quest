
"""
main.py
CyberQuest: O Protocolo ORÁCULO

Arquivo principal responsável por integrar:
- HISTORIA
- INVESTIGACAO
- SALVAMENTO

Responsabilidades:
- Iniciar ou carregar uma partida.
- Controlar os menus.
- Coordenar as ações do jogador.
- Integrar os módulos dos três capítulos.
- Realizar o salvamento automático.
- Controlar o avanço dos capítulos e o encerramento do jogo.

Execute a partir da raiz do projeto:

python -m main
"""

from HISTORIA import historia

from INVESTIGACAO import personagens
from INVESTIGACAO import investigacao
from INVESTIGACAO import capitulo1
from INVESTIGACAO import capitulo2
from INVESTIGACAO import capitulo3

from SALVAMENTO import ambientes
from SALVAMENTO import salvamento


# ============================================================
# FUNÇÕES GERAIS
# ============================================================

def salvar_progresso(estado_jogo):
    """Salva o estado atual do jogo."""

    if salvamento.salvar_jogo(estado_jogo):
        print("\n[PROGRESSO SALVO]")
        return True

    print("\n[AVISO] Não foi possível salvar o progresso.")
    return False


def mostrar_inventario(estado_jogo):
    """Exibe os documentos encontrados pelo jogador."""

    inventario = investigacao.obter_inventario(estado_jogo)

    print("\n========== INVENTÁRIO ==========")

    if not inventario:
        print("Você ainda não encontrou documentos.")
    else:
        for documento in inventario:
            print(f"\nCódigo: {documento['codigo']}")
            print(f"Nome: {documento['nome']}")
            print(f"Autor: {documento['autor']}")
            print(f"Classificação: {documento['classificacao']}")

            if documento["entregue"]:
                print(f"Situação: Entregue para {documento['entregue_para']}")
            else:
                print("Situação: Em posse de Alex")

    print("\n================================")


def mostrar_personagens_ambiente(nome_ambiente):
    """Mostra os personagens disponíveis no ambiente."""

    ids = ambientes.obter_personagens_ambiente(nome_ambiente)

    if not ids:
        print("Não há personagens neste ambiente.")
        return

    print("\nPersonagens presentes:")

    for personagem_id in ids:
        dados = personagens.obter_personagem(personagem_id)

        if dados:
            print(f"- {dados['nome']}")


def escolher_opcao(mensagem, opcoes_validas):
    """Solicita uma opção até receber uma resposta válida."""

    while True:
        escolha = input(mensagem).strip()

        if escolha in opcoes_validas:
            return escolha

        print("Opção inválida. Tente novamente.")


# ============================================================
# INTERAÇÕES COM PERSONAGENS
# ============================================================

def conversar_com_karla(estado_jogo):
    """Executa a conversa com Karla no Capítulo 1."""

    if personagens.verificar_personagem_abordado(estado_jogo, "karla"):
        print("\nAlex já conversou com Karla neste capítulo.")
        return False

    conversa = historia.apresentar_conversa_karla()

    print("\n" + conversa["texto"])

    print("\nEscolha sua resposta:")

    for numero, descricao in conversa["opcoes"].items():
        print(f"{numero} - {descricao}")

    escolha = escolher_opcao("Sua escolha: ", ["1", "2"])

    resultado = capitulo1.interagir_com_karla(
        estado_jogo,
        escolha
    )

    if not resultado.get("sucesso"):
        print("\n" + resultado.get("mensagem", "Não foi possível conversar."))
        return False

    print("\n" + resultado["texto"])

    return True


def conversar_com_oraculo(estado_jogo):
    """Registra a conversa opcional com ORÁCULO no Capítulo 1."""

    if personagens.verificar_personagem_abordado(estado_jogo, "oraculo"):
        print("\nAlex já conversou com ORÁCULO neste capítulo.")
        return False

    print("\n" + historia.apresentar_conversa_oraculo())

    sucesso = capitulo1.registrar_conversa_oraculo(estado_jogo)

    if not sucesso:
        print("Não foi possível registrar a conversa.")
        return False

    return True


def conversar_com_helena(estado_jogo):
    """Executa as duas etapas da conversa com Helena."""

    conversa = historia.apresentar_conversa_helena()

    print("\n" + conversa["texto"])

    etapas = conversa["etapas"]

    for etapa in etapas:

        chave = f"helena_{etapa}_capitulo_2"

        # Permite continuar uma conversa interrompida.
        if chave in estado_jogo["decisoes"]:
            print(f"\nEtapa '{etapa}' já registrada.")
            continue

        print(f"\nEtapa: {etapa.upper()}")

        opcoes = conversa["opcoes"][etapa]

        for numero, descricao in opcoes.items():
            print(f"{numero} - {descricao}")

        escolha = escolher_opcao("Sua escolha: ", ["1", "2"])

        resultado = capitulo2.interagir_com_helena(
            estado_jogo,
            etapa,
            escolha
        )

        if not resultado.get("sucesso"):
            print("\n" + resultado.get("mensagem", "Erro na interação."))
            return False

        print("\n" + resultado["texto"])

        # Salva cada etapa para permitir retomada.
        salvar_progresso(estado_jogo)

    return True


def conversar_com_dante(estado_jogo):
    """Executa as duas etapas da conversa com Dante."""

    conversa = historia.apresentar_conversa_dante()

    print("\n" + conversa["texto"])

    etapas = conversa["etapas"]

    for etapa in etapas:

        chave = f"dante_{etapa}_capitulo_3"

        # Permite continuar uma conversa interrompida.
        if chave in estado_jogo["decisoes"]:
            print(f"\nEtapa '{etapa}' já registrada.")
            continue

        print(f"\nEtapa: {etapa.upper()}")

        opcoes = conversa["opcoes"][etapa]

        for numero, descricao in opcoes.items():
            print(f"{numero} - {descricao}")

        escolha = escolher_opcao("Sua escolha: ", ["1", "2"])

        resultado = capitulo3.interagir_com_dante(
            estado_jogo,
            etapa,
            escolha
        )

        if not resultado.get("sucesso"):
            print("\n" + resultado.get("mensagem", "Erro na interação."))
            return False

        print("\n" + resultado["texto"])

        # Salva cada etapa para permitir retomada.
        salvar_progresso(estado_jogo)

    return True


# ============================================================
# DOCUMENTOS
# ============================================================

def encontrar_documento(estado_jogo, acao):
    """Localiza o documento correspondente à ação escolhida."""

    documentos = {
        "encontrar_doc01": (
            capitulo1.encontrar_doc01,
            historia.apresentar_doc01
        ),
        "encontrar_doc02": (
            capitulo1.encontrar_doc02,
            historia.apresentar_doc02
        ),
        "encontrar_doc03": (
            capitulo2.encontrar_doc03,
            historia.apresentar_doc03
        ),
        "encontrar_doc04": (
            capitulo3.encontrar_doc04,
            historia.apresentar_doc04
        )
    }

    if acao not in documentos:
        print("Documento não reconhecido.")
        return False

    funcao_encontrar, funcao_narrativa = documentos[acao]

    if not funcao_encontrar(estado_jogo):
        print("\nEste documento já foi encontrado ou não está disponível.")
        return False

    print("\n" + funcao_narrativa())

    return True


def entregar_documentos(estado_jogo):
    """Permite entregar documentos encontrados a outros personagens."""

    inventario = investigacao.obter_inventario(estado_jogo)

    disponiveis = [
        documento
        for documento in inventario
        if not documento["entregue"]
    ]

    if not disponiveis:
        print("\nNão existem documentos disponíveis para entrega.")
        return False

    destinatarios = investigacao.listar_destinatarios()

    entregou_algum = False

    while disponiveis:

        print("\n========== DOCUMENTOS DISPONÍVEIS ==========")

        for documento in disponiveis:
            print(
                f"{documento['codigo']} - {documento['nome']}"
            )

        print("0 - Encerrar entregas")

        codigo = input("\nDigite o código do documento: ").strip().upper()

        if codigo == "0":
            break

        documento_escolhido = next(
            (
                documento
                for documento in disponiveis
                if documento["codigo"] == codigo
            ),
            None
        )

        if documento_escolhido is None:
            print("Código inválido.")
            continue

        print("\n========== DESTINATÁRIOS ==========")

        for indice, destinatario in enumerate(destinatarios, start=1):
            print(f"{indice} - {destinatario['nome']}")

        print("0 - Cancelar entrega")

        escolha = input("\nEscolha o destinatário: ").strip()

        if escolha == "0":
            continue

        if not escolha.isdigit():
            print("Opção inválida.")
            continue

        indice = int(escolha) - 1

        if indice < 0 or indice >= len(destinatarios):
            print("Destinatário inválido.")
            continue

        destinatario = destinatarios[indice]

        sucesso = investigacao.entregar_documento(
            estado_jogo,
            codigo,
            destinatario["id"]
        )

        if sucesso:
            print(
                f"\nDocumento {codigo} entregue para "
                f"{destinatario['nome']}."
            )

            entregou_algum = True

            salvar_progresso(estado_jogo)

            disponiveis = [
                documento
                for documento in disponiveis
                if documento["codigo"] != codigo
            ]

        else:
            print("Não foi possível entregar este documento.")

    return entregou_algum


# ============================================================
# EXECUÇÃO DAS AÇÕES DOS AMBIENTES
# ============================================================

def executar_conversa(estado_jogo, acao):

    conversas = {
        "conversar_karla": conversar_com_karla,
        "conversar_oraculo": conversar_com_oraculo,
        "conversar_helena": conversar_com_helena,
        "conversar_dante": conversar_com_dante
    }

    funcao = conversas.get(acao)

    if funcao is None:
        return False

    return funcao(estado_jogo)


def executar_acao(estado_jogo, acao):
    """Executa uma ação disponível no ambiente atual."""

    nome_ambiente = estado_jogo["ambiente_atual"]

    if ambientes.acao_ja_realizada(estado_jogo, acao):
        print("\nEsta ação já foi realizada neste ambiente.")
        return

    # --------------------------------------------------------
    # ENCONTRAR DOCUMENTOS
    # --------------------------------------------------------

    if acao.startswith("encontrar_doc"):

        sucesso = encontrar_documento(
            estado_jogo,
            acao
        )

        if not sucesso:
            return

    # --------------------------------------------------------
    # CONVERSAR COM PERSONAGENS
    # --------------------------------------------------------

    elif acao.startswith("conversar_"):

        sucesso = executar_conversa(
            estado_jogo,
            acao
        )

        if not sucesso:
            return

    # --------------------------------------------------------
    # ENTREGAR DOCUMENTOS
    # --------------------------------------------------------

    elif acao == "entregar_documentos":

        sucesso = entregar_documentos(estado_jogo)

        if not sucesso:
            return

    # --------------------------------------------------------
    # OUTRAS AÇÕES NARRATIVAS
    # --------------------------------------------------------

    else:

        narrativa = historia.obter_narrativa_acao(
            nome_ambiente,
            acao
        )

        if narrativa:
            print("\n" + narrativa)
        else:
            print("\nAção realizada.")

    # --------------------------------------------------------
    # REGISTRAR A AÇÃO E SALVAR
    # --------------------------------------------------------

    if ambientes.registrar_acao_ambiente(estado_jogo, acao):
        salvar_progresso(estado_jogo)
    else:
        print("\nNão foi possível registrar esta ação.")


# ============================================================
# MENU DENTRO DOS AMBIENTES
# ============================================================

def menu_ambiente(estado_jogo):
    """Controla as opções enquanto Alex está dentro de um ambiente."""

    nome_ambiente = estado_jogo["ambiente_atual"]

    while estado_jogo["ambiente_atual"] is not None:

        dados_ambiente = ambientes.AMBIENTES[nome_ambiente]

        print("\n" + "=" * 50)
        print(f"AMBIENTE: {nome_ambiente.upper()}")
        print("=" * 50)

        mostrar_personagens_ambiente(nome_ambiente)

        acoes_disponiveis = [
            (codigo, descricao)
            for codigo, descricao in dados_ambiente["acoes"].items()
            if not ambientes.acao_ja_realizada(estado_jogo, codigo)
        ]

        print("\nO que deseja fazer?")

        for indice, (codigo, descricao) in enumerate(
            acoes_disponiveis,
            start=1
        ):
            print(f"{indice} - {descricao}")

        print("\n0 - Consultar inventário")
        print("9 - Sair do ambiente")

        escolha = input("\nEscolha: ").strip()

        if escolha == "0":
            mostrar_inventario(estado_jogo)

        elif escolha == "9":

            if ambientes.sair_ambiente(estado_jogo):
                print(f"\nAlex saiu de {nome_ambiente}.")

                salvar_progresso(estado_jogo)

            return

        elif escolha.isdigit():

            indice = int(escolha) - 1

            if 0 <= indice < len(acoes_disponiveis):

                codigo = acoes_disponiveis[indice][0]

                executar_acao(
                    estado_jogo,
                    codigo
                )

            else:
                print("Opção inválida.")

        else:
            print("Digite uma opção válida.")


# ============================================================
# ENTRADA NOS AMBIENTES
# ============================================================

def entrar_em_ambiente(estado_jogo, nome):
    """Realiza a entrada em um ambiente e salva o progresso."""

    motivo = ambientes.motivo_bloqueio_entrada(
        estado_jogo,
        nome
    )

    if motivo is not None:
        print("\n" + motivo)
        return

    if ambientes.entrar_ambiente(estado_jogo, nome):

        print(f"\nAlex entrou em {nome}.")

        salvar_progresso(estado_jogo)

        menu_ambiente(estado_jogo)


# ============================================================
# AVANÇO DOS CAPÍTULOS
# ============================================================

def encerrar_e_avancar_capitulo(estado_jogo):
    """Encerra o capítulo atual e avança para o próximo."""

    resultado = historia.encerrar_capitulo(estado_jogo)

    if not resultado.get("sucesso"):
        print("\n" + resultado["texto"])
        return

    print("\n" + resultado["texto"])

    capitulo_atual = estado_jogo["capitulo_atual"]

    if capitulo_atual >= 3:
        return

    if historia.avancar_capitulo(estado_jogo):

        salvar_progresso(estado_jogo)

        print("\n" + "=" * 50)
        print(f"CAPÍTULO {estado_jogo['capitulo_atual']}")
        print("=" * 50)

        abertura = historia.abrir_capitulo(estado_jogo)

        if abertura:
            print("\n" + abertura)


# ============================================================
# CONFRONTO E DECISÃO FINAL
# ============================================================

def resolver_final(estado_jogo):
    """Executa o confronto com Dante e a decisão sobre ORÁCULO."""

    decisoes = estado_jogo["decisoes"]

    # --------------------------------------------------------
    # CONFRONTO COM DANTE
    # --------------------------------------------------------

    if not decisoes.get("dante_confrontado"):

        resultado = historia.registrar_confronto_dante(
            estado_jogo
        )

        if not resultado.get("sucesso"):
            print("\n" + resultado.get("mensagem", "Não foi possível confrontar Dante."))
            return False

        print("\n" + resultado["texto"])

        salvar_progresso(estado_jogo)

    # --------------------------------------------------------
    # ÚLTIMA CONVERSA COM ORÁCULO
    # --------------------------------------------------------

    if estado_jogo["decisao_final"] is None:

        print("\n" + historia.apresentar_persuasao_oraculo(estado_jogo))

        escolha = escolher_opcao(
            "\nQual será o destino de ORÁCULO? ",
            ["1", "2"]
        )

        resultado = historia.registrar_decisao_final(
            estado_jogo,
            escolha
        )

        if not resultado.get("sucesso"):
            print("\n" + resultado.get("mensagem", "Decisão inválida."))
            return False

        salvar_progresso(estado_jogo)

    # --------------------------------------------------------
    # APRESENTAR FINAL
    # --------------------------------------------------------

    texto_final = historia.apresentar_final(estado_jogo)

    if texto_final:
        print("\n" + "=" * 60)
        print(texto_final)
        print("=" * 60)

    return True


# ============================================================
# LOOP PRINCIPAL DA PARTIDA
# ============================================================

def executar_jogo(estado_jogo):
    """Controla o fluxo geral dos três capítulos."""

    if estado_jogo["jogo_concluido"]:
        texto_final = historia.apresentar_final(estado_jogo)

        if texto_final:
            print("\n" + texto_final)

        return

    while not estado_jogo["jogo_concluido"]:

        capitulo = estado_jogo["capitulo_atual"]

        # Se o jogador estava dentro de uma sala quando saiu,
        # o ambiente será retomado automaticamente.
        if estado_jogo["ambiente_atual"] is not None:

            menu_ambiente(estado_jogo)

            continue

        # Capítulo 3: depois de sair do escritório, inicia o final.
        if (
            capitulo == 3
            and "Escritório de Dante" in estado_jogo["ambientes_visitados"]
        ):

            resolver_final(estado_jogo)

            if not estado_jogo["jogo_concluido"]:
                print("\nNão foi possível concluir o capítulo.")
                break

            continue

        ambientes_disponiveis = ambientes.listar_ambientes(
            estado_jogo
        )

        # Todos os ambientes obrigatórios foram visitados.
        if not ambientes_disponiveis:

            encerrar_e_avancar_capitulo(estado_jogo)

            continue

        print("\n" + "=" * 50)
        print(f"CYBERQUEST — CAPÍTULO {capitulo}")
        print("=" * 50)

        print("\nEscolha um ambiente:")

        for indice, nome in enumerate(
            ambientes_disponiveis,
            start=1
        ):
            print(f"{indice} - {nome}")

        print("\n0 - Consultar inventário")
        print("9 - Salvar e sair do jogo")

        escolha = input("\nEscolha: ").strip()

        if escolha == "0":

            mostrar_inventario(estado_jogo)

        elif escolha == "9":

            salvar_progresso(estado_jogo)

            print("\nJogo encerrado. Seu progresso foi preservado.")

            return

        elif escolha.isdigit():

            indice = int(escolha) - 1

            if 0 <= indice < len(ambientes_disponiveis):

                nome = ambientes_disponiveis[indice]

                entrar_em_ambiente(
                    estado_jogo,
                    nome
                )

            else:
                print("Opção inválida.")

        else:
            print("Digite uma opção válida.")

    if estado_jogo["jogo_concluido"]:
        print("\nObrigado por jogar CyberQuest: O Protocolo ORÁCULO!")


# ============================================================
# MENU INICIAL
# ============================================================

def iniciar_nova_partida():
    """Cria uma partida nova e salva o estado inicial."""

    estado_jogo = salvamento.criar_estado_inicial()

    salvar_progresso(estado_jogo)

    print("\n" + "=" * 60)
    print("CYBERQUEST: O PROTOCOLO ORÁCULO")
    print("=" * 60)

    abertura = historia.abrir_capitulo(estado_jogo)

    if abertura:
        print("\n" + abertura)

    return estado_jogo


def menu_inicial():
    """Permite iniciar uma partida ou carregar um save existente."""

    estado_salvo, erro = salvamento.carregar_jogo()

    print("\n" + "=" * 60)
    print("CYBERQUEST: O PROTOCOLO ORÁCULO")
    print("=" * 60)

    if estado_salvo is not None:

        print("\n1 - Continuar partida")
        print("2 - Iniciar nova partida")
        print("0 - Sair")

        escolha = escolher_opcao(
            "\nEscolha: ",
            ["0", "1", "2"]
        )

        if escolha == "0":
            return None

        if escolha == "1":

            print("\nProgresso carregado com sucesso.")

            print(
                f"Capítulo atual: {estado_salvo['capitulo_atual']}"
            )

            if estado_salvo["ambiente_atual"] is not None:
                print(
                    "Ambiente em andamento: "
                    + estado_salvo["ambiente_atual"]
                )

            return estado_salvo

        if escolha == "2":

            confirmacao = input(
                "\nIsso substituirá o progresso salvo. Deseja continuar? (s/n): "
            ).strip().lower()

            if confirmacao != "s":
                return None

            return iniciar_nova_partida()

    else:

        print("\nNenhum progresso válido foi encontrado.")

        if erro:
            print(erro)

        print("\n1 - Iniciar nova partida")
        print("0 - Sair")

        escolha = escolher_opcao(
            "\nEscolha: ",
            ["0", "1"]
        )

        if escolha == "0":
            return None

        return iniciar_nova_partida()


# ============================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================

def main():

    estado_jogo = menu_inicial()

    if estado_jogo is None:
        print("\nAté a próxima!")
        return

    executar_jogo(estado_jogo)


if __name__ == "__main__":
    main()
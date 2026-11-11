"""
ambientes.py - Ambientes do CyberQuest: O Protocolo ORÁCULO
Responsável: Integrante 4 (Sistemas e Persistência)

O QUE ESTE MÓDULO FAZ
    - Cadastra os 4 ambientes oficiais (em qual capítulo estão, quem está lá,
      que ações existem e qual documento cada um guarda).
    - Controla entrada e saída: cada ambiente só pode ser visitado UMA vez
      por partida, e só conta como visitado quando Alex SAI dele.
    - Não tem textos de história nem menus (isso é da historia.py e do main.py).

CHAVES DO estado_jogo USADAS AQUI
    ambiente_atual       -> nome do ambiente onde Alex está (ou None).
                            Se o jogo fechar no meio da visita, continua preenchido:
                            é assim que a visita é retomada ao carregar o save.
    ambientes_visitados  -> lista dos ambientes já CONCLUÍDOS (Alex já saiu).
    ambientes_estado     -> progresso de cada sala. Formato proposto:
                            {"Laboratório": {"acoes_realizadas": ["observar_equipamentos"]}}
    capitulo_atual       -> usado para saber quais ambientes estão disponíveis.

CONVENÇÃO DO GRUPO
    As funções recebem o estado_jogo como primeiro parâmetro, alteram o PRÓPRIO
    dicionário (nunca uma cópia) e devolvem True/False (ou o dado pedido).
    Quem chama salvamento.salvar_jogo(estado_jogo) depois é o main.py.

IMPORTANTE: este módulo NÃO importa historia.py nem personagens.py
    (evita import circular). Quem coordena os módulos é o main.py.
"""

# ------------------------------------------------------------------
# CADASTRO DOS AMBIENTES (dados vindos do roteiro, seção 6)
# Os nomes precisam ser IDÊNTICOS (acentos incluídos) aos usados em
# historia.obter_ambientes_capitulo, senão o capítulo nunca avança.
# "acoes" e "documento": formato a confirmar com os integrantes 2 e 3.
# ------------------------------------------------------------------
AMBIENTES = {
    "Laboratório": {
        "capitulo": 1,
        "personagens": ["Karla", "ORÁCULO"],
        "documento": "DOC01",
        "acoes": {
            "observar_equipamentos": "Observar equipamentos",
            "investigar_ponto_cego": "Investigar um ponto cego das câmeras",
            "encontrar_doc01": "Procurar o documento DOC01",
            "conversar_karla": "Conversar com a Dra. Karla",
            "conversar_oraculo": "Conversar com ORÁCULO (opcional)",
        },
    },
    "Sala de Segurança": {
        "capitulo": 1,
        "personagens": ["ORÁCULO"],
        "documento": "DOC02",
        "acoes": {
            "consultar_registros": "Consultar registros de entrada e saída",
            "comparar_horarios": "Comparar horários de acesso",
            "encontrar_doc02": "Procurar o documento DOC02",
            "conversar_oraculo": "Conversar com ORÁCULO (se ainda não abordado)",
        },
    },
    "Sala de Planejamento": {
        "capitulo": 2,
        "personagens": ["Helena"],
        "documento": "DOC03",
        "acoes": {
            "examinar_projecoes": "Examinar projeções estratégicas",
            "investigar_planos": "Investigar os planos da NEXUS",
            "encontrar_doc03": "Procurar o documento DOC03",
            "conversar_helena": "Conversar com Helena",
            "entregar_documentos": "Entregar documentos encontrados",
            "comunicacao_oraculo": "Receber a comunicação remota de ORÁCULO",
        },
    },
    "Escritório de Dante": {
        "capitulo": 3,
        "personagens": ["Dante"],
        "documento": "DOC04",
        "acoes": {
            "investigar_escritorio": "Investigar o escritório",
            "explorar_ponto_cego": "Explorar um ponto cego próximo aos documentos confidenciais",
            "encontrar_doc04": "Procurar o documento DOC04",
            "conversar_dante": "Conversar com Dante",
            "entregar_documentos": "Entregar documentos a Dante",
        },
    },
}


def _motivo_bloqueio(estado_jogo, nome):
    """
    Concentra TODAS as regras de entrada em um só lugar.
    Devolve None se Alex pode entrar, ou um texto dizendo por que não pode.
    """
    # 1) O ambiente existe no cadastro?
    if not isinstance(nome, str) or nome not in AMBIENTES:
        return "Esse ambiente não existe."

    # 2) Visita única: já saiu dele antes?
    if nome in estado_jogo["ambientes_visitados"]:
        return "Você já visitou este ambiente."

    # 3) Ele pertence ao capítulo atual?
    if AMBIENTES[nome]["capitulo"] != estado_jogo["capitulo_atual"]:
        return "Este ambiente não faz parte do capítulo atual."

    # 4) Já está dentro de outro ambiente? (se for o MESMO, é retomada: pode)
    atual = estado_jogo["ambiente_atual"]
    if atual is not None and atual != nome:
        return f"Você ainda está em {atual}. Saia antes de entrar em outro ambiente."

    return None


def motivo_bloqueio_entrada(estado_jogo, nome):
    """EXTRA (não está na seção 12): texto explicando por que a entrada foi
    negada, ou None se pode entrar. Útil para o main.py mostrar ao jogador."""
    return _motivo_bloqueio(estado_jogo, nome)


def entrar_ambiente(estado_jogo, nome):
    """Alex entra no ambiente. Devolve True se entrou (ou retomou), False se não pôde."""
    if _motivo_bloqueio(estado_jogo, nome) is not None:
        return False

    estado_jogo["ambiente_atual"] = nome
    # Prepara o registro de progresso da sala só se ainda não existir
    # (numa retomada, o progresso anterior é preservado).
    estado_jogo["ambientes_estado"].setdefault(nome, {"acoes_realizadas": []})
    return True


def sair_ambiente(estado_jogo):
    """Alex sai do ambiente atual. SÓ AGORA o ambiente conta como visitado.
    Devolve True se saiu, False se não estava em nenhum ambiente."""
    atual = estado_jogo["ambiente_atual"]
    if atual is None:
        return False

    if atual not in estado_jogo["ambientes_visitados"]:
        estado_jogo["ambientes_visitados"].append(atual)
    estado_jogo["ambiente_atual"] = None
    return True


def listar_ambientes(estado_jogo):
    """Nomes dos ambientes do capítulo atual que ainda não foram visitados.
    (Se há uma visita em andamento, o ambiente dela continua na lista.)"""
    return [
        nome
        for nome, dados in AMBIENTES.items()
        if dados["capitulo"] == estado_jogo["capitulo_atual"]
        and nome not in estado_jogo["ambientes_visitados"]
    ]


def obter_personagens_ambiente(nome):
    """Lista dos personagens que podem ser abordados no ambiente
    (lista vazia se o ambiente não existir). Devolve uma cópia."""
    if not isinstance(nome, str) or nome not in AMBIENTES:
        return []
    return list(AMBIENTES[nome]["personagens"])


def verificar_ambiente_visitado(estado_jogo, nome):
    """True se Alex já visitou (e saiu de) o ambiente."""
    return nome in estado_jogo["ambientes_visitados"]


# ------------------------------------------------------------------
# EXTRAS (não estão na seção 12): progresso dentro da sala, para retomar
# a visita do ponto onde parou. Confirmar o formato com o integrante 3.
# ------------------------------------------------------------------
def registrar_acao_ambiente(estado_jogo, acao):
    """Registra uma ação feita no ambiente ATUAL (usar um id de AMBIENTES[...]["acoes"]).
    Devolve True se registrou; False se não há ambiente atual, a ação não
    existe ali ou já tinha sido feita."""
    atual = estado_jogo["ambiente_atual"]
    if atual is None or acao not in AMBIENTES[atual]["acoes"]:
        return False

    registro = estado_jogo["ambientes_estado"].setdefault(atual, {})
    feitas = registro.setdefault("acoes_realizadas", [])
    if acao in feitas:
        return False
    feitas.append(acao)
    return True


def acao_ja_realizada(estado_jogo, acao):
    """True se a ação já foi registrada no ambiente ATUAL."""
    atual = estado_jogo["ambiente_atual"]
    if atual is None:
        return False
    registro = estado_jogo["ambientes_estado"].get(atual, {})
    return acao in registro.get("acoes_realizadas", [])

# import sys
# from pathlib import Path

# sys.path.append(str(Path(__file__).resolve().parent.parent))

# from investigacao import *

# # # encontrar_documento("projeto_oraculo")
# # # encontrar_documento("relatorio_seguranca")

# # # exibir_inventario()

# # # consultar_documento()

# # # entregar_documento()

# # # consultar_historico_entregas()

# # # from investigacao import *

# # # # Encontrar documento
# # # encontrar_documento("projeto_oraculo")

# # # # Primeira entrega
# # # print("\n===== PRIMEIRA ENTREGA =====")
# # # entregar_documento()

# # # # Segunda tentativa
# # # print("\n===== SEGUNDA ENTREGA =====")
# # # entregar_documento()

# # # # Consultar inventário
# # # exibir_inventario()

# # # from investigacao import *

# # # print("\n===== PRIMEIRA TENTATIVA =====")
# # # encontrar_documento("projeto_oraculo")

# # # print("\n===== SEGUNDA TENTATIVA =====")
# # # encontrar_documento("projeto_oraculo")

# # # print("\n===== INVENTÁRIO FINAL =====")
# # # exibir_inventario()

# # # from investigacao import *

# # # # Encontrar documento
# # # encontrar_documento("projeto_oraculo")

# # # # Tentar entregar e cancelar
# # # print("\n===== TESTE DE CANCELAMENTO =====")
# # # entregar_documento()

# # # # Conferir inventário
# # # print("\n===== INVENTÁRIO FINAL =====")
# # # exibir_inventario()

# # # from investigacao import *

# # # encontrar_documento("projeto_oraculo")

# # # print("\n===== TESTE DE DESTINATÁRIO INVÁLIDO =====")
# # # entregar_documento()

# # # print("\n===== INVENTÁRIO FINAL =====")
# # # exibir_inventario()

# # # print("\n===== TESTE 1: ENCONTRAR DOCUMENTO =====")
# # # encontrar_documento("projeto_oraculo")

# # # print("\n===== TESTE 2: TENTAR ENCONTRAR NOVAMENTE =====")
# # # encontrar_documento("projeto_oraculo")

# # # print("\n===== TESTE 3: EXIBIR INVENTÁRIO =====")
# # # exibir_inventario()

# # # print("\n===== TESTE 4: CONSULTAR DOCUMENTO =====")
# # # consultar_documento()

# # # print("\n===== TESTE 5: LISTAR DESTINATÁRIOS =====")
# # # listar_destinatarios()

# # # print("\n===== TESTE 6: CONSULTAR HISTÓRICO =====")
# # # consultar_historico_entregas()

# # print("\n===== PREPARANDO DOCUMENTO PARA ENTREGA =====")
# # encontrar_documento("projeto_oraculo")

# print("\n===== TESTE 7: ENTREGAR DOCUMENTO =====")
# entregar_documento()

# print("\n===== TESTE 8: TENTAR ENTREGAR NOVAMENTE =====")
# entregar_documento()

# print("\n===== TESTE 9: CONFERIR INVENTÁRIO =====")
# exibir_inventario()

# print("\n===== TESTE 10: CONFERIR HISTÓRICO =====")
# consultar_historico_entregas()

# print("\n===== TESTE 11: ALTERAR CONFIANÇA PELA INVESTIGAÇÃO =====")
# aplicar_impacto_confianca("karla", 10, "capitulo_1")

# print("\n===== TESTE 12: OBTER ESTADO DA INVESTIGAÇÃO =====")

# estado = obter_estado_investigacao()

# print("Tipo do estado:", type(estado))
# print("Informações armazenadas:", list(estado.keys()))


# print("\n===== TESTE 13: MODIFICAR O ESTADO =====")

# encontrar_documento("relatorio_seguranca")

# print("\nInventário após encontrar outro documento:")
# exibir_inventario()


# print("\n===== TESTE 14: RESTAURAR ESTADO ANTERIOR =====")

# carregar_estado_investigacao(estado)

# print("\nInventário após restaurar:")
# exibir_inventario()


# print("\n===== TESTE 15: CONFERIR HISTÓRICO RESTAURADO =====")

# consultar_historico_entregas()
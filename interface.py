# =========================================================
# ARQUIVO: interface.py (Sua Interface Cyberpunk no Tkinter)
# =========================================================
import investigacao; print("---> FICHEIRO QUE ESTÁ A SER LIDO:", investigacao.__file__)

import tkinter as tk
from tkinter import simpledialog

# Importando os arquivos dos seus colegas
import historia
import investigacao



class SistemaNexusGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA OPERACIONAL NEXUS v2.0 // Protocolo ORÁCULO")
        self.root.geometry("950x650")
        self.root.configure(bg="#0d1117")

        # Cores do Tema Cyberpunk / Terminal
        self.cor_bg = "#0d1117"
        self.cor_card = "#161b22"
        self.cor_texto = "#58a6ff"      # Ciano
        self.cor_destaque = "#3fb950"   # Verde terminal
        self.cor_aviso = "#f85149"      # Vermelho erro/alerta
        self.cor_amarelo = "#d29922"    # Amarelo alerta

        # Estado da História (veio do historia.py)
        self.estado_jogo = historia.criar_estado_inicial()
        
        self.criar_componentes()
        self.carregar_cena_atual()

    def criar_componentes(self):
        # Título da Janela
        self.lbl_header = tk.Label(
            self.root, 
            text="> SISTEMA OPERACIONAL NEXUS v2.0 // PROTOCOLO ORÁCULO", 
            bg=self.cor_bg, 
            fg=self.cor_destaque, 
            font=("Consolas", 14, "bold")
        )
        self.lbl_header.pack(pady=10)

        # Quadro do Terminal (História)
        self.frame_terminal = tk.Frame(self.root, bg=self.cor_card, bd=1, relief="solid")
        self.frame_terminal.pack(fill="both", expand=True, padx=20, pady=5)

        self.txt_terminal = tk.Text(
            self.frame_terminal, 
            bg="#010409", 
            fg=self.cor_texto, 
            font=("Consolas", 11),
            insertbackground="white",
            state="disabled",
            bd=0,
            wrap="word"
        )
        self.txt_terminal.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(self.frame_terminal, command=self.txt_terminal.yview)
        scrollbar.pack(side="right", fill="y")
        self.txt_terminal.config(yscrollcommand=scrollbar.set)

        # Área de Botões da História (Criados dinamicamente)
        self.frame_opcoes = tk.Frame(self.root, bg=self.cor_bg)
        self.frame_opcoes.pack(fill="x", padx=20, pady=5)

        # Painel Inferior: Ferramentas de Investigação
        self.frame_ferramentas = tk.Frame(self.root, bg=self.cor_card, bd=1, relief="solid")
        self.frame_ferramentas.pack(fill="x", padx=20, pady=10)

        lbl_tools = tk.Label(
            self.frame_ferramentas, 
            text="[ MÓDULOS DE INVESTIGAÇÃO ]", 
            bg=self.cor_card, 
            fg=self.cor_amarelo, 
            font=("Consolas", 9, "bold")
        )
        lbl_tools.pack(anchor="w", padx=10, pady=2)

        # Botão 1: Ver Personagens (Chama investigacao.py)
        self.btn_personagem = tk.Button(
            self.frame_ferramentas,
            text="Buscar Personagem",
            bg="#21262d",
            fg=self.cor_texto,
            font=("Consolas", 9, "bold"),
            relief="flat",
            command=self.acao_consultar_personagem
        )
        self.btn_personagem.pack(side="left", padx=10, pady=5)

        # Botão 2: Inventário (Chama investigacao.py)
        self.btn_inventario = tk.Button(
            self.frame_ferramentas,
            text="Ver Inventário",
            bg="#21262d",
            fg=self.cor_destaque,
            font=("Consolas", 9, "bold"),
            relief="flat",
            command=self.acao_ver_inventario
        )
        self.btn_inventario.pack(side="left", padx=5, pady=5)

        # Botão 3: Escanear Pista (Chama investigacao.py)
        self.btn_buscar_pista = tk.Button(
            self.frame_ferramentas,
            text="Escanear Pista (1 a 4)",
            bg="#21262d",
            fg=self.cor_amarelo,
            font=("Consolas", 9, "bold"),
            relief="flat",
            command=self.acao_escanear_pista
        )
        self.btn_buscar_pista.pack(side="left", padx=5, pady=5)

    def escrever_no_terminal(self, texto, limpar=False):
        """Escreve o texto dentro da caixa cinza do terminal."""
        self.txt_terminal.config(state="normal")
        if limpar:
            self.txt_terminal.delete("1.0", "end")
        self.txt_terminal.insert("end", texto + "\n\n")
        self.txt_terminal.see("end")
        self.txt_terminal.config(state="disabled")

    def carregar_cena_atual(self):
        """Carrega a história do capitulo do historia.py"""
        cena_id = self.estado_jogo["cena_atual"]
        cap = historia.CAPITULOS.get(cena_id)

        # Limpa botões de escolhas anteriores
        for widget in self.frame_opcoes.winfo_children():
            widget.destroy()

        if not cap:
            self.escrever_no_terminal("=== FIM DA DEMONSTRAÇÃO ===", limpar=True)
            return

        # Exibe o texto da história
        conteudo = f"--- {cap['titulo'].upper()} ---\n\n{cap['texto']}"
        self.escrever_no_terminal(conteudo, limpar=True)

        # Cria os botões com as opções da história
        if cap["opcoes"]:
            lbl_escolha = tk.Label(
                self.frame_opcoes, 
                text="SELECIONE SUA AÇÃO:", 
                bg=self.cor_bg, 
                fg=self.cor_destaque, 
                font=("Consolas", 10, "bold")
            )
            lbl_escolha.pack(anchor="w", pady=2)

            for num_opcao, desc in cap["opcoes"].items():
                btn = tk.Button(
                    self.frame_opcoes,
                    text=f"[{num_opcao}] {desc}",
                    bg="#21262d",
                    fg="#c9d1d9",
                    font=("Consolas", 10),
                    anchor="w",
                    justify="left",
                    relief="flat",
                    activebackground="#30363d",
                    activeforeground=self.cor_destaque,
                    command=lambda o=num_opcao: self.tomar_decisao(o)
                )
                btn.pack(fill="x", pady=2)
        else:
            self.escrever_no_terminal("\n[ FIM DA DEMONSTRAÇÃO DA SPRINT ]")

    def tomar_decisao(self, opcao):
        """Avança a história quando clica num botão."""
        cena_atual = self.estado_jogo["cena_atual"]
        proxima_cena = historia.processar_escolha(cena_atual, opcao, self.estado_jogo)
        self.estado_jogo["cena_atual"] = proxima_cena
        self.carregar_cena_atual()

    # --- AÇÕES DOS BOTÕES DE INVESTIGAÇÃO ---

    def acao_consultar_personagem(self):
        nome = simpledialog.askstring("NEXUS DB", "Digite o nome (alex, dante, karla, helena, oraculo):")
        if nome:
            resultado = investigacao.buscar_personagem(nome)
            self.escrever_no_terminal(f">> CONSULTA DE PERSONAGEM:\n{resultado}")

    def acao_ver_inventario(self):
        texto_inv = investigacao.exibir_inventario_texto()
        self.escrever_no_terminal(f">> {texto_inv}")

    def acao_escanear_pista(self):
        doc_id = simpledialog.askinteger("Scanner", "Digite o ID do documento (1, 2, 3 ou 4):")
        if doc_id:
            resultado = investigacao.encontrar_documento_por_id(doc_id)
            self.escrever_no_terminal(f">> SCANNER: {resultado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaNexusGUI(root)
    root.mainloop()
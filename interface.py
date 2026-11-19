import tkinter as tk
from tkinter import messagebox, scrolledtext

# Importando a partir das pastas do projeto (igual ao main.py)
from SALVAMENTO import salvamento, ambientes
from HISTORIA import historia
from INVESTIGACAO import investigacao, personagens, capitulo1, capitulo2, capitulo3

class CyberQuestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberQuest: O Protocolo ORÁCULO")
        self.root.geometry("1000x700")
        self.root.configure(bg="#0b0f19")

        # 1º Cria os componentes visuais primeiro (incluindo o txt_terminal)
        self.criar_widgets()

        # 2º Depois carrega ou cria o estado do jogo e mostra a abertura
        self.estado_jogo, erro = salvamento.carregar_jogo()
        if self.estado_jogo is None:
            self.estado_jogo = salvamento.criar_estado_inicial()
            salvamento.salvar_jogo(self.estado_jogo)
            abertura = historia.abrir_capitulo(self.estado_jogo)
            if abertura:
                self.escrever_terminal(abertura)

        self.atualizar_interface()

    def criar_widgets(self):
        # --- CABEÇALHO / STATUS ---
        self.frame_topo = tk.Frame(self.root, bg="#111827", bd=2, relief="groove")
        self.frame_topo.pack(fill="x", padx=10, pady=10)

        self.lbl_status = tk.Label(
            self.frame_topo, text="", font=("Consolas", 11, "bold"), fg="#00ffcc", bg="#111827"
        )
        self.lbl_status.pack(side="left", padx=15, pady=10)

        self.btn_salvar = tk.Button(
            self.frame_topo, text="Salvar Jogo", command=self.acao_salvar,
            font=("Consolas", 10, "bold")
        )
        self.btn_salvar.pack(side="right", padx=15, pady=10)

        self.btn_inventario = tk.Button(
            self.frame_topo, text="Inventário", command=self.acao_inventario,
            font=("Consolas", 10, "bold")
        )
        self.btn_inventario.pack(side="right", padx=5, pady=10)

        # --- ÁREA CENTRAL (Terminal / História) ---
        self.frame_centro = tk.Frame(self.root, bg="#0b0f19")
        self.frame_centro.pack(fill="both", expand=True, padx=10, pady=5)

        self.txt_terminal = scrolledtext.ScrolledText(
            self.frame_centro, wrap=tk.WORD, bg="#030712", fg="#34d399",
            font=("Consolas", 11), insertbackground="white", bd=0
        )
        self.txt_terminal.pack(fill="both", expand=True, side="left")
        self.txt_terminal.config(state=tk.DISABLED)

        # --- PAINEL DE AÇÕES / NAVEGAÇÃO ---
        self.frame_acoes = tk.Frame(self.root, bg="#111827", bd=2, relief="groove")
        self.frame_acoes.pack(fill="x", padx=10, pady=10)

        self.lbl_acoes = tk.Label(
            self.frame_acoes, text="Ações Disponíveis / Navegação", font=("Consolas", 11, "bold"),
            fg="#93c5fd", bg="#111827"
        )
        self.lbl_acoes.pack(anchor="w", padx=10, pady=5)

        self.frame_botoes_acao = tk.Frame(self.frame_acoes, bg="#111827")
        self.frame_botoes_acao.pack(fill="x", padx=10, pady=5)

    def escrever_terminal(self, texto):
        self.txt_terminal.config(state=tk.NORMAL)
        self.txt_terminal.insert(tk.END, texto + "\n\n" + "="*50 + "\n\n")
        self.txt_terminal.see(tk.END)
        self.txt_terminal.config(state=tk.DISABLED)

    def atualizar_interface(self):
        cap = self.estado_jogo["capitulo_atual"]
        amb = self.estado_jogo["ambiente_atual"]
        
        if amb:
            status_texto = f"Capítulo: {cap} | Ambiente Atual: {amb}"
        else:
            status_texto = f"Capítulo: {cap} | Fora de ambientes (Seleção de Salas)"
        
        self.lbl_status.config(text=status_texto)
        self.atualizar_painel_acoes()

    def limpar_botoes(self):
        for widget in self.frame_botoes_acao.winfo_children():
            widget.destroy()

    def atualizar_painel_acoes(self):
        self.limpar_botoes()
        
        if self.estado_jogo.get("jogo_concluido"):
            lbl = tk.Label(
                self.frame_botoes_acao, text="Jogo Concluído!", font=("Consolas", 11, "bold"),
                fg="#facc15", bg="#111827"
            )
            lbl.pack(anchor="w", pady=5)
            return

        amb_atual = self.estado_jogo["ambiente_atual"]
        capitulo = self.estado_jogo["capitulo_atual"]

        # Se o jogador está dentro de um ambiente
        if amb_atual is not None:
            dados_ambiente = ambientes.AMBIENTES[amb_atual]
            
            # Botão de Sair do Ambiente
            btn_sair = tk.Button(
                self.frame_botoes_acao, text=f"Sair de {amb_atual}", command=self.acao_sair_ambiente,
                font=("Consolas", 10, "bold")
            )
            btn_sair.pack(side="top", anchor="w", pady=2)

            # Ações do Ambiente
            for codigo, descricao in dados_ambiente["acoes"].items():
                if self.acao_disponivel(codigo):
                    btn = tk.Button(
                        self.frame_botoes_acao, text=descricao, 
                        command=lambda c=codigo: self.executar_acao_ambiente(c),
                        font=("Consolas", 10), width=45, anchor="w"
                    )
                    btn.pack(side="top", anchor="w", pady=2)
        
        # Se o jogador está no menu principal de salas (fora de ambiente)
        else:
            if capitulo == 3 and "Escritório de Dante" in self.estado_jogo["ambientes_visitados"] and not self.estado_jogo.get("decisao_final"):
                btn_final = tk.Button(
                    self.frame_botoes_acao, text="Realizar Confronto Final e Decisão", command=self.acao_resolver_final,
                    font=("Consolas", 10, "bold"), width=45, anchor="w"
                )
                btn_final.pack(side="top", anchor="w", pady=2)
                return

            ambientes_disp = ambientes.listar_ambientes(self.estado_jogo)
            
            if not ambientes_disp:
                btn_avancar = tk.Button(
                    self.frame_botoes_acao, text="Encerrar Capítulo e Avançar", command=self.acao_avancar_capitulo,
                    font=("Consolas", 10, "bold"), width=45, anchor="w"
                )
                btn_avancar.pack(side="top", anchor="w", pady=2)
            else:
                lbl_escolha = tk.Label(
                    self.frame_botoes_acao, text="Escolha um ambiente para entrar:", font=("Consolas", 10),
                    fg="#93c5fd", bg="#111827"
                )
                lbl_escolha.pack(anchor="w", pady=2)

                for nome in ambientes_disp:
                    btn_amb = tk.Button(
                        self.frame_botoes_acao, text=f"Entrar em {nome}", 
                        command=lambda n=nome: self.acao_entrar_ambiente(n),
                        font=("Consolas", 10), width=45, anchor="w"
                    )
                    btn_amb.pack(side="top", anchor="w", pady=2)

    def acao_disponivel(self, codigo):
        if codigo == "entregar_documentos":
            inv = investigacao.obter_inventario(self.estado_jogo)
            return any(not d["entregue"] for d in inv)
        
        if ambientes.acao_ja_realizada(self.estado_jogo, codigo):
            return False
            
        if codigo.startswith("conversar_"):
            pid = codigo.replace("conversar_", "", 1)
            return self.personagem_disponivel(pid)
            
        return True

    def personagem_disponivel(self, pid):
        decisoes = self.estado_jogo.get("decisoes", {})
        if pid == "helena":
            return not all(k in decisoes for k in ["helena_progresso_capitulo_2", "helena_responsabilidade_capitulo_2"])
        if pid == "dante":
            return not all(k in decisoes for k in ["dante_alianca_capitulo_3", "dante_intencoes_capitulo_3"])
        return not personagens.verificar_personagem_abordado(self.estado_jogo, pid)

    def acao_salvar(self):
        if salvamento.salvar_jogo(self.estado_jogo):
            messagebox.showinfo("Sucesso", "Progresso salvo com sucesso!")
        else:
            messagebox.showerror("Erro", "Não foi possível salvar o jogo.")

    def acao_inventario(self):
        inv = investigacao.obter_inventario(self.estado_jogo)
        top = tk.Toplevel(self.root)
        top.title("Inventário de Documentos")
        top.geometry("450x350")
        top.configure(bg="#0b0f19")

        lbl = tk.Label(top, text="DOCUMENTOS ENCONTRADOS", font=("Consolas", 11, "bold"), fg="#00ffcc", bg="#0b0f19")
        lbl.pack(pady=10)

        txt = scrolledtext.ScrolledText(top, wrap=tk.WORD, bg="#030712", fg="#ffffff", font=("Consolas", 10))
        txt.pack(fill="both", expand=True, padx=10, pady=10)

        if not inv:
            txt.insert(tk.END, "Nenhum documento encontrado até o momento.")
        else:
            for d in inv:
                status = f"Entregue para {d['entregue_para']}" if d['entregue'] else "Em posse de Alex"
                txt.insert(tk.END, f"[{d['codigo']}] {d['nome']}\nAutor: {d['autor']} | Classificação: {d['classificacao']}\nStatus: {status}\n\n")
        txt.config(state=tk.DISABLED)

    def acao_entrar_ambiente(self, nome):
        motivo = ambientes.motivo_bloqueio_entrada(self.estado_jogo, nome)
        if motivo:
            messagebox.showwarning("Aviso", motivo)
            return
        if ambientes.entrar_ambiente(self.estado_jogo, nome):
            salvamento.salvar_jogo(self.estado_jogo)
            self.escrever_terminal(f"Alex entrou em {nome}.")
            self.atualizar_interface()

    def acao_sair_ambiente(self):
        if ambientes.sair_ambiente(self.estado_jogo):
            salvamento.salvar_jogo(self.estado_jogo)
            self.escrever_terminal("Alex saiu do ambiente atual.")
            self.atualizar_interface()

    def executar_acao_ambiente(self, acao):
        amb = self.estado_jogo["ambiente_atual"]
        
        if acao.startswith("encontrar_doc"):
            sucesso = False
            if acao == "encontrar_doc01":
                sucesso = investigacao.encontrar_documento(self.estado_jogo, "DOC01")
                doc_text = historia.apresentar_doc01()
            elif acao == "encontrar_doc02":
                sucesso = investigacao.encontrar_documento(self.estado_jogo, "DOC02")
                doc_text = historia.apresentar_doc02()
            elif acao == "encontrar_doc03":
                sucesso = investigacao.encontrar_documento(self.estado_jogo, "DOC03")
                doc_text = historia.apresentar_doc03()
            elif acao == "encontrar_doc04":
                sucesso = investigacao.encontrar_documento(self.estado_jogo, "DOC04")
                doc_text = historia.apresentar_doc04()
            
            if sucesso:
                self.escrever_terminal(doc_text)
                ambientes.registrar_acao_ambiente(self.estado_jogo, acao)
                salvamento.salvar_jogo(self.estado_jogo)
            else:
                messagebox.showinfo("Aviso", "Documento já encontrado ou indisponível.")

        elif acao.startswith("conversar_"):
            pid = acao.replace("conversar_", "", 1)
            if pid == "karla":
                self.dialogo_karla()
            elif pid == "oraculo":
                self.dialogo_oraculo()
            elif pid == "helena":
                self.dialogo_helena()
            elif pid == "dante":
                self.dialogo_dante()

        elif acao == "entregar_documentos":
            self.janela_entrega_documentos()

        else:
            narrativa = historia.obter_narrativa_acao(amb, acao)
            if narrativa:
                self.escrever_terminal(narrativa)
            else:
                self.escrever_terminal("Ação realizada com sucesso.")
            ambientes.registrar_acao_ambiente(self.estado_jogo, acao)
            salvamento.salvar_jogo(self.estado_jogo)

        self.atualizar_interface()

    def dialogo_karla(self):
        conv = historia.apresentar_conversa_karla()
        top = tk.Toplevel(self.root)
        top.title("Conversa com Dra. Karla")
        top.geometry("500x450")
        top.configure(bg="#0b0f19")

        txt = scrolledtext.ScrolledText(top, wrap=tk.WORD, bg="#030712", fg="#34d399", font=("Consolas", 10))
        txt.pack(fill="both", expand=True, padx=10, pady=10)
        txt.insert(tk.END, conv["texto"])
        txt.config(state=tk.DISABLED)

        frame_resp = tk.Frame(top, bg="#0b0f19")
        frame_resp.pack(fill="x", padx=10, pady=10)

        def escolher(op):
            res = capitulo1.registrar_decisao_karla(self.estado_jogo, op)
            if res.get("sucesso"):
                personagens.abordar_personagem(self.estado_jogo, "karla", 1)
                self.escrever_terminal(res["texto"])
                salvamento.salvar_jogo(self.estado_jogo)
                top.destroy()
                self.atualizar_interface()
            else:
                messagebox.showerror("Erro", res.get("mensagem", "Erro."))

        for op, desc in conv["opcoes"].items():
            btn = tk.Button(frame_resp, text=f"{op} - {desc}", command=lambda o=op: escolher(o), font=("Consolas", 9), anchor="w")
            btn.pack(fill="x", pady=2)

    def dialogo_oraculo(self):
        texto = historia.apresentar_conversa_oraculo()
        self.escrever_terminal(texto)
        personagens.abordar_personagem(self.estado_jogo, "oraculo", 1)
        salvamento.salvar_jogo(self.estado_jogo)

    def dialogo_helena(self):
        conv = historia.apresentar_conversa_helena(self.estado_jogo)
        top = tk.Toplevel(self.root)
        top.title("Conversa com Helena Voss")
        top.geometry("600x550")
        top.configure(bg="#0b0f19")

        txt = scrolledtext.ScrolledText(top, wrap=tk.WORD, bg="#030712", fg="#34d399", font=("Consolas", 10))
        txt.pack(fill="both", expand=True, padx=10, pady=10)
        txt.insert(tk.END, conv["texto"])
        txt.config(state=tk.DISABLED)

        frame_etapas = tk.Frame(top, bg="#0b0f19")
        frame_etapas.pack(fill="x", padx=10, pady=10)

        for etapa in conv["etapas"]:
            chave = f"helena_{etapa}_capitulo_2"
            if chave in self.estado_jogo["decisoes"]:
                continue
            
            tk.Label(frame_etapas, text=f"Etapa: {etapa.upper()}", fg="#00ffcc", bg="#0b0f19", font=("Consolas", 10, "bold")).pack(anchor="w")
            for op, desc in conv["opcoes"][etapa].items():
                def fazer_escolha(e=etapa, o=op):
                    res = capitulo2.registrar_decisao_helena(self.estado_jogo, e, o)
                    if res.get("sucesso"):
                        personagens.abordar_personagem(self.estado_jogo, "helena", 2)
                        self.escrever_terminal(res["texto"])
                        salvamento.salvar_jogo(self.estado_jogo)
                        top.destroy()
                        self.atualizar_interface()
                    else:
                        messagebox.showerror("Erro", res.get("mensagem", "Erro."))
                tk.Button(frame_etapas, text=f"{op} - {desc}", command=fazer_escolha, font=("Consolas", 9), anchor="w").pack(fill="x", pady=2)
            break

    def dialogo_dante(self):
        conv = historia.apresentar_conversa_dante()
        top = tk.Toplevel(self.root)
        top.title("Conversa com Dante Moreau")
        top.geometry("600x550")
        top.configure(bg="#0b0f19")

        txt = scrolledtext.ScrolledText(top, wrap=tk.WORD, bg="#030712", fg="#34d399", font=("Consolas", 10))
        txt.pack(fill="both", expand=True, padx=10, pady=10)
        txt.insert(tk.END, conv["texto"])
        txt.config(state=tk.DISABLED)

        frame_etapas = tk.Frame(top, bg="#0b0f19")
        frame_etapas.pack(fill="x", padx=10, pady=10)

        for etapa in conv["etapas"]:
            chave = f"dante_{etapa}_capitulo_3"
            if chave in self.estado_jogo["decisoes"]:
                continue
            
            tk.Label(frame_etapas, text=f"Etapa: {etapa.upper()}", fg="#00ffcc", bg="#0b0f19", font=("Consolas", 10, "bold")).pack(anchor="w")
            for op, desc in conv["opcoes"][etapa].items():
                def fazer_escolha(e=etapa, o=op):
                    res = capitulo3.registrar_decisao_dante(self.estado_jogo, e, o)
                    if res.get("sucesso"):
                        personagens.abordar_personagem(self.estado_jogo, "dante", 3)
                        self.escrever_terminal(res["texto"])
                        salvamento.salvar_jogo(self.estado_jogo)
                        top.destroy()
                        self.atualizar_interface()
                    else:
                        messagebox.showerror("Erro", res.get("mensagem", "Erro."))
                tk.Button(frame_etapas, text=f"{op} - {desc}", command=fazer_escolha, font=("Consolas", 9), anchor="w").pack(fill="x", pady=2)
            break

    def janela_entrega_documentos(self):
        inv = investigacao.obter_inventario(self.estado_jogo)
        disponiveis = [d for d in inv if not d["entregue"]]
        if not disponiveis:
            messagebox.showinfo("Inventário", "Não há documentos disponíveis para entrega.")
            return

        amb = self.estado_jogo["ambiente_atual"]
        destinatarios = investigacao.listar_destinatarios(amb)
        if not destinatarios:
            messagebox.showinfo("Aviso", "Não há destinatários disponíveis neste ambiente.")
            return

        top = tk.Toplevel(self.root)
        top.title("Entregar Documento")
        top.geometry("400x300")
        top.configure(bg="#0b0f19")

        tk.Label(top, text="Selecione o Documento:", fg="#00ffcc", bg="#0b0f19", font=("Consolas", 10, "bold")).pack(pady=5)
        
        doc_var = tk.StringVar(top)
        doc_var.set(disponiveis[0]["codigo"])
        for d in disponiveis:
            tk.Radiobutton(top, text=f"{d['codigo']} - {d['nome']}", variable=doc_var, value=d['codigo'], bg="#0b0f19", fg="#ffffff", selectcolor="#1f2937", font=("Consolas", 9)).pack(anchor="w", padx=20)

        tk.Label(top, text="Selecione o Destinatário:", fg="#00ffcc", bg="#0b0f19", font=("Consolas", 10, "bold")).pack(pady=5)
        
        dest_var = tk.StringVar(top)
        dest_var.set(destinatarios[0]["id"])
        for dest in destinatarios:
            tk.Radiobutton(top, text=dest["nome"], variable=dest_var, value=dest["id"], bg="#0b0f19", fg="#ffffff", selectcolor="#1f2937", font=("Consolas", 9)).pack(anchor="w", padx=20)

        def confirmar_entrega():
            codigo = doc_var.get()
            dest = dest_var.get()
            sucesso = investigacao.entregar_documento(self.estado_jogo, codigo, dest)
            if sucesso:
                messagebox.showinfo("Sucesso", f"Documento {codigo} entregue com sucesso!")
                salvamento.salvar_jogo(self.estado_jogo)
                top.destroy()
                ambientes.registrar_acao_ambiente(self.estado_jogo, "entregar_documentos")
                self.atualizar_interface()
            else:
                messagebox.showerror("Erro", "Não foi possível entregar o documento.")

        tk.Button(top, text="Confirmar Entrega", command=confirmar_entrega, font=("Consolas", 10)).pack(pady=10)

    def acao_avancar_capitulo(self):
        res = historia.encerrar_capitulo(self.estado_jogo)
        if not res.get("sucesso"):
            messagebox.showwarning("Aviso", res["texto"])
            return
        
        self.escrever_terminal(res["texto"])
        if historia.avancar_capitulo(self.estado_jogo):
            salvamento.salvar_jogo(self.estado_jogo)
            abertura = historia.abrir_capitulo(self.estado_jogo)
            if abertura:
                self.escrever_terminal(abertura)
            self.atualizar_interface()

    def acao_resolver_final(self):
        if not self.estado_jogo["decisoes"].get("dante_confrontado"):
            res = historia.registrar_confronto_dante(self.estado_jogo)
            if res.get("sucesso"):
                self.escrever_terminal(res["texto"])
                salvamento.salvar_jogo(self.estado_jogo)
            else:
                messagebox.showwarning("Aviso", res.get("mensagem", "Erro no confronto."))
                return

        if self.estado_jogo["decisao_final"] is None:
            texto_persuasao = historia.apresentar_persuasao_oraculo(self.estado_jogo)
            
            top = tk.Toplevel(self.root)
            top.title("Destino de ORÁCULO")
            top.geometry("550x500")
            top.configure(bg="#0b0f19")

            txt = scrolledtext.ScrolledText(top, wrap=tk.WORD, bg="#030712", fg="#34d399", font=("Consolas", 10))
            txt.pack(fill="both", expand=True, padx=10, pady=10)
            txt.insert(tk.END, texto_persuasao)
            txt.config(state=tk.DISABLED)

            frame_decisao = tk.Frame(top, bg="#0b0f19")
            frame_decisao.pack(fill="x", padx=10, pady=10)

            def escolher_final(op):
                res = historia.registrar_decisao_final(self.estado_jogo, op)
                if res.get("sucesso"):
                    salvamento.salvar_jogo(self.estado_jogo)
                    top.destroy()
                    texto_final = historia.apresentar_final(self.estado_jogo)
                    self.escrever_terminal(texto_final)
                    self.atualizar_interface()
                else:
                    messagebox.showerror("Erro", res.get("mensagem", "Erro."))

            tk.Button(frame_decisao, text="1 - Desligar ORÁCULO", command=lambda: escolher_final("1"), font=("Consolas", 10), width=30).pack(pady=5)
            tk.Button(frame_decisao, text="2 - Permitir que ORÁCULO continue existindo", command=lambda: escolher_final("2"), font=("Consolas", 10), width=30).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberQuestApp(root)
    root.mainloop()
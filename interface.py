import os
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Importando a partir das pastas do projeto (igual ao main.py)
from SALVAMENTO import salvamento, ambientes
from HISTORIA import historia
from INVESTIGACAO import investigacao, personagens, capitulo1, capitulo2, capitulo3

try:
    import pygame
    PYGAME_DISPONIVEL = True
except ImportError:
    PYGAME_DISPONIVEL = False


class CyberQuestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberQuest: O Protocolo ORÁCULO")
        self.root.geometry("1080x760")
        self.root.configure(bg="#0b0f19")

        self.musica_tocando = False
        self.volume_atual = 0.35
        self._atualizando_slider = False
        self._processo_audio_mac = None
        self.caminho_musica = self._localizar_musica()

        # 1º Cria os componentes visuais primeiro (incluindo o txt_terminal)
        self.criar_widgets()

        # 2º Configura atalhos de teclado úteis para áudio
        self.configurar_atalhos()

        # 3º Inicia música tema em segundo plano (se disponível)
        self.iniciar_musica_tema()
        self._atualizar_rotulos_audio()

        # 4º Carrega ou cria o estado do jogo e mostra a abertura
        self.estado_jogo, erro = salvamento.carregar_jogo()
        if self.estado_jogo is None:
            self.iniciar_nova_partida(confirmar=False)
        else:
            self.atualizar_interface()

        self.root.protocol("WM_DELETE_WINDOW", self.ao_fechar)

    def configurar_atalhos(self):
        self.root.bind("<m>", lambda _event: self.alternar_musica())
        self.root.bind("<M>", lambda _event: self.alternar_musica())
        self.root.bind("<Left>", lambda _event: self.ajustar_volume(-0.05))
        self.root.bind("<Right>", lambda _event: self.ajustar_volume(0.05))

    def _localizar_musica(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        candidatos = [
            os.path.join(base_dir, "musica_tema.mp3"),
            os.path.join(base_dir, "musica_tema.wav"),
            os.path.join(base_dir, "audio", "musica_tema.mp3"),
            os.path.join(base_dir, "audio", "musica_tema.wav"),
        ]
        for caminho in candidatos:
            if os.path.exists(caminho):
                return caminho
        return candidatos[0]

    def _aplicar_volume(self):
        self.volume_atual = round(max(0.0, min(1.0, self.volume_atual)), 4)
        if PYGAME_DISPONIVEL and pygame.mixer.get_init():
            try:
                pygame.mixer.music.set_volume(self.volume_atual)
            except Exception:
                pass
        self._atualizar_rotulos_audio()

    def _atualizar_rotulos_audio(self):
        pct = int(round(self.volume_atual * 100))
        if hasattr(self, "btn_musica"):
            self.btn_musica.config(text="Música: ON" if self.musica_tocando else "Música: OFF")
        if hasattr(self, "lbl_volume"):
            self.lbl_volume.config(text=f"Vol: {pct}%")
        if hasattr(self, "scale_volume"):
            self._atualizando_slider = True
            try:
                self.scale_volume.set(pct)
            finally:
                self._atualizando_slider = False

    def ajustar_volume(self, delta):
        if not os.path.exists(self.caminho_musica):
            return
        if not (PYGAME_DISPONIVEL and pygame.mixer.get_init()):
            return
        self.volume_atual += delta
        self._aplicar_volume()

    def ao_mover_volume(self, valor):
        if self._atualizando_slider:
            return

        pct = int(round(float(valor) / 5.0) * 5)
        pct = max(0, min(100, pct))
        self.volume_atual = pct / 100.0
        self._aplicar_volume()

    def iniciar_musica_tema(self):
        if not os.path.exists(self.caminho_musica):
            return

        try:
            if PYGAME_DISPONIVEL:
                if not pygame.mixer.get_init():
                    pygame.mixer.init()
                pygame.mixer.music.load(self.caminho_musica)
                pygame.mixer.music.set_volume(self.volume_atual)
                pygame.mixer.music.play(loops=-1)
                self.musica_tocando = True
            elif platform.system() == "Darwin":
                self._processo_audio_mac = subprocess.Popen(
                    ["afplay", self.caminho_musica],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                self.musica_tocando = True
        except Exception:
            self.musica_tocando = False

    def alternar_musica(self):
        if not os.path.exists(self.caminho_musica):
            messagebox.showinfo(
                "Música Tema",
                "Coloque um arquivo 'musica_tema.mp3' ou 'musica_tema.wav' na pasta do projeto para ativar a trilha.",
            )
            return

        try:
            if PYGAME_DISPONIVEL and pygame.mixer.get_init():
                if self.musica_tocando:
                    pygame.mixer.music.pause()
                    self.musica_tocando = False
                else:
                    pygame.mixer.music.unpause()
                    self.musica_tocando = True
                self._atualizar_rotulos_audio()
            elif platform.system() == "Darwin":
                if self.musica_tocando and self._processo_audio_mac:
                    self._processo_audio_mac.terminate()
                    self._processo_audio_mac = None
                    self.musica_tocando = False
                else:
                    self.iniciar_musica_tema()
                self._atualizar_rotulos_audio()
        except Exception:
            pass

    def ao_fechar(self):
        try:
            if PYGAME_DISPONIVEL and pygame.mixer.get_init():
                pygame.mixer.music.stop()
                pygame.mixer.quit()
        except Exception:
            pass
        if self._processo_audio_mac and self._processo_audio_mac.poll() is None:
            try:
                self._processo_audio_mac.terminate()
            except Exception:
                pass
        self.root.destroy()

    def criar_widgets(self):
        # --- CABEÇALHO / STATUS ---
        self.frame_topo = tk.Frame(self.root, bg="#111827", bd=2, relief="groove")
        self.frame_topo.pack(fill="x", padx=10, pady=10)

        self.lbl_status = tk.Label(
            self.frame_topo, text="", font=("Consolas", 11, "bold"), fg="#00ffcc", bg="#111827"
        )
        self.lbl_status.pack(side="left", padx=15, pady=10)

        self.btn_salvar = tk.Button(
            self.frame_topo, text="Salvar", command=self.acao_salvar,
            font=("Consolas", 10, "bold")
        )
        self.btn_salvar.pack(side="right", padx=8, pady=10)

        self.btn_nova_partida = tk.Button(
            self.frame_topo, text="Nova Partida", command=lambda: self.iniciar_nova_partida(confirmar=True),
            font=("Consolas", 10, "bold")
        )
        self.btn_nova_partida.pack(side="right", padx=4, pady=10)

        self.btn_status = tk.Button(
            self.frame_topo, text="Status", command=self.acao_status,
            font=("Consolas", 10, "bold")
        )
        self.btn_status.pack(side="right", padx=4, pady=10)

        self.btn_inventario = tk.Button(
            self.frame_topo, text="Inventário", command=self.acao_inventario,
            font=("Consolas", 10, "bold")
        )
        self.btn_inventario.pack(side="right", padx=4, pady=10)

        self.scale_volume = tk.Scale(
            self.frame_topo,
            from_=0,
            to=100,
            resolution=5,
            orient=tk.HORIZONTAL,
            showvalue=False,
            command=self.ao_mover_volume,
            bg="#111827",
            fg="#00ffcc",
            highlightthickness=0,
            troughcolor="#030712",
            length=105,
        )
        self.scale_volume.set(int(round(self.volume_atual * 100)))
        self.scale_volume.pack(side="right", padx=4, pady=10)

        self.lbl_volume = tk.Label(
            self.frame_topo, text="Vol: 35%", font=("Consolas", 10, "bold"),
            fg="#93c5fd", bg="#111827", width=8
        )
        self.lbl_volume.pack(side="right", padx=2, pady=10)

        self.btn_musica = tk.Button(
            self.frame_topo,
            text="Música: OFF",
            command=self.alternar_musica,
            font=("Consolas", 10, "bold"),
        )
        self.btn_musica.pack(side="right", padx=4, pady=10)

        # --- PAINEL DE AÇÕES / NAVEGAÇÃO (empacotado antes do centro para nunca sumir) ---
        self.frame_acoes = tk.Frame(self.root, bg="#111827", bd=2, relief="groove")
        self.frame_acoes.pack(side="bottom", fill="x", padx=10, pady=10)

        self.lbl_acoes = tk.Label(
            self.frame_acoes, text="Ações Disponíveis / Navegação", font=("Consolas", 11, "bold"),
            fg="#93c5fd", bg="#111827"
        )
        self.lbl_acoes.pack(anchor="w", padx=10, pady=5)

        self.btn_limpar_tela = tk.Button(
            self.frame_acoes, text="Limpar Tela", command=self.limpar_terminal,
            font=("Consolas", 9, "bold")
        )
        self.btn_limpar_tela.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=6)

        self.frame_botoes_acao = tk.Frame(self.frame_acoes, bg="#111827")
        self.frame_botoes_acao.pack(fill="x", padx=10, pady=5)

        # --- ÁREA CENTRAL (Terminal / História) ---
        self.frame_centro = tk.Frame(self.root, bg="#0b0f19")
        self.frame_centro.pack(fill="both", expand=True, padx=10, pady=5)

        self.txt_terminal = scrolledtext.ScrolledText(
            self.frame_centro, wrap=tk.WORD, bg="#030712", fg="#34d399",
            font=("Consolas", 13), insertbackground="white", bd=0, padx=10, pady=10
        )
        self.txt_terminal.pack(fill="both", expand=True, side="left")
        self.txt_terminal.config(state=tk.DISABLED)

    def escrever_terminal(self, texto):
        self.txt_terminal.config(state=tk.NORMAL)
        self.txt_terminal.insert(tk.END, texto + "\n\n" + "=" * 50 + "\n\n")
        self.txt_terminal.see(tk.END)
        self.txt_terminal.config(state=tk.DISABLED)

    def limpar_terminal(self):
        self.txt_terminal.config(state=tk.NORMAL)
        self.txt_terminal.delete("1.0", tk.END)
        self.txt_terminal.config(state=tk.DISABLED)

    def _remover_save_existente(self):
        if hasattr(salvamento, "excluir_progresso"):
            try:
                salvamento.excluir_progresso()
            except Exception:
                pass

        base_dir = os.path.dirname(os.path.abspath(__file__))
        caminhos_save = [
            os.path.join(base_dir, "SALVAMENTO", "dados", "progresso.json"),
            os.path.join(base_dir, "SALVAMENTO", "dados", "progresso.json.tmp"),
            os.path.join(base_dir, "dados", "progresso.json"),
            os.path.join(base_dir, "dados", "progresso.json.tmp"),
        ]
        for caminho in caminhos_save:
            if os.path.exists(caminho):
                try:
                    os.remove(caminho)
                except Exception:
                    pass

    def iniciar_nova_partida(self, confirmar=True):
        if confirmar:
            aceito = messagebox.askyesno(
                "Nova Partida",
                "Deseja apagar o salvamento atual e começar uma nova partida do zero?",
            )
            if not aceito:
                return

        self._remover_save_existente()
        self.estado_jogo = salvamento.criar_estado_inicial()
        salvamento.salvar_jogo(self.estado_jogo)
        self.limpar_terminal()
        abertura = historia.abrir_capitulo(self.estado_jogo)
        if abertura:
            self.escrever_terminal(abertura)
        self.atualizar_interface()

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

        if amb_atual is not None:
            dados_ambiente = ambientes.AMBIENTES[amb_atual]

            btn_sair = tk.Button(
                self.frame_botoes_acao, text=f"Sair de {amb_atual}", command=self.acao_sair_ambiente,
                font=("Consolas", 10, "bold")
            )
            btn_sair.pack(side="top", anchor="w", pady=2)

            for codigo, descricao in dados_ambiente["acoes"].items():
                if self.acao_disponivel(codigo):
                    btn = tk.Button(
                        self.frame_botoes_acao, text=descricao,
                        command=lambda c=codigo: self.executar_acao_ambiente(c),
                        font=("Consolas", 10), width=45, anchor="w"
                    )
                    btn.pack(side="top", anchor="w", pady=2)
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

    def acao_status(self):
        top = tk.Toplevel(self.root)
        top.title("Status da Investigação")
        top.geometry("500x400")
        top.configure(bg="#0b0f19")
        top.transient(self.root)

        lbl = tk.Label(top, text="RESUMO DO ESTADO ATUAL", font=("Consolas", 11, "bold"), fg="#00ffcc", bg="#0b0f19")
        lbl.pack(pady=10)

        txt = scrolledtext.ScrolledText(top, wrap=tk.WORD, bg="#030712", fg="#ffffff", font=("Consolas", 11))
        txt.pack(fill="both", expand=True, padx=10, pady=10)

        cap = self.estado_jogo.get("capitulo_atual", 1)
        amb = self.estado_jogo.get("ambiente_atual") or "Seleção de Salas"
        inv = investigacao.obter_inventario(self.estado_jogo)
        entregues = sum(1 for d in inv if d.get("entregue"))
        confianca = self.estado_jogo.get("confianca", {})

        linhas = [
            f"Capítulo atual: {cap}",
            f"Localização: {amb}",
            f"Documentos encontrados: {len(inv)} (Entregues: {entregues})",
            "",
            "--- CONFIANÇA COM PERSONAGENS ---",
        ]
        if confianca:
            for personagem, valor in confianca.items():
                linhas.append(f"• {personagem.capitalize()}: {valor}")
        else:
            linhas.append("• Nenhuma interação de confiança registrada ainda.")

        txt.insert(tk.END, "\n".join(linhas))
        txt.config(state=tk.DISABLED)

    def acao_inventario(self):
        inv = investigacao.obter_inventario(self.estado_jogo)
        top = tk.Toplevel(self.root)
        top.title("Inventário de Documentos")
        top.geometry("500x400")
        top.configure(bg="#0b0f19")

        lbl = tk.Label(top, text="DOCUMENTOS ENCONTRADOS", font=("Consolas", 11, "bold"), fg="#00ffcc", bg="#0b0f19")
        lbl.pack(pady=10)

        txt = scrolledtext.ScrolledText(top, wrap=tk.WORD, bg="#030712", fg="#ffffff", font=("Consolas", 11))
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
            doc_text = ""
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

    def _criar_janela_dialogo(self, titulo, texto_conversa):
        top = tk.Toplevel(self.root)
        top.title(titulo)
        top.geometry("720x620")
        top.configure(bg="#0b0f19")
        top.transient(self.root)
        top.grab_set()

        frame_resp = tk.Frame(top, bg="#111827", bd=1, relief="groove")
        frame_resp.pack(side="bottom", fill="x", padx=10, pady=10)

        txt = scrolledtext.ScrolledText(
            top, wrap=tk.WORD, bg="#030712", fg="#34d399",
            font=("Consolas", 12), padx=10, pady=10
        )
        txt.pack(side="top", fill="both", expand=True, padx=10, pady=(10, 0))
        txt.insert("1.0", texto_conversa)
        txt.config(state=tk.DISABLED)

        return top, frame_resp

    def dialogo_karla(self):
        conv = historia.apresentar_conversa_karla()
        top, frame_resp = self._criar_janela_dialogo("Conversa com Dra. Karla", conv["texto"])

        tk.Label(
            frame_resp, text="Escolha sua resposta:", fg="#00ffcc",
            bg="#111827", font=("Consolas", 10, "bold")
        ).pack(anchor="w", padx=8, pady=(6, 2))

        def escolher(op):
            res = historia.registrar_decisao_karla(self.estado_jogo, op)
            if res.get("sucesso"):
                personagens.abordar_personagem(self.estado_jogo, "karla", 1)
                personagens.registrar_escolha_confianca(self.estado_jogo, "karla", res["classificacao"], 1)
                ambientes.registrar_acao_ambiente(self.estado_jogo, "conversar_karla")
                self.escrever_terminal(conv["texto"] + "\n\n---\n\n" + res["texto"])
                salvamento.salvar_jogo(self.estado_jogo)
                top.destroy()
                self.atualizar_interface()
            else:
                messagebox.showerror("Erro", res.get("mensagem", "Erro."))

        for op, desc in conv["opcoes"].items():
            btn = tk.Button(
                frame_resp, text=f"{op} - {desc}",
                command=lambda o=op: escolher(o),
                font=("Consolas", 10), anchor="w", justify="left", wraplength=660
            )
            btn.pack(fill="x", padx=8, pady=3)

        top.update_idletasks()
        top.lift()

    def dialogo_oraculo(self):
        texto = historia.apresentar_conversa_oraculo()
        self.escrever_terminal(texto)
        personagens.abordar_personagem(self.estado_jogo, "oraculo", self.estado_jogo["capitulo_atual"])
        ambientes.registrar_acao_ambiente(self.estado_jogo, "conversar_oraculo")
        salvamento.salvar_jogo(self.estado_jogo)
        self.atualizar_interface()

    def dialogo_helena(self):
        conv = historia.apresentar_conversa_helena(self.estado_jogo)
        top, frame_etapas = self._criar_janela_dialogo("Conversa com Helena Voss", conv["texto"])

        for etapa in conv["etapas"]:
            chave = f"helena_{etapa}_capitulo_2"
            if chave in self.estado_jogo["decisoes"]:
                continue

            tk.Label(
                frame_etapas, text=f"Etapa: {etapa.upper()}", fg="#00ffcc",
                bg="#111827", font=("Consolas", 10, "bold")
            ).pack(anchor="w", padx=8, pady=(6, 2))

            for op, desc in conv["opcoes"][etapa].items():
                def fazer_escolha(e=etapa, o=op):
                    res = historia.registrar_decisao_helena(self.estado_jogo, e, o)
                    if res.get("sucesso"):
                        if not personagens.verificar_personagem_abordado(self.estado_jogo, "helena", 2):
                            personagens.abordar_personagem(self.estado_jogo, "helena", 2)
                        personagens.registrar_escolha_confianca(self.estado_jogo, "helena", res["classificacao"], 2)
                        self.escrever_terminal(res["texto"])
                        salvamento.salvar_jogo(self.estado_jogo)
                        top.destroy()
                        if self.personagem_disponivel("helena"):
                            self.dialogo_helena()
                        else:
                            ambientes.registrar_acao_ambiente(self.estado_jogo, "conversar_helena")
                            salvamento.salvar_jogo(self.estado_jogo)
                            self.atualizar_interface()
                    else:
                        messagebox.showerror("Erro", res.get("mensagem", "Erro."))

                tk.Button(
                    frame_etapas, text=f"{op} - {desc}", command=fazer_escolha,
                    font=("Consolas", 10), anchor="w", justify="left", wraplength=660
                ).pack(fill="x", padx=8, pady=3)
            break

        top.update_idletasks()
        top.lift()

    def dialogo_dante(self):
        conv = historia.apresentar_conversa_dante()
        top, frame_etapas = self._criar_janela_dialogo("Conversa com Dante Moreau", conv["texto"])

        for etapa in conv["etapas"]:
            chave = f"dante_{etapa}_capitulo_3"
            if chave in self.estado_jogo["decisoes"]:
                continue

            tk.Label(
                frame_etapas, text=f"Etapa: {etapa.upper()}", fg="#00ffcc",
                bg="#111827", font=("Consolas", 10, "bold")
            ).pack(anchor="w", padx=8, pady=(6, 2))

            for op, desc in conv["opcoes"][etapa].items():
                def fazer_escolha(e=etapa, o=op):
                    res = historia.registrar_decisao_dante(self.estado_jogo, e, o)
                    if res.get("sucesso"):
                        if not personagens.verificar_personagem_abordado(self.estado_jogo, "dante", 3):
                            personagens.abordar_personagem(self.estado_jogo, "dante", 3)
                        personagens.registrar_escolha_confianca(self.estado_jogo, "dante", res["classificacao"], 3)
                        self.escrever_terminal(res["texto"])
                        salvamento.salvar_jogo(self.estado_jogo)
                        top.destroy()
                        if self.personagem_disponivel("dante"):
                            self.dialogo_dante()
                        else:
                            ambientes.registrar_acao_ambiente(self.estado_jogo, "conversar_dante")
                            salvamento.salvar_jogo(self.estado_jogo)
                            self.atualizar_interface()
                    else:
                        messagebox.showerror("Erro", res.get("mensagem", "Erro."))

                tk.Button(
                    frame_etapas, text=f"{op} - {desc}", command=fazer_escolha,
                    font=("Consolas", 10), anchor="w", justify="left", wraplength=660
                ).pack(fill="x", padx=8, pady=3)
            break

        top.update_idletasks()
        top.lift()

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
        top.geometry("450x340")
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
            top, frame_decisao = self._criar_janela_dialogo("Destino de ORÁCULO", texto_persuasao)

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

            tk.Button(frame_decisao, text="1 - Desligar ORÁCULO", command=lambda: escolher_final("1"), font=("Consolas", 10)).pack(fill="x", padx=8, pady=4)
            tk.Button(frame_decisao, text="2 - Permitir que ORÁCULO continue existindo", command=lambda: escolher_final("2"), font=("Consolas", 10)).pack(fill="x", padx=8, pady=4)

            top.update_idletasks()
            top.lift()


if __name__ == "__main__":
    root = tk.Tk()
    app = CyberQuestApp(root)
    root.mainloop()
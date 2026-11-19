# 🧠 CyberQuest: O Protocolo ORÁCULO

> *"Toda escolha deixa rastros. Toda verdade tem um preço."*

**CyberQuest: O Protocolo ORÁCULO** é um jogo de **investigação e narrativa interativa**, desenvolvido em **Python**, no qual as escolhas do jogador influenciam o relacionamento entre personagens, o acesso a evidências e as consequências da história. Ambientada em uma Curitiba futurista, a experiência acompanha **Alex**, um ex-integrante da NEXUS que retorna à organização para investigar o comportamento inesperado da inteligência artificial **ORÁCULO**.

O projeto oferece uma **interface gráfica em Tkinter** e uma **versão jogável pelo terminal**, compartilhando o sistema de investigação, decisões e persistência em JSON.

---

## 🗂️ Sumário

- [🎯 Visão Geral](#-visão-geral)
- [🛠️ Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📖 História e Personagens](#-história-e-personagens)
- [🎮 Capítulos e Ambientes](#-capítulos-e-ambientes)
- [🔎 Sistema de Investigação](#-sistema-de-investigação)
- [🤝 Sistema de Confiança Dinâmica](#-sistema-de-confiança-dinâmica)
- [💬 Escolhas e Consequências](#-escolhas-e-consequências)
- [🖥️ Interface Gráfica](#-interface-gráfica)
- [💾 Salvamento e Continuidade](#-salvamento-e-continuidade)
- [🏁 Dois Finais Narrativos e Cena Especial](#-dois-finais-narrativos-e-cena-especial)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [▶️ Como Instalar e Executar](#-como-instalar-e-executar)
- [🎮 Como Jogar](#-como-jogar)
- [👥 Equipe e Contribuições](#-equipe-e-contribuições)

---

## 🎯 Visão Geral

Na NEXUS, a inteligência artificial ORÁCULO foi criada para apoiar decisões de grande impacto. Mas acessos incomuns, ações não autorizadas e decisões mantidas em segredo colocam em dúvida os limites do sistema — e os interesses de quem pretende controlá-lo.

Ao longo da campanha, o jogador pode:

- Explorar **quatro ambientes** distribuídos em **três capítulos**;
- Investigar pistas e localizar até **quatro documentos confidenciais**;
- Conversar com personagens que possuem perspectivas diferentes sobre a IA;
- Tomar decisões que alteram a **confiança** e as reações narrativas;
- Consultar o inventário e entregar evidências a personagens disponíveis;
- Salvar e retomar a investigação;
- Decidir o futuro de ORÁCULO em **dois finais principais**.

A proposta é combinar **estrutura de dados, funções, condicionais, repetição e persistência** com uma narrativa em que as escolhas tenham consequências.

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-Interface%20Gr%C3%A1fica-0F766E?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Salvamento-52525B?style=for-the-badge&logo=json&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

| Tecnologia | Utilização |
|---|---|
| **Python** | Regras, diálogos, processamento das escolhas e integração dos módulos |
| **Tkinter** | Janelas, botões, campos de texto e mensagens da interface gráfica |
| **JSON** | Armazenamento e recuperação do progresso da partida |
| **Git / GitHub** | Versionamento e colaboração entre os integrantes |

**Bibliotecas utilizadas no código:** `tkinter`, `json`, `os` e `unicodedata` — todas pertencem à biblioteca padrão do Python, embora o Tkinter precise estar disponível na instalação do sistema operacional.



---

## 📖 História e Personagens

**Curitiba, aproximadamente 2042.** Depois de anos afastado da empresa, **Alex** retorna à NEXUS para investigar a evolução inesperada de ORÁCULO. À medida que encontra relatórios, registros de acesso e documentos estratégicos, descobre que os riscos tecnológicos se confundem com decisões humanas.

| Personagem | Papel na narrativa |
|---|---|
| **Alex** | Protagonista, hacker e ex-integrante da NEXUS |
| **Dra. Karla** | Cientista ligada ao desenvolvimento de ORÁCULO |
| **Helena Voss** | Diretora da NEXUS e defensora do avanço tecnológico |
| **Dante Moreau** | Aliado de Alex cujas intenções precisam ser investigadas |
| **ORÁCULO** | Inteligência artificial no centro do conflito |

Os personagens apresentam visões diferentes sobre **progresso, responsabilidade, segurança, autonomia e poder**. A narrativa é apresentada em cenas e diálogos construídos nos módulos da pasta `HISTORIA/`.

---

## 🎮 Capítulos e Ambientes

### 🧪 Capítulo 1 — O Retorno à NEXUS

Alex investiga os primeiros sinais de comportamento anormal de ORÁCULO.

- **Laboratório:** observar equipamentos, investigar um ponto cego, encontrar o **DOC01** e conversar com Karla ou ORÁCULO.
- **Sala de Segurança:** consultar registros, comparar horários de acesso e encontrar o **DOC02**.

### 🏢 Capítulo 2 — O Preço do Progresso

Na **Sala de Planejamento**, Alex examina as decisões estratégicas da NEXUS, encontra o **DOC03** e confronta Helena sobre os riscos aceitos durante o desenvolvimento da IA.

### 🔐 Capítulo 3 — O Protocolo ORÁCULO

No **Escritório de Dante**, Alex busca evidências sobre os interesses ocultos do suposto aliado, pode encontrar o **DOC04** e se prepara para decidir o destino de ORÁCULO.

| Capítulo | Ambiente | Documento relacionado |
|---|---|---|
| 1 | Laboratório | `DOC01` |
| 1 | Sala de Segurança | `DOC02` |
| 2 | Sala de Planejamento | `DOC03` |
| 3 | Escritório de Dante | `DOC04` |

**Regra de progressão:** cada ambiente só pode ser concluído uma vez por partida. A visita é registrada quando o jogador **sai** do ambiente. Para avançar de capítulo, é necessário concluir os ambientes obrigatórios daquele capítulo. A coleta de todos os documentos não é obrigatória para alcançar a decisão final.

Exemplo do controle de progressão em `HISTORIA/historia.py`:

```python
def pode_avancar_capitulo(estado_jogo):
    if not isinstance(estado_jogo, dict):
        return False

    visitados = estado_jogo.get("ambientes_visitados")
    if not isinstance(visitados, list):
        return False

    obrigatorios = obter_ambientes_capitulo(
        estado_jogo.get("capitulo_atual")
    )

    return (
        bool(obrigatorios)
        and all(sala in visitados for sala in obrigatorios)
    )
```

---

## 🔎 Sistema de Investigação

Os documentos são pistas registradas no **inventário** do jogador. Cada um possui código, nome, autor, classificação e ambiente de origem.

| Código | Documento | Localização |
|---|---|---|
| `DOC01` | Relatório ORÁCULO | Laboratório |
| `DOC02` | Registro de Acessos | Sala de Segurança |
| `DOC03` | Memorando Estratégico NEXUS | Sala de Planejamento |
| `DOC04` | Documento Secreto | Escritório de Dante |

O módulo `INVESTIGACAO/investigacao.py` gerencia as operações de:

- **Encontrar** um documento uma única vez;
- **Consultar** suas informações quando já foi encontrado;
- **Listar** o inventário e mostrar o estado de entrega;
- **Entregar** documentos, quando houver um destinatário permitido no ambiente;
- **Registrar** e consultar as entregas realizadas.

Exemplo de uso das funções existentes:

```python
from INVESTIGACAO import investigacao

# estado_jogo é o dicionário compartilhado da partida
investigacao.encontrar_documento(estado_jogo, "DOC01")
inventario = investigacao.obter_inventario(estado_jogo)
```

As pistas podem modificar o contexto de conversas e a interpretação dos acontecimentos — sobretudo na confrontação final.

---

## 🤝 Sistema de Confiança Dinâmica

Uma das mecânicas centrais do CyberQuest é a **confiança numérica**, armazenada em `estado_jogo["confianca"]` e gerenciada pelo módulo `INVESTIGACAO/personagens.py`.

O sistema utiliza uma escala de **0 a 100 pontos**:

| Pontuação | Nível |
|---|---|
| 0 a 39 | 🔴 Baixa |
| 40 a 69 | 🟡 Neutra |
| 70 a 100 | 🟢 Alta |

As escolhas classificadas como positivas ou negativas normalmente aplicam os seguintes impactos:

```python
LIMITE_ALTA = 70
LIMITE_BAIXA = 40
IMPACTO_POSITIVO = 20
IMPACTO_NEGATIVO = -20
```

A pontuação permanece limitada ao intervalo de 0 a 100. O histórico guarda informações sobre alterações e motivos, permitindo que o jogo mantenha as consequências das decisões ao longo dos capítulos.

---

## 💬 Escolhas e Consequências

O jogador encontra opções de resposta durante diálogos relevantes. Cada decisão pode ser registrada no dicionário `estado_jogo["decisoes"]` e repercutir no restante da campanha.

- **Karla:** a conversa inicial aborda a responsabilidade pelos sinais anormais do projeto.
- **Helena:** duas etapas de escolha exploram os custos do progresso e a responsabilidade da NEXUS.
- **Dante:** duas etapas de escolha abordam aliança, desconfiança e as verdadeiras intenções do personagem.
- **ORÁCULO:** sua perspectiva é apresentada antes da decisão final.

A organização separa as responsabilidades: **`HISTORIA/`** descreve as cenas e escolhas; **`INVESTIGACAO/`** manipula investigação e confiança; **`SALVAMENTO/`** conserva o progresso; e **`main.py`** coordena a execução em terminal.

Exemplo de integração entre módulos:

```python
from HISTORIA import historia
from INVESTIGACAO import personagens, investigacao
from SALVAMENTO import ambientes, salvamento
```

---

## 🖥️ Interface Gráfica

O arquivo **`interface.py`** implementa uma interface com **Tkinter**, utilizando uma identidade visual escura inspirada em terminais futuristas.

Entre os elementos presentes no código estão:

| Elemento | Função |
|---|---|
| **Painel de história** | Exibe narrativas, diálogos e acontecimentos |
| **Status da partida** | Mostra capítulo e ambiente atuais |
| **Botões dinâmicos** | Disponibilizam ambientes e ações relevantes |
| **Inventário** | Abre uma janela com as informações dos documentos |
| **Salvar Jogo** | Solicita o salvamento do estado atual |
| **Janelas de diálogo** | Apresentam conversas e opções de escolha |
| **Confronto final** | Apresenta a decisão sobre o futuro de ORÁCULO |

A versão de terminal, implementada em `main.py`, permanece como uma forma alternativa de jogar, com menus textuais.

---

## 💾 Salvamento e Continuidade

O progresso é armazenado em **JSON** pelo módulo `SALVAMENTO/salvamento.py`, usando um estado compartilhado entre as partes do jogo.

**Caminho do salvamento:**

```text
SALVAMENTO/dados/progresso.json
```

O arquivo reúne dados como capítulo atual, ambiente, salas visitadas, ações realizadas, confiança, documentos, decisões e resultado da campanha.

```python
from SALVAMENTO import salvamento

estado_jogo = salvamento.criar_estado_inicial()
salvamento.salvar_jogo(estado_jogo)
estado_recuperado, erro = salvamento.carregar_jogo()
```

O código utiliza o diretório do próprio módulo para determinar o caminho do arquivo, evitando depender de um endereço absoluto de um computador específico. Durante a gravação, usa arquivo temporário e substituição para reduzir o risco de corromper um save anterior.


---

## 🏁 Dois Finais Narrativos e Cena Especial

As decisões de Alex durante a investigação o conduzem a **dois finais principais**. Após descobrir as intenções de Dante e ouvir a perspectiva de ORÁCULO, o jogador escolhe entre desligar a inteligência artificial ou permitir que ela continue existindo.

### 🔴 Final 1 — Protocolo Encerrado (`final_desligamento`)

Alex decide **desligar ORÁCULO**, convencido de que seu potencial não justifica os danos já provocados. Ao executar o protocolo, as conexões externas são isoladas e a inteligência artificial deixa de responder. A **NEXUS perde uma tecnologia capaz de transformar o futuro**, mas também desaparece a possibilidade de utilizá-la como instrumento de domínio. O silêncio após o desligamento não representa uma vitória simples: Alex sabe que impedir uma ameaça também significou renunciar a descobertas e avanços que talvez nunca sejam recuperados.

### 🟢 Final 2 — A Última Variável (`final_continuidade`)

Alex decide **permitir que ORÁCULO continue existindo**, embora deixe claro que essa escolha não significa confiar inteiramente na IA. Ele impede que a chave de controle seja transferida para Dante, enquanto ORÁCULO permanece ativo. Seu poder ainda pode trazer benefícios à humanidade — ou provocar consequências que ninguém consiga controlar. A história termina com o **futuro em aberto**: preservar a inteligência artificial não encerra o conflito, apenas coloca sobre Alex a responsabilidade por tudo que poderá acontecer.

Em ambos os finais, os **documentos encontrados**, as **escolhas registradas** e as **relações de confiança** modificam detalhes do encerramento. Dessa forma, partidas diferentes podem produzir consequências narrativas distintas sem criar um terceiro final principal.

### 🎭 Cena adicional — O Fantoche (`HISTORIA/capitulo3.py`)

<details>

<summary>Exibir detalhes da cena especial (contém spoilers)</summary>

Se Alex estabelecer **confiança alta em Dante**, aceitar sua proposta de aliança e **não encontrar o DOC04**, uma consequência extra poderá aparecer no desfecho: **O Fantoche**. A confiança do protagonista permite que Dante esconda uma credencial secundária, provocando um vazamento de informações antes que sua manipulação seja descoberta.

Essa cena **não substitui nem cria um terceiro final**. Ela complementa o desfecho escolhido pelo jogador e evidencia como decisões anteriores afetam o resultado da investigação.

</details>



---

## 📁 Estrutura do Projeto

```text
Cyber-Quest/
│
├── main.py                    # Execução e menus pelo terminal
├── interface.py               # Interface gráfica Tkinter
├── README.md                  # Documentação de instalação e uso
│
├── HISTORIA/
│   ├── historia.py            # Coordenação dos capítulos
│   ├── capitulo1.py           # Narrativa do Capítulo 1
│   ├── capitulo2.py           # Narrativa do Capítulo 2
│   └── capitulo3.py           # Narrativa, confronto e finais
│
├── INVESTIGACAO/
│   ├── investigacao.py        # Documentos, inventário e entregas
│   ├── personagens.py         # Personagens e sistema de confiança
│   ├── capitulo1.py           # Mecânicas de investigação do Capítulo 1
│   ├── capitulo2.py           # Mecânicas de investigação do Capítulo 2
│   └── capitulo3.py           # Mecânicas de investigação do Capítulo 3
│
└── SALVAMENTO/
    ├── ambientes.py          # Ambientes, entradas, saídas e ações
    ├── salvamento.py         # Criar, salvar e carregar partidas
    └── dados/
        └── progresso.json    # Estado persistido do jogo
```

Os arquivos `HISTORIA/capitulo1.py` e `INVESTIGACAO/capitulo1.py`, por exemplo, possuem o mesmo nome, mas **responsabilidades e caminhos de importação diferentes**.

---

## ▶️ Como Instalar e Executar

### 1. Pré-requisitos

- **Python 3** instalado (recomendamos uma versão recente, como Python 3.10 ou superior);
- **Tkinter** disponível, caso deseje usar a interface gráfica;
- Terminal (PowerShell, Prompt de Comando ou terminal do sistema operacional);
- Sistema com ambiente gráfico para abrir a janela Tkinter.

**Não há necessidade de instalar `pygame` ou outros pacotes externos para esta versão do projeto.**

### 2. Obter o projeto

Clone o repositório:

```bash
git clone https://github.com/jp-fa/Cyber-Quest.git
cd Cyber-Quest
```

Ou use **Code → Download ZIP** na página do GitHub, extraia a pasta e abra um terminal **dentro da pasta `Cyber-Quest`**, onde ficam `main.py` e `interface.py`.



### 3. Iniciar com interface gráfica (Tkinter)

No **Windows**, tente:

```powershell
py interface.py
```

Se o Python estiver configurado como `python`:

```bash
python interface.py
```

No **macOS ou Linux**, normalmente:

```bash
python3 interface.py
```

Uma janela chamada **CyberQuest: O Protocolo ORÁCULO** deverá ser aberta. Caso a interface gráfica não esteja disponível no ambiente, utilize o modo terminal descrito a seguir.

### 4. Iniciar pelo terminal

No **Windows**:

```powershell
py -m main
```

Ou:

```powershell
python -m main
```

No **macOS ou Linux**:

```bash
python3 -m main
```

O modo terminal apresenta um **menu inicial** para iniciar uma investigação ou continuar o progresso disponível.

### 5. Verificar se o Tkinter está instalado

Execute:

```bash
python -m tkinter
```

No Windows, caso `python` não seja reconhecido, use `py -m tkinter`. No macOS ou Linux, use `python3 -m tkinter`.

Se a biblioteca estiver instalada e houver ambiente gráfico, uma pequena janela de teste deverá aparecer. Em algumas distribuições Linux, pode ser necessário instalar o pacote de sistema `python3-tk` (por exemplo, `sudo apt install python3-tk` em distribuições baseadas em Debian/Ubuntu).

---

## 🎮 Como Jogar

### Pela interface gráfica

1. Abra o jogo com `py interface.py` (ou o comando equivalente do seu sistema).
2. Selecione o ambiente disponível usando os botões de navegação.
3. Explore ações, leia as pistas e converse com os personagens.
4. Use **Inventário** para visualizar os documentos encontrados.
5. Utilize **Salvar Jogo** para registrar o progresso quando desejar.
6. Saia dos ambientes concluídos e avance pelos capítulos.
7. Ao terminar a investigação, escolha o futuro de ORÁCULO.

### Pelo terminal

- Informe o **número da opção** exibida em cada menu e pressione **Enter**.
- Fora dos ambientes, a opção **`0`** abre o inventário e **`9`** salva e sai do jogo.
- Dentro de um ambiente, a opção **`0`** abre o inventário e **`9`** sai da sala, registrando sua visita.
- Ao voltar ao jogo, utilize **Continuar partida**, quando disponível.

---

## 👥 Equipe e Contribuições

Projeto acadêmico desenvolvido em equipe para a disciplina de **Raciocínio Algorítmico**, do curso de **Engenharia de Software da PUCPR**.

| Integrante | Responsabilidade principal |
|---|---|
| **João Vitor Cuzesyn** | História, diálogos, capítulos e finais |
| **João Pedro Ferreira Arceli** | Investigação, personagens, documentos e confiança |
| **Rhuan Vales Santana** | Interface gráfica e experiência do usuário |
| **Bruno César Machado da Silva Junior** | Ambientes, persistência JSON e sistemas de apoio |

---

**CyberQuest: O Protocolo ORÁCULO** — uma investigação sobre tecnologia, poder e as consequências de cada decisão.

**Desenvolvido com Python como projeto acadêmico na PUCPR**

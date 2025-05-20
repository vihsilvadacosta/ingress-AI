# 🎟️ IngressAI - Plataforma Inteligente de Ingressos

**IngressAI** é uma plataforma de análise de logs reais de usuários com foco na visualização de comportamento e detecção de sessões suspeitas. O projeto utiliza dashboards interativos, banco de dados real (`SQLite`) e algoritmos de inteligência artificial para identificar padrões e anomalias no uso da plataforma de compra de ingressos.

---

## 🔍 Funcionalidades

- 📊 Dashboards em Jupyter para análise visual interativa
- 🧠 Detecção de sessões anômalas com Isolation Forest (IA)
- 📁 Armazenamento de logs reais em banco de dados SQLite
- 🎛️ Interface amigável com Gradio para explorar dados
- 📅 Métricas por sessão: duração, ações realizadas, classificação
- 🔒 Classificação de sessões: **Normal** ou **Suspeito**

---

## 🖼️ Interface Visual

> A interface inclui filtros por usuário, gráficos de dispersão com classificação de sessões e visualização de ações registradas no banco de dados real.

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório:

```bash
git clone https://github.com/vihsilvadacosta/ingress-AI.git
cd ingress-AI
```

### 2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação:

#### Para rodar a interface Gradio:
```bash
python app.py
```

#### Ou abra os dashboards:
Abra os arquivos `.ipynb` no Jupyter Notebook, por exemplo:
- `dashboard_gradio_ingressos.ipynb`
- `pipeline_logs_ingressos_com_anomalias.ipynb`

---

## 📂 Estrutura do Projeto

```
├── app.py                        # Código principal da aplicação Gradio
├── criar_banco.py               # Script de criação e inicialização do banco
├── database.db                  # Banco de dados SQLite com logs reais
├── dashboards_melhorados/       # Dashboards Jupyter (com IA e análises)
│   ├── dashboard_logs_interativo_com_anomalias.ipynb
│   └── pipeline_logs_ingressos_novo.ipynb
├── static/                      # Arquivos estáticos (CSS, imagens)
├── templates/                   # Páginas HTML (login, cadastro)
├── README.md                    # Este documento
└── requirements.txt             # Bibliotecas usadas no projeto
```

---

## 📌 Observações Importantes

- A coluna **`id` representa o identificador do log** (registro de evento), **não** o identificador do usuário.
- Os dados de log utilizados são reais, simulando acessos e interações em uma plataforma de ingressos.

---

## 🧠 Tecnologias e Bibliotecas

- Python 3.12+
- Pandas, Matplotlib, Seaborn
- Scikit-learn (`IsolationForest`)
- Gradio
- SQLite3
- Flask 
- Jupyter Notebooks

---

## 👩‍💻 Autoria

Projeto desenvolvido por **Vitória Costa e Suelen Araujo** como parte de estudo acadêmico, com foco em:
- Inteligência Artificial aplicada à análise de logs
- Usabilidade e experiência do usuário
- Detecção de comportamentos anômalos em sistemas de ingresso

---

## 📃 Licença

Este projeto é de uso acadêmico e livre para fins de aprendizado e demonstração.

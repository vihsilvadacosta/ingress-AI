# ![Logo](imagem/logoIngressAI.png)

# 🧠 Ingress-AI: Plataforma de Ingressos com Inteligência Artificial

Este projeto consiste em uma plataforma de compra de ingressos com funcionalidades aprimoradas por **Inteligência Artificial (IA)** para análise de sessões de usuários e comportamento de compras. Ele une o back-end em **Flask + SQLite** com dashboards interativos em **Gradio**, além de pipelines em **Jupyter Notebook**.

---

## 🎯 Objetivo

Detectar sessões e comportamentos de compra **anômalos** a partir de logs de uso com técnicas de IA, auxiliando na **melhoria da usabilidade** da plataforma e na identificação de padrões fora do comum.

---

## ⚙️ Tecnologias Utilizadas

- `Python 3`
- `Flask`
- `SQLite3`
- `Gradio`
- `Jupyter Notebook`
- `Pandas`
- `Plotly`
- `Scikit-learn (Isolation Forest)`

---

## 📁 Estrutura do Projeto

```
📦 plataforma_ingressos_completa_com_ia/
├── app.py                    # Backend Flask (compra, login, log)
├── static/                   # CSS e imagens
├── templates/                # HTML (login, cadastro, compra)
├── database.db               # Banco de dados SQLite
├── dashboard_gradio_ingressos.ipynb     # Dashboard de compras com IA
├── dashboard_logs_interativo_com_anomalias.ipynb  # Dashboard de sessões com IA
├── pipeline_logs_anomalias_ia_novo.ipynb          # Pipeline de sessões com IA
├── pipeline_logs_ingressos_atualizado.ipynb       # Pipeline de compras com IA
├── imagem/                  # Imagens do README e telas
└── README.md
```

---

## 🧪 Funcionalidades com IA

### ✅ Sessões

- Classificação automática usando `Isolation Forest`
- Detecção de sessões com duração ou ações fora do padrão
- Visualização de sessões por usuário e por classificação (Normal x Anômala)

### 🎟️ Compras de Ingressos

- Agrupamento por usuário e evento
- Classificação de usuários com comportamento de compra atípico
- Apoio à detecção de **problemas de usabilidade** ou uso indevido

---

## 📊 Dashboards Interativos

Disponíveis via **Gradio**:

- `dashboard_logs_interativo_com_anomalias.ipynb`
- `dashboard_gradio_ingressos.ipynb`

Com filtros por **ID**, **nome** e **email**, os gráficos incluem:

- Duração da sessão vs ações
- Compras por evento e por usuário
- Gráficos de classificação com IA

---

## 🚀 Execução Simultânea (Plataforma + Notebooks)

Execute a plataforma Flask em uma porta (ex: `localhost:5000`) e os dashboards/notebooks em outra (ex: `localhost:7860`).

Exemplo:
```bash
# Terminal 1
python app.py

# Terminal 2
jupyter notebook dashboard_logs_interativo_com_anomalias.ipynb
```

---

## 👩‍💻 Autores

- Vitória Costa
- Suelen Araujo

---

## 📸 Demonstrações

### 🟣 Plataforma Web - Compra de Ingressos
![Tela de Compras](imagem/telaCompras.png)

### 🔐 Tela de Login
![Login](imagem/login.png)

### 📝 Tela de Cadastro
![Cadastro](imagem/cadastro.png)

### 🏠 Tela Inicial da Plataforma
![Tela Inicial](imagem/telaInicial.png)

---

### 📊 Dashboard de Sessões com IA
![Dashboard Sessões](imagem/dashboardSessoes.png)

### 📈 Pipeline de Sessões com IA
![Pipeline Sessões](imagem/pipelineSessoes.png)

---

### 🎟️ Dashboard de Compras com IA
![Dashboard Compras](imagem/dashboardCompras.png)

### 📉 Pipeline de Compras com IA
![Pipeline Compras](imagem/pipelineIngressos.png)

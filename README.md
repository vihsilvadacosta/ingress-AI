<p align="center">
  <img src="imagem/logoIngressAI.png" alt="Logo IngressAI" width="250"/>
</p>

# 🎟️ Plataforma de Venda de Ingressos com Análise Inteligente de Usabilidade

Este projeto integra uma plataforma de venda de ingressos com uma suíte de dashboards interativos e pipelines que utilizam **Inteligência Artificial (IA)** para analisar **comportamentos de usuários**, detectar **anomalias em sessões** e identificar **possíveis problemas de usabilidade** da plataforma.

## 👥 Autoria

- Vitória Costa – Desenvolvimento da plataforma, backend, dashboards e pipelines com IA
- Suelen Araujo – Coautoria no desenvolvimento e testes de usabilidade e sessões anômalas com IA

---

## 🚀 Tecnologias Utilizadas

- **Flask** – Backend da plataforma de ingressos
- **SQLite3** – Banco de dados leve e embutido
- **HTML + CSS** – Interface visual da plataforma
- **Plotly Express** – Visualização interativa dos dados
- **Scikit-learn** – Algoritmo de IA (Isolation Forest)
- **Gradio** – Dashboards com filtros e interação em tempo real
- **Jupyter Notebook** – Desenvolvimento e execução dos pipelines analíticos

---

## 🧠 IA aplicada à Análise de Usabilidade

Utilizamos o algoritmo **Isolation Forest** para detectar **sessões e comportamentos anômalos** com base nos seguintes fatores:

- **Duração da sessão** (em minutos)
- **Número de ações realizadas**
- **Padrões incomuns de compra**

> As classificações resultantes (`Normal`, `Anômala`) ajudam a identificar possíveis **gargalos de navegação**, **comportamentos fora do padrão** ou **ações que indicam dificuldades de uso**.

---

## 📊 Dashboards Interativos

1. **Dashboard de Sessões (IA)**
   - Classifica sessões como `Normal` ou `Anômala`
   - Exibe dispersão de duração vs. ações, sessões por usuário, e gráfico de classificação geral
   - Interface construída com **Gradio**

2. **Dashboard de Compras (IA)**
   - Analisa padrões de compra com base em eventos, datas e usuários
   - Exibe gráficos de barras, pizza e evolução temporal
   - Também utiliza IA para destacar possíveis anomalias

3. **Dashboard Jupyter**
   - Alternativa interativa em notebooks para análise e apresentação acadêmica
   - Permite visualização personalizada e execução modular

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/plataforma-ingressos-ia.git
cd plataforma-ingressos-ia
```

### 2. Instalar dependências
Crie um ambiente virtual e instale os pacotes:
```bash
pip install -r requirements.txt
```

### 3. Executar simultaneamente:

#### 🟢 Backend Flask
```bash
python app.py
# Ou em porta customizada:
# python app.py --port 5000
```

#### 🔵 Jupyter Notebooks (dashboards e pipelines)
```bash
jupyter notebook
```

Execute os arquivos:

- `pipeline_logs_anomalias_ia_novo.ipynb`
- `dashboard_logs_interativo_com_anomalias.ipynb`
- `pipeline_logs_ingressos_atualizado.ipynb`
- `dashboard_gradio_ingressos.ipynb`

---

## 📁 Estrutura de Arquivos

```
├── app.py                            # Plataforma de vendas (Flask)
├── database.db                       # Banco de dados SQLite
├── templates/                        # HTMLs da interface
├── static/                           # CSS
├── pipeline_logs_anomalias_ia_novo.ipynb
├── dashboard_logs_interativo_com_anomalias.ipynb
├── pipeline_logs_ingressos_atualizado.ipynb
├── dashboard_gradio_ingressos.ipynb
├── README.md
```

---

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido com foco em **melhoria da usabilidade** e **detecção de anomalias em logs de interação**, podendo ser apresentado em mostras tecnológicas e TCCs com ênfase em:

- Experiência do Usuário (UX)
- Inteligência Artificial aplicada a análise de logs
- Segurança e monitoramento de plataformas web

---

## 📬 Contato

Para dúvidas ou colaborações:
- **Vitória Costa**
- **Suelen Araujo**

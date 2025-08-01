Exercícios de consumo de API, uso de venv, .env, uso .gitignore (ignorar arquivos venv)

```m# 💸 Projeto: Cotação de Moedas com API

Este é um projeto simples em **Python** para consultar a cotação de moedas estrangeiras em tempo real usando a **ExchangeRate API**. Ele aplica boas práticas como uso de ambiente virtual (`venv`), variáveis de ambiente (`.env`), dependências (`requirements.txt`) e versionamento com Git e GitHub.

---

## 📌 Funcionalidades

✅ Consulta em tempo real das cotações de moedas  
✅ Uso de chave de API via `.env`  
✅ Suporte para múltiplas moedas (BRL, EUR, GBP, etc.)  
✅ Código limpo e bem estruturado  
✅ Pronto para subir no GitHub

---

## 🧰 Tecnologias Utilizadas

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- ExchangeRate API (https://www.exchangerate-api.com)

---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/cotacao_api.git
cd cotacao_api

### 2. Crie e ative o ambiente virtual

**Linux/macOS:**

```bash
python3 -m venv venv_seunome
source venv_seunome/bin/activate
```

**Windows:**

```bash
python -m venv venv_seunome
venv_seunome\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da API

- Crie um arquivo `.env` com o seguinte conteúdo:

```
API_KEY=sua_chave_aqui
```

- Use o arquivo `.env.example` como modelo.

> 🔐 Obtenha sua chave gratuita em: [https://www.exchangerate-api.com](https://www.exchangerate-api.com)

### 5. Execute o script

```bash
python consulta.py
```

---

## 📁 Estrutura do Projeto

```
cotacao_api/
├── .env              # Suas variáveis secretas (NÃO subir no GitHub)
├── .env.example      # Exemplo do arquivo .env
├── .gitignore        # Ignora arquivos/diretórios sensíveis
├── consulta.py       # Script principal da aplicação
├── requirements.txt  # Dependências do projeto
└── README.md         # Este arquivo
```

---

## 📊 O Script Faz:

- Carrega a chave da API do `.env`
- Realiza uma requisição para a URL:
  ```
  https://v6.exchangerate-api.com/v6/SUA_CHAVE/latest/USD
  ```
- Mostra no terminal as cotações do **dólar (USD)** para:
  - Real brasileiro (BRL)
  - Euro (EUR)
  - Libra esterlina (GBP)
  - Outras moedas (você pode modificar!)

---

## 🔁 Reinstalação após Clonar

Se você apagar a pasta local e quiser reinstalar tudo:

```bash
git clone https://github.com/seu-usuario/cotacao_api.git
cd cotacao_api
python -m venv venv_seunome
source venv_seunome/bin/activate  # ou Scripts\activate no Windows
pip install -r requirements.txt
# Recrie o arquivo .env com sua chave
python consulta.py
```

---

## 📜 Licença

Este projeto é apenas para fins educacionais e não possui licença comercial.

---

> 💡 Projeto criado para praticar consumo de APIs reais, boas práticas de Python e versionamento com Git/GitHub.
```

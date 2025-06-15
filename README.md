# 🧠 CS50 Wiki Clone

Este projeto é uma mini-enciclopédia online que permite ao usuário criar, visualizar, editar e pesquisar páginas em Markdown. Ele foi desenvolvido como parte do curso [CS50’s Web Programming with Python and JavaScript](https:/cs50.harvard.edu/web/2020/) da Universidade de Harvard.

---

## 🎯 Objetivo do Projeto

O objetivo era recriar o funcionamento básico da Wikipedia com as seguintes funcionalidades:

- Listagem de páginas disponíveis
- Visualização do conteúdo convertido de Markdown para HTML
- Criação de novas páginas
- Edição de páginas existentes
- Pesquisa simples e exata
- Página aleatória

---

## 🧱 Tecnologias Utilizadas

- Python 3
- Django (Framework Web)
- HTML/CSS
- Markdown2 (parser de Markdown para HTML)

---

## 🛠️ Como Rodar Localmente

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/cs50-wiki-clone.git
cd cs50-wiki-clone/wiki
```

### 2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Rode o servidor Django:

```bash
python manage.py runserver
```

### 5. Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 📁 Estrutura do Projeto

```
wiki/
├── encyclopedia/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── wiki/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

---

## ✨ Funcionalidades

- Conversão de Markdown em tempo real
- CRUD de páginas
- Pesquisa de termos
- Página aleatória
- Edição protegida contra duplicatas

---

## 📌 Melhorias Futuras

- Estilização com CSS aprimorada
- Suporte a upload de imagens
- Sistema de login para edições autenticadas

---

## 📜 Licença

Este projeto foi desenvolvido para fins educacionais como parte do curso CS50.  
Licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---

## 👨‍💻 Autor

Desenvolvido por [Estevão Amaro] – GitHub: [@Steve09012004](https://github.com/Steve09012004)

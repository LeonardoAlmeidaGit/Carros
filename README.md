# Carros — Sistema de Gestão de Veículos

Sistema web completo para gestão de veículos desenvolvido com Django. Permite cadastrar, visualizar, editar e deletar carros, gerenciar marcas e controlar o inventário de veículos com atualização automática via Django Signals.

## 🚀 Tecnologias

- Python 3.x
- Django 5.x
- PostgreSQL
- Pillow
- Bootstrap 5
- HTML e CSS

## ✅ Funcionalidades

- Listagem de carros com filtro de busca por modelo
- Cadastro completo de veículos com foto, marca, ano de fabricação, ano do modelo, placa e valor
- Visualização detalhada de cada veículo
- Edição e exclusão de veículos
- Gerenciamento de marcas
- Atualização automática do inventário via Django Signals
- Sistema de autenticação com login, logout e registro de usuários
- Controle de acesso com proteção de rotas via login_required
- Validação de valor mínimo e ano de fabricação no formulário

## 🔧 Como rodar o projeto localmente

Pré-requisitos: Python 3.x e PostgreSQL instalados

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/carros.git
cd carros
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=cole-sua-SECRET_KEY-aqui
DEBUG=True
DB_NAME=carros
DB_USER=seu-usuario
DB_PASSWORD=sua-senha
DB_HOST=localhost
DB_PORT=5432
```

### 5. Execute as migrations

```bash
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse http://127.0.0.1:8000 no navegador.

## 🔐 Autenticação e Controle de Acesso

O sistema utiliza o sistema nativo de autenticação do Django. As rotas de cadastro, edição e exclusão de veículos são protegidas e exigem login. Usuários não autenticados são redirecionados automaticamente para a página de login.

## 📁 Estrutura do Projeto
carros/ ├── app/ # Configurações principais, settings e urls ├── cars/ # Gestão de veículos, marcas e inventário ├── accounts/ # Autenticação, login, logout e registro

## 👨‍💻 Autor

Leonardo — [LinkedIn](https://www.linkedin.com/in/leonardoalmeida-/) · [GitHub](https://github.com/LeonardoAlmeidaGit)


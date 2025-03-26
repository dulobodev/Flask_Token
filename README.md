# API REST com Flask e Autenticação JWT

Este projeto implementa uma API REST básica utilizando **Flask** com operações **CRUD** (Create, Read, Update, Delete) e **autenticação via JWT** (JSON Web Token). O foco dessa API é mostrar um pouco de segurança, contendo criptografia da senha, um banco um pouco mais seguro, mas em geral, funcionalidades simples.

## Funcionalidades ⚙️

- **Operações CRUD completas**:
  - **GET**: Listar recursos / Obter recurso específico
  - **POST**: Criar novo recurso
  - **PUT**: Atualizar recurso
  - **DELETE**: Remover recurso
- **Autenticação baseada em JWT**.
- **Configuração de ambiente** usando arquivo `.env`.
- **Banco de dados SQLite** com **Flask-SQLAlchemy**.
- **CORS habilitado** para integração com frontends.

## Pré-requisitos 📋

- Python 3.7+
- **pip** (gerenciador de pacotes do Python)
```bash
pip install flask flask-sqlalchemy flask-jwt-extended flask-cors python-dotenv
```

## Instruções de Configuração

### 1. Clone o repositório

```bash
git clone [URL_DO_SEU_REPOSITÓRIO]
cd [DIRETÓRIO_DO_PROJETO]
```

### 2. Crie um arquivo .env
- Crie um novo arquivo com o nome **.env**
- Dentro do arquivo adicione:
``` bash
SECRET_KEY = 'YOUR SECRET_KEY'
JWT_SECRET_KEY = SECRET_KEY
DATABASE = 'database.db'
```

### 3. Rode a aplicação
**python app.py**

  
## Rotas 🧭
**users** (parte para cadastrar usuarios com permisão para utilizar a api)
```bash
GET |/me |/me/id |
POST|/register |/login |
PUT |/me|
DELETE |/me|
```
**cadastrado** ( parte para cadastro de pessoas, só é possivel utilizar com autentificação)
```bash
GET |/id |
POST|/create |
PUT |/update/id|
DELETE |/delete/id|
```


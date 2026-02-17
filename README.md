# 🌐 Animus ERP

### Status do projeto: Em produção 🏗️

---

O **Animus** é um sistema de Gestão de Recursos Empresariais (ERP) simplificado, focado em eficiência, segurança e escalabilidade. O projeto foi desenvolvido para demonstrar a aplicação de boas práticas de programação e arquitetura de software.

---

### 📜 Sobre o Projeto

O Animus centraliza algumas das princípais operações de uma empresa em uma estrutura robusta.

### Funcionalidades Principais:
* **Controle de Estoque:** Gestão de entrada/saída de produtos, categorias e alertas de estoque baixo.
* **Gestão de Usuários:** Autenticação segura e controle de acesso baseado em funções (RBAC).
* **Ponto de Vendas (PDV):** Interface para registro de vendas com atualização de inventário em tempo real.

---

## 🛠️ Princípais Tecnologias Utilizadas no Backend:

- **FastAPI** -> Contrução da API.
- **Uvicorn** -> Servidor de aplicação.
- **SQLAlchemy** -> Manipulação do banco de dados atráves de código.
- **Pytest** -> Testes automátizados.
- **psycopg2** -> Driver de conexão com o Banco de dados principal.
- **Alembic** -> Migrações de bancos de dados.

> **Nota**: Você pode encontrar todas as dependências utilizadas no backend e suas versões no arquivo de pedências do projeto, que fica em **backend/requirements.txt.**

---

## 🏗️ Estrutura do Backend

O projeto segue uma organização de pastas pensada para facilitar a manutenção e a criação de testes:

```text
animus-erp/
├── backned/
│    ├──src
│    │   ├── routes/        # Endpoints e controladores das rotas
│    │   ├── config/        # Configurações globais
│    │   ├── database/      # Lógica de conexão com banco de dados     
│    │   ├── models/        # Modelos de dados (Entidades do Banco)
│    │   ├── schemas/       # Esquemas de validação e serialização
│    │   ├── repositories/  # Lógica de cominicação com o banco de dados
│    │   └── database.py    # Conexão e sessão do banco de dados
│    ├── tests/             # Suíte de testes automatizados
│    ├── .env.example       # Modelo de variáveis de ambiente
│    └── app.py             # Ponto de entrada da aplicação
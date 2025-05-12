# 📌 Desafio Técnico – Desenvolvedor(a) Back-end Sênior

A Prefeitura do Rio de Janeiro quer oferecer aos cidadãos uma API de Carteira Digital, onde os usuários poderão armazenar e gerenciar documentos digitais, consultar e carregar créditos do transporte público e acessar serviços municipais via chatbot.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python com FastAPI  
- **Banco de Dados:** PostgreSQL  
- **ORM:** SQLAlchemy com Alembic  
- **Testes:** Pytest  
- **Autenticação:** Bearer Token (JWT)  
- **Documentação:** OpenAPI gerada automaticamente pelo FastAPI  
- **Controle de Versão:** Git e GitHub  
- **CI/CD:** GitHub Actions  
- **Conteinerização:** Docker e Docker Compose
  
---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos
- Python 3.10+  
- Docker e Docker Compose configurados  
- Ambiente virtual configurado (venv)  

### Passos para Execução

Clone o repositório
```bash
git clone https://github.com/gabrielaM0tta/desafio-senior-backend-developer.git
```
Suba o projeto e o banco de dados através do docker
```bash
docker compose up -d
```
Execute as migrations para criação das tabelas no banco 
```bash
alembic upgrade head
```
---

## 🚀 Como Testar

### Rodando os Testes
```bash
# Ative o ambiente virtual
source venv/bin/activate

# Rode os testes com pytest
pytest
```
### Testando a API
- Você pode verificar se o banco está ativo através do endpoint `http://localhost:8000/health`.  
- Use a rota de autenticação para obter o token JWT e acessar as demais rotas.

---
## 🌐 Documentação da API
- A documentação automática da API está disponível em `http://localhost:8000/docs#/` (OpenAPI).  

---

## 📝 Decisões Técnicas

### 📌 Arquitetura
- O projeto foi desenvolvido como uma API Monolítica, eu escolhi essa arquitetura por se tratar de um projeto simples e com curto prazo de entrega.  
- Escolhi o padrão **Controller-Service-Repository (CSR)** adaptado ao fastApi por acreditar que por ter essa separação de camadas o código fica mais organizado e mais fácil de dar manutenção.
- O ORM escolhido foi o **SQLAlchemy** com **Alembic** para controle de migrações, pois eu trabalho melhor com códigos síncronos.  
- As rotas foram estruturadas com controle de autenticação via JWT.

### 📌 Banco de Dados
- Utilizado PostgreSQL, configurado via Docker Compose para facilitar o desenvolvimento.  
- As migrações são gerenciadas com Alembic.  

### 📌 Testes Automatizados
- Utilizado **Pytest** para testes unitários.  
- Testes foram organizados para cobrir as funcionalidades de documentação e passe de transporte.  
- Teste de verificação de saúde da API (`/health`) garante que o banco está acessível.  

### 📌 Configuração de CI/CD
- Utilizado GitHub Actions para configurar um workflow simples que roda os testes automaticamente a cada push na main.  

---
## 📊 Modelagem de Banco de Dados
![teste drawio](https://github.com/user-attachments/assets/03caa509-66ca-462c-83c0-13caa370ed4f)

## 💡 Contato

- **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/gabrielasantosmotta/)  
- **E-mail:** gbss.santos1707@gmail.com


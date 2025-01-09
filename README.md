Bem-vindo à API de To-Do List desenvolvida em Python com o framework Flask.
Este repositório demonstra um CRUD básico (Create, Read, Update, Delete) para gerenciar tarefas, mostrando conceitos de desenvolvimento Back-End.

Índice
Descrição do Projeto
Funcionalidades
Tecnologias Utilizadas
Como Executar
Pré-requisitos
Instalação
Executando a Aplicação
Estrutura de Pastas
Endpoints
Possíveis Melhorias
Contribuindo
Licença
Contato
Descrição do Projeto
Este projeto é uma API REST que gerencia tarefas (To-Do List). Ele permite criar, listar, atualizar e excluir tarefas por meio de endpoints que retornam e recebem dados em formato JSON.

O objetivo principal é exemplificar conceitos de desenvolvimento web com Python e Flask, servindo como um ponto de partida para quem deseja aprender sobre:

Estrutura de rotas e métodos HTTP (GET, POST, PUT, DELETE).
Manipulação de dados no formato JSON.
Princípios básicos de organização de um projeto Back-End.
Funcionalidades
Listar tarefas: Retorna todas as tarefas cadastradas.
Criar nova tarefa: Permite adicionar uma nova tarefa à lista.
Atualizar uma tarefa: Altera título ou status (“concluído” ou não).
Excluir tarefa: Remove a tarefa desejada pelo seu ID.
Tecnologias Utilizadas
Python 3.x
Flask
pip para gerenciamento de pacotes
(Opcional) Virtualenv para ambiente virtual
Como Executar
Pré-requisitos
Ter o Python 3.x instalado.
(Opcional, porém recomendado) Ter um ambiente virtual configurado (pode ser venv ou virtualenv).
Git instalado, caso queira clonar este repositório via linha de comando.
Instalação
Clonar este repositório:

bash
Copiar código
git clone https://github.com/SEU_USUARIO/todo-list-flask.git
Se preferir, baixe o arquivo ZIP diretamente pelo GitHub e extraia em uma pasta local.

Criar e ativar um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
cd todo-list-flask
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
Instalar as dependências:

bash
Copiar código
pip install -r requirements.txt
Caso não exista um requirements.txt, você pode instalar manualmente com pip install flask, por exemplo.

Executando a Aplicação
Certifique-se de estar na pasta do projeto:

bash
Copiar código
cd todo-list-flask
Inicie a aplicação Flask:

bash
Copiar código
python app.py
Se você estiver com debug habilitado, a aplicação ficará acessível em
http://127.0.0.1:5000 (ou conforme exibido no terminal).

Testar: Você pode testar os endpoints usando ferramentas como Postman, Insomnia ou até mesmo curl no terminal.

Estrutura de Pastas
Um exemplo de estrutura do projeto pode ser:

arduino
Copiar código
todo-list-flask/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── venv/ (opcional - ambiente virtual)
app.py: Arquivo principal onde está definido o Flask app e as rotas.
requirements.txt: Lista de dependências para instalar com pip.
.gitignore: Arquivos e pastas que não devem ser versionados (por exemplo, venv).
venv/: Ambiente virtual (gerado localmente, não é obrigatório versionar).
Endpoints
A API expõe endpoints básicos para interação com as tarefas. Abaixo, seguem exemplos de uso (via cURL).

1. Listar todas as tarefas
Rota: GET /tasks
Exemplo:
bash
Copiar código
curl -X GET http://127.0.0.1:5000/tasks
Resposta (JSON):
json
Copiar código
[
  {
    "id": 1,
    "title": "Estudar Python",
    "done": false
  },
  {
    "id": 2,
    "title": "Fazer compras",
    "done": false
  }
]
2. Criar uma tarefa
Rota: POST /tasks
Exemplo:
bash
Copiar código
curl -X POST http://127.0.0.1:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title": "Aprender Flask"}'
Resposta (JSON):
json
Copiar código
{
  "id": 3,
  "title": "Aprender Flask",
  "done": false
}
3. Obter uma tarefa específica
Rota: GET /tasks/<int:task_id>
Exemplo:
bash
Copiar código
curl -X GET http://127.0.0.1:5000/tasks/1
Resposta (JSON):
json
Copiar código
{
  "id": 1,
  "title": "Estudar Python",
  "done": false
}
4. Atualizar uma tarefa
Rota: PUT /tasks/<int:task_id>
Exemplo:
bash
Copiar código
curl -X PUT http://127.0.0.1:5000/tasks/1 \
     -H "Content-Type: application/json" \
     -d '{"title": "Estudar Flask", "done": true}'
Resposta (JSON):
json
Copiar código
{
  "id": 1,
  "title": "Estudar Flask",
  "done": true
}
5. Excluir uma tarefa
Rota: DELETE /tasks/<int:task_id>
Exemplo:
bash
Copiar código
curl -X DELETE http://127.0.0.1:5000/tasks/1
Resposta: 204 No Content (sem conteúdo)
Possíveis Melhorias
Banco de Dados: Integrar com SQLite, PostgreSQL ou outro SGBD usando SQLAlchemy.
Autenticação: Proteger endpoints com JWT (ex.: Flask-JWT-Extended).
Testes Automatizados: Utilizar pytest ou unittest para garantir a qualidade do código.
Docker: Containerizar a aplicação para facilitar o deploy e padronizar o ambiente.
Documentação: Adicionar Swagger ou OpenAPI para documentar os endpoints.
Contribuindo
Ficarei feliz em receber contribuições de qualquer forma:

Reportando bugs (via Issues).
Enviando Pull Requests com melhorias ou correções.
Sugerindo novas funcionalidades.
Siga este fluxo básico:

Faça um fork do repositório.
Crie uma branch (ex.: feature/minha-feature).
Realize suas alterações, commit e push.
Abra um Pull Request descrevendo suas mudanças.

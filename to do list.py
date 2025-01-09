from flask import Flask, request, jsonify

app = Flask(__name__)

# Nossa "base de dados" temporária para as tarefas (somente para testes)
tasks = [
    {"id": 1, "title": "Estudar Python", "done": False},
    {"id": 2, "title": "Fazer compras", "done": False},
]


# Função auxiliar para gerar ID
def get_new_id():
    if not tasks:
        return 1
    # retorna o maior id + 1
    return max(task['id'] for task in tasks) + 1


@app.route('/')
def hello_world():
    return "API de To-Do List - Flask"


# 1. Listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200


# 2. Criar nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Título é obrigatório"}), 400

    new_task = {
        "id": get_new_id(),
        "title": data['title'],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


# 3. Obter uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    return jsonify(task), 200


# 4. Atualizar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task is None:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    if 'title' in data:
        task['title'] = data['title']
    if 'done' in data:
        task['done'] = data['done']

    return jsonify(task), 200


# 5. Excluir uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task is None:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204


# Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)

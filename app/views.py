from flask import Blueprint, render_template, request, redirect, url_for

app = Blueprint('app', __name__)

# Lista de tareas (almacenada con un estado)
to_do_list = []

@app.route('/')
def index():
    return render_template('index.html', to_do_list=to_do_list)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        # Nueva tarea con estado "Pendiente"
        to_do_list.append({'task': task, 'status': 'Pendiente'})
    return redirect(url_for('app.index'))

@app.route('/update_status/<int:task_id>', methods=['POST'])
def update_status(task_id):
    if 0 <= task_id < len(to_do_list):
        new_status = request.form.get('status')
        to_do_list[task_id]['status'] = new_status
    return redirect(url_for('app.index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(to_do_list):
        del to_do_list[task_id]
    return redirect(url_for('app.index'))
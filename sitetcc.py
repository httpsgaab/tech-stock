from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de usuários permitidos e senha
allowed_users = ['davi', 'gaab', 'romulo', 'luiz', 'kaua']
password = '12345678'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['usuario']
    entered_password = request.form['senha']

    if username in allowed_users and entered_password == password:
        # Redirecionar para a função de visualização associada à rota 'menu'
        return redirect(url_for('menu'))
    else:
        return "Usuário ou senha incorretos."

@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)

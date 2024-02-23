from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
# estoque = pd.read_excel(r"C:\Users\USER\Desktop\sistemy-stk-1\bd-estoque\estoque.xlsx")
# print(estoque)


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

@app.route('/estoque')
def stk():
    try:
        estoque = pd.read_excel(r"app/estoque.xlsx")
        # Convertendo os dados do DataFrame para HTML
        estoque_html = estoque.to_html()
    except Exception as e:
        return f"Erro ao ler o arquivo Excel: {str(e)}"

    return render_template('estoque.html', estoque_html=estoque_html)

@app.route('/notas')
def nts():
    try:
        notas=pd.read_excel(r"notas/nfss.xlsx")
        notas_html=notas.to_html()
    except Exception as e:
        return f"Erro ao executar arquivo {str(e)}"
        
    return render_template('notas.html', notas_html=notas_html)

@app.route('/add-itm')

def add():
    return render_template('add.html')
    
if __name__ == '__main__':
    app.run(debug=True)

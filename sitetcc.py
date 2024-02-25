from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import tkinter as tk
from tkinter import ttk

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
    global estoque
    try:
        estoque = pd.read_excel(r"app/estoque.xlsx")
        # Convertendo os dados do DataFrame para HTML
        estoque_html = estoque.to_html()
    except Exception as e:
        return f"Erro ao ler o arquivo Excel: {str(e)}"

    return render_template('estoque.html', estoque_html=estoque_html)

@app.route('/add-itm', methods=['GET', 'POST'])
def add():
    mensagem = None
    
    try:
        estoque = pd.read_excel("app/estoque.xlsx")  # Atualize o caminho para o arquivo 'estoque.xlsx'
    except FileNotFoundError:
        return "Arquivo 'estoque.xlsx' não encontrado."

    if request.method == 'POST':
        novo_item = {}
        for coluna in estoque.columns:
            novo_item[coluna] = request.form[coluna]

        # Criar um novo DataFrame com o novo item
        novo_df = pd.DataFrame([novo_item], columns=estoque.columns)
        
        # Concatenar o DataFrame existente com o novo DataFrame
        estoque = pd.concat([estoque, novo_df], ignore_index=True)
        
        # Salvar o DataFrame atualizado no arquivo Excel
        estoque.to_excel("app/estoque.xlsx", index=False)  # Atualize o caminho para salvar o arquivo
        
        mensagem = "Item adicionado com sucesso!"

    return render_template('add.html', estoque=estoque, mensagem=mensagem)

@app.route('/delete-item', methods=['POST'])
def delete_item():
    index = int(request.form['index'])
    
    try:
        estoque = pd.read_excel("app/estoque.xlsx")  # Carregar o DataFrame do arquivo Excel
    except FileNotFoundError:
        return "Arquivo 'estoque.xlsx' não encontrado."
    
    # Deletar o item pelo índice
    estoque = estoque.drop(index=index)
    
    # Salvar o DataFrame atualizado no arquivo Excel
    estoque.to_excel("app/estoque.xlsx", index=False)  # Atualize o caminho para salvar o arquivo
    
    # Redirecionar de volta para a página de adição com uma mensagem de sucesso
    return redirect(url_for('add'))

@app.route('/notas')
def notas():
    try:
        notas = pd.read_excel(r"notas/notas.xlsx")
        # Convertendo os dados do DataFrame para HTML
        notas_html = notas.to_html()
    except Exception as e:
        return f"Erro ao ler o arquivo Excel: {str(e)}"

    return render_template('notas.html', notas_html=notas_html)
    
if __name__ == '__main__':
    app.run(debug=True)

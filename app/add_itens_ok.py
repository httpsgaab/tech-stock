import pandas as pd
import tkinter as tk
from tkinter import ttk
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Coloque aqui o código Python que você quer rodar
    # Exemplo:
    estoque_html = "<p>Conteúdo dinâmico gerado pelo Flask!</p>"
    return render_template('add.html', estoque_html=estoque_html)

    estoque = pd.read_excel(r"C:\Users\USER\Desktop\sistemy-stk-1\bd-estoque\estoque.xlsx", sheet_name="ESTOQUE")

    def adicionar_item():
        global estoque  #global para acessar a variável externa.
        novo_item = {}
        for coluna in estoque.columns:
            novo_item[coluna] = entry_vars[coluna].get()
        
        # Criar um novo DataFrame com o novo item
        novo_df = pd.DataFrame([novo_item], columns=estoque.columns)
        
        # Concatenar o DataFrame existente com o novo DataFrame
        estoque = pd.concat([estoque, novo_df], ignore_index=True)
        
        # Salvar o DataFrame atualizado no arquivo Excel
        estoque.to_excel("estoque.xlsx", sheet_name="ESTOQUE", index=False)
        
        update_treeview()

    def update_treeview():
        tree.delete(*tree.get_children())  # Limpar a Treeview
        for index, row in estoque.iterrows():
            tree.insert("", "end", values=tuple(row))


    root = tk.Tk()
    root.title("Controle de Estoque")

    # Criar uma árvore para exibir os dados
    tree = ttk.Treeview(root)
    tree["columns"] = tuple(estoque.columns)

    # Configurar as colunas
    for coluna in estoque.columns:
        tree.heading(coluna, text=coluna)
        tree.column(coluna, width=100)


    update_treeview()

    # Adicionar o Treeview/tabela à interface
    tree.pack(expand=True, fill=tk.BOTH)

    # Adicionar entrada para cada coluna para adicionar novos itens
    entry_vars = {}
    for coluna in estoque.columns:
        label = tk.Label(root, text=coluna)
        label.pack()
        
        entry_var = tk.StringVar()
        entry = tk.Entry(root, textvariable=entry_var)
        entry.pack()
        
        entry_vars[coluna] = entry_var

    #Add item
    btn_adicionar = tk.Button(root, text="Adicionar Item", command=adicionar_item)
    btn_adicionar.pack(pady=10)


    btn_fechar = tk.Button(root, text="Fechar", command=root.destroy)
    btn_fechar.pack(pady=10)


    root.mainloop()

if __name__ == '__main__':
    app.run(debug=True)




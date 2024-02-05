#!/usr/bin/env python
# coding: utf-8

# In[1]:


#teste para ler as duas guias ao mesmo tempo com filtro numa delas:

import pandas as pd

estoque = pd.read_excel(r"C:\Users\USER\Desktop\sistemy-stk-1\bd-estoque\estoque.xlsx")

item = 'ITEM 1'


filtro = estoque['NOME'] == item
itens_filtrados = estoque[filtro]


print(itens_filtrados)


usuarios = pd.read_excel("estoque.xlsx", sheet_name="USUARIOS")


print(usuarios)


# In[ ]:





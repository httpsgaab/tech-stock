#!/usr/bin/env python
# coding: utf-8

# In[1]:


#teste para ler todas as guias:
import pandas as pd


guias = pd.read_excel(r"C:\Users\USER\Desktop\sistemy-stk-1\bd-estoque\estoque.xlsx", sheet_name=None)

for sheet_name, df in guias.items():
    print(f"Dados da guia '{sheet_name}':")
    display(df)


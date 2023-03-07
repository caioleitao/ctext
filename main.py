import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from tkinter import filedialog as fd
import os
janela = tk.Tk()

#areas de butons
butao_novo_arquivo = Button(janela, text="Novo Arquivo", command=lambda:novo_arquivo())
butao_abrir_arquivo = Button(janela, text="Abrir arquivo", command=lambda:abrir_arquivo())
butao_salvar_arquivo = Button(janela, text="Salvar Arquivo", command=lambda:salvar_arquivo())

butao_novo_arquivo.pack(pady=10)
butao_abrir_arquivo.pack(pady=10)
butao_salvar_arquivo.pack(pady=10)

#area de texto
caixa_de_texto = tk.Text()
caixa_de_texto.pack()

def novo_arquivo():
    if messagebox.askokcancel("Tem certeza?", "Você apagara todo contêudo atual para gerar um novo arquivo"): 
        caixa_de_texto.delete('1.0', 'end')

def fecha_janela():
    if messagebox.askokcancel("Tem certeza?", "Você deseja salvar antes de sair?"):
        salvar_arquivo()
        janela.destroy()
    else:
        janela.destroy()

def salvar_arquivo():
    arquivo_texto = open('test.txt', 'w')
    arquivo_texto.write(caixa_de_texto.get(1.0,END))
    arquivo_texto.close()

def abrir_arquivo():
    arquivo_texto = open('test.txt', 'r')
    conteudo = arquivo_texto.read()
    caixa_de_texto.insert(END,conteudo)
    arquivo_texto.close()

janela.protocol("WM_DELETE_WINDOW", fecha_janela)

janela.mainloop()

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

janela = tk.Tk()
janela.title("Ctext")
janela.iconbitmap("icone.png")
janela.columnconfigure(0, weight=1)
janela.rowconfigure(1, weight=1)
#areas de butons
butao_novo_arquivo = Button(janela, text="Novo Arquivo", command=lambda:novo_arquivo()).grid(column=0,row=0,sticky="W")
butao_abrir_arquivo = Button(janela, text="Abrir arquivo", command=lambda:abrir_arquivo()).grid(column=1,row=0,sticky="W")
butao_salvar_arquivo = Button(janela, text="Salvar onde", command=lambda:salvar_arquivo()).grid(column=2,row=0,sticky="W")
butao_salvar_arquivo_atual = Button(janela, text="Salvar arquivo", command=lambda:salvar_arquivo_atual()).grid(column=3,row=0,sticky="W")

#area de texto
caixa_de_texto = tk.Text()
caixa_de_texto.grid(column=0,row=1,columnspan=4,sticky="NSEW")
caixa_de_texto.columnconfigure(0, weight=1)
caixa_de_texto.rowconfigure(0,weight=1)

diretorio_atual = StringVar()
diretorio_atual_label = Label(janela, textvariable=diretorio_atual, relief=SUNKEN, anchor=W)
diretorio_atual_label.grid(column=0, row=2, columnspan=4, sticky="NSEW")

def novo_arquivo():
    if messagebox.askokcancel("Tem certeza?", "Você apagara todo contêudo atual para gerar um novo arquivo"): 
        caixa_de_texto.delete('1.0', 'end')
        atualiza_diretorio_atual(None)

def fecha_janela():
    if messagebox.askokcancel("Tem certeza?", "Você deseja salvar antes de sair?"):
        salvar_arquivo()
        janela.destroy()
    else:
        janela.destroy()


def salvar_arquivo():

    arquivo_selecionado = filedialog.asksaveasfilename(defaultextension='.txt')

    if arquivo_selecionado:
        with open(arquivo_selecionado, 'w') as arquivo_texto:
            arquivo_texto.write(caixa_de_texto.get('1.0', END))
        atualiza_diretorio_atual(arquivo_atual)

def salvar_arquivo_atual():
    global arquivo_atual
    if arquivo_atual:
        with open(arquivo_atual, 'w') as arquivo_texto:
            arquivo_texto.write(caixa_de_texto.get('1.0', END))
    else:
        arquivo_selecionado = filedialog.asksaveasfilename(defaultextension='.txt')
    
    if arquivo_selecionado:
        with open(arquivo_selecionado, 'w') as arquivo_texto:
            arquivo_texto.write(caixa_de_texto.get('1.0', END))
        
    
    arquivo_atual = arquivo_selecionado

def abrir_arquivo():
    global arquivo_atual
    arquivo_selecionado = filedialog.askopenfilename()

    if arquivo_selecionado:
        with open(arquivo_selecionado, 'r') as arquivo_texto:
            conteudo = arquivo_texto.read()
            caixa_de_texto.delete('1.0', END)
            caixa_de_texto.insert(END, conteudo)

    arquivo_atual = arquivo_selecionado

janela.protocol("WM_DELETE_WINDOW", fecha_janela)

janela.mainloop()

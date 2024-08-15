import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Cadastro de Funcionários")
        
        self.lbl_nome = tk.Label(self.janela, text='Nome:')
        self.lbl_nome.grid(row=0, column=0, sticky=tk.W)
        self.ent_nome = tk.Entry(self.janela, width=30)
        self.ent_nome.grid(row=0, column=1)
        self.lbl_email = tk.Label(self.janela, text='Email:')
        self.lbl_email.grid(row=1, column=0, sticky=tk.W)
        self.ent_email = tk.Entry(self.janela, width=30)
        self.ent_email.grid(row=1, column=1)
        
        universidade = ['UFAC', 'UNINORTE', 'IFAC']
        self.lbl_universidade = tk.Label(self.janela, text='Qual sua universidade:')
        self.lbl_universidade.grid(row=2, column=1)
        self.cmb_universidade = ttk.Combobox(self.janela, values=universidade)
        self.cmb_universidade.grid(row=3, column=1)
        
        self.var_java = tk.IntVar()
        self.var_javas = tk.IntVar()
        self.var_py = tk.IntVar()
        
        self.lbl_linguagens = tk.Label(self.janela, text='Tem experiência em qual Linguagens?', wraplength=150)
        self.lbl_linguagens.grid(row=0, column=2)
        self.chk_java = tk.Checkbutton(self.janela, variable=self.var_java, text='Java')
        self.chk_java.grid(row=1, column=2, sticky=tk.W)
        self.chk_javaScript = tk.Checkbutton(self.janela, variable=self.var_javas, text='JavaScript')
        self.chk_javaScript.grid(row=2, column=2, sticky=tk.W)
        self.chk_python = tk.Checkbutton(self.janela, variable=self.var_py, text='Python')
        self.chk_python.grid(row=3, column=2, sticky=tk.W)
        
        self.var_radio =tk.IntVar()
        self.lbl_exp = tk.Label(self.janela, text='Experiência com Programação Orientada a Objetos?', wraplength=150)
        self.lbl_exp.grid(row=0, column=3)
        self.radio_nenhuma = tk.Radiobutton(self.janela, text='Nenhuma', variable=self.var_radio, value=1)
        self.radio_nenhuma.grid(row=1, column=3, sticky=tk.W)
        self.radio_razoavel = tk.Radiobutton(self.janela, text='Razoável', variable=self.var_radio, value=2)
        self.radio_razoavel.grid(row=2, column=3, sticky=tk.W)
        self.radio_excelente = tk.Radiobutton(self.janela, text='Excelente', variable=self.var_radio, value=3)
        self.radio_excelente.grid(row=3, column=3, sticky=tk.W)
        
        self.btn_cadastrar = tk.Button(self.janela, text='Cadastrar', command=self.cadastrar)
        self.btn_cadastrar.grid(row=4, column=0, columnspan=5, sticky=tk.NSEW)
               
        colunas = ['nome', 'email', 'universidade', 'poo', 'exp']
        self.tvw_func = ttk.Treeview(self.janela, columns=colunas, show='headings')
        self.tvw_func.grid(row=5, column=0, columnspan=4)
        
        self.tvw_func.heading('nome', text='Nome')
        self.tvw_func.heading('email', text='Email')
        self.tvw_func.heading('universidade', text='Universidade')
        self.tvw_func.heading('exp', text='Experiência')
        self.tvw_func.heading('poo', text='Orientado a Objetos')
        
        self.tvw_func.column('nome', width=100)
        self.tvw_func.column('email', width=150)
        self.tvw_func.column('universidade', width=100)
        self.tvw_func.column('exp', width=100)
        self.tvw_func.column('poo', width=150)
        
        #Barra de Rolagem
        self.scb_barra = ttk.Scrollbar(self.janela,
                                       command=self.tvw_func.yview)
        self.scb_barra.grid(row=5, column=4, sticky=tk.NS)
        self.tvw_func.config(yscrollcommand=self.scb_barra.set)
        
    def cadastrar(self):
        nome = self.ent_nome.get()
        email = self.ent_email.get()
        universidade = self.cmb_universidade.get()
        
        poo = ''
        if self.var_radio.get() == 1:
            poo = 'Nenhuma'
        elif self.var_radio.get() == 2:
            poo = 'Razoavel'
        elif self.var_radio.get() == 3:
            poo = 'Excelente'
        
        
        exp = ''
        n = self.var_java.get(), self.var_javas.get(), self.var_py.get()
        if n[0] == 1:
            exp = 'Java' 
        if n[1] == 1:
            exp = 'JavaScript'
        if n[2] == 1:
            exp = 'Python'
        if n[0] == 1 and n[1] == 1:
            exp = 'Java e JavaScript' 
        if n[0] == 1 and n[2] == 1:
            exp = 'Java e Python'
        if n[1] == 1 and n[2] == 1:
            exp = 'JavaScript e Python'
        if n[0] == 1 and n[1] == 1 and n[2] == 1:
            exp = 'Java, JavaScript e Python'
        
        self.tvw_func.insert(parent='', index='end', values=[nome, email, universidade, exp, poo])
        
janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
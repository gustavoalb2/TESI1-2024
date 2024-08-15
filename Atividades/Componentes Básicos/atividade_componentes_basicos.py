import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Tela com Menu')
        self.janela.geometry('400x300')
        self.mnu_barra = tk.Menu(self.janela) #barra
        self.mnu_cadastro = tk.Menu(self.mnu_barra, tearoff=0) #item
        self.mnu_visualizar = tk.Menu(self.mnu_barra, tearoff=0) #item
        self.mnu_barra.add_cascade(label='Cadastro', menu=self.mnu_cadastro) #label
        # self.mnu_barra.add_cascade(label='Visualizar', menu=self.mnu_visualizar) #label
        self.mnu_cadastro.add_command(label='Novo', command=self.cadastro) #comandos
        # self.mnu_visualizar.add_command(label='Funcionários')

        self.janela.config(menu=self.mnu_barra) #adiciona na janela
        
    def cadastro(self):
        self.cadastro = tk.Toplevel(self.janela)
        self.cadastro.title('Novo Cadastro')
        self.lbl = tk.Label(self.cadastro, text='Nome')
        self.lbl.grid(row=0, column=0)
        self.ent_nome = tk.Entry(self.cadastro)
        self.ent_nome.grid(row=0, column=1)
        self.lbl_data = tk.Label(self.cadastro, text='Data de Nascimento')
        self.lbl_data.grid(row=1, column=0)
        self.ent_data = tk.Entry(self.cadastro)
        self.ent_data.grid(row=1, column=1)
        self.lbl_cpf = tk.Label(self.cadastro, text='CPF')
        self.lbl_cpf.grid(row=2, column=0)
        self.ent_cpf = tk.Entry(self.cadastro)
        self.ent_cpf.grid(row=2, column=1)
        self.lbl_email = tk.Label(self.cadastro, text='E-mail')
        self.lbl_email.grid(row=3, column=0)
        self.ent_email = tk.Entry(self.cadastro)
        self.ent_email.grid(row=3, column=1)
        self.lbl_telefone = tk.Label(self.cadastro, text='Telefone')
        self.lbl_telefone.grid(row=4, column=0)
        self.ent_telefone = tk.Entry(self.cadastro)
        self.ent_telefone.grid(row=4, column=1)
        self.btn_salvar = tk.Button(self.cadastro, text='Salvar', command=self.salvar)
        self.btn_salvar.grid(row=5, column=1)
        
    def salvar(self):
        self.nome = self.ent_nome.get()
        self.data = self.ent_data.get()
        self.cpf = self.ent_cpf.get()
        self.email = self.ent_email.get()
        self.telefone = self.ent_telefone.get()
        self.tvw = ttk.Treeview(self.cadastro, columns=('Nome', 'Data de Nascimento', 'CPF', 'E-mail', 'Telefone'), show='headings')
        self.tvw.grid(row=6, column=0, columnspan=2)
        
        self.tvw.heading('Nome', text='Nome')
        self.tvw.heading('Data de Nascimento', text='Data de Nascimento')
        self.tvw.heading('CPF', text='CPF')
        self.tvw.heading('E-mail', text='E-mail')
        self.tvw.heading('Telefone', text='Telefone')
        
        self.tvw.column('Nome', minwidth=0, width=100)
        self.tvw.column('Data de Nascimento', minwidth=0, width=100)
        self.tvw.column('CPF', minwidth=0, width=100)
        self.tvw.column('E-mail', minwidth=0, width=100)
        self.tvw.column('Telefone', minwidth=0, width=100)
                
        self.tvw.insert('', 'end', values=(self.nome, self.data, self.cpf, self.email, self.telefone))
        
        
        # print(f'Nome: {self.nome}\nData de Nascimento: {self.data}\nCPF: {self.cpf}\nE-mail: {self.email}\nTelefone: {self.telefone}')


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
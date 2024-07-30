import tkinter as tk

class Tela:    
    def mostrar(self):
        if self.var_opcoes.get() == 1:
            self.cbt_IA.config(state='normal')
            self.cbt_IOT.config(state='normal')
            self.cbt_VR.config(state='normal')
        else:
            self.cbt_IA.config(state='disabled')
            self.cbt_IOT.config(state='disabled')
            self.cbt_VR.config(state='disabled')
        
    def __init__(self, master):
        self.janela = master
        self.janela.title('Questão1')
        self.janela.geometry('400x400')
        
        self.lbl_email = tk.Label(self.janela, text='Email')
        self.lbl_email.pack()
        
        self.ent_nome = tk.Entry(self.janela)
        self.ent_nome.pack()
        
        self.lbl_senha = tk.Label(self.janela, text='Senha')
        self.lbl_senha.pack()
        
        self.ent_senha = tk.Entry(self.janela)
        self.ent_senha.pack()
        
        self.var_opcoes = tk.IntVar()
        self.cbt_opcoes = tk.Checkbutton(self.janela,
                                         text='Desejo receber notificações',
                                         selectcolor='',
                                         variable=self.var_opcoes,
                                         command=self.mostrar)
        self.cbt_opcoes.pack()
        
        self.lb1_escolha = tk.Label(self.janela)
        self.lb1_escolha.pack()

        self.cbt_IA = tk.Checkbutton(self.janela, text='Sobre IA',
                                     selectcolor='grey',
                                     state='disabled')
        self.cbt_IA.pack()
        
        self.cbt_IOT = tk.Checkbutton(self.janela, text='Sobre IoT',
                                      selectcolor='grey',
                                      state='disabled')
        self.cbt_IOT.pack()
        
        self.cbt_VR = tk.Checkbutton(self.janela, text='Sobre VR',
                                     selectcolor='grey',
                                     state='disabled')
        self.cbt_VR.pack()
        
        self.bt1_ok = tk.Button(self.janela, text='Ok')
        self.bt1_ok.pack()

app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()

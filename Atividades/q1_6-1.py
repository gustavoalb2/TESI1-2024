import tkinter as tk

class Tela:
    def idade(self):
        nome = self.ent_nome.get()
        dia = int(self.ent_dia.get())
        mes = int(self.ent_mes.get())
        ano = int(self.ent_ano.get())
        
        dia_atual = 23
        mes_atual = 7
        ano_atual = 2024
        
        ano_idade = ano_atual - ano
        dia_idade = dia_atual - dia
        mes_idade = mes_atual - mes
        
        
    
        if mes > 7:
            idade -= 1
        elif mes == 7:
            if dia > 23:
                idade -= 1
        
        self.lbl_idade = tk.Label(self.janela, text=f'{nome} tem {idade} anos, {(dia_atual+30) - dia} dias, {mes-(mes_atual-12)} meses')
        self.lbl_idade.pack()
        
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x400')
        self.lbl_nome = tk.Label(self.janela, text='Nome')
        self.ent_nome = tk.Entry(self.janela)
        self.lbl_nome.pack()
        self.ent_nome.pack()
        self.lbl_dia = tk.Label(self.janela, text='Dia')
        self.lbl_dia.pack()
        self.ent_dia = tk.Entry(self.janela)
        self.ent_dia.pack()
        self.lbl_mes = tk.Label(self.janela, text='Mês')
        self.lbl_mes.pack()
        self.ent_mes = tk.Entry(self.janela)
        self.ent_mes.pack()
        self.lbl_ano = tk.Label(self.janela, text='Ano')
        self.lbl_ano.pack()
        self.ent_ano = tk.Entry(self.janela)
        self.ent_ano.pack()
        
        self.btn = tk.Button(self.janela, text='OK', command=self.idade)
        self.btn.pack()
        
janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
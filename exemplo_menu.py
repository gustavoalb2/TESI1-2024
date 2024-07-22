import tkinter as tk

class Tela:
    def abrir(self):
        lista = ['Uva', 'Maçã', 'Manga']
        valores = [i for i in range(1,13)]
        self.spb_meses = tk.Spinbox(self.janela, values=valores, wrap=True, state="readonly", fg='black')
        self.spb_meses.pack()
        self.scl_dias = tk.Scale(self.janela, from_=1, to=31)
        self.scl_dias.pack()

    
    def __init__(self, master):
        self.janela = master
        self.menu_barra = tk.Menu(self.janela)
        self.menu_arquivo = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_editar = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Arquivo', menu=self.menu_arquivo)
        self.menu_barra.add_cascade(label='Editar', menu=self.menu_editar)
        self.menu_arquivo.add_command(label='Salvar')
        self.menu_arquivo.add_separator()
        self.menu_arquivo.add_command(label='Abrir', command=self.abrir)
        self.menu_editar.add_command(label='Copiar')
        self.menu_editar.add_separator()
        self.menu_editar.add_command(label='Colar')
        
        self.janela.config(menu=self.menu_barra)
        
janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
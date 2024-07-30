import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x200')
        lbl1 = tk.Label(self.janela, text='TOPO', bg='yellow')
        lbl1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        lbl4 = tk.Label(self.janela, text='ESQUERDA', bg='blue')
        lbl4.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        lbl2 = tk.Label(self.janela, text='DIREITA', bg='red')
        lbl2.pack(side=tk.LEFT, fill=tk.X, expand=True)
        lbl3 = tk.Label(self.janela, text='RODAPÉ', bg='green')
        lbl3.pack(side=tk.RIGHT, fill=tk.X, expand=True)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
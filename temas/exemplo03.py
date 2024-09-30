import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = ttk.Button(self.janela, text='Teste de Tema', bootstyle=SUCCESS)
        self.btn.pack()
        self.btn2 = ttk.Button(self.janela, text='Teste de Tema', bootstyle="info-outline")
        self.btn2.pack()
janela = ttk.Window(themename="litera") #tk.Tk()
app = Tela(janela)
janela.mainloop()
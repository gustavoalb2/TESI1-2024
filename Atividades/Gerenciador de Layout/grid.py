import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x200')
        self.janela.title('Grid')
        self.janela.configure()
        lbl1 = tk.Button(self.janela, text='1', width=4, height=2)
        lbl1.grid(row=1, column=1, columnspan=4, padx=1, pady=1)
        lbl2 = tk.Button(self.janela, text='2', width=4, height=2)
        lbl2.grid(row=2, column=1, columnspan=2, padx=1, pady=1)
        lbl3 = tk.Button(self.janela, text='3', width=4, height=2)
        lbl3.grid(row=2, column=2, columnspan=2, padx=1, pady=1)
        lbl4 = tk.Button(self.janela, text='4', width=4, height=2)
        lbl4.grid(row=3, column=1, padx=1, pady=1)
        lbl5 = tk.Button(self.janela, text='5', width=4, height=2)
        lbl5.grid(row=3, column=2, padx=1, pady=1)
        lbl6 = tk.Button(self.janela, text='6', width=4, height=2)
        lbl6.grid(row=3, column=3, padx=1, pady=1)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
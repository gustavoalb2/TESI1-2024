import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x320')
        self.janela.title('Calculadora Simples')
        self.janela.resizable(width=False, height=False)
        self.janela.config(bg='#343434')
        
        self.ent_valor = tk.Entry(self.janela, width=30, bg='#343434', fg='white', border=5)
        self.ent_valor.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
        
        self.btn1 = tk.Button(self.janela, text='1', bg='#343434', fg='white')
        self.btn1.grid(row=1, column=1, ipadx=13, ipady=13, pady=2)
        self.btn2 = tk.Button(self.janela, text='2', bg='#343434', fg='white')
        self.btn2.grid(row=1, column=2, ipadx=13, ipady=13, pady=2)
        self.btn3 = tk.Button(self.janela, text='3', bg='#343434', fg='white')
        self.btn3.grid(row=1, column=3, ipadx=13, ipady=13, pady=2)
        self.btnMult = tk.Button(self.janela, text='+', bg='#343434', fg='white')
        self.btnMult.grid(row=1, column=4, ipadx=13, ipady=13, pady=2)
        
        self.btn4 = tk.Button(self.janela, text='4', bg='#343434', fg='white')
        self.btn4.grid(row=2, column=1, ipadx=13, ipady=13, pady=2)
        self.btn5 = tk.Button(self.janela, text='5', bg='#343434', fg='white')
        self.btn5.grid(row=2, column=2, ipadx=13, ipady=13, pady=2)
        self.btn6 = tk.Button(self.janela, text='6', bg='#343434', fg='white')
        self.btn6.grid(row=2, column=3, ipadx=13, ipady=13, pady=2)
        self.btnMenos = tk.Button(self.janela, text='-', bg='#343434', fg='white')
        self.btnMenos.grid(row=2, column=4, ipadx=14, ipady=14, pady=2)
        
        self.btn7 = tk.Button(self.janela, text='7', bg='#343434', fg='white')
        self.btn7.grid(row=3, column=1, ipadx=13, ipady=13, pady=2)
        self.btn8 = tk.Button(self.janela, text='8', bg='#343434', fg='white')
        self.btn8.grid(row=3, column=2, ipadx=13, ipady=13, pady=2)
        self.btn9 = tk.Button(self.janela, text='9', bg='#343434', fg='white')
        self.btn9.grid(row=3, column=3, ipadx=13, ipady=13, pady=2)
        self.btnMais = tk.Button(self.janela, text='*', bg='#343434', fg='white')
        self.btnMais.grid(row=3, column=4, ipadx=14, ipady=14, pady=2)
        
        self.btn0 = tk.Button(self.janela, text='0', bg='#343434', fg='white')
        self.btn0.grid(row=4, column=1, ipadx=13, ipady=13, pady=2)
        self.btnDiv = tk.Button(self.janela, text='/', bg='#343434', fg='white')
        self.btnDiv.grid(row=4, column=4, ipadx=14, ipady=14, pady=2)
        self.btnDot = tk.Button(self.janela, text='.', bg='#343434', fg='white')
        self.btnDot.grid(row=4, column=2, ipadx=14, ipady=13, pady=2)
        self.btnClear = tk.Button(self.janela, text='C', bg='#343434', fg='white')
        self.btnClear.grid(row=4, column=3, ipadx=13, ipady=13, pady=2)
        
        self.btnIgual = tk.Button(self.janela, text='=', bg='green')
        self.btnIgual.grid(row=5, column=1, columnspan=4, ipadx=92, ipady=15)
    

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
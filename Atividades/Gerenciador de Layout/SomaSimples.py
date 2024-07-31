import tkinter as tk
class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x70')
        self.janela.title('Soma Simples')
        self.janela.configure()
        
        janela.title('Soma Simples')
        janela.geometry('200x70')
        self.num1 = tk.IntVar()
        self.num2 = tk.IntVar()
                
        self.lbl1 = tk.Label(self.janela, text='Número 1:',)
        self.lbl1.grid(row=0, column=0)
        self.ent_num1 = tk.Entry(self.janela, textvariable=self.num1)
        self.ent_num1.grid(row=0, column=1)
        self.lbl2 = tk.Label(self.janela, text='Número 2:')
        self.lbl2.grid(row=1, column=0)
        self.ent_num2 = tk.Entry(self.janela, textvariable=self.num2)
        self.ent_num2.grid(row=1, column=1)
        self.btn_soma = tk.Button(self.janela, text='Somar>>>', width=5, command=self.soma)
        self.btn_soma.grid(row=2, column=0, ipadx=15)
        self.ent_result = tk.Entry(self.janela, width=10)
        self.ent_result.grid(row=2, column=1)
        
    def soma(self):
        n1 = self.num1.get()
        n2 = self.num2.get()
        result = n1 + n2
        self.ent_result.delete(0, tk.END)
        self.ent_result.insert(0, result)
        
janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
import tkinter as tk

class Tela:
    def clicou(self):    
        if self.var_argentina.get() == 0 or self.var_brasil.get() == 0:
            self.lbl_mostrar['text'] = ''
        if self.var_brasil.get() == 1 and self.var_argentina.get() == 0:
            self.lbl_mostrar['text'] = 'Nunca será'
        if self.var_brasil.get() == 0 and self.var_argentina.get() == 1:
            self.lbl_mostrar['text'] = 'Campeão'
        if self.var_brasil.get() == 1:
                    self.lbl_mostrar['text'] = 'Nunca será'
        if self.var_argentina.get() == 1:
                    self.lbl_mostrar.config(text='Campeão')
        
              
    def __init__(self, master):        
        self.janela = master
        self.var_brasil = tk.IntVar()
        self.var_argentina = tk.IntVar()
        
        self.cbt_brasil = tk.Checkbutton(self.janela, text='Brasil', variable=self.var_brasil, command=self.clicou)
        self.cbt_argentina = tk.Checkbutton(self.janela, text='Argentina', command=self.clicou, variable=self.var_argentina)        
        self.cbt_brasil.pack()
        self.cbt_argentina.pack()
        self.lbl_mostrar = tk.Label(self.janela, foreground='black')
        self.lbl_mostrar.pack()
        
janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x200')
        self.janela.resizable(width=False, height=False)

        lbl1 = tk.Label(self.janela, text='Red', bg='red')
        lbl1.pack(fill=tk.X, ipady=7)
        lbl2 = tk.Label(self.janela, text='Green', bg='green')
        lbl2.pack(fill=tk.X, ipady=7)
        lbl3 = tk.Label(self.janela, text='Blue', bg='blue')
        lbl3.pack(fill=tk.X, ipady=7)

        lbl4 = tk.Label(self.janela, text='Gray', bg='gray', fg='white')
        lbl4.pack(fill=tk.Y, ipadx=5, side=tk.LEFT)
        lbl5 = tk.Label(self.janela, text='Gray', bg='gray', fg='white')
        lbl5.pack(fill=tk.Y, ipadx=5, side=tk. RIGHT)

        frame = tk.Frame(self.janela)
        frame.pack(fill=tk.X)
        lbl7 = tk.Label(frame, text='Cyan', bg='cyan')
        lbl7.grid(row=0, column=0, ipadx=16, ipady=8)
        lbl8 = tk.Label(frame, text='Magenta', bg='magenta')
        lbl8.grid(row=0, column=1, ipadx=16, ipady=8)
        lbl9 = tk.Label(frame, text='Yellow', bg='yellow')
        lbl9.grid(row=0, column=2, ipadx=16, ipady=8)

        lbl10 = tk.Label(self.janela, text='Black', bg='black', fg='white')
        lbl10.pack(fill=tk.X, ipady=50, side=tk.BOTTOM)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
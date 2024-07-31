import tkinter as tk

janela = tk.Tk()
janela.title('Calculadora simples')
janela.resizable(width=False, height=False)
janela.config(bg='#343434')
ent_valor = tk.Entry(janela, bg='#343434', fg='white', border=5)
ent_valor.pack(fill=tk.X, padx=5, pady=5)

frame = tk.Frame(janela, bg='#343434')
frame.pack()

btn1 = tk.Button(frame, text='1', bg='#343434', fg='white')
btn1.grid(row=2, column=0, ipadx=13, ipady=13, pady=2)
btn2 = tk.Button(frame, text='2', bg='#343434', fg='white')
btn2.grid(row=2, column=1, ipadx=13, ipady=13, pady=2)
btn3 = tk.Button(frame, text='3', bg='#343434', fg='white')
btn3.grid(row=2, column=2, ipadx=13, ipady=13, pady=2)
btnMult = tk.Button(frame, text='*', bg='#343434', fg='white')
btnMult.grid(row=2, column=3, ipadx=13, ipady=13, pady=2)

btn4 = tk.Button(frame, text='4', bg='#343434', fg='white')
btn4.grid(row=1, column=0, ipadx=13, ipady=13, pady=2)
btn5 = tk.Button(frame, text='4', bg='#343434', fg='white')
btn5.grid(row=1, column=1, ipadx=13, ipady=13, pady=2)
btn6 = tk.Button(frame, text='6', bg='#343434', fg='white')
btn6.grid(row=1, column=2, ipadx=13, ipady=13, pady=2)
btnMenos = tk.Button(frame, text='-', bg='#343434', fg='white')
btnMenos.grid(row=1, column=3, ipadx=13, ipady=13, pady=2)

btn7 = tk.Button(frame, text='7', bg='#343434', fg='white')
btn7.grid(row=0, column=0, ipadx=13, ipady=13, pady=2)
btn8 = tk.Button(frame, text='8', bg='#343434', fg='white')
btn8.grid(row=0, column=1, ipadx=13, ipady=13, pady=2)
btn9 = tk.Button(frame, text='9', bg='#343434', fg='white')
btn9.grid(row=0, column=2, ipadx=13, ipady=13, pady=2)
btnMais = tk.Button(frame, text='+', bg='#343434', fg='white')
btnMais.grid(row=0, column=3, ipadx=12, ipady=13, pady=2)

btn0 = tk.Button(frame, text='0', bg='#343434', fg='white')
btn0.grid(row=3, column=0, ipadx=13, ipady=13, pady=2)
btnDiv = tk.Button(frame, text='/', bg='#343434', fg='white')
btnDiv.grid(row=3, column=3, ipadx=13, ipady=13, pady=2)
btnDot = tk.Button(frame, text='.', bg='#343434', fg='white')
btnDot.grid(row=3, column=1, ipadx=14, ipady=13, pady=2)
btnClear = tk.Button(frame, text='C', bg='#343434', fg='white')
btnClear.grid(row=3, column=2, ipadx=13, ipady=13, pady=2)

btnIgual = tk.Button(frame, text='=', bg='green')
btnIgual.grid(row=4, column=0, columnspan=4, ipadx=92, ipady=15)

 

janela.mainloop()
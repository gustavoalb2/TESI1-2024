import tkinter as tk
from tkinter import messagebox

# Função para calcular se um ano é bissexto
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Função para calcular a idade
def calculate_age():
    try:
        # Obter valores de entrada
        name = entry_name.get()
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        
        # Data atual (substituir pelos valores reais se necessário)
        current_day = 23
        current_month = 7
        current_year = 2024
        
        # Calcular idade em anos, meses e dias
        age_years = current_year - year
        age_months = current_month - month
        age_days = current_day - day
        
        if age_days < 0:
            age_months -= 1
            age_days += 30  # Aproximando para 30 dias em um mês
        
        if age_months < 0:
            age_years -= 1
            age_months += 12
        
        # Calcular idade em dias
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap_year(year):
            days_in_months[1] = 29
        
        total_days = age_years * 365 + sum(days_in_months[:current_month-1]) + current_day
        total_days -= (sum(days_in_months[:month-1]) + day)
        for past_year in range(year, current_year):
            if is_leap_year(past_year):
                total_days += 1

        # Exibir resultado
        result_text = f"Idade: {age_years} anos, {age_months} meses e {age_days} dias ou {total_days} dias"
        label_result.config(text=result_text)
    
    except ValueError:
        messagebox.showerror("Erro de entrada", "Por favor, insira valores válidos.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Idade")

# Criar e posicionar os widgets
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Dia de Nascimento:").grid(row=1, column=0, padx=10, pady=10)
entry_day = tk.Entry(root)
entry_day.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Mês de Nascimento:").grid(row=2, column=0, padx=10, pady=10)
entry_month = tk.Entry(root)
entry_month.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Ano de Nascimento:").grid(row=3, column=0, padx=10, pady=10)
entry_year = tk.Entry(root)
entry_year.grid(row=3, column=1, padx=10, pady=10)

button_calculate = tk.Button(root, text="Calcular Idade", command=calculate_age)
button_calculate.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Iniciar o loop principal
root.mainloop()

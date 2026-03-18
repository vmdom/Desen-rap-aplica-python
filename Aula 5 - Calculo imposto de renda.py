import tkinter as tk
from tkinter import messagebox

class CalculadoraIR:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Imposto de Renda")

        # Criando os widgets
        self.label_salario = tk.Label(master, text="Salário Bruto:")
        self.label_salario.pack()

        self.entry_salario = tk.Entry(master)
        self.entry_salario.pack()

        self.label_inss = tk.Label(master, text="Desconto INSS:")
        self.label_inss.pack()

        self.entry_inss = tk.Entry(master)
        self.entry_inss.pack()

        self.calcular_button = tk.Button(master, text="Calcular IR", command=self.calcular_desconto)
        self.calcular_button.pack()

        self.resultado_label = tk.Label(master, text="")
        self.resultado_label.pack()

    def calcular_desconto(self):
        try:
            salario_bruto = float(self.entry_salario.get())
            desconto_inss = float(self.entry_inss.get())

            salario_base = salario_bruto - desconto_inss

            if salario_base <= 1903.98:
                desconto_ir = 0
            elif salario_base <= 2826.65:
                desconto_ir = (salario_base * 0.075) - 142.8
            elif salario_base <= 3751.05:
                desconto_ir = (salario_base * 0.15) - 354.8
            elif salario_base <= 4664.68:
                desconto_ir = (salario_base * 0.225) - 636.13
            else:
                desconto_ir = (salario_base * 0.275) - 869.36

            self.resultado_label.config(text=f"Desconto IR: R${desconto_ir:.2f}")

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criando a janela principal e instanciando a calculadora
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraIR(root)
    root.mainloop()

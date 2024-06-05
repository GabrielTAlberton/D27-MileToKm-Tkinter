from tkinter import *

FONTE = ("Arial", 14, "bold")

tela = Tk()
tela.title("Conversor Milha para Kilometro")
tela.config(padx=20, pady=20)

# textos estáticos #

# milhas
mile_label = Label(text="Milhas", font=FONTE)
mile_label.grid(column=2, row=0)

# Km
km_label = Label(text="Km", font=FONTE)
km_label.grid(column=2, row=1)

# igual a
igual_label = Label(text="é igual a", font=FONTE)
igual_label.grid(column=0, row=1)

# textos variáveis #

# resultado em Km
valor_km = 0
valor_km_label = Label(text=valor_km, font=FONTE)
valor_km_label.grid(column=1, row=1)

# botoes #

# botao calcular
def calcular_km():
    milhas = round(float(milhas_input.get()) * 1.60934)
    valor_km_label.config(text=f"{milhas}")


calcular = Button(text="Calcular", command=calcular_km)
calcular.grid(column=1, row=2)

# campos #

# campo milhas
milhas_input = Entry(width=8)
milhas_input.grid(column=1, row=0)





tela.mainloop()

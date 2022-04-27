from tkinter import *
from tkinter.ttk import *
from time import strftime
# Função para definir horário
def hora():
    agora = strftime('%H:%M:%S %p')
    lbl1.config(text=agora)
    lbl1.after(1000, hora)
# Função para definir data
def data():
    hoje = strftime('%d/%m/%y')
    lbl2.config(text=hoje)
    lbl2.after(1000, hoje)
# Janela
main = Tk()
main.title('Relógio')
# Personalização
main.configure(background="black")
main.resizable(False, False)
lbl1 = Label(main, font=('arial', 30, 'bold'), background='black', foreground='white')
lbl2 = Label(main, font=('arial', 30, 'bold'), background='black', foreground='white')
# Posição
lbl1.pack(side=TOP)
lbl2.pack(side=TOP)
hora()
data()
main.mainloop()

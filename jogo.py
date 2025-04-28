from tkinter import *
import random
def verificar_palpite(resultado):
    palpite = int(caixatexto.get())
    if palpite == numero_secreto:
        resultado ["text"] = "Parabéns! Você acertou"
        resultado.pack(pady=100)
    else :
        resultado ["text"] = "Errou! Tente novamente."
        resultado.pack(pady=100)
numero_secreto = random.randint(0,10)

janela = Tk()
janela.title("Jogo")
janela.geometry("450x400")
janela.resizable(False,False)
instrucoes = Label(janela,text = "Digite um número de 1 a 10")
instrucoes.pack(pady = 20)
caixatexto = Entry(janela)
caixatexto.pack(padx=10,pady=50)
resultado = Label(janela, text="a")
divi = Button(janela,text="ENVIAR",pady=14,padx=14,bd=4,command=lambda: verificar_palpite(resultado))
divi.place(x=180,y=170)
janela.mainloop()
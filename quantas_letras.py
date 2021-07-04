from tkinter import *


def conta_string(texto):
    ja_foi = []
    contadas = dict()
    for letra in texto:
        if letra not in ja_foi:
            ja_foi.append(letra)
            contadas[letra] = texto.count(letra)
    contadas.pop('\n')
    texto_resposta['text'] = ''
    for i, v in contadas.items():
        texto_resposta['text'] += f'Letra: {i}, Vezes: {v}\n'


def segura_ai():
    mensagem = texto.get('1.0', END)
    conta_string(mensagem)


janela = Tk()
janela.geometry('220x550')
janela.configure(background='#dde')
janela.title('Quantas Letras')

mensagem_inicial = Label(janela, text='DIGITE O TEXTO', background='#dde', foreground='#009', anchor='w')
mensagem_inicial.place(x=60, y=10, width=100, height=20)

texto = Text(janela)
texto.place(x=10, y=30, width=200, height=100)


botao = Button(janela, text='Contar agora', command=segura_ai)
botao.place(x=35, y=145, width=150, height=50)

texto_resposta = Label(janela, text='Esperando clique no botão')
texto_resposta.place(x=10, y=220, width=200, height=300)


janela.mainloop()

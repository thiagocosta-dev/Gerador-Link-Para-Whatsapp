from tkinter import *
import clipboard

#  Criando janela = Tamanho e título
janela = Tk()
janela.geometry('480x170')
janela.title('# Gerador de Link para Whatsapp #')


#  Função para gerar link
def gerar_link():
    global link # Colocando a variável local Link como Global (Obs: não é melhor forma de fazer)
    num = inputtxt.get(1.0, "end-1c").strip().replace(' ', '').replace('-', '').replace('+55', '')
    parte_link = 'https://api.whatsapp.com/send?phone=55'
    link = parte_link + num
    lbl.config(text="Link Gerado: " + link)


#  Função para copiar link gerado
def copiar_link():
    from tkinter import messagebox
    messagebox.showinfo(title='Gerador de Link', message='Link copiado com sucesso!')
    global link
    return clipboard.copy(link)


#  Tamanho da janela input
inputtxt = Text(janela, height=2, width=20)
inputtxt.pack()

#  Botão para gerar link
botao_imprimir = Button(janela, text="Gerar Link", command=gerar_link)
botao_imprimir.pack()

#  Botão copiar link
botao_copiar = Button(janela, text="Copiar Link", command=copiar_link)
botao_copiar.pack()


#  Texto de saída
lbl = Label(janela, text="")
lbl.pack()


janela.mainloop()

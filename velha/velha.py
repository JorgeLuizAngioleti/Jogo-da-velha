import turtle
from poderes import animacao
janela = turtle.Screen()
janela.title('Jogo Py')
janela.setup(1280,720)

janela.tracer(0)
def inicio():
  import tela


janela.listen()
janela.onkey(inicio, "Return")
janela.mainloop()

import turtle
from poderes import animacao

janela = turtle.Screen()
janela.title('Jogo Py')
janela.setup(1280, 720)
janela.bgcolor('black')
janela.register_shape('x.gif')
janela.register_shape('oo.gif')
janela.register_shape('o.gif')
janela.register_shape('xx.gif')
janela.register_shape('menu.gif')
janela.register_shape('m2.gif')
janela.register_shape('jogo.gif')
janela.register_shape('jg.gif')
janela.tracer(0)

"""Jogo da velha com turtle """


class Escreve(turtle.Turtle):
    def __init__(self, texto, x, y):
        turtle.Turtle.__init__(self)
        self.speed()
        self.up()
        self.color('black')
        self.hideturtle()  # esconde//showturtle()mostra
        self.setposition(x, y)
        self.style = ('arial', 30, 'italic')
        self.write(texto, move=True, align="center", font=(self.style))


class Casa(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.up()
        self.speed(0)
        self.shape('square')
        self.color('white', 'blue')
        self.shapesize(10, 10, 5)  # tamanho em pix, 5 é o contorno

    def click(self):
        janela.listen()
        self.onclick(self.muda, 1)

    def muda(self, x, y):
        global vez
        if self.shape() == 'square':
            if vez == 'x':
                self.shape('x.gif')
                vez = 'o'
            elif vez == 'o':
                self.shape('o.gif')
                vez = 'x'
            self.insere()

    def insere(self):
        "inverte a vez e insere na lista os campos corretamente"
        global lista
        self.insere = 0
        if vez == 'x':
            self.insere = 'o'
        else:
            self.insere = 'x'
        if (self.pos()) == (-210, 210):
            lista[0][0] = self.insere
        elif (self.pos()) == (0, 210):
            lista[0][1] = self.insere
        elif (self.pos()) == (210, 210):
            lista[0][2] = self.insere
        elif (self.pos()) == (-210, 0):
            lista[1][0] = self.insere
        elif (self.pos()) == (0, 0):
            lista[1][1] = self.insere
        elif (self.pos()) == (210, 0):
            lista[1][2] = self.insere
        elif (self.pos()) == (-210, -210):
            lista[2][0] = self.insere
        elif (self.pos()) == (0, -210):
            lista[2][1] = self.insere
        elif (self.pos()) == (210, -210):
            lista[2][2] = self.insere
    # print(lista)


def vitoria(jogador):
    if lista[0][0] == jogador and lista[0][1] == jogador and lista[0][2] == jogador:
        return True
    elif lista[1][0] == jogador and lista[1][1] == jogador and lista[1][2] == jogador:
        return True
    elif lista[2][0] == jogador and lista[2][1] == jogador and lista[2][2] == jogador:
        return True
    elif lista[0][0] == jogador and lista[1][0] == jogador and lista[2][0] == jogador:
        return True
    elif lista[0][1] == jogador and lista[1][1] == jogador and lista[2][1] == jogador:
        return True
    elif lista[0][2] == jogador and lista[1][2] == jogador and lista[2][2] == jogador:
        return True
    elif lista[0][0] == jogador and lista[1][1] == jogador and lista[2][2] == jogador:
        return True
    elif lista[2][0] == jogador and lista[1][1] == jogador and lista[0][2] == jogador:
        return True
    else:
        return False


def inicio():
    global vez
    global lista
    vez = 'x'
    lista = [[2, 2, 2],
             [2, 2, 2],
             [2, 2, 2]]
    jogar(lista, vez)


janela.listen()
janela.onkey(inicio, "a")
# escreve antes de iniciar o jogo
'''
Escreve('Jogo da velha', 0, 275)
Escreve(' Aperte a para começar o jogo.', 0, 200)
'''

janela.bgpic('menu.gif')


def jogar(l, v):
    janela.reset()
    fundo = animacao.Animacao()
    fundo.animacao()
    texto = Escreve('Jogo da velha', 0, 315)
    x = [-210, 0, 210]
    y = [210, 0, -210]
    instancias = []
    for c in x:
        for l in y:
            n = Casa()
            n.goto(l, c)
            instancias.append(n)
    aberta = True
    while aberta:
        janela.update()
        for i in instancias:
            i.click()
        if vitoria('x'):
            Escreve('Jogador X venceu!', 0, -355)
            janela.update()
            aberta = False


        elif vitoria('o'):
            # escreve1.clear()
            Escreve('Jogador O venceu!', 0, -355)
            janela.update()
            aberta = False


janela.mainloop()
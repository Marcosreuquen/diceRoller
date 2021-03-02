from random import *
from tkinter import *
from tkinter import messagebox as mb

#----------------------------------Ventana
ventana = Tk()
ventana.geometry('650x650')
ventana.title('Lanza el dado...')
ventana.config(bg='white smoke')
ventana.iconbitmap('C:\\Users\\Usuario\\Desktop\\Programacion\\python\\projects\\diceroller\\more.ico')
#----------------------------------Variables
global dado
dado = 0
#----------------------------------Funciones

def diceRoller():
    global dado
    diceNumber = randrange(1,7)
    numDado = diceNumber
    if numDado == 0:
        Imagen['file'] = 'C:\\Users\\Usuario\\Desktop\\Programacion\\python\\projects\\diceroller\\more.png'
    elif numDado == 1:
        Imagen['file'] = 'C:\\Users\\Usuario\\Desktop\\Programacion\\python\\projects\\diceroller\\diceOne.png'
    elif numDado == 2:
        Imagen['file'] = 'C:\\Users\\Usuario\\Desktop\\Programacion\\python\\projects\\diceroller\\diceTwo.png'
    elif numDado == 3:
        Imagen['file'] = 'C:\\Users\\Usuario\\Desktop\\Programacion\\python\\projects\\diceroller\\diceThree.png'
    elif numDado == 4:
        Imagen['file'] = 'C:\\Users\\Usuario\\Desktop\\Programacion\\python\\projects\\diceroller\\diceFour.png'
    elif numDado == 5:
        Imagen['file'] = 'C:\\Users\\Usuario\\Desktop\\Programacion\\python\\projects\\diceroller\\diceFive.png'
    elif numDado == 6:
        Imagen['file'] = 'C:\\Users\\Usuario\\Desktop\\Programacion\\python\\projects\\diceroller\\diceSix.png'
    dado = numDado

#----------------------------------Etiqueta de Bienvenida
welcome = Label(text= '¡Bienvenido y mucha suerte!', fg='black', bg='white smoke', font = ('Lucida Sans', 15, 'bold'))
welcome.pack(padx = 10, pady = 10)
#----------------------------------Botón
tirarDado = Button(ventana, bg='white', text= 'Tirar el dado', font = ('Roboto', 15, 'normal'), command = lambda: diceRoller())
tirarDado.pack(padx = 10, pady = 10)
#----------------------------------frane para imagen
Myframe = Frame(ventana)
Myframe.pack(fill="both",expand=False, padx=10, pady=10)

#----------------------------------imagen en frame
Imagen = PhotoImage()
Labelimg = Label(Myframe, image = Imagen, bg='white smoke')
Labelimg.pack()    

ventana.mainloop()
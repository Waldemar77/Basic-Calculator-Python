'''
Created on 11/04/2020

@author: sergio
'''
from tkinter import *

#===============================================================================
# Esta Calculadora super básica tendrá la labor de resolver operaciones matemáticas
# muy básicas, siempre usando el orden lógico de cada operación por aparte.
#===============================================================================


#===============================================================================
# Estructura principal
#===============================================================================

root = Tk()
root.title("Calculadora Básica")
mainFrame = Frame(root, bg="black")
mainFrame.pack()

#===============================================================================
# variables
#===============================================================================

#Será la variable que muestre los numeros ingresados en el widget izquierdo
numIngreso = StringVar()

#Será la variable que muestre los numeros ingresados en el widget derecho
numResultado = StringVar()

#Será la lista que muestre el resumen de las operaciones realizadas
resumenOperacion = []

#Lista que captura cada tecla pulsada (números y operadores matemáticos)
capturaNumeros = []

#Será la lista que muestre el resumen de las operaciones realizadas en el widget superior
msmOperacion = StringVar()

#Permitirá saber qué tipo de operacón se está ejecutando para la toma de decisiones
operacion = 0

#Guarda el resultado de las funsiones matemáticas indicadas.
resultado = 0

#===============================================================================
# Pantalla de resumen de operaciones
#===============================================================================

resumResultado = Label(mainFrame, bg="black", fg="#04fced", textvariable=msmOperacion)
resumResultado.grid(row=1, column=1, columnspan=4, sticky = "nsew")
resumResultado.config(justify="left")

#===============================================================================
# Pantalla de ingreso de números
#===============================================================================

entPantalla = Entry(mainFrame, bg="black", fg="#04fced", textvariable=numIngreso)
entPantalla.grid(row=2, column=1, columnspan=2)
entPantalla.config(justify="right")

#Esta función se encarga de almacenar el número pulsado y almacenarlo en las listas
#creadas para el manejo del flujo de ejecución.
def ingNumeros(num):
    global operacion
    
    if num == 0 and len(capturaNumeros) == 1:
        capturaNumeros.append(num)
        capturaNumeros.pop()
    else:
        capturaNumeros.append(num)
        
    if capturaNumeros[-1] == "+" or capturaNumeros[-1] == "-" or capturaNumeros[-1] == "x" or capturaNumeros[-1] == "÷":
        capturaNumeros.clear()
    else:
        numIngreso.set("".join(capturaNumeros))

    resumenOperacion.append(num)
    msmOperacion.set("".join(resumenOperacion))

#===============================================================================
# Pantalla de resultado
#===============================================================================

entPantalla2 = Entry(mainFrame, bg="black", fg="#04fced", text="0", textvariable=numResultado)
entPantalla2.grid(row=2, column=3, columnspan=2)
entPantalla2.config(justify="right")

#===============================================================================
# Fila de operaciones:Identificará pulsaciones con el teclado numerico o normal 
#y además los eventos del mouse.
#===============================================================================
#===============================================================================
# Boton Suma  
#===============================================================================
def btnAdd(event):
    suma(numIngreso.get())
    
btnSuma = Button(mainFrame, text="+", width=7, fg="#04fc17", command=lambda:suma(numIngreso.get()))
btnSuma.grid(row=3, column=1)
root.bind("+", btnAdd)
root.bind("<KP_Add>", btnAdd)

#===============================================================================
# Boton resta
#===============================================================================
def btnSubtract(event):
    resta(numIngreso.get())
        
btnResta = Button(mainFrame, text="-", width=7, fg="#04fc17", command=lambda:resta(numIngreso.get()))
btnResta.grid(row=3, column=2)
root.bind("-", btnSubtract)
root.bind("<KP_Subtract>", btnSubtract)

#===============================================================================
# Boton Multiplicar
#===============================================================================
def btnMultiply(event):
    multiplica(numIngreso.get())
    
btnMult = Button(mainFrame, text="x", width=7, fg="#04fc17", command=lambda:multiplica(numIngreso.get()))
btnMult.grid(row=3, column=3)
root.bind("*", btnMultiply)
root.bind("<KP_Multiply>", btnMultiply)

#===============================================================================
# Boton Divide
#===============================================================================
def btnDivide(event):
    divide(numIngreso.get())
    
btnDiv = Button(mainFrame, text="÷", width=7, fg="#04fc17", command=lambda:divide(numIngreso.get()))
btnDiv.grid(row=3, column=4)
root.bind("/", btnDivide)
root.bind("<KP_Divide>", btnDivide)

#===============================================================================
# Funciones y operaciones de la calculadora
#===============================================================================

#===============================================================================
# Funcion suma (operacion 1)
#Asigna a la variable 'operacion' el numero '1' y agrega a la lista el 
#simbolo '+'.
#===============================================================================
def suma(num):
    global operacion
    global resultado
    
    operacion = 1
    capturaNumeros.append("+")
    
    if capturaNumeros[-1] == "+":
        capturaNumeros.clear()
    
    resultado += float(num)
    
    numResultado.set(f'{resultado:,.2f}')
    resumenOperacion.append("+")
    

#===============================================================================
# Funcion Resta (operacion 2)
#===============================================================================
numResta = ""
contarSigno = 0
esPrimerNum = False
def resta(num):
    global operacion
    global resultado
    global contarSigno
    global esPrimerNum
    global numResta
    
    operacion = 2
    contarSigno = resumenOperacion.count("-") + resumenOperacion.count("+") + resumenOperacion.count("x") + resumenOperacion.count("÷")
    
    if contarSigno == 0:
        esPrimerNum = True
    else:
        esPrimerNum = False
    capturaNumeros.append("-")
    
    if capturaNumeros[-1] == "-":
        capturaNumeros.clear()
    
    if esPrimerNum:
        resultado = float(numResta.join(resumenOperacion))
    elif esPrimerNum == False and (resumenOperacion.count("+") != 0 or resumenOperacion.count("x") != 0 or resumenOperacion.count("÷") != 0):
        resultado = float(numIngreso.get())
    else:
        resultado -= float(num)
        
    numResultado.set(f'{resultado:,.2f}')
    resumenOperacion.append("-")
    
#===============================================================================
# Funcion operacion multiplicacion (operacion 3)
#===============================================================================
numMultiplica = ""
def multiplica(num):
    global operacion
    global resultado
    global esPrimerNum
    global numMultiplica
    global contarSigno
    
    operacion = 3
    contarSigno = resumenOperacion.count("-") + resumenOperacion.count("+") + resumenOperacion.count("x") + resumenOperacion.count("÷")
    
    if contarSigno == 0:
        esPrimerNum = True
    else:
        esPrimerNum = False
    
    capturaNumeros.append("x")
    
    if capturaNumeros[-1] == "x":
        capturaNumeros.clear()
    
    if esPrimerNum:
        resultado = float(numMultiplica.join(resumenOperacion))
    elif esPrimerNum == False and (resumenOperacion.count("+") != 0 or resumenOperacion.count("-") != 0 or resumenOperacion.count("÷") != 0):
        resultado = float(numIngreso.get())
    else:
        resultado *= float(num)
    
    numResultado.set(f'{resultado:,.2f}')
    resumenOperacion.append("x")
    
    
#===============================================================================
# Funcion Division (operacion 4) 
#===============================================================================
numDivide = ""
def divide(num):
    global operacion
    global resultado
    global esPrimerNum
    global numDivide
    global contarSigno    
    operacion = 4
    
    contarSigno = resumenOperacion.count("-") + resumenOperacion.count("+") + resumenOperacion.count("x") + resumenOperacion.count("÷")
    
    if contarSigno == 0:
        esPrimerNum = True
    else:
        esPrimerNum = False
    
    capturaNumeros.append("÷")
    
    if capturaNumeros[-1] == "÷":
        capturaNumeros.clear()
    
    if esPrimerNum:
        resultado = float(numMultiplica.join(resumenOperacion))
    elif esPrimerNum == False and (resumenOperacion.count("+") != 0 or resumenOperacion.count("-") != 0 or resumenOperacion.count("x") != 0):
        resultado = float(numIngreso.get())
    else:
        if float(num) != 0:
            resultado /= float(num)
        else:
            numResultado.set("ERR")
    
    numResultado.set(f'{resultado:,.2f}')
    resumenOperacion.append("÷")

#===============================================================================
# Boton de igual (=)
#===============================================================================

def totalResultado():
    global resultado
    global operacion

    if operacion == 1:
        numResultado.set(f'{(resultado + float("".join(capturaNumeros))):,.2f}')
        numIngreso.set(resultado + float("".join(capturaNumeros)))
    elif operacion == 2:
        numResultado.set(f'{(resultado - float(numIngreso.get())):,.2f}')
        numIngreso.set(resultado - float(numIngreso.get()))
    elif operacion == 3:
        numResultado.set(f'{(resultado * float(numIngreso.get())):,.2f}')
        numIngreso.set(resultado * float(numIngreso.get()))
    elif operacion == 4:
        numResultado.set(f'{(resultado / float(numIngreso.get())):,.2f}')
        numIngreso.set(resultado / float(numIngreso.get()))
    
    resultado = 0
    msmOperacion.set("".join(resumenOperacion))

#===============================================================================
# Boton para borrar pantallas y variables
#===============================================================================

def borrarPantalla():
    global resultado
    global operacion
    resultado = 0
    operacion = ""
    numIngreso.set("")
    numResultado.set("")
    resumenOperacion.clear()
    capturaNumeros.clear()
    msmOperacion.set("")
    
#===============================================================================
# Boton de porcentaje para el resultado
#===============================================================================

def porcentaje(num):
    global resultado
    
    if resultado == 0:
        numResultado.set(f'{float(numIngreso.get())/100:,.2f}')
    else:       
        if operacion == 1:
            numResultado.set(f'{(resultado + float("".join(capturaNumeros))/100):,.2f}')
            numIngreso.set(resultado + float("".join(capturaNumeros))/100)
        elif operacion == 2:
            numResultado.set(f'{(resultado - float(numIngreso.get())/100):,.2f}')
            numIngreso.set(resultado - float(numIngreso.get())/100)
        elif operacion == 3:
            numResultado.set(f'{(resultado * float(numIngreso.get())/100):,.2f}')
            numIngreso.set(resultado * float(numIngreso.get())/100)
        elif operacion == 4:
            numResultado.set(f'{(resultado / float(numIngreso.get())/100):,.2f}')
            numIngreso.set(resultado / float(numIngreso.get())/100)
        else:
            numResultado.set(float(numIngreso.get())/100)
            
    resumenOperacion.append("%")
    msmOperacion.set("".join(resumenOperacion))
    
#===============================================================================
# Fila de botones numeros superiores
#===============================================================================

#===============================================================================
# Boton 7
#===============================================================================
def btnSeven(event):
    writeNum = event.char
    ingNumeros(str(writeNum))

btn7 = Button(mainFrame, text="7", width=7, command=lambda:ingNumeros("7"))
btn7.grid(row=4, column=1)
root.bind(f"<KP_{7}>", btnSeven)
root.bind("<Key-7>", btnSeven)

#===============================================================================
# Boton 8
#===============================================================================
def btnEight(event):
    writeNum = event.char
    ingNumeros(str(writeNum))

btn8 = Button(mainFrame, text="8", width=7, command=lambda:ingNumeros("8"))
btn8.grid(row=4, column=2)
root.bind(f"<KP_{8}>", btnEight)
root.bind("<Key-8>", btnEight)

#===============================================================================
# Boton 9
#===============================================================================
def btnNine(event):
    writeNum = event.char
    ingNumeros(str(writeNum))

btn9 = Button(mainFrame, text="9", width=7, command=lambda:ingNumeros("9"))
btn9.grid(row=4, column=3)
root.bind(f"<KP_{9}>", btnNine)
root.bind("<Key-9>", btnNine)

#===============================================================================
# Boton Igual
#===============================================================================
def btnEqual(event):
    totalResultado()

btnIgual = Button(mainFrame, text="=", width=7, fg="#08fc15", command=lambda:totalResultado())
btnIgual.grid(row=4, column=4, rowspan=3, sticky="nsew")
root.bind(f"<KP_Enter>", btnEqual)
root.bind("<Return>", btnEqual)

#===============================================================================
# Fila de botones numeros del medio
#===============================================================================

#===============================================================================
# Boton 4
#===============================================================================
def btnFour(event):
    writeNum = event.char
    ingNumeros(str(writeNum))

btn4 = Button(mainFrame, text="4", width=7, command=lambda:ingNumeros("4"))
btn4.grid(row=5, column=1)
root.bind(f'<KP_{4}>', btnFour)
root.bind("<Key-4>", btnFour)

#===============================================================================
# Boton 5
#===============================================================================
def btnFive(event):
    writeNum = event.char
    ingNumeros(str(writeNum))

btn5 = Button(mainFrame, text="5", width=7, command=lambda:ingNumeros("5"))
btn5.grid(row=5, column=2)
root.bind(f'<KP_{5}>', btnFive)
root.bind("<Key-5>", btnFive)

#===============================================================================
# Boton 6
#===============================================================================
def btnSix(event):
    writeNum = event.char
    ingNumeros(str(writeNum))

btn6 = Button(mainFrame, text="6", width=7, command=lambda:ingNumeros("6"))
btn6.grid(row=5, column=3)
root.bind(f"<KP_{6}>", btnSix)
root.bind("<Key-6>", btnSix)

#===============================================================================
# Fila de botones numeros inferiores
#===============================================================================
#===============================================================================
# Boton 1
#===============================================================================
def btnOne(event):
    writeNum = event.char
    ingNumeros(writeNum)

btn1 = Button(mainFrame, text="1", width=7, command=lambda:ingNumeros("1"))
btn1.grid(row=6, column=1)
root.bind(f'<KP_{1}>', btnOne)
root.bind("<Key-1>", btnOne)

#===============================================================================
# Boton 2
#===============================================================================
def btnTwo(event):
    writeNum = event.char
    ingNumeros(writeNum)

btn2 = Button(mainFrame, text="2", width=7, command=lambda:ingNumeros("2"))
btn2.grid(row=6, column=2)
root.bind(f'<KP_{2}>', btnTwo)
root.bind("<Key-2>", btnTwo)

#===============================================================================
# Boton 3
#===============================================================================
def btnThree(event):
    writeNum = event.char
    ingNumeros(writeNum)
    
btn3 = Button(mainFrame, text="3", width=7, command=lambda:ingNumeros("3"))
btn3.grid(row=6, column=3)
root.bind(f'<KP_{3}>', btnThree)
root.bind("<Key-3>", btnThree)

#===============================================================================
# Fila de botones numeros inferiores
#===============================================================================
#===============================================================================
# Boton %
#===============================================================================
btnPorc = Button(mainFrame, text="%", width=7, fg="#04fc17", command=lambda:porcentaje(numIngreso.get()))
btnPorc.grid(row=7, column=1)

#===============================================================================
# Boton 0
#===============================================================================
def btnZero(event):
    writeNum = event.char
    ingNumeros(writeNum)

btn0 = Button(mainFrame, text="0", width=7, command=lambda:ingNumeros("0"))
btn0.grid(row=7, column=2)
root.bind(f'<KP_{0}>', btnZero)
root.bind('<Key-0>', btnZero)

#===============================================================================
# Boton decimal
#===============================================================================
def btnDecimal(event):
    writeNum = event.char
    ingNumeros(writeNum)

btnDecimal = Button(mainFrame, text=".", width=7, fg="#04fc17", command=lambda:ingNumeros("."))
btnDecimal.grid(row=7, column=3)
root.bind(f'<KP_Decimal>', btnZero)

#===============================================================================
# Boton borrar
#===============================================================================
def btnCleanAll(event):
    borrarPantalla()
    
btnBorrar = Button(mainFrame, text="C", width=7, fg="#04fc17", command=lambda:borrarPantalla())
btnBorrar.grid(row=7, column=4)
root.bind("<Delete>", btnCleanAll)


root.mainloop()

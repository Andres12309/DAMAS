from tkinter import *
ventana = Tk()
ventana.title("DAMAS")
frame = Frame()
frame.pack()

def posin(event):
    global f,c
    info = event.widget.grid_info()
    f= info["row"]
    c= info["column"]
    print((info["row"], info["column"]))

def casillas(texto, colortexto, color, fila, columna):
    casilla = Button(frame, text = texto)
    casilla.grid(row = fila, column = columna)
    casilla.config(bg = color, fg = colortexto, width = 5)
    casilla.bind("<Button 1>",posin)

def tablero():
    for f in range(2, 10):
        for c in range(2, 10):
            if((f%2 != 0) and (c%2 != 0)): 
                casillas(" ", 'black', 'black', f, c)
            elif((f%2 == 0) and (c%2 == 0)):
                casillas(" ", 'black', 'black', f, c)
            else:
                casillas(" ", 'white', 'white', f, c)
            

def clickNuevoJuego():
    for f in range(2, 10):
        for c in range(2, 10):
            if(f<5):
                if((f%2 != 0) and (c%2 != 0)):
                    casillas("O", 'red', 'black', f, c)
                elif((f%2 == 0) and (c%2 == 0)):
                    casillas("O", 'red','black', f, c)
            if(f>6):
                if((f%2 != 0) and (c%2 != 0)):
                    casillas("O", 'white', 'black', f, c)
                if((f%2 == 0) and (c%2 == 0)):
                    casillas("O", 'white', 'black', f, c)

def obtener_boton(fila,columna):
    
    boton = root.grid_slaves(row=fila, column=columna)
    
    return boton

def intercalar(event):
    event.widget.config(text='O') 

def movimiento1(event):
    if(f>=4 and c>=2):
        if(casillas("O", 'white','black', f, c)==casillas(" ", 'black', 'black', f, c) or casillas(" ", 'red','black', f, c)==casillas(" ", 'black', 'black', f, c)):
            casillas("O", 'white','black', f, c)==casillas(" ", 'black', 'black', f, c)
    if(f>4 and c>2):
        if(casillas(" ", 'white','black', f, c)==casillas(" ", 'black', 'black', f, c)):
            casillas(" ", 'black', 'black', f, c)==casillas("O", 'red','black', f, c)




ventana.bind("<Button 1>",movimiento1)

def movimiento2(event):
    if(f<=7 and c<=4):
        if(casillas("O", 'white','black', f, c)==casillas(" ", 'black', 'black', f, c) or casillas(" ", 'white','black', f, c)==casillas(" ", 'black', 'black', f, c)):
            casillas("O", 'white','black', f, c)==casillas(" ", 'black', 'black', f, c)
    if(f<6 and c<5):
        if(casillas(" ", 'white','black', f, c)==casillas(" ", 'black', 'black', f, c)):
            casillas(" ", 'black', 'black', f, c)==casillas("O", 'white','black', f, c)

ventana.bind("<Button 2>",movimiento2)

#-------CREACION DEL TABLERO------------
tablero()
#-----------BOTONES DE OPCIONES-----------
botonNuevoJuego = Button(frame, text = "NUEVO JUEGO", command = clickNuevoJuego())
botonNuevoJuego.grid(row = 10, column = 1, columnspan = 8)

ventana.mainloop()
from tkinter import *
tk = Tk()
inBal_x = 450
inBal_y = 250


canvas = Canvas(tk, width=900, height=500)
imagen = PhotoImage(file="A1.gif")
canvas.create_image(650,100, anchor=NW, image=imagen)
image1 = PhotoImage(file="ARCOIZQUIERDO.gif")
canvas.create_image(50,100, anchor=NW, image=image1)
balon = PhotoImage(file="ball.gif", width=500, height=500)
canvas.create_image(inBal_x,inBal_y, anchor=NW, image=balon)
canvas.create_text(80, 10, text='Prueba Gol', fill='green')

def movertriangle (event):
    global inBal_x, inBal_y
    if event.keysym == 'Up':
        x = 0
        y = -5
        canvas.move(3,x,y)
        inBal_y = inBal_y  + y

        ## llamado funcion para saber si es gol (goliz)
        goliz(inBal_x,inBal_y)
        
        print (inBal_y,inBal_x)
        
    elif event.keysym == 'Down':
        x = 0
        y = +5
        canvas.move(3,x,y)
        inBal_y = inBal_y +y

        ## llamado funcion para saber si es gol (goliz)
        goliz(inBal_x,inBal_y)
        
        print (inBal_y,inBal_x)
         
    elif event.keysym == 'Left':
        x = -5
        y = 0
        canvas.move(3,x, y)
        inBal_x = inBal_x + x

        ## llamado funcion para saber si es gol (goliz)
        goliz(inBal_x,inBal_y)

        print (inBal_y,inBal_x)
        
    elif event.keysym == 'Right':
        x =+5
        y= 0
        canvas.move(3,x, y)
        inBal_x = inBal_x + x

        ## llamado funcion para saber si es gol (goliz)
        goliz(inBal_x,inBal_y)
        
        print (inBal_y,inBal_x)

def goliz(x,y):
    ## Verificación del gol
    if (x == 195  & y == 195):
            print ("Gol")
            mensaje()           
    elif x== 705:
        if y == 185:
            mensaje()
    else:
            print (" ")                

def mensaje():
    ventana_msg = Tk()
    ventana_msg.title("Aviso")
    ventana_msg.geometry("100x100+350+250")
    msg = Message(ventana_msg, text="Gol", relief=RIDGE, bd=1)
    msg.pack(expand=YES, fill=BOTH)
    
    


canvas.bind_all('<KeyPress-Up>',movertriangle)
canvas.bind_all('<KeyPress-Down>',movertriangle)
canvas.bind_all('<KeyPress-Left>',movertriangle)
canvas.bind_all('<KeyPress-Right>',movertriangle)


canvas.pack()
canvas.mainloop()


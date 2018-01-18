from tkinter import *
tk = Tk()
pos_inic = 800
canvas = Canvas(tk, width=900, height=800)

imagen = PhotoImage(file="A1.gif")
canvas.create_image(650,100, anchor=NW, image=imagen)
image1 = PhotoImage(file="ARCOIZQUIERDO.gif")
canvas.create_image(50,100, anchor=NW, image=image1)
balon = PhotoImage(file="ball.gif", width=500, height=500)
canvas.create_image(450,250, anchor=NW, image=balon)


def movimimiento(event):
        global pos_inic
        if event.keysym == 'Left':
                canvas.move(3, -5, 0)
                pos_inic = pos_inic - 5
                print(pos_inic)
        elif event.keysym == 'Right':
                canvas.move(3, 5, 0)
                pos_inic = pos_inic + 5
                print(pos_inic)
canvas.bind_all('<KeyPress-Left>', movimimiento)
canvas.bind_all('<KeyPress-Right>', movimimiento)
canvas.pack()
canvas.mainloop()

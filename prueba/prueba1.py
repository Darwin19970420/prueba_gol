from tkinter import *
tk = Tk()
pos_inic = 800
gol = 12

canvas = Canvas(tk, width=900, height=500)
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
                if pos_inic == 475 or  pos_inic == 585:
                        ventana_msg = Tk()
                        ventana_msg.title("Aviso")
                        ventana_msg.geometry("100x100+350+250")
                        msg = Message(ventana_msg, text="Gol", relief=RIDGE, bd=5)
                        msg.pack(expand=YES, fill=BOTH)
                else:
                        print()
        elif event.keysym == 'Right':
                canvas.move(3, 5, 0)
                pos_inic = pos_inic + 5
                print(pos_inic)

canvas.bind_all('<KeyPress-Left>', movimimiento)
canvas.bind_all('<KeyPress-Right>', movimimiento)
canvas.pack()
canvas.mainloop()

from tkinter import *
tk = Tk()
pos_inic = 800
canvas = Canvas(tk, width=900, height=800)

imagen = PhotoImage(file="arco.gif")
canvas.create_image(50,100, anchor=NW, image=imagen)
balon = PhotoImage(file="ball.gif", width=500, height=500)
canvas.create_image(800,350, anchor=NW, image=balon)


def movimimiento(event):
	global pos_inic
	if event.keysym == 'Up':
		canvas.move(2, -5, 0)
		pos_inic = pos_inic - 5
		print(pos_inic)

canvas.bind_all('<KeyPress-Up>', movimimiento)
canvas.pack()
canvas.mainloop()

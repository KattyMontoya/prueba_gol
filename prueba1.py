from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_image=PhotoImage(file="ball.gif")
imagen=PhotoImage(file="arco.png")
x=0
y=200
canvas.create_image(0,200,anchor=NW,image=my_image)
canvas.create_image(200,140,anchor=NW,image=imagen)
def movetriangle(event): 
    if event.keysym == 'Left':
        global x
        global y
        x=x-3
        y=y-3
        print("Coordenadas:",x,y)
        canvas.move(1, -3, 0)
        
    else:
        global x
        global y
        x=x+3
        y=y+3
        print("Coordenadas:",x,y)
        canvas.move(1, 3, 0)
        
     
    if x>200:
        print("GOL!!")

canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()

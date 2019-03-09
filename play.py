
from tkinter import Tk, Canvas
from space_invaders.game import MyCanvas, Game

def key(event):
    if event.keysym == 'space':
        game.tank_fire()
    elif event.keysym == 'Left':
        game.move_tank_to_left()
    elif event.keysym == 'Right':
        game.move_tank_to_right()
    else:
        print("We don't care this key")

master = Tk()
master.title( "Space Invanders" )
canvas = Canvas(master, height=MyCanvas.HEIGHT, width=MyCanvas.WIDTH)
canvas.bind("<1>", lambda event: canvas.focus_set())
canvas.bind("<Key>", key)
canvas.pack()
game = Game(canvas, MyCanvas.WIDTH, MyCanvas.HEIGHT)
master.mainloop()

from game import Game
from tkinter import Tk, Canvas

if __name__ == '__main__':
    map_size = 20
    block_size = 30
    root = Tk()
    canvas = Canvas(root, width=map_size*block_size, height=map_size*block_size, bg="black")
    canvas.pack()
    game = Game(canvas, block_size, map_size)
    root.mainloop()
from random import randint
from tkinter import *
from mysocket import DataTransferServer
from threading import Thread

class Game:
    def __init__(self, canvas, block_size, map_size):
        self.block_size = block_size
        self.map_size = map_size

        self.data_transfer_server = DataTransferServer(4088)

        self.canvas = canvas
        self.snake_coords = [[map_size // 2, map_size // 2]]
        self.apple_coords = [randint(0, self.map_size-1) for i in range(2)]
        self.vector = {"Up":(0,-1), "Down":(0, 1), "Left": (-1,0), "Right": (1, 0)}
        self.direction = self.vector["Right"]
        self.canvas.focus_set()
        # self.canvas.bind("<KeyPress>", self.set_direction)

        self.key_thread = Thread(target = self.recv_direction)
        self.key_thread.start()
        
        self.GAME()

    def set_apple(self):
        self.apple_coords = [randint(0, self.map_size-1) for i in range(2)]
        if self.apple_coords in self.snake_coords:
            self.set_apple()

    # def set_direction(self, event):
    #     if event.keysym in self.vector:
    #         if self.vector[event.keysym][0] + self.direction[0] != 0 or self.vector[event.keysym][1] + self.direction[1] != 0:
    #             self.direction = self.vector[event.keysym]

    def recv_direction(self):
        while True:
            data = self.data_transfer_server.recv_direction()
            if data:
                self.direction = self.vector[data]

    def draw(self):
        self.canvas.delete(ALL)
        x_apple, y_apple = self.apple_coords
        self.canvas.create_rectangle(x_apple*self.block_size, y_apple*self.block_size, (x_apple+1)*self.block_size, (y_apple+1)*self.block_size, fill="red", width=0)
        for x, y in self.snake_coords:
            self.canvas.create_rectangle(x*self.block_size, y*self.block_size, (x+1)*self.block_size, (y+1)*self.block_size, fill="green", width=0)

    def coord_check(self, coord):
        return 0 if coord > self.map_size-1 else self.map_size-1 if coord < 0 else coord
      
    def GAME(self):
        self.draw()
        # self.recv_direction()
        x,y = self.snake_coords[0]
        x += self.direction[0]; y += self.direction[1]
        x = self.coord_check(x)
        y = self.coord_check(y)
        if x == self.apple_coords[0] and y == self.apple_coords[1]:
            self.set_apple()
        elif [x, y] in self.snake_coords:
            self.snake_coords = []
        else:
            self.snake_coords.pop()
        self.snake_coords.insert(0, [x,y])
        self.canvas.after(100, self.GAME)
        
        

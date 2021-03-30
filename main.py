import maze_essentials
from tkinter import *


maze_size = 50


def kruskal(event):
    maze.generateKruskal()


def DFS(event):
    maze.generateDFS()


def showPath(path):
    # prev = path[0]
    for p in path:
        # offX = p[0] - prev[0]
        # offY = p[1] - prev[1]
        c.create_rectangle(squareSizeX * (2 * p[1] + 1), squareSizeY * (2 * p[0] + 1),
                           squareSizeX * (2 * p[1] + 2), squareSizeY * (2 * p[0] + 2),
                           fill='red')
        '''
        c.create_rectangle(squareSizeX * (2 * p[1] + 1 + offY), squareSizeY * (2 * p[0] + 1 + offX),
                           squareSizeX * (2 * p[1] + 2 + offY), squareSizeY * (2 * p[0] + 2 + offX),
                           fill='red')
        prev = p
        '''


def showExpanded(ex):
    for e in ex:
        c.create_rectangle(squareSizeX * (2 * e[1] + 1), squareSizeY * (2 * e[0] + 1),
                           squareSizeX * (2 * e[1] + 2), squareSizeY * (2 * e[0] + 2),
                           fill='blue')


def BFS(event):
    p, ex = maze.findBFS((0, 0), (maze_size - 1, maze_size - 1))
    showExpanded(ex)
    showPath(p)


def AStar(event):
    p, ex = maze.findAStar((0, 0), (maze_size - 1, maze_size - 1))
    showExpanded(ex)
    showPath(p)


def drawMaze(event):
    c.delete()
    image = maze.getMaze()
    for i in range(len(image) + 1):
        for j in range(len(image[0]) + 1):
            filler = 'black'
            if i < len(image) and j < len(image[0]) and image[i][j] == 0:
                filler = 'white'
            c.create_rectangle(squareSizeX * j, squareSizeY * i, squareSizeX * (j + 1), squareSizeY * (i + 1),
                               fill=filler)


root = Tk()
maze = maze_essentials.Maze(width=maze_size, height=maze_size)

squareSizeX = 7
squareSizeY = squareSizeX
print(maze.h)
print(maze.w)
c = Canvas(root, width=(maze.w * 2 + 1) * squareSizeX, height=(maze.h * 2 + 1) * squareSizeY, bg='white')
c.pack(side='right')
btn1 = Button(root,
              text='Generate with DFS',
              width=30, height=5,
              bg='white', fg='black')
btn2 = Button(root,
              text='Generate with Kruskal',
              width=30, height=5,
              bg='white', fg='black')
btn3 = Button(root,
              text='Show',
              width=30, height=5,
              bg='white', fg='black')
btn4 = Button(root,
              text='Find path via greedy BFS',
              width=30, height=5,
              bg='white', fg='black')
btn5 = Button(root,
              text='Find path via A star',
              width=30, height=5,
              bg='white', fg='black')
btn1.bind("<Button-1>", DFS)
btn2.bind("<Button-1>", kruskal)
btn3.bind("<Button-1>", drawMaze)
btn4.bind("<Button-1>", BFS)
btn5.bind("<Button-1>", AStar)
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
root.mainloop()
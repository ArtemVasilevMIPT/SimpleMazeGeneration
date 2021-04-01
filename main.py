import maze_essentials
from tkinter import Canvas, Tk, Button


maze_size = 50


def kruskal(event):
    maze.generateKruskal()
    drawMaze(event)


def DFS(event):
    maze.generateDFS()
    drawMaze(event)


def showPath(path, color='red'):
    for p in path:
        c.create_rectangle(squareSizeX * (2 * p[1] + 1),
                           squareSizeY * (2 * p[0] + 1),
                           squareSizeX * (2 * p[1] + 2),
                           squareSizeY * (2 * p[0] + 2),
                           fill=color)


def BFS(event):
    c.delete()
    drawMaze(event)
    p, ex = maze.findBFS((0, 0), (maze_size - 1, maze_size - 1))
    showPath(ex, 'blue')
    showPath(p)


def AStar(event):
    c.delete()
    drawMaze(event)
    p, ex = maze.findAStar((0, 0), (maze_size - 1, maze_size - 1))
    showPath(ex, 'blue')
    showPath(p)


def drawMaze(event):
    c.delete()
    image = maze.getMaze()
    for i in range(len(image) + 1):
        for j in range(len(image[0]) + 1):
            filler = 'black'
            if i < len(image) and j < len(image[0]) and image[i][j] == 0:
                filler = 'white'
            c.create_rectangle(squareSizeX * j, squareSizeY * i,
                               squareSizeX * (j + 1), squareSizeY * (i + 1),
                               fill=filler)


def createButton(rt, txt, func):
    b = Button(rt,
               text=txt,
               width=30, height=5,
               bg='white', fg='black')
    b.bind('<Button-1>', func)
    b.pack()
    return b


root = Tk()
maze = maze_essentials.Maze(width=maze_size, height=maze_size)

squareSizeX = 7
squareSizeY = squareSizeX
print(maze.h)
print(maze.w)
c = Canvas(root, width=(maze.w * 2 + 1) * squareSizeX, height=(maze.h * 2 + 1) * squareSizeY, bg='white')
c.pack(side='right')
btn1 = createButton(root, 'Generate with DFS', DFS)
btn2 = createButton(root, 'Generate with Kruskal', kruskal)
btn4 = createButton(root, 'Find path via greedy BFS', BFS)
btn5 = createButton(root, 'Find path via A star', AStar)
root.mainloop()

from ursina import *

app = Ursina()
pillow = Animation('MERG Pillow', scale=1.5, collider='box')
bg = Entity(model="quad", scale=(30, 15), texture="BG", z=1)

camera.orthographic= True
camera.fov = 15

def update():
    pillow.y = pillow.y -0.05
    for pipe in pipes:
        pipe.x= pipe.x -0.03
    if pillow.y < -8 :
        quit()
    if pillow.y > 8  :      
        quit() 
    if pillow.intersects().hit:
        quit()

def input(key):
    if key == 'space':
        pillow.y = pillow.y + 0.9   

pipes = []

pipe= Entity(model="quad", color=color.green, texture="white_cube", position=(30, 15), scale=(1.5, 15, 1), collider='box')

def newPipes():
    ranY =  random.randint(2 , 10 )
    newPipe = duplicate(pipe, y=ranY)
    newPipe2 = duplicate(pipe, y=ranY-20)
    pipes.append(newPipe)
    pipes.append(newPipe2)
    invoke(newPipes, delay=4  )


newPipes()
 
app.run() 
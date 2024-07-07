import turtle
import math
import pygame
import time

def draw_pattern(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    h = 2
    turtle.color(color)
    for i in range(195):
        h += 0.006
        turtle.lt(179)
        turtle.backward(i * 0.1)
        turtle.circle(i * 0.3, 120)
        turtle.rt(14)
        turtle.forward(i * 0.1)
        turtle.circle(i * 0.3, 120)

def draw_spiral(turtle_shape, pencolor, fillcolor, x, y):
    turtle.shape(turtle_shape)
    turtle.pencolor(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.speed(0.2)
    phi = 137.508 * (math.pi / 180.0)
    
    for i in range(300):
        r = 4 * math.sqrt(i)
        theta = i * phi
        x_pos = r * math.cos(theta)
        y_pos = r * math.sin(theta)
        turtle.penup()
        turtle.goto(x + x_pos, y - y_pos)
        turtle.setheading(i * 137.508)
        turtle.pendown()
        turtle.stamp()

def main():
    # Inicializar Pygame para la música
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")  # Reemplaza con la ruta a tu archivo de música
    pygame.mixer.music.play(-1)  # Reproduce en bucle

    # Tamaño de la ventana
    turtle.setup(width=500, height=500)
    turtle.tracer(6)
    turtle.bgcolor('black')
    turtle.pensize(2)
    
    # Dibujar seis patrones y espirales
    positions = [
        (-turtle.window_width()/3.4 + 50, turtle.window_height()/2.2 - 250, 'yellow', 'orangered', 'orange'),
        (-turtle.window_width()/300 + 250, turtle.window_height()/2.2 - 250, 'purple', 'pink', 'purple'),
        (-turtle.window_width()/3.4 + 50, turtle.window_height()/4.3 - 250, 'blue', 'blue', 'green'),
        (-turtle.window_width()/300 + 250, turtle.window_height()/4.3 - 250, 'white', 'orangered', 'yellow'),
        (-turtle.window_width()/3.4 + 50, turtle.window_height()/46 - 250, 'magenta', 'magenta', 'red'),
        (-turtle.window_width()/300 + 250, turtle.window_height()/46 - 250, 'red', 'red', 'pink')
    ]
    
    for pos in positions:
        draw_pattern(pos[2], pos[0], pos[1])
        draw_spiral('turtle', pos[3], pos[4], pos[0], pos[1])
    
    # Agregar texto debajo de los dibujos
    turtle.penup()
    turtle.goto(0, -700)
    turtle.pendown()
    turtle.color('#ffd700')
    turtle.write("¿Te acuerdas del significado de 6 gerberas?", align="center", font=("Calibri", 8, "roman"))
    
    turtle.hideturtle()
    turtle.done()

    # Esperar un poco antes de salir para que la música siga sonando
    time.sleep(10)

if __name__ == "__main__":
    main()
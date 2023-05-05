# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from turtle import width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas,scene_width,scene_height)

    #draw grid for referencing purposes
    #draw_grid(canvas,scene_width,scene_height, 25)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

def draw_sky(canvas, scene_width, scene_height):
    #draw the sky and snow lines
    draw_rectangle(canvas, 0, scene_height/4, scene_width, scene_height, width=0, fill= "deepSkyBlue")
    draw_snowing_low(canvas,scene_width,scene_height, 20)
    draw_snowing_high(canvas,scene_width,scene_height, 20)
    draw_clouds(canvas,scene_width,scene_height)

def draw_snowing_low(canvas,scene_width,scene_height, interval):
    #draw lower snow lines
    interval = interval*2
    scene_height = scene_height*.9
    draw_snowing(canvas,scene_width,scene_height, interval)

def draw_snowing_high(canvas,scene_width,scene_height, interval):
    #draw higher snow lines
    draw_snowing(canvas,scene_width,scene_height, interval)

def draw_snowing(canvas, scene_width, scene_height, interval):
    #draw diagonal lines to look like snowing   
    x0 = interval - (scene_height/7)
    y0 = scene_height * 3 / 5 
    x1 = interval
    y1 = scene_height * .85
    number_of_lines = (scene_width + (scene_height/7)) / interval
    
    #for loop to create lots of lines
    for i in range(int(number_of_lines)):
        draw_line(canvas, x0, y0, x1, y1, width=1, fill="white" )
        x0 += interval
        x1 += interval

def draw_clouds(canvas, scene_width, scene_height):
    #draw the clouds randomly. Heavily inspired by example 5 in the draw2d library
    cloud_height = round(scene_height*3/4)
    min_diam = 50
    max_diam = 80

    for i in range(200):
        x = random.randint(0, scene_width )
        y = random.randint(cloud_height,scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter/2,width=0,
                fill="gray90")

def draw_ground(canvas, scene_width, scene_height):
    #draws everything on the groung
    draw_igloo(canvas, 75, 450, 125, 250)
    #draw first snowman
    draw_snowman_body(canvas, 500, 80, 50)
    draw_snowman_face(canvas, 500, 80, 50)

    #draw second snowman
    draw_snowman_body(canvas, 625, 100, 70)
    draw_snowman_face(canvas, 625, 100, 70)

    #draw third snowman
    draw_snowman_body(canvas, 700, 100, 80)
    draw_snowman_face(canvas, 700, 100, 80)
    draw_rectangle(canvas, 0, 0, scene_width, scene_height/4, fill="snow1")

def draw_igloo(canvas, center_x, width, horizon, height):
    #draw an igloo on the left on the groundlevel

    #point calculations for door way 
    #placed before the dome so that it is drawn behind
    x0 = center_x 
    y0 = horizon
    x1 = center_x + (width*1.2)
    y1 = horizon + height/3

    draw_rectangle(canvas, 200, 185, 325, 100, width=1, fill='snow2')

    
    #point calculations for dome
    x0 = center_x - (width/2)
    y0 = horizon - height*.8
    x1 = center_x + (width/2)
    y1 = height

    draw_oval(canvas,x0, y0, x1, y1, width=1, outline='black', fill='snow2' )

def draw_snowman_body(canvas, center_x, bottom, diameter):
    #draw snowman body circles and hat
    
    #point calculations for bottom circle
    x0 = center_x - (diameter/2)
    y0 = bottom
    x1 = center_x + (diameter/2)
    y1 = bottom + diameter
    #draw botton circle
    draw_oval(canvas, x0, y0, x1, y1, width=1, fill="white")

    
    #point calculations for middle circle
    x0 = center_x - (diameter * .75/2)
    y0 = bottom + diameter * .75
    x1 = center_x + (diameter *.75/2)
    y1 = bottom + diameter * 1.5
    #draw middle circle
    draw_oval(canvas, x0, y0, x1, y1, width=1, fill="white")


    #point calculations for head circle
    x0 = center_x - (diameter *.55/2)
    y0 = bottom + diameter * 1.4
    x1 = center_x + (diameter *.55/2)
    y1 = bottom + diameter * 1.9
    #draw head circle
    draw_oval(canvas, x0, y0, x1, y1, width=1, fill="white")


    #point calculations for hat rim
    x0 = center_x - (diameter*.55/2)
    y0 = bottom + diameter * 1.8
    x1 = center_x + (diameter*.55/2)
    y1 = bottom + diameter * 1.9
    #draw hat rim
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, fill="Black")


    #point calculations for hat top
    x0 = center_x - (diameter*.3/2)
    y0 = bottom + diameter * 1.8
    x1 = center_x + (diameter*.3/2)
    y1 = bottom + diameter * 2.2
    #draw hat top
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, fill="Black")

def draw_snowman_face(canvas, center_x, bottom, diameter):
    #draw snowman eyes and nose and scarf

    #point calculations for left eye
    x0 = center_x - (diameter *.03)
    y0 = bottom + diameter * 1.7
    x1 = center_x - (diameter *.13)
    y1 = bottom + diameter * 1.75
    #draw left eye
    draw_oval(canvas, x0, y0, x1, y1, width=1, fill="black")

    #point calculations for right eye
    x0 = center_x + (diameter *.03)
    y0 = bottom + diameter * 1.7
    x1 = center_x + (diameter *.13)
    y1 = bottom + diameter * 1.75
    #draw right eye
    draw_oval(canvas, x0, y0, x1, y1, width=1, fill="black")

    #point calculations for nose
    x0 = center_x
    y0 = bottom + diameter * 1.65
    x1 = center_x
    y1 = bottom + diameter * 1.55
    x2 = center_x - diameter * .135
    y2 = bottom + diameter * 1.6
    #draw nose
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, width=1, fill="orange")

    #point calculations for scarf horizontal
    x0 = center_x - (diameter*.45/2)
    y0 = bottom + diameter * 1.5
    x1 = center_x + (diameter*.45/2)
    y1 = bottom + diameter * 1.35
    #draw scarf horizontal
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, fill="red3")

    #point calculations for scarf verticle
    x0 = center_x - (diameter*.25/2)
    y0 = bottom + diameter * 1.5
    x1 = center_x - (diameter*.45/2)
    y1 = bottom + diameter
    #draw scarf verticle
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, fill="red3")

# Call the main function so that
# this program will start executing.
main()
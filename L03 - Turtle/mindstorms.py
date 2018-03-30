import turtle

side = 0

def  draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_circle()
    draw_square()
    window.exitonclick()

    
def draw_square():
    point = turtle.Turtle()
    point.shape("turtle")
    point.color("yellow")
    point.speed(10)
    for i in range(1,3):
        for angle in range(0,36):
            for side in range(0,4):
                point.forward(50*i)
                point.right(90)
                side = side+1
            side=0
            point.right(10)
        i=i+1
##    window.exitonclick()

def draw_circle():
    point = turtle.Turtle()
    point.shape("circle")
    point.color("blue")
    point.circle(100)
    
    
draw_art();

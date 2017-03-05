import turtle

def semeon_square(a_turtle):
    for i in range(1,5):
        a_turtle.forward(100)
        a_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green");
    #create the turtle George - Draws Square
    george = turtle.Turtle()
    george.color("yellow")
    george.shape("turtle")
    george.speed(2)
    for i in range(1,37):
        semeon_square(george)
        george.right(10)
    semeon_square(george)
    
    #create the turtle Clooney - draws Circle
    clooney = turtle.Turtle();
    clooney.color("blue")
    clooney.shape("arrow")
    clooney.speed(3)
    clooney.circle(100)
    
    window.exitonclick()

draw_art()

semeon_square()

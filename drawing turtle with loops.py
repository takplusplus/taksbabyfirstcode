import turtle
a = 3
b = 2
while a < b:
    print(r'\'well shit i guess i should stop')


    break
print(r'\'end')

my_turtle = turtle.Turtle()
my_turtle.speed(15)
def square(length,angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)
for i in range(36):
    square(100,90)
    my_turtle.right(10)
    my_turtle.right(10) 

import turtle

t=turtle.Turtle()
t.shape("turtle")

t.color("light blue")
for _ in range(4):
    t.forward(100)
    t.right(90)

for i in range(10):
	t.forward(100)
	if i % 2 == 0: t.left(72)
	else: t.right(144)



for _ in range(3):
    t.forward(100)
    t.right(120)

turtle.done()
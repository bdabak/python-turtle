import turtle;

myPen = turtle.Turtle();
turtle.bgcolor("black");

myPen.speed(1);

myPen.color('#285078', '#a0c8f0');
myPen.begin_fill();
myPen.circle(100);
myPen.end_fill();

myPen.begin_poly();
myPen.goto(0,0)
myPen.goto(0,10)
myPen.goto(0,30)
myPen.goto(0,40)
myPen.goto(0,50)
myPen.goto(0,50)
myPen.goto(0,50)
myPen.goto(0,60)
myPen.end_poly();
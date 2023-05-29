# 导入turtle模块
import turtle

# 定义绘制爱心的函数
def draw_heart(x,y,size):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    turtle.begin_fill()
    turtle.left(45)

    turtle.forward(size)
    turtle.circle(size/2,180)
    turtle.right(90)
    turtle.circle(size/2,180)

    turtle.forward(size)
    turtle.end_fill()

# 设置画布
turtle.setup(800, 600)
turtle.bgcolor("white")

# 绘制爱心
turtle.color("red")
draw_heart(0,0,100)

# 写出生日快乐
turtle.color("black")
turtle.penup()
turtle.goto(0,-120)
turtle.write("生日快乐",align="center",font=("Arial",24,"normal"))

# 隐藏画笔
turtle.hideturtle()

# 等待用户关闭窗口
turtle.done()

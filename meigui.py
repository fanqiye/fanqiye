import turtle

# 设置画笔颜色和形状
turtle.shape("turtle")
turtle.speed(50)

# 画花瓣
for i in range(20):
    turtle.color("#FFC0CB", "#FFC0CB")
    turtle.begin_fill()
    turtle.circle(100, 80)
    turtle.left(120)
    turtle.circle(100, 80)
    turtle.circle(100, 80)
    turtle.left(120)
    turtle.circle(100, 80)
    turtle.circle(100, 80)
    turtle.left(120)
    turtle.circle(100, 80)
    turtle.end_fill()
    turtle.left(30)

    if i == 48:
        # 画出玫瑰花形状就停下
        break

# 隐藏画笔
turtle.hideturtle()

# 显示绘画窗口
turtle.done()

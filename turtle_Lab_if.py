import turtle

while True:
    shape = input('Enter shape: ')
    if shape == 'circle':
        turtle.circle(50)
    elif shape == 'triangle':
        #문장과 문장을 구분하기 위해서는 세미콜론을 사용해야한다
      turtle.forward(50); turtle.right(120)
      turtle.forward(50); turtle.right(120)
      turtle.forward(50)
    elif shape == 'quit':
        break
    else:
        print('shape is wrong')
turtle.bye()

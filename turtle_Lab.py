import turtle

count = 12

#파이썬은 함수에 괄호가 없다
#중괄호(브레이스?)도 없다. 대신 들여쓰기(인덴트)로 구분
#--,++ 과 같은 문법이 없다
while count > 0:
    turtle.forward(100)
    turtle.left(30)
    count -= 1
else:
    print('count is zero')
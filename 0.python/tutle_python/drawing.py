# 파이썬으로 그림판 만들기

# 터틀 모듈을 임포트
import turtle


# 그림판의 제목과 크기를 설정하는 함수
def setup():
    turtle.title("그림판")
    turtle.setup(800, 600)


# 펜의 색상을 변경하는 함수
def change_color(color):
    turtle.color(color)


# 펜의 두께를 변경하는 함수
def change_width(width):
    turtle.pensize(width)


# 펜을 들어서 이동하는 함수
def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# 지우개 기능을 수행하는 함수
def erase():
    turtle.clear()


# 메인 함수
def main():
    # 그림판을 설정하는 함수 호출
    setup()
    # 펜의 속도를 최대로 설정
    turtle.speed(0)
    # 마우스 클릭 이벤트에 따라 색상과 두께를 변경하는 문장
    turtle.onscreenclick(turtle.goto)
    turtle.getscreen().onkeypress(lambda: change_color("red"), "r")
    turtle.getscreen().onkeypress(lambda: change_color("green"), "g")
    turtle.getscreen().onkeypress(lambda: change_color("blue"), "b")
    turtle.getscreen().onkeypress(lambda: change_width(1), "1")
    turtle.getscreen().onkeypress(lambda: change_width(3), "3")
    turtle.getscreen().onkeypress(lambda: change_width(5), "5")
    # 스페이스바를 누르면 지우개 기능을 수행하는 문장
    turtle.getscreen().onkeypress(erase, "space")
    # 키보드 입력을 받을 수 있도록 설정하는 문장
    turtle.listen()
    # 그림판을 유지하는 문장
    turtle.done()


# 메인 함수 호출
if __name__ == "__main__":
    main()

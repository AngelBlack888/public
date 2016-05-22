# ���� Colliding Balls ������ 0.5 �� 5 ��� 2016
import tkinter
import random

# ���������
WIDTH = 540
HEIGHT = 480
BG_COLOR = 'white'
MAIN_BALL_COLOR = 'blue'
MAIN_BALL_RADIUS = 25
BAD_COLOR = 'red'
COLORS = ['aqua', 'fuchsia', BAD_COLOR, 'pink', 'yellow', BAD_COLOR, 'gold', 'chartreuse', BAD_COLOR]
NUM_OF_BALLS = 9
MAX_RADIUS = 35
MIN_RADIUS = 15
DELAY = 8
INIT_DX = 1
INIT_DY = 1
ZERO = 0


# ����� ������
class Ball():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color,
                           outline=self.color if self.color != BAD_COLOR else 'black')

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=BG_COLOR,
                           outline=BG_COLOR)

    def is_collision(self, ball):
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a * a + b * b) ** 0.5 <= self.r + ball.r

    def move(self):
        # ������������ �� ��������
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= ZERO):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= ZERO):
            self.dy = -self.dy
        # ������������ � ������� ������
        for ball in balls:
            if self.is_collision(ball):
                if ball.color != BAD_COLOR:  # �� ������� ���
                    ball.hide()
                    balls.remove(ball)
                    self.dx = -self.dx
                    self.dy = -self.dy
                else:  # ������� ���
                    self.dx = self.dy = 0
        self.hide()
        self.x += self.dx
        self.y += self.dy
        if self.dx * self.dy != 0:
            self.draw()


# ������������ ������� �� ����
def mouse_click(event):
    global main_ball
    if event.num == 1:  # ����� ������ ����
        if 'main_ball' not in globals():  # �����
            main_ball = Ball(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR, INIT_DX, INIT_DY)
            if main_ball.x > WIDTH / 2:
                main_ball.dx = -main_ball.dx
            if main_ball.y > HEIGHT / 2:
                main_ball.dy = -main_ball.dy
            main_ball.draw()
        else: # ������� ������
            if main_ball.dy * main_ball.dx > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3:  # ������ ������ ����: ������� �������
        if main_ball.dy * main_ball.dx > 0:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy


# ������� ������ ��������-�����
def create_list_of_balls(number):
    lst = []
    while len(lst) < number:
        next_ball = Ball(random.choice(range(MAX_RADIUS, WIDTH - MAX_RADIUS)),
                         random.choice(range(MAX_RADIUS, HEIGHT - MAX_RADIUS)),
                         random.choice(range(MIN_RADIUS, MAX_RADIUS)),
                         random.choice(COLORS))
        is_collision = False
        for ball in lst:
            if next_ball.is_collision(ball):
                is_collision = True
                break
        if not is_collision:
            lst.append(next_ball)
            next_ball.draw()
    return lst


# ������� ���������� ������ �����
def count_bad_balls(list_of_balls):
    result = 0
    for ball in list_of_balls:
        if ball.color == BAD_COLOR:
            result += 1
    return result


# �������� ���� ����
def main():
    if 'main_ball' in globals():
        main_ball.move()
        if len(balls) - num_of_bad_balls == 0:
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text="YOU WON!", font="Arial 20", fill="lime")
            main_ball.dx = main_ball.dy = 0
        elif main_ball.dx * main_ball.dy == 0:
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text="YOU LOSE!", font="Arial 20", fill="red")
    root.after(DELAY, main)


# ������� ����, ����� � ��������� ���� ����
root = tkinter.Tk()
root.title("Colliding Balls")
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
balls = create_list_of_balls(NUM_OF_BALLS)
num_of_bad_balls = count_bad_balls(balls)
if 'main_ball' in globals():  # ��� ��������� ��������
    del main_ball
main()
root.mainloop()
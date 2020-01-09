import keyboard
import time
import multiprocessing
import random

area=[]
for i in range(25):
    area.append(["-"]*20)

rows = len(area)
cols = len(["-"]*20)



x=10 #ordinata
y=10 #abcisa

manager=multiprocessing.Manager()
shared_list=manager.list()

snake = [[x, y], [x, y-1], [x, y-2]]
food = [random.randint(1,23), random.randint(1,18)]
shared_list.append("")



def printing():
    while True:

        for i in snake:
            area[i[0]][i[1]]="S"
        for row in range(25):
            print(area[row])
        area[food[0]][food[1]]="F"

        head = snake[0]
        direction = [snake[0][0], snake[0][1] + 1]


        if shared_list[0] == "esc":
            raise Exception("Game stopped!")
        elif shared_list[0] == "up":
            direction = [head[0] - 1, head[1]]
        elif shared_list[0] == "down":
            direction = [head[0] + 1, head[1]]
        elif shared_list[0] == "right":
            direction = [head[0], head[1] + 1]
        elif shared_list[0] == "left":
            direction = [head[0], head[1] - 1]


        new_head = direction
        snake.insert(0,new_head)
        if area[new_head[0]][new_head[1]]=="S":
            raise Exception("GAME OVER!")

        else:
            area[new_head[0]][new_head[1]]="S"


        if snake[0][0]==food[0] and snake[0][1]==food[1]:
            snake.append(new_head)
            food[0] = random.randint(1, 23)
            food[1]=random.randint(1, 18)
        else:
            deleted_element=snake.pop()
            area[deleted_element[0]][deleted_element[1]]="-"
        time.sleep(1)





if __name__ == '__main__':
    printing=multiprocessing.Process(target=printing)

    printing.start()
    while True:
        shared_list[0] = keyboard.read_key()



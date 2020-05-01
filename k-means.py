import math
import random


class coordinate():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def input_coordinate():
    point = []  
    #k = input("输入K值")
    k = 2
    num = 10
    #num = int(input("输入值的个数"))
    #while(num):
    #    x = int(input("输入第"+ num + "的x值"))
    #    y = int(input("输入第"+ num + "的x值"))
    #    temp = coordinate(x,y)
    #    point.append(temp)
    #    num = num - 1
    point.append(coordinate(0,0))
    point.append(coordinate(1,0))
    point.append(coordinate(0,1))
    point.append(coordinate(2,1))
    point.append(coordinate(4,5))
    point.append(coordinate(6,4))
    point.append(coordinate(8,5))
    point.append(coordinate(9,4))
    point.append(coordinate(8,9))
    point.append(coordinate(9,9))
    return point , k , num

def random_num(num):
    random_num_list = []
    while(num):
        random_num_list.append(0 , num-1)
        num = num - 1
    ret = []
    for num in random_num_list:
        while(num in ret):
            num = random.randint(0 , num-1)
            ret.append(num)
            break
        if num in ret:
            continue
        else:
            ret.append(num)
    return ret

    
first_random = random.randint(1,10)
secoden_random =random.randint(1,10)
while (first_random == secoden_random ):
    secoden_random =random.randint(1,10)

def test():
    random_num_list = [1,2,2,3]
    ret = []
    for num in random_num_list:
        while(num in ret):
            num = random.randint(0 , num-1)
            ret.append(num)
            break
        if num in ret:
            continue
        else:
            ret.append(num)

def main():
    #point , k , num = input_coordinate()
    
    test()

if __name__ == "__main__":
    main()
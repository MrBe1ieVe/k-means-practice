import math
import random

class coordinate():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.distance = []
        self.cluster = []
    def append_distance(self,distance):
        self.distance.append(distance)

    def append_cluster(self,coordinate_):
        self.cluster.append(coordinate_)
    

def input_coordinate():
    point = []  
    #k = input("输入K值")
    k = 2
    #num = 10
    #num = int(input("输入值的个数"))
    #while(num):
    #    x = int(input("输入第"+ num + "的x值"))
    #    y = int(input("输入第"+ num + "的x值"))
    #    temp = coordinate(x,y)
    #    point.append(temp)
    #    num = num - 1
    #point.append(coordinate(0,0))
    #point.append(coordinate(1,0))
    #point.append(coordinate(0,1))
    #point.append(coordinate(2,1))
    #point.append(coordinate(4,5))
    #point.append(coordinate(6,4))
    #point.append(coordinate(8,5))
    #point.append(coordinate(9,4))
    #point.append(coordinate(8,9))
    #point.append(coordinate(9,9))

    #test data
    num = 3
    point.append(coordinate(0,0))
    point.append(coordinate(0,1))
    point.append(coordinate(9,9))

    return point , k , num

def cal_euclidean_distance(x1 , x2 , y1 , y2):
    return math.sqrt(math.pow((x1 - x2) , 2) + math.pow((y1 - y2) , 2))

def random_num_list(k):
    random_num_list = []
    count = k
    while(count):
        random_num_list.append(random.randint(0 , k-1))
        count = count - 1
    ret = []
    for num in random_num_list:
        while(num in ret):
            num = random.randint(0 , k-1)
            ret.append(num)
            break
        if num in ret:
            continue
        else:
            ret.append(num)
    return ret

def cal_distance(point , k , num):
    for coordinate_ in point:
        for be_cal in point:
            temp = cal_euclidean_distance(coordinate_.x , be_cal.x , coordinate_.y , be_cal.y)
            coordinate_.append_distance(temp)

def clusting(point , random_num):
    for coordinate_ in point:
        min_ = float('inf') #获取float最大值
        for num in random_num:
            if coordinate_.distance[num] < min_:
                min_ = num
        point[min_].append_cluster(coordinate_)
    

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
    point , k , num = input_coordinate()
    random_num = random_num_list(k)
    cal_distance(point , k , num)
    clusting(point , random_num)

    #test()

if __name__ == "__main__":
    main()
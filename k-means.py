import math
import random
import copy

class coordinate():

    def __init__(self,x,y):
        self.x = x  #坐标x
        self.y = y  #坐标y
        self.distance = []
        

    def append_distance(self, distance):
        self.distance.append(distance)

    def reset_distance(self):
        self.distance = []

class centroid():

    def __init__(self, x, y):
        self.x = float(x)    #归类点x
        self.y = float(y)    #归类点y
        self.cluster = []

    def update_centroid(self, x, y):
        self.x = float(x)    
        self.y = float(y)    

    def append_cluster(self, coordinate_):
        self.cluster.append(coordinate_)

    def reset_cluster(self):
        self.cluster = []

def output_centroid_list(centroid_list):
    print("centroid coordinate:")
    for centroid_ in centroid_list:
            print("(" + str(centroid_.x) + "," + str(centroid_.y) + ")", end=' ')
    print()
    print("="*5)

def output_centroid_cluster(centroid_list):
    for centroid_ in centroid_list:
        print("centroid coordinate:")
        print("(" + str(centroid_.x) + "," + str(centroid_.y) + ")")
        print("the coordinate in cluster:")
        for coordinate_ in centroid_.cluster:
            print("(" + str(int(coordinate_.x)) + "," + str(int(coordinate_.y)) + ")", end=' ')
        print()
    print("="*5)

def input_coordinate():     # input the coordinate
    coordinate_list = []  
    k = int(input("please input the k.(int) "))
    #k = 2
    #num = 10   
    num = int(input("please input how many coordinates you want to set.(int) "))
    i = 1
    while(not i == num+1):
        x = int(input("please input the x coordinate of x"+ str(i) + "(int) "))
        y = int(input("please input the y coordinate of x"+ str(i) + "(int) "))
        temp = coordinate(x,y)
        coordinate_list.append(temp)
        i = i + 1
    #coordinate_list.append(coordinate(0,0))
    #coordinate_list.append(coordinate(1,0))
    #coordinate_list.append(coordinate(0,1))
    #coordinate_list.append(coordinate(2,1))
    #coordinate_list.append(coordinate(4,5))
    #coordinate_list.append(coordinate(6,4))
    #coordinate_list.append(coordinate(8,5))
    #coordinate_list.append(coordinate(9,4))
    #coordinate_list.append(coordinate(8,9))
    #coordinate_list.append(coordinate(9,9))

    #test data
    #num = 3
    #coordinate_list.append(coordinate(0,0))
    #coordinate_list.append(coordinate(0,1))
    #coordinate_list.append(coordinate(9,9))

    return coordinate_list , k , num

def pick_random_centroid(coordinate_list, k, num):     # pick out the random coordinate as the centroid
    pick_random_centroid = []
    centroid_list = []
    count = k

    #
    while(count):
        pick_random_centroid.append(random.randint(0, num-1))
        count = count - 1
    #pick_random_centroid = [1,1] # test data
    result = []     #store the coordinate index
    for num in pick_random_centroid:
        while(num in result):
            num = random.randint(0, num-1)
            if num in result:
                continue    
            else:
                result.append(num)
                break
        if num in result:
            continue
        else:
            result.append(num) 
    #test
    #result =  [1,0]

    #set the centroid
    print("random centroid is")
    for num in result:
        print("(" + str(coordinate_list[num].x) + "," + str(coordinate_list[num].y) + ")")
        x = coordinate_list[num].x
        y = coordinate_list[num].y
        centroid_list.append(centroid(x, y))
    return centroid_list


def cal_euclidean_distance(x1 , x2 , y1 , y2):      # sqrt((x1 - x2)^2 + (y1 + y2)^2)
    return math.sqrt(math.pow((x1 - x2) , 2) + math.pow((y1 - y2) , 2))

def cal_coordinate_distance(coordinate_list, centroid_list):     # calculate the distance between the coordinates and the centroid
    for coordinate_ in coordinate_list:
        for be_cal in centroid_list:
            temp = cal_euclidean_distance(coordinate_.x , be_cal.x , coordinate_.y , be_cal.y)
            coordinate_.append_distance(temp)

def append_cluster_to_centroid(coordinate_list, centroid_list):
    for coordinate_ in coordinate_list:
        min_ = float('inf')     # maximu float
        for distance in coordinate_.distance:
            if distance < min_:
                min_ = distance
                index = coordinate_.distance.index(distance)    # the distance list only store the num
        cloest_centroid = centroid_list[index]        # use the index to get the centroid
        cloest_centroid.append_cluster(coordinate_)

def fisrt_clusting(coordinate_list, k, num):
    centroid_list = pick_random_centroid(coordinate_list, k, num)
    cal_coordinate_distance(coordinate_list, centroid_list)
    append_cluster_to_centroid(coordinate_list, centroid_list)
    output_centroid_cluster(centroid_list)
    return centroid_list

def update_centroid(coordinate_list, centroid_list):
    centroid_change_flag = True
    copy_centroid_list_cluster = []
    while(centroid_change_flag): #while centroid dont change, break
        
        temp = []
        for centroid_ in centroid_list:
            temp.append(centroid_.cluster)
        if copy_centroid_list_cluster == temp:     
            centroid_change_flag = False
            break
        copy_centroid_list_cluster = []
        for centroid_ in centroid_list:
            copy_centroid_list_cluster.append(centroid_.cluster)  
        # because of the deep copy and the shallow copy
        # so im using centroid coordinate list to check

        for centroid_ in centroid_list:
            x_total = 0.0
            y_total = 0.0
            for coordinate_ in centroid_.cluster:   # the point in cluster
                x_total = coordinate_.x + x_total
                y_total = coordinate_.y + y_total
            x = x_total / len(centroid_.cluster)    
            y = y_total / len(centroid_.cluster)
            centroid_.update_centroid(x, y)
        
        for coordinate_ in coordinate_list:
            coordinate_.reset_distance()

        for centroid_ in centroid_list:
            centroid_.reset_cluster()

        cal_coordinate_distance(coordinate_list, centroid_list)
        append_cluster_to_centroid(coordinate_list, centroid_list)
        
        output_centroid_cluster(centroid_list)





def main():
    coordinate_list , k , num = input_coordinate()
    centroid_list = fisrt_clusting(coordinate_list, k, num)
    update_centroid(coordinate_list, centroid_list)
    print("Final Result：")
    print()
    output_centroid_cluster(centroid_list)

"""
1.set the coordinate
first_clusting():
    2.pick out random coordinate as centroid
    3.clustering 
update_centroid():
    4.update centroid until dont change
5.output the cluster
"""

if __name__ == "__main__":
    main()
#COVID centres
import math


TESTING_CENTRES = [["NEW_YORK" , [40.7128,74.0060]],  #[NORTH,WEST]
["CHICAGO" ,[41.8781,87.6298]],
["DENVER" ,[39.7392,104.9903]],
["LOS_ANGELES",[34.0522,118.2437]]]

friend_location =[28.5383,81.3792]
min_dist = -1
centre = None
for city in TESTING_CENTRES:
    n_diff=abs(city[1][0]-friend_location[0])
    w_diff = abs(city[1][1]-friend_location[1])
    # 60 and 54 as mentioned in problem statement that a latitude is around 60 miles and longitude 54 miles
    n_diff = n_diff*60
    w_diff = w_diff*54
    dist = math.sqrt(n_diff**2+ w_diff**2)
    if dist < min_dist or min_dist==-1:
        min_dist = dist
        centre = city[0]
print("Closest centre:", centre)
print("Travel Distance:", round(min_dist,3), " miles")
#hour hand : 30 degrees in 1 hr => 2.5 degrees per 5 minutes
#minute hand: 360 degrees in 1 hr => 30 degrees per 5 minutes
for i in range (0,12):
    for j in range (0,12):
        hr_angle = 30*i+2.5*j - 90
        min_angle = 30*j
        diff = (hr_angle-min_angle)%360

#abs() is not necessary but the if condition is required as otherwise angle at 9:00 is 270 while at 3:00 is 90 which should not be the case
        if diff> 180:
            diff = 360 -diff

# comparing with 3 as starting is 9 and 12 PM is a corner case, if done without it, the program will show 00 PM 
#for a general start time, the if conditions can be modified as "if start+i == 12" and similarly others
        if i<3:
            print(9+i,":",str(j*5).rjust(2,'0'),"AM","-",diff)
        elif i==3:
            print(9+i,":",str(j*5).rjust(2,'0'),"PM","-",diff)
        else:
            print(9+i-12,":",str(j*5).rjust(2,'0'),"PM","-",diff)
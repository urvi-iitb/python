#hour hand : 30 degrees in 1 hr => 2.5 degrees per 5 minutes
#minute hand: 360 degrees in 1 hr => 30 degrees per 5 minutes
for i in range (0,12):
    for j in range (0,12):
        hr_angle = 30*i+2.5*j - 90
        min_angle = 30*j
        diff = abs(hr_angle-min_angle)%360
        if diff> 180:
            diff = 360 -diff
        if i<3:
            print(9+i,":",str(j*5).rjust(2,'0'),"AM","-",diff)
        elif i==3:
            print(9+i,":",str(j*5).rjust(2,'0'),"PM","-",diff)
        else:
            print(9+i-12,":",str(j*5).rjust(2,'0'),"PM","-",diff)
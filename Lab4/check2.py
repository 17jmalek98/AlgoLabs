x =[[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]];
y = [[11,1100],[1,10]]
i = 0;
w = 100;
max = 0;
maxval = 0;
total = 0;
totalval = 0;
while(total < w):
    max = 0;
    maxval = 0;

    i = 0;
    while(i < len(x)):
        if(x[i][0] < w):
            #print(x[i][1]/float(x[i][0]))
            if(x[i][1]/float(x[i][0]) > maxval):

                maxval = x[i][1]/float(x[i][0]);

                max = i;
        i+=1;
        
    if((total + x[max][0]) < w):
        print("adding")
        print(x[max])
        totalval += x[max][1]
        total += x[max][0]
        del x[max]
    else:
        if(len(x) > 1):
            #print("deleting ")
            #print(x[max])
            del x[max]
        else:
            break
print totalval;

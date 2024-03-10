list = [(0,0), (1,0), (1,1), (1,2)]

ad = 0

for i in range(0, len(list), 1):
    adx = (list[i][0] - list[i+1][0])**2
    ady = (list[i][1] - list[i+1][1])**2
    ad = ad + (adx + ady)**(1/2)

print(ad)
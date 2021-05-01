# Hello World program in Python
    
# print ("Hello World!")
import sys, math
from pprint import pprint
cases = []

sources = 2
secondary = 8
primary = 3

# secondary_list : list of remaing end locations to be transported
# primary_capasity : capacity dictionary of distribution locations

def find_min(curr_sec,capacity,requirement_secondary,Primary,source_primary,primary_secondary):
    ii=curr_sec
    if(ii>=8):
        return [0,[]]


    # print("hii",pri,curr_sec)

    mn = math.inf
    path=[]
    for jj in range(Primary):
        if(capacity[jj]>=requirement_secondary[ii]):
            capacity[jj]=capacity[jj]-requirement_secondary[ii]
        else:
            continue
    # for jj in range(len(primary_secondary)):
        # print(jj,ii)

        for kk in range(sources):
            
            # print(source_primary[kk][jj] + primary_secondary[jj][ii])
            rest_cost,rest_path=find_min(curr_sec+1,capacity,requirement_secondary,Primary,source_primary,primary_secondary)
            cost=rest_cost+source_primary[kk][jj] + primary_secondary[jj][ii]
            

            if cost < mn:
                mn = cost
                # print(mn)
                path=rest_path
                path.append([kk,jj,ii])

        capacity[jj]=capacity[jj]+requirement_secondary[ii] 
              
    return [mn,path]
        

# nums=[0,1,2,4,8,16,32,64,128]
for i in range(2**secondary-1):

    binary = bin(i)[2:]
    
    # binary = '00000011'

    binary = '0'*(secondary-len(binary)) + binary   

    
    primary_capacities=[60,100,80]
    secondary_capacities=[60,60,60,60,60,60,60,60]
    requirement_secondary=[10,40,20,50,30,20,10,10]

    capacity=primary_capacities

    pri=[]
    for j,val in enumerate(binary):
        if val=='1':
            pri.append(j)
            capacity.append(secondary_capacities[j-1])
    Primary = primary+len(pri)
    

    #print(Primary, pri, binary)

    source_primary = [
                        [1, 1, 1],
                        [1, 1, 1]
                    ]
    primary_secondary = [
                            [1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1]
                        ]
    source_secondary = [
                            [1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1]
                        ]

    secondary_secondary = [
                            [0, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 1, 1, 1, 1, 1, 1],
                            [1, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1, 0]
                        ]
    


    source_primary = [
                        [1400, 600, 700],
                        [1500, 950, 150]
                    ]
    primary_secondary = [
                            [250, 220, 260, 790, 850, 360, 2210, 2180],
                            [120, 1030, 950, 200, 520, 510, 1180, 1340],
                            [1800, 1720, 1760, 820, 745, 1180, 700, 650]
                        ]
    source_secondary = [
                            [1740, 1620, 1570, 780, 1000, 1100, 840, 1200],
                            [1900, 1750, 1800, 850, 780, 1210, 570, 630]
                        ]

    secondary_secondary = [
                            [0, 200, 250, 1040, 1100, 600, 2400, 2450],
                            [200, 0, 370, 1000, 1000, 500, 2350, 2400],
                            [250, 370, 0, 980, 1070, 530, 2400, 2430],
                            [1040, 1000, 980, 0, 300, 430, 1450, 1480],
                            [1100, 1000, 1070, 300, 0, 475, 1370, 1400],
                            [600, 500, 530, 430, 475, 0, 1300, 1330],
                            [2400, 2350, 2400, 1450, 1370, 1300, 0, 350],
                            [2450, 2400, 2430, 1480, 1400, 1330, 350, 0]
                        ]

    source_primary = [
                        [626,1498, 1176],
                        [2210, 1534, 952]
                    ]
    primary_secondary = [
                            [347, 800, 646, 2460, 2070, 2800, 1570, 1855],
                            [1900, 8870, 1400, 1784, 1554, 1030, 135, 1010],
                            [1492, 1627, 1317, 1187, 682, 253, 1870, 1086]
                        ]
    source_secondary = [
                            [570, 625, 145, 1844, 1556, 2410, 1395, 1225],
                            [2177, 1828, 1549, 276, 280, 1928, 1530, 496]
                        ]

    secondary_secondary = [
                            [0, 1012, 725, 2435, 2037, 3003, 1773, 1816],
                            [1012, 0, 556, 2065, 1797, 1817, 777, 1311],
                            [725, 556, 0, 1809, 1409,2225, 1229, 1189],
                            [2435, 2065, 1809, 0, 515, 2238, 1842, 805],
                            [2037, 1797, 1409, 515, 0, 1948, 1558, 515],
                            [3003, 1817, 2225, 2238, 1948, 0, 1127, 1452],
                            [1773, 777, 1229, 1842, 1558, 1127, 0, 1060],
                            [1816, 1311, 1189, 805, 515, 1452, 1060, 0]
                        ]



    
    

    for x in pri:
        primary_secondary.append(secondary_secondary[x])
        for i in range(sources):
            source_primary[i].append(source_secondary[i][x])
    
    # pprint(source_primary)
    
    

    #print(Primary, secondary)
    #print(len(primary_secondary[0]), len(source_primary[0]))
    # 3*8, 2*3
    


    truck_weight = 1

    secondary_weight = [10.6, 2.3, 1.8, 18, 12.7, 10.7, 20, 15]  
    

    for i in range(secondary):
        secondary_weight[i] = math.ceil(secondary_weight[i]/truck_weight)
                                      
    secondary_relocation = [200]*secondary                         

    arr = []
    paths = []

    cost,path=find_min(0,capacity,requirement_secondary,Primary,source_primary,primary_secondary)
    
    # arr.append(cost);
    # paths.append(path)

    # for ii in range(secondary):
        
    #     mn = math.inf
    #     path = []
    #     for jj in range(Primary):
    #     # for jj in range(len(primary_secondary)):
    #         # print(jj,ii)

    #         for kk in range(sources):
                
    #             # print(source_primary[kk][jj] + primary_secondary[jj][ii])
    #             if source_primary[kk][jj] + primary_secondary[jj][ii] < mn:
    #                 mn = source_primary[kk][jj] + primary_secondary[jj][ii]
    #                 # print(mn)
    #                 path = [kk, jj, ii]
    #     # print(mn,"----------------------------------------")
    #     arr.append(mn)
    #     paths.append(path)
    # print(values)


    #arr = arr[::-1]
    # value = 0
    # for i in range(secondary):
    #     value += secondary_weight[i]*arr[i]
    
    #print(value)
    for x in pri:
        cost += secondary_relocation[x]

    # value /= secondary

    print(binary, cost)
    cases.append([cost, binary, pri, path])

    # break
cases.sort()

# print(cases)

print(path)


print("The minimum cost is:", cases[0][0])
print("Secondary which are relocated are:", ' '.join([str(x+1) for x in cases[0][2]]))

for i,p in enumerate(cases[0][3]):
    print("Path {} --> Source {} to Primary {} to Secondary {}".format(i+1, p[0]+1, p[1]+1, p[2]+1))
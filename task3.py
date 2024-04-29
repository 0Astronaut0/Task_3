import random
def matrix_making(num):
    list_3d = []
    while (len(list_3d) <= num):
        list_status = []
        for _ in range(4):
            row = []
            for _ in range(3):
                row.append(random.choice([True,False]))
            list_status.append(row)
        t_count = 0
        f_count = 0
        for row in list_status:
            for j in row:
                if j == True:
                    t_count+=1
                else:
                    f_count+=1
        if(t_count == 6 and f_count == 6 and not (list_status in list_3d)):
            list_3d.append(list_status)
    return list_3d
out = matrix_making(923)
suspect_list = ['A','B','C','D']
score_list = [0,0,0,0]

for m in out:
    if m[0][0] == True and m[2][0] == False:
        for n,i in enumerate(m):
            for x in i:
                if(x == False):
                    score_list[n]+=1   
                    
if m[0][0] == False and m[2][0] == True:
        for n,i in enumerate(m):
            for x in i:
                if(x == False):
                    score_list[n]+=1 
                      
if m[1][0] == True and m[3][0] == False:
        for n,i in enumerate(m):
            for x in i:
                if(x == False):
                    score_list[n]+=1  
                     
if m[1][0] == False and m[3][0] == True:
        for n,i in enumerate(m):
            for x in i:
                if(x == False):
                    score_list[n]+=1   

print("the thife is:",suspect_list[score_list.index(max(score_list))])
   
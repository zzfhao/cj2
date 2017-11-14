import numpy as np
string1 = input()
string2 = input()
#string1 = 'IS_ME_TO!'
#string2 = 'ALGORITHMS!'
list1 = list(string1)
list2 = list(string2)

l1 = len(list1)
l2 = len(list2)
d = np.zeros((l1,l2))

for i in range(l1):
    for j in range(l2):
        if list1[i] == list2[j]:            
            if i == 0 or j == 0:
                d[i][j]=1    
            else:
                d[i][j]=d[i-1][j-1]+1
        else:
            d[i][j]=max(d[i-1][j],d[i][j-1])
#0: upper arrow, 1:left arrow, 2: diagonal arrow
#print(d)
#print ('longest common subsequence is:')
#numli = int(d[l1-1][l2-1])-1
result = list()
def lcs(d,list1,list2,n,m):
   # print(n,m)
   # print(d[n-1][m],d[n][m-1])
    if n < 0 or m < 0:
        return      
    elif n == 0 and d[n,m] > 0:
        if list1[n] == list2[m]:
            #print(list1[n] ) 
            result.insert(0,str(list2[m]))      
            return
        lcs(d,list1,list2,n,m-1)
    else:
        if list1[n] == list2[m]:
            #print(list1[n] ) 
            result.insert(0,str(list2[m]))
            lcs(d,list1,list2,n-1,m-1)
        elif d[n-1][m] >= d[n][m-1]:
            lcs(d,list1,list2,n-1,m)
        else:       
            lcs(d,list1,list2,n,m-1)
n = l1-1 
m = l2-1
lcs(d,list1,list2,n,m)
res_str = ''.join(result)
print(res_str)

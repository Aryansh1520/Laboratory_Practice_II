jobs=["j1", "j2", "j3", "j4", "j5"]
profit=[15,27,10,100, 150]
deadl=[2,3,3,3,4]

z=list(zip(jobs,profit,deadl))                         # important 
z=sorted(z, key= lambda x:x[1], reverse=True)    #important sorted not sort, lambda not lamda, t capital in true, also = , check all
                                                 #reverse sort coz we first take highest price job

print(max(deadl))

Tprofit=0                         
ans=[]                          #to store the final answers of jobs / also we will use this to check weather aparticular slot is empty instead of making a completely new variable list

for i in range(len(jobs)):
    ans.append('null')

for i in range(len(z)):

    x=z[i]                          #using 'job' keyword we can access inside the tupple, coz profitNJobs is list of tuples vs job is one tuple
    for j in range(x[2], 0, -1):    # reverse coz if fill from backside in js algo, x[] x on 2nd index x[2] contains deadl

        if ans[j]=='null':
            ans[j]= x[0]     
            Tprofit += x[1]
            break

print(ans)
print(Tprofit)

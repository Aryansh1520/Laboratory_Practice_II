n = int(input("Enter the number of jobs : "))
z = []
for _ in range(n):
    name = str(input("Enter name of the job : "))
    profit = int(input("Enter profit : "))
    deadline = int(input("Enter deadline : "))
    z.append((name,profit,deadline))

z = sorted(z ,key = lambda x:x[1],reverse = True)
t_profit = 0
ans = ['null'*n]

for i in range(n):
    x = z[i]
    for j in range(x[2],0,-1):
        if ans == 'null':
            ans = x[0]
            t_profit += x[1]
            break
print(ans)
print(t_profit)

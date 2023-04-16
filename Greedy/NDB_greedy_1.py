n, m, k=map(int, input().split())
nums=list(map(int, input().split()))

nums.sort(reverse=True)
cnt=0
result=0
if m<=k:
    print(m*nums[0])
else:
    for i in range(m):
        cnt+=1
        if cnt==(k+1):
            result+=nums[1]
            cnt=0
        else:
            result+=nums[0]
        print(result)
print(result)



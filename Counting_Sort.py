# Sort Colors
arr = [2,0,2,1,1,0]
max_val=max(arr)
count=[0]*(max_val+1)
for num in arr:
    count[num]+=1
j=0
for i in range(len(count)):
    while count[i]>0:
        arr[j]=i
        j+=1
        count[i]-=1
print(arr)
        
# Height Checker
heights = [1,1,4,2,1,3]
max_val=max(heights)
count=[0]*(max_val+1)
for num in heights:
    count[num]+=1
res=[]
for i in range(len(count)):
    while count[i]>0:
        res.append(i)
        count[i]-=1
print(res)
res=[1,1,1,2,3,4]
count=0
for i in range(len(heights)):
    if heights[i]==res[i]:
        count+=1
print(count)
       
arr=[4,2,2,8,1,1,3]
max_val=max(arr)
count=[0]*(max_val+1)
for num in arr:
    count[num]+=1
for i in range(1,len(count)):
    count[i]+=count[i-1]
output=[0]*len(arr)
for i in reversed(arr):
    output[count[i]-1]=i
    count[i]-=1
print(output)
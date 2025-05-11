f = open('17.txt')
nums = list(map(int, f.readlines()))
count = 0
minnum = 20001
max1= 0

for i in range(len(nums)-1):
    if len(str(nums[i]))==3 and nums[i]%10==5:
        minnum = min(minnum, nums[i])
for i in range(len(nums)-1):
    if (len(str(nums[i]))==4) != (len(str(nums[i+1]))==4) and ((nums[i]**2 + nums[i+1]**2) % minnum==0):
        count+=1
        max1 = max(max1, (nums[i]**2 + nums[i+1]**2))
print(count, max1)

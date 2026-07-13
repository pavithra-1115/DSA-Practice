#1 largest number
#date = 13-07-2026
arr = [7,8,4,2,6]
larg = arr[0]
for i in range(len(arr)):
    if arr[i] > larg:
        larg = arr[i]
print(larg)

#2 smallest number
arr = [7,8,4,2,6]
small = arr[0]
for i in range(len(arr)):
    if arr[i] < small:
        small = arr[i]
print(small)

#3 Reverse array
arr = [7,8,4,2,6]
arr2 = []
for i in range(len(arr)-1,-1,-1):
    arr2.append(arr[i])
print(arr2)


arr = [7,8,4,2,6]
left = 0
right = len(arr)-1

while left < right:
    arr[left],arr[right] = arr[right],arr[left]
    left += 1
    right -= 1

print(arr)

#4.remove duplicates
arr1 = [1,2,1,3,4,2]
arr2 = []
for i in arr1:
    if i not in arr2:
        arr2.append(i)
print(arr2)

#5 rotate array left
arr = [7,8,4,2,6]
k = 1
result = arr[k:] + arr[:k]
print(result)

#6 rotate array right 
arr = [7,8,4,2,6]
k = 1
result = arr[-k:] + arr[:-k]
print(result)

#7.count frequency
arr = [1,2,4,8,2,1,4,4]
freq = {}
for i in arr:
    if i in freq:
      freq[i] = freq[i]+1
    else:
        freq[i] = 1
print(freq)


arr = [1,2,4,8,2,1,4,4]
freq = {}
for num in arr:
    freq[num] = freq.get(num,0) + 1

print(freq)

#8.move zeros at end
arr = [1,0,2,0,3,0]
arr1 = []
arr2 = []
for i in arr:
    if i != 0:
        arr1.append(i)
    else:
        arr2.append(i)
result = arr1 + arr2
print(result)

#9 move zeros at starting
arr = [1,0,2,0,3,0]
arr1 = []
zero_count = 0
for i in arr:
    if i != 0:
        arr1.append(i)
    else:
        zero_count += 1
result = [0]*zero_count + arr1
print(result)

#10 merge  2 arrays 
arr1 = [1,2,3]
arr2 = [4,5,6]
result = arr1 + arr2
print(result)


arr1 = [1,3,5]
arr2 = [2,4,6]
 

i = 0
j = 0
result = []
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i+=1
    else:
        result.append(arr2[j])
        j+=1

while i < len(arr1):
    result.append(arr1[i])
    i+=1

while j < len(arr2):
    result.append(arr2[j])
    j+=1

print(result)

#11 find missig number
arr = [1,2,3,5]
n = len(arr) + 1
total = n*(n+1)//2
missing_num = total - sum(arr)
print(missing_num)

#12 linear search

arr = [10,20,30,40,50]
target = 40
for i in arr:
    if i == target:
        print("found",target)

#13 binary search
arr = [10,20,30,40,50,60,70]

target = 40
left = 0
right = len(arr)-1
while left < right:
    mid = (left + right)//2
    if arr[mid] == target:
        print("target",mid)
        break
    elif arr[mid] <  target:
        left = mid+1
    else:
        right = mid-1

print("not found")

#14.average
arr = [10,20,30,40,50]
avg = sum(arr)/len(arr)
print(avg)

#15. sum of arr
arr = [10,20,30,40,50]
sum = 0
for i in arr:
    sum += i
print(sum)

#16. pair sum

arr = [2,7,11,15]
target = 13
left = 0
right = len(arr)-1
while left < right:
    total = arr[left] + arr[right] 

    if total == target:
        print(arr[left],arr[right])
        break
    elif total  < target:
        left += 1
    else:
        right -= 1


arr = [2,7,11,15]

target = 9

seen = {}

for i in range(len(arr)):

    complement = target - arr[i]

    if complement in seen:
        print(seen[complement], i)
        break

    seen[arr[i]] = i


arr = [2,7,11,15]

target = 9

seen = set()

for num in arr:

    complement = target - num

    if complement in seen:
        print(complement , num)
        

    seen.add(num)

#17.reverse using 2 pointers

arr = [1,2,3,4,5]
for i in range(len(arr)):
    for j in range(len(arr)-1,-1,-1):
        arr[i],arr[j] = arr[j],arr[i]
print(arr)
     
#18.prefix sum

arr = [2,4,6,8,10]
prefix = [0]*len(arr)
prefix[0] = arr[0]
for i in range(1,len(arr)):
    prefix[i] = prefix[i-1]+arr[i]
print(prefix)

left = 1
right = 3
if left == 0:
    print(prefix[right])
else:
    print(prefix[right]-prefix[left-1])


#19.Remove duplicates in sorted array
arr1 = [1,2,3,3,4,2,5]
arr2 = []
for i in arr1:
    if i not in arr2:
        arr2.append(i)
print(arr2)


#20 maximum subarray
arr = [-2,1,-3,4,-1,2,1,-5,4]

current_sum = 0
max_sum = arr[0]

i = 0
while i < len(arr):
    current_sum += arr[i]
    if current_sum > max_sum:
        max_sum = current_sum

    if current_sum < 0:
        current_sum = 0
    
    i+=1

print(max_sum)

arr = [1,2,3,5]

n = len(arr) + 1

xor1 = 0
xor2 = 0

for i in range(1, n + 1):
    xor1 ^= i

for num in arr:
    xor2 ^= num

print(xor1 ^ xor2)
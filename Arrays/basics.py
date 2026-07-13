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

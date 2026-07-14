#21 Rotate array left by one step
arr = [1,2,3,4,5]
temp = arr[0]
n = len(arr)-1
for i in range(len(arr)-1):
    arr[i] = arr[i+1]
arr[n]  = temp
print(arr)

#22 Rotate array right by one step
arr = [1,2,3,4,5]
temp = arr[len(arr) - 1]
for i in range(len(arr)-1,-1,-1):
    arr[i] = arr[i-1]

arr[0] = temp
print(arr)

#23 Rotate array right by k steps
arr = [1,2,3,4,5]
result = [0]*len(arr)
k = 2
for i in range(len(arr)):
    new_index = (i+k)%len(arr)
    result[new_index] = arr[i]

print(result)

#24 Rotate array left by k steps
arr = [1,2,3,4,5]
n = len(arr)
result = [0]*n
k = 2
for i in range(n-1,-1,-1):
    new_index = (i-k+n)%n
    result[new_index] = arr[i]

print(result)


arr = [1,2,3,4,5]
result = [0]*len(arr)
k = 2
for i in range(len(arr)):
    new_index = (i-k)%len(arr)
    result[new_index] = arr[i]

print(result)


#25 
arr = [1,2,3,4,5,6,8]
n = len(arr)+1
total = n*(n+1)//2
missing_number = total - sum(arr)
print(missing_number)

arr = [10,11,12,13,15]
start = min(arr)
end = max(arr)
expected = 0
for i in range(start,end+1):
    expected += i

print(expected - sum(arr))



arr = [10,11,12,14,15]

start = min(arr)
end = max(arr)

expected = 0

for i in range(start, end + 1):
    expected += i

print(expected - sum(arr))


start = min(arr)
end = max(arr)

expected = sum(range(start, end + 1))

print(expected - sum(arr))


arr = [1,2,5,6,8]

s = set(arr)

for i in range(min(arr), max(arr) + 1):
    if i not in s:
        print(i)

      
#26 duplicate number
arr = [1,3,2,4,2,3]
seen = set()
result = []
for num in arr:
    if num not in result:
        seen.add(num)
        result.append(num)
print(result)


#27  find all pairs with given sum

arr = [2,7,11,0,9,5,4,15]
target = 9
seen = set()
for i in arr:
    complement = target - i

    if complement in seen:
        print(complement,i)
    seen.add(i)


arr = [2,7,11,0,1,9,5,4,8]

#arr = [1,2,3,4,5,6,7,8]


target = 10
left = 0
right = len(arr)-1

while left < right:
    total = arr[left] + arr[right]
    if total == target:
        print(arr[left],arr[right])
        left += 1
        right -= 1

    elif total < target:
        left += 1

    else:
        right -= 1

#28 find subarray with maximum sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
current_ele = 0
max_sub = arr[0]
for i in arr:
    current_ele += i
    if current_ele > max_sub:
       max_sub = current_ele

    if   current_ele < 0:
        current_ele = 0


print(max_sub)
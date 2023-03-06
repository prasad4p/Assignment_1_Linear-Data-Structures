# Assignment_number_1= Linear Data Structures
# Question_number_1 = Write a program to find all pairs of an integer array whose sum is equal to a given number?


def find_pairs(arr,target):
    pairs = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [2,5,4,6,9,8]
target = 10
print(find_pairs(arr,target))



#frequency of each element in the array
#[1,2,4,5,2,3,1,1,]  {1:3, 2:2, 4:1, 5:1, 3:1}
def frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq 
print(frequency([1, 2, 4, 5, 2, 3, 1, 1])) # Output: {1: 3, 2: 2, 4: 1, 5: 1, 3: 1}
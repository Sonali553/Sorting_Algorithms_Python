#Insertion sort
# star building a sequence with one element
#for each iteration compare the taken element with sorted array
# and place it in the correct position in sorted sequence
#O(n^2) time complexity
lst = [1, 35, 30, 39, 45,2,9, 0]
for start in range(0, len(lst)):
    pos = start
    while(pos > 0 and lst[pos - 1] > lst[pos]):
        (lst[pos], lst[pos - 1]) = (lst[pos - 1], lst[pos])
        pos = pos - 1
print(lst)

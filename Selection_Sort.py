#Selection Sort
#check slices like lst[0:len(lst)],lst[1:len(lst)],lst[2:len(lst)],...
#In each iteration find the minimum and push it to the left
#It works slower beyond 5000 values 0r 7 to 10 digits
lst = [13,12,50,23,45]
for start in range(len(lst)):
    minpos = start
    for i in range(start+1, len(lst)):
        if(lst[i] < lst[minpos]):
            minpos = i
    if minpos != start:
     (lst[start], lst[minpos]) = (lst[minpos], lst[start])
print(lst)

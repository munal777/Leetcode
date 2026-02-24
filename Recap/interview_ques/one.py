def mainFunc(x,arr):
    count = 0

    for n in arr:
        if n <= x:
            count += 1
    
    return count

x = 9
arr = [10,1,2,8,4,5]

print(mainFunc(x,arr))
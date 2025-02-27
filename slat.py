def mysum(*numbers):
    sum = 0
    for num in numbers:
        sum +=num
    return(sum)

print(mysum(2,3,4,5))
def mean(*nums):
    avg =mysum(*nums)/len(nums)
    return(avg)

print(mean(2,4,4,6))
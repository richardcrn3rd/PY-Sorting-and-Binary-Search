import numpy as np

b = np.array([1,5,-2,10])

# iterative approach
def array_sum(numberArr):
    arrSum = 0
    for i in numberArr:
        arrSum = arrSum + i
    return arrSum

#print(array_sum(b))

def array_sum_r_2(numberArr, i=0, count=0):
    print(i)
    print(count)
    if len(numberArr) == i:
        print(numberArr[i] + count)
    else:
        count += numberArr[i]
        i+1
        array_sum_r_2(numberArr, i, count)

print("Cody's first draft")
array_sum(b)

# uncomment the below function to test the recursive approach
def array_sum_recursive(numberArr):
    if len(numberArr) == 1:
        return numberArr[0]
    
    # Recursive case
    return numberArr[0] + array_sum(numberArr[1:])

print(array_sum_recursive(b))


# uncomment the below line to test the solution using the NumPy sum operator
print(b.sum())
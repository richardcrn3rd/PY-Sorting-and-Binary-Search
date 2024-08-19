# code your iterative algorithm here
# code your iterative algorithm below here

def binary_search(data, el):
    first = 0
    last = len(data)-1 
    found = False

    while first <= last and not found:
        mid = (first+last)//2

        print("Checking: " + str(data[mid]))

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]: 
                last = mid-1
            else: 
                first = mid+1
    return found

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31,40]

# print(binary_search(test_list, 12))
print(binary_search(test_list, 19))
# print(binary_search(test_list, 112))
# print(binary_search(test_list, 0))
# print(binary_search(test_list, 4))

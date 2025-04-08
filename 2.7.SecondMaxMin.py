def input_array():
    array = []
    while True:
        try:
            line = input().strip()
            if line == "":
                break 

            # Convert the line into a list of integers
            for element in line.split():
                row = int(element)                
                array.append(row)

        except EOFError:
            break
    return array

def find_second_max_min(array):
    n = len(array) 
    arr = array.copy()
    arr.sort()

    
    if n < 1:
        return Exception()

    # Check has only one element or two elements
    if n < 3:
        if n == 2:
            return arr[0], arr[1]
        return Exception("Do not find second max, min in an array has 1 element")#arr[0], arr[0]
    
    arr_reverse = []
    for i in range(len(arr)):
        arr_reverse.append(arr[n - 1 - i])

    a = arr_reverse[1] # second_max
    b = arr[1] # second_min
    return a, b

array = input_array()
print(find_second_max_min(array))
def inputArray():
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
    
def sort_array(array):
    r = array.sort()
    return r
    
def printArray(r):
    for i in r:
        print(i)

arr = inputArray()
r = sort_array(arr)
printArray(arr)
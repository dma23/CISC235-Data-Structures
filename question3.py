import random
import time 

def algoA(randValues, target):
    """
    algoA is a linear search algorithm 
    Takes in two parameters, randValues as a list of integers and target as a list of target values to search for
    """
    for i in randValues:
        if i == target:
            return True
    return False

def algoB(randValues, target):
    """
    algoB is a binary search algorithm 
    Takes in two parameters, randValues as a list of integers and target as a list of target values to search for
    """
    # randValues is sorted before being passed in as a variable
    high = len(randValues) - 1
    low = 0
    # program continues to iterate the list until it cannot cut the list any further
    while low <= high: 
        mid = (high + low) // 2 
        # if the target value is greater than the current midpoint, the program will search the top half of the current midpoint
        if randValues[mid] > target:
            high = mid - 1
        # if the target value is smaller than the current midpoint, the program will search the bottom half of the current midpoint
        elif randValues[mid] < target: 
            low = mid + 1
            #count += 1
        # if the midpoint is neither higher or lower than the target, then we have found the target value and return true
        else:
            return True
    # if reached, target value was not found and return false  
    return False

def mergeSort(randValues): 
    """
    MergeSort algorithms divide the array into L/R sides recursively until it is a single node and sorts it while putting it back together
    The average time complexity for MergeSort is O(nlogn)   
    """
    if len(randValues) > 1:
        mid = len(randValues)//2
        # Dividing the array elements in half
        leftSide = randValues[:mid]
        rightSide = randValues[mid:]
        # Sorting left and right sides 
        mergeSort(leftSide)
        mergeSort(rightSide)
        # temp values, i/j used for left/right side values, k used for moving through randValues
        i = 0
        j = 0
        k = 0
        # compares the values of the left and right side
        while i < len(leftSide) and j < len(rightSide):
            # compares values of left and right side, swaps if statement is met
            if leftSide[i] < rightSide[j]:
                randValues[k] = leftSide[i]
                i += 1
            else:
                randValues[k] = rightSide[j]
                j += 1
            # move onto next value
            k += 1
        
        while i < len(leftSide):
            randValues[k] = leftSide[i]
            i += 1
            k += 1
    
        while j < len(rightSide):
            randValues[k] = rightSide[j]
            j += 1
            k += 1
    return randValues

def createList(n):
    # Creating a list S, of values
    # List size is passed through the n variable
    S = []
    for i in range(n):
        S.append(random.randrange(2, n * 100, 2))
    return S

def createSearchList(random_list, k):
    search_list = []
    # choose at least 10 search values
    num_targets = 10 + k
    #print(k)
    # get k values in randomly generated list 
    for i in range(0, num_targets//2):
        search_list.append(random_list[random.randint(0,len(random_list)-1)])
        odd_number = random.randrange(1, None, 2)
        search_list.append(odd_number)
    return search_list

def algoTest():
    # not necessary to the assignment, testing pruposes only
    # running both algorithms on their own to test functionality 
    n = [1000, 5000, 10000]
    # creates and iterates through the n array
    for i in n:
        # print(i)
        # creates a random list and random target list based on the initial n value
        randValues = createList(i)
        target_list = createSearchList(randValues)
        
        for target in target_list:
            # searches for every target in the target array using algoA (Linear Search) and algoB (Binary Search)
            # prints true for target found, false for target not in array
            print(algoA(randValues, target))
            print(algoB(randValues, target))

def getBinaryTime(lst, target_list):
    # Get time for binary search
    bTime = 0
    # starts timing how long it takes to search through the target list
    start = time.perf_counter()
    mergeSort(lst)
    for target in target_list:
        algoB(lst, target)
    stop = time.perf_counter()
    bTime = stop - start
    print("Took %s seconds for binary search with %s targets on a %s element list" %(bTime, len(target_list), len(lst)))
    return bTime

def getLinearTime(lst, target_list):
    # get time for linear search
    aTime = 0
    # starts timing how long it takes to search through the target list
    start = time.perf_counter()
    for target in target_list:
        algoA(lst, target)
    stop = time.perf_counter()
    aTime = stop - start
    print("Took %s seconds for linear search with %s targets on a %s element list" %(aTime, len(target_list), len(lst)))
    return aTime

def main():
    """
    To get the smallest k value, I started off with the minimum number of targets and incremented it by 1 each time the returned data 
    showed that the linear search was faster

    I used time.perf_counter() to get the speed of each search operation 
    (I know the lecture used timeit but I prefer the perf_counter since it was more simplistic) 
    """
    k_values = []
    n = [1000, 5000, 10000]
    for i in n:
        randValues = createList(i)
        k = 10 # defaults to 10 targets in createSearchList
        aTime = 0
        bTime = 0
        while(aTime <= bTime): # while linear search is faster
            targets = createSearchList(randValues, k+1)
            aTime = getLinearTime(randValues, targets)
            bTime = getBinaryTime(randValues, targets)
            # if linear search takes longer, append that k value to a list
            if aTime > bTime:
                k_values.append(k)
                break
                
            k += 1
    
    print("Minimum K targets for: %s elements:%s, %s elements:%s, %s elements:%s" %(n[0],k_values[0],n[1],k_values[1],n[2],k_values[2])) 

main()


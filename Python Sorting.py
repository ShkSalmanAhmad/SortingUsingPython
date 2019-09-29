import random
import time
array=[]


def menu():


    print("************MAIN MENU**************")
    print()

    choice = input("""
                      1: Bubble Sort
                      2: Merge Sort
                      3: Counting Sort
                      4: Insertion Sort
                      5: Selection Algo
                      6: (Q)uit/Log Out

                      Please enter your choice: """)
#    if choice=="1" or choice=="2" or choice=="3" or choice=="4" or choice=="5":
#        size=100
#        print ("\t\t",end=" ")
#        for i in range(10):
#            print(size,"\t",end =" "),
#            size=size+250        
#        size=100
#        print()
    if choice == "1":
        size=100
        print ("\t\t",end=" ")
        for i in range(10):
            print(size,"\t",end =" "),
            size=size+250        
        size=100
        print()
        print ("Bubble Sort\t",end =" "),
        for i in range(10): 
            array.clear()
            random_array(size)
            start_time=time.time()
            BubbleSort(array)
            end_time=time.time()
            time_elapsed=end_time-start_time
            time_elapsed = str(round(time_elapsed, 3))
            print(time_elapsed,"\t",end =" "),
            size=size+250
            
    elif choice == "2":
        size=100
        print ("\t\t",end=" ")
        for i in range(10):
            print(size,"\t",end =" "),
            size=size+250        
        size=100
        print()
        
        print ("Merge Sort\t",end =" "),
        for i in range(10): 
            array.clear()
            random_array(size)
            start_time=time.time()
            mergeSort(array)
            end_time=time.time()
            time_elapsed=end_time-start_time
            time_elapsed = str(round(time_elapsed, 3))
            print(time_elapsed,"\t",end =" "),
            
            size=size+250
    elif choice == "3":
        size=100
        print ("\t\t",end=" ")
        for i in range(10):
            print(size,"\t",end =" "),
            size=size+250        
        size=100
        print()
        print ("Counting Sort\t",end =" "),
        for i in range(10): 
            array.clear()
            random_array(size)
            start_time=time.time()
            counting_sort(array,max(array))
            end_time=time.time()
            time_elapsed=end_time-start_time
            time_elapsed = str(round(time_elapsed, 3))
            print(time_elapsed,"\t",end =" "),
            
            size=size+250
    elif choice == "4":
        size=100
        print ("\t\t",end=" ")
        for i in range(10):
            print(size,"\t",end =" "),
            size=size+250        
        size=100
        print()
        print ("Insertion Sort\t",end =" "),
        for i in range(10): 
            array.clear()
            random_array(size)
            start_time=time.time()
            insertionSort(array)
            end_time=time.time()
            time_elapsed=end_time-start_time
            time_elapsed = str(round(time_elapsed, 3))
            print(time_elapsed,"\t",end =" "),
            
            size=size+250
    elif choice == "5":
        size=100
        print ("\t\t",end=" ")
        for i in range(10):
            print(size,"\t",end =" "),
            size=size+250        
        size=100
        print()
        print ("Selection Sort\t",end =" "),
        for i in range(10): 
            array.clear()
            random_array(size)
            start_time=time.time()
            selectionSort(array)
            end_time=time.time()
            time_elapsed=end_time-start_time
            time_elapsed = str(round(time_elapsed, 3))
            print(time_elapsed,"\t",end =" "),
            
            size=size+250
    elif choice=="Q" or choice=="q":
        exit
    else:
        print("You must only select either 1,2,3,4,5 or Q ")
        print("Please try again")
        menu()
        
def random_array(MyRange):
    for i in range(0,MyRange,1):
        array.append(random.randint(0,(MyRange+1)))
        
def BubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if j<len(array)-1:
                if array[j+1] > array[j]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp                

def BubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if j<len(array)-1:
                if array[j+1] > array[j]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp                

def mergeSort(array): #http://interactivepython.org/lpomz/courselib/static/pythonds/SortSearch/TheMergeSort.html
    if len(array)>1: #array is divided until single 1 index arrays left
        mid = len(array)//2 #divide the array into half
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf) #keep on dividing the array into half
        mergeSort(righthalf)#keep on dividing the array into half

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf): #arrays are sorted and merged
            if lefthalf[i] < righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1

def counting_sort(array, max_val):#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
    m = max_val + 1 
    count = [0] * m                
	    
    for a in array:
        count[a] += 1 # count occurences of that element
        i = 0
        for a in range(m):       
            for c in range(count[a]): 
                array[i] = a  #put that element in the count index
                i += 1
    return array
def insertionSort(array): #https://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
   for index in range(1,len(array)):

     currentvalue = array[index] 
     position = index
#starting from last index
     while position>0 and array[position-1]>currentvalue:  #if position at previous index is greater than current
         array[position]=array[position-1] #change value of current index
         position = position-1

     array[position]=currentvalue 


def selectionSort(array): #http://interactivepython.org/lpomz/courselib/static/pythonds/SortSearch/TheSelectionSort.html
   for fillslot in range(len(array)-1,0,-1): #starting from last index
       positionOfMax=0
       for location in range(1,fillslot+1):
           if array[location]>array[positionOfMax]:
               positionOfMax = location #selecting the position with maximum number
       temp = array[fillslot] #swapping the selected index with the position with selected slot for it
       array[fillslot] = array[positionOfMax]
       array[positionOfMax] = temp


def printfun():
    for i in range(len(array)):
        print(array[i])
        i+=1


menu()

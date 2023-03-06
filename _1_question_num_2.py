# Assignment_number_1 = Linear Data Structures
# Question_number_2 = Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def Reverse(array):
    reverse_array = array[::-1]
    print("Original Array", array)
    print("Reversed Array", reverse_array)
    
array = [1,2,3,4,5,6]   
obj = Reverse(array)

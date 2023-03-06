# Assignment_number_1= Linear Data Structures
# Question_number_3 = Write a program to check if two strings are a rotation of each other?

def Rotations(string_1, string_2):
    size_1 = len(string_1)
    size_2 = len(string_2)
    temp = ''

    if size_1 != size_2:
        return 0
 
    temp = string_1 + string_1

    if (temp.count(string_2) > 0):
        return 1
    else:
        return 0
 
if __name__ == "__main__":
    string_1 = "AACD"
    string_2 = "ACDA"

    if Rotations(string_1, string_2):
        print("Strings Are Rotations of Each Other")
    else:
        print("Strings Are Not Rotations of Each Other")
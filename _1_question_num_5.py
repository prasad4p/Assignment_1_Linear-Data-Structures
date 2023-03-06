# Assignment_number_1= Linear Data Structures
# Question_number_5 =  Read about the Tower of Hanoi algorithm. Write a program to implement it.


def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
   if n == 1:
      print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
      return
   TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
   print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
   TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print ("Sorted array is:")
for i in range(n):
    print ([i],end=" ")
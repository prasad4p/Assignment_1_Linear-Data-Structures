# Assignment_number_1= Linear Data Structures
# Question_number_7 = Write a program to check if all the brackets are closed in a given code snippet.

def bracketsCheck( seq ):  
   while True:  
       if '()' in seq :  
           seq = seq.replace ( '()' , '' )  
       elif '{}' in seq :  
           seq = seq.replace ( '{}' , '' )  
       elif '[]' in seq :  
           seq = seq.replace ( '[]' , '' )  
       else :  
           return not seq  
  
seq = '{[()]}'  
print(f'Is {seq} valid ? : {bracketsCheck(seq)}')  
seq1 = '{[()]}{]{}}'  
print(f'Is {seq1} valid ? : {bracketsCheck (seq1)}')
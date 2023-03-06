# Assignment_number_1= Linear Data Structures
# Question_number_4 = Write a program to print the first non-repeated character from a string?


def first_non_repeating_character(string):
  char_order = []
  ctr = {}
  for i in string:
    if i in ctr:
      ctr[i] += 1
    else:
      ctr[i] = 1 
      char_order.append(i)
  for i in char_order:
    if ctr[i] == 1:
      return i
  return None

print(first_non_repeating_character('abcdefa'))
print(first_non_repeating_character('acddca'))
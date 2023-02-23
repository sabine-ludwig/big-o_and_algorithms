'''Task 1: Even or Odd
Given a numeric value, determine if it is even or odd.
The function should take the value in as a parameter and return 
a boolean value (True if even, False if odd).'''

# O(1)
def even_or_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False

# print(even_or_odd(16))

'''Task 2: Less than 100
Given a list of numbers, determine if each item in the list is lower than 100.
The function should take in the list as a parameter and return a boolean value 
(False if there are any numbers greater than or equal to 100, True if all 
numbers are less than 100).'''

# O(n)
def less_than_100(list):
    all_nums_under_100 = True

    for num in list:
        if num >= 100:
            all_nums_under_100 = False
    return all_nums_under_100

# nums = [1, 2, 3, 4, 4, 5, 100]
# print(less_than_100(nums))

'''Task 3: Repeated Names
Given a list of names, determine if any names are contained in the list more 
than once. The function should take in the list as a parameter and return 
a boolean value (True if there are any repeated names, False if there are 
no repeats).'''

# O(n)
def repeated_names(list):
    are_there_repeats = False
    new_list = []

    for name in list:
        if name not in new_list:
            new_list.append(name)

    if new_list != list:
        are_there_repeats = True
    return are_there_repeats    

# names = ['sabine', 'olly', 'francis', 'sue']
# print(repeated_names(names))

'''Task 4: Sort List
Given a list of numbers, manually sort the list into ascending order. 
(may not use built in .sort() method).
Suggested strategy:
Starting with the first two numbers, compare them to see which is larger. 
Place the lower number to the left and the higher number to the right.
Iterate through the list, checking each pair of numbers one at a time.
Repeat from the start until the entire list is sorted.
'''

# O(n**2)
def sort_list(list):
    sorted_list = []
    
    while list:
        smallest_num = list[0]

        for num in list:
            if num < smallest_num:
                smallest_num = num
        sorted_list.append(smallest_num)
        list.remove(smallest_num)

    return sorted_list    

nums = [1,2,4,2,6,4,7,8]
print(sort_list(nums))       
        
  




























    

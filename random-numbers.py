#  Use the following code to create a list of 10 random numbers. Each number will be between 0 and 6.
# import random

# my_randoms = list()
# for i in range(10):
#     my_randoms.append(random.randrange(1, 6))

# Then iterate a different list of numbers that are sequential from 1 to 10. Use the following code as your starting point.

import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))
    print(my_randoms)

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)
print(numbers_1_to_10)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

    # Iterate your random number list here
    for random in my_randoms:
        # Does my_randoms contain number? Change the boolean.
        if random == number:
            the_numbers_match = True
            break
        else:
            the_numbers_match = False
    if the_numbers_match == True:
        print(f'my_randoms_list contains {number}')
    else:
        print(f'my_randoms_list does not contain {number}') 
        
# Example Output in the Terminal
# my_randoms list contains 0
# my_randoms list does not contain 1
# my_randoms list does not contain 2
# my_randoms list contains 3
# my_randoms list contains 4
# my_randoms list does not contain 5
# NOTE: Each run will produce different output.
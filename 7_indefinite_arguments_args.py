def tea_order(customer_name, tea_type, **kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for key, value in kwargs.items():
        print(" - Add", key, ":", value)
# tea_order("Roni", "chamomile")
# tea_order("Roni", "chamomile")
tea_order("Roni", "chamomile", sweatner="honey")



# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
def sum_squared(*args):
    sum=0
    for num in args:
        sum += num **2
        return sum
    
print(sum_squared(4, 5, 6, 7, 7, 7, 8, 9, 9, 9))


def absolute_sum(*args):
    sum=0
    for num in args:
        sum += abs (num)
        return sum
    
print(absolute_sum(-10, 5, -3, 7, -2, 6, 7, -8, 9))

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
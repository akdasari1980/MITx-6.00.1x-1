# Problem 6
# 0.0/20.0 points (graded)
# Implement a function that meets the specifications below.

# def max_val(t): 
#     """ t, tuple or list
#         Each element of t is either an int, a tuple, or a list
#         No tuple or list is empty
#         Returns the maximum int in t or (recursively) in an element of t """ 
#     # Your code here
# For example,

# max_val((5, (1,2), [[1],[2]])) returns 5.
# max_val((5, (1,2), [[1],[9]])) returns 9.
# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here

    def openItem(term):
        newList = []

        for item in term:
           if type(item) == int:
              newList.append(item)

           else:
              newList += openItem(item)

        return newList

    sortingList = openItem(t)

    maximum = sortingList[0]

    for item in sortingList:
        if maximum < item:
            maximum = item

    return maximum


print(max_val((5, (1,2), [[1],[2]])))
print(max_val((5, (1,2), [[1],[9]])))

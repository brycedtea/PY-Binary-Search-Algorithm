# We are going to write a binary search algorithm. If the desired element is found, we want the function to return True. If the desired element is not found, we want the function to return False.

"""
Define a function called binary_search that takes a list and an element. Name the parameters data and el, respectively.
Create two variables called first and last to store the index values of the first and last positions in the list.
Create a variable called found and set equal to False. We will use this variable to store True if the desired element is found later on.
Create a while loop that runs when first is less than or greater than last and the element is not found (found is False).
Inside the while loop, declare a variable called mid that will store the middle element's index by adding the first and last position and dividing by two.
In the while loop, check if the middle element's value is equal to the desired element. If it is, set found to True.
Otherwise, we need to decide if we are using the left or right half.
Write the case for the left half. If the desired element is less than the middle element's value, set last equal to one less than the index of the middle element (mid-1).
Otherwise, deal with the right half. Set first equal to one more than the index of the middle element (mid+1).
Outside of the while loop, return the variable found.
Create a list and test your function! If the element we are searching for is in the list, we expect an output of True. If the element is not in the list, we expect an output of False.
"""          
def binary_search(data, el):
    first = 0
    last = len(data)-1 
    found = False

    while first <= last and not found:
        mid = (first+last)//2

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]: 
                last = mid-1
            else: 
                first = mid+1
    return found

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(binary_search(test_list, 12))
      
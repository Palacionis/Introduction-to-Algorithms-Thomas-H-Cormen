# Chapter 1 - the algorithms in computing
# insertion sort

a = [1, 100, 1, -1]

for x in range(1, len(a)):
    key = a[x]  # the first key is the second object in a sequence
    i = x - 1  # i is the previous index
    while (i >= 0 and a[i] > key):  # while we can go back in a sequence index and the previous object is higher than the current index
        a[i + 1] = a[i]  # move the object one index back
        i -= 1  # check if now the new object to the left if higher than the current one being moved
    a[i + 1] = key  # if not, take the next key to be checked
print(a)
# [-1, 1, 1, 100]


# same example with more informative variables

a = [0, 1, -10, 50, -100]

for x in range(1, len(a)):
    current_object = a[x]
    previous_index = x - 1
    while previous_index >= 0 and a[previous_index] > current_object:
        a[previous_index + 1] = a[previous_index]
        previous_index = previous_index - 1
    a[previous_index + 1] = current_object
print(a)
# [-100, -10, 0, 1, 50]


# same thing but more pythonic

a = [0, 1, -10, 50, -100]

for i in range(1,len(a)-1):
  j = i
  while j > 0 and a[j-1] > a[j]:
    a[j], a[j-1] = a[j-1], a[j]
    j -= 1

print(a)
# [-10, 0, 1, 50, -100]
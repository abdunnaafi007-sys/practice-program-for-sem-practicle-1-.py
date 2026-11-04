# Input
tup = ('a', 'a', 'c', 'b', 'd')
lst = ['a', 'b']
# Count occurrences
count = 0
for item in lst:
    count += tup.count(item)
# Output the result
print("Total occurrences of list items in the tuple:", count)

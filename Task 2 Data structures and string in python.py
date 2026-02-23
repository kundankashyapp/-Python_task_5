'''
1. Create a list of numbers from 1 to 10
2. Extracts the first five elements from the list
3. Reverses these extracted elements
4. prints both the extracted list and the reversed list
'''

numbers = list(range(1 ,11))

first_five = numbers[:5]

reverse_list = first_five[::-1]

print(f"original list: ",numbers)
print(f"Extracted first five elements: ",first_five)
print(f"Reversed extracted elements: ",reverse_list)


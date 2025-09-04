'''Task 2: Demonstrate List Slicing
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

#Solution 1
list= [1,2,3,4,5,6,7,8,9,10]

#Solution 2
Extract_element = list[0:5]

#Solutiuon 3
Reversed_element = Extract_element[::-1]

#Solution 4
print("Extracts the first five elements from the list ",Extract_element)

print("Reverses these extracted elements",Reversed_element)
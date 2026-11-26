print("=========================student marks list analyzer=========================")

#Part 1 : Create the empty list & marks list 

empty_list = []
marks_list = [50,42,45,50,49.5,50]


#Part 2 : Repeat a sample list 

sample_list = [20,40,60,80] * 2

#Part 3 : Find the list length

length_of_list = len(marks_list)
print(f"the length of list is {length_of_list}")

#Part 4 : Access items with Indexing 

marks_list[0]
marks_list[-1]

#Part 5 : Access a range with Slicing

marks_list[0:3] 
marks_list[::-1]

#Part 6 : Iterate through values
marks = [2,4,6,8,10,22,44,66,88,222,444,66]  
def match_marks(mark_list):
    count = 0
    matched_marks = []
 
    for mark in mark_list:
        mark_text = str(mark)
 
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)
 
    
    return count
 
same_digit_count = match_marks([88, 72, 99, 65, 77])
print("Number of matching marks:", same_digit_count)

#Part 7 : Calculate summary values

total = 0 

len(marks)

print(f"Largest Mark :" [-1])
print(f"Shortest Mark : "[0])



 

# DICTIONARiES AND NESTING
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "function": "A piece of code that you cann easily call over and over agian.",
}


# RETRIEVING ITEMS FROM THE DICTIONARY.
# print(programming_dictionary["Bug"])

# ADDING NEW ITEMS TO DICTIONARY.
programming_dictionary["Loop"] = "The action of doing something over and over again"

# print(programming_dictionary)

# CREATING A NEW DICTIONARY.
empty_dictionary = {}

# WIPE AN EXISTING DICTIONARY:  CLEARS THE DICTIONARY
# programming_dictionary = {}
# print(programming_dictionary)

# EDITTING AN ITEM IN THE DICTIONARY
programming_dictionary["Bug"] =  "A moth in your computer."

# print(programming_dictionary)


# LOOPING THROUGH A DICTIONARY
for key in programming_dictionary:
    print (key)
    print(programming_dictionary[key])
    
    
# GRADING PRORGAM EXERCISE

student_scores = {
    "Harry": 81,
    "Ron": 78, 
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62,
}
for key in student_scores:
    if student_scores[key] >= 91:
        student_scores[key] = "Outstanding" 
        print(student_scores[key])
        
        
        # FINIRE
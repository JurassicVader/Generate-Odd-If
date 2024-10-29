"""
Created by: Spencer Burchfield
Date: 10/29/24
Description: 
   This program writes to another file which checks if a number is even or odd.
   The reason is because it was a demonstration that you can write python in a
   python file using python from a different file. 
   I understand that the created program is not practical in any way. It was 
   inspired by comical programming TikToks from 2020.

Special Notes *
-  using if instead of elif; 
-  Although it would be more efficient, it throws a memory error.
"""

working = True
while working: # Making sure that the user enters a number that will not crash the program.
    try:
        gen_num = int(input("Pick a number:\n1 to 1,000,000 (Without Commas): "))
        if gen_num > 1000000:
            print("Number Exceeded 1,000,000")
        else:
            print("generating")
            working = False
    except: # If this happens, the user likely entered a string.
        print("Please enter a whole number.")
f = open("info.py", "a") # Change info.py to the file that you would like to write to.
count = 0
cases = "" # This just holds even or odd string for the program file.
f.write("num = int(input('Enter a number: '))\n") # First line of the program
while count <= gen_num: # Runs the rest of the program.
    if count % 2 == 1:
        cases = "odd"
    else:
        cases = "even"
    f.write(f"if num == {count}:\n\tprint('{cases}')\n") # Prints 2 lines, the if and the following statement
    count += 1
f.close()
print("completed") # If you do not see a completed after running then the program is running or failed.
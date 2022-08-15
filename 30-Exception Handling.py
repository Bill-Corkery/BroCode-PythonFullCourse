#Lesson 30: Exception Handling
# Exceptions are events detected during execution that interrupt the flow of a program.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    results = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero! Idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers please.")
except Exception as e:  #good pratice to put specific exceptions first.
    print(e)
    print("Something went wrong: ")
else:
    print(results)
finally:  #should be at end as want to close files when done
    print("This will always execute")
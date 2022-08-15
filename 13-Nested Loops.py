#Lesson 13: Nested Loops
# the "inner loop" will finish all its interations before
# finishing on iteration of the "outer loop"
# https://www.youtube.com/watch?v=XKHEtdqhLK8

#going to draw a rectange with nested loops.
#Outer loop will be in charge of rows. Inner incharge of columns.
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")
#common convetion for innter for loops is j.
#end="" prevents cursor from moving to next line.
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
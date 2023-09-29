mark = float(input("Enter your cgpa:"))
if(mark>=9):
    print("Grade A")
elif(mark<9 and mark>8):
    print("Grade B")
elif(mark<8 and mark>7):
    print("Grade C")
elif(mark<7 and mark>6):
    print("Grade D")
else:
    print("Grade E")
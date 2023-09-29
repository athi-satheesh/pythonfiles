# half-triangle
# for i in range(10):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
#

# inverted triangle
# for i in range(10,0,-1):
#     for j in range(i,0,-1):
#         print("*", end=" ")
#     print()

# full-triangle
n=6
for i in range(n):
    for j in range(2*(n-i)-1):
        print(" ", end="")
    for k in range(i):
        print("*", end="   ")
    print()

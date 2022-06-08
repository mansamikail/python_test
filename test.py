# s = int(input('star: '))
# for i in range(0, s):
#     print((5-i-1)*' ', end='')
#     print('*'*(i+1))

# for row in range(7):
#     for col in range(5):
#         if (col == 0) or (col == 4) and (row != 0 and row != 6) or ((row == 0 or row == 6) and (0 < col < 4)):
#             print('*', end='')
#         else:
#             print(end=" ")
#     print()

# for i in range(7):
#     for j in range(7):
#         if (j == 0 or j == 6) or ((i == 1) and (j == 1 or j == 5)) or ((i == 2) and (j == 2 or j == 4)) or (i == 3 and j == 3):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

k = 1
for i in range(7):
    print(' '*(7-i-1),end='')
    print('*'*k)
    k += 2

for i in range(6):
    for j in range(5):
        if ((j == 0 or j == 4) and (i != 0 or i != 3)) or ((i == 0 or i == 3) and (0 < j < 4)):
            print("*", end='')
        else:
            print(' ', end='')
    print()

# The pound sign marks the start of a comment. Python itself
# ignores the comments, but they are helpful for anyone reading code.
for i in [1, 2, 3, 4, 5]:
    print(i)                    # first line in "for i block"
    for j in [1, 2, 3, 4, 5]:
        print(j)                # first line in "for j" block
        print(i + j)            # last line in "for j" block
    print(i)                    # last line in "for j" block
print("done looping")
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                            13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

two_plus_three = 2 + \
                    3

for i in [1, 2, 3, 4, 5]:

    # notice the blank line
    print(i)

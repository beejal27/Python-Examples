""" Author : Beejal Vibhakar
    Date   : 03/04/2020
    Given two sorted arrays (ascending order), this program merges these two array. The elements in the
    merged array are sorted (ascending order).
    e.g. a = [12, 17, 23, 54] & b = [10, 13, 14, 55], the program would give output as [10, 12, 13, 14, 17, 23, 54, 55].
    Conceptually the algorithm works as follows.
    
    Greater of 54 and 55        [None, None, None, None, None, None, None, 55]
    Greater of 54 and 14        [None, None, None, None, None, None, 54, 55]
    Greater of 23 and 14        [None, None, None, None, None, 23, 54, 55] 
    Greater of 17 and 14        [None, None, None, None, 17, 23, 54, 55] 
    Greater of 12 and 14        [None, None, None, 12, 17, 23, 54, 55] 
    Greater of None and 14      [None, None, 14, 12, 17, 23, 54, 55]
    Greater of None and 13      [None, 13, 14, 12, 17, 23, 54, 55]
    Greater of None and 10      [10, 13, 14, 12, 17, 23, 54, 55]

 """
DEBUG = True
def merge(a, b):
    print(f'a = {a}')
    print(f'b = {b}')

    indexA = len(a) - 1  # Index of last element in array a
    indexB = len(b) - 1  # Index of last element in array b
    indexMerged = len(a) + len(b) - 1 # end of merged array
    if DEBUG:
        print(f'indexA = {indexA}, indexB = {indexB}, indexMerged = {indexMerged}')
    c = [None] * (indexMerged + 1)

    while indexB >=0:
        if indexA >=0 and a[indexA] > b[indexB]:
            c[indexMerged] = a[indexA]
            indexA -= 1
        else:
            c[indexMerged] = b[indexB]
            indexB -= 1
        indexMerged -= 1
    
    while indexA >= 0:
        c[indexMerged] = a[indexA]
        indexA -= 1
        indexMerged -= 1
    print(f'Final output : {c}')
    print()
        

if __name__ == '__main__':
    print("Test::1")
    a = [12, 17, 23, 54]
    b = [10, 13, 14, 55]
    merge(a, b)

    print("Test::2")
    a = [12, 17, 23, 54]
    b = [55, 56, 57]
    merge(a, b)    

    print("Test::3")
    a = [9, 17, 23, 54]
    b = [10, 13, 14, 55]
    merge(a, b)
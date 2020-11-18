def oddDigitSumLessThen15(x):
    digitSum = 0
    for char in str(x): 
        digitSum = digitSum + int(char)
    return (digitSum % 2 and (not digitSum > 15))
    
def oddDigitSum(x):
    digitSum = 0
    for char in str(x): 
        digitSum = digitSum + int(char)
    return digitSum % 2
deck =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 21, 21, 21, 21, 21, 22, 23, 23, 24, 24, 25, 25, 25, 26, 27, 27, 27, 28, 28, 28, 29, 29, 30, 30, 30, 31, 32, 32, 33, 34, 34, 35, 35, 35, 35, 36, 36, 36, 37, 38, 39, 40, 40, 41, 42, 42, 43, 44, 45, 45, 45, 46, 47, 48, 49, 49, 49, 50, 50, 51, 52, 53, 54, 55, 55, 55, 56, 56, 56, 57, 58, 59, 60, 61, 62, 63, 63, 64, 64, 64, 64, 65, 66, 67, 68, 69, 70, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 81, 82, 83, 84, 84, 85, 86, 87, 88, 89, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 100, 120, 125, 128, 165, 216, 220, 256, 343, 512, 512, 729, 1000]
def checker(condition):
    l = [x for x in range(1,101) if eval(condition)]
    dl = [x for x in deck if eval(condition)]
    if len(l) < 51: 
        print("This is a valid list with", len(l), "numbers between 1 and 100:\n", l)
    elif len(dl) < len(deck) / 2:
        print("This is a valid list with", len(dl), "instances in the deck:\n", dl)
    else: 
        print("This is an invalid list with", len(l), "numbers between 1 and 100:\n", l)

checker("oddDigitSum(x)")

# prettyListChecker([x for x in range(1,101) if oddDigitSumLessThen15(x)])
# prettyListChecker([x for x in range(1,101) if oddDigitSum(x)])

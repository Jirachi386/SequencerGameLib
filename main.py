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
    
def prettyListChecker(l):
    if len(l) < 50: 
        print("This is a valid list with", len(l), "numbers between 1 and 100:\n", l)
    else: 
        print("This is an invalid list with", len(l), "numbers between 1 and 100:\n", l)
        
# prettyListChecker([x for x in range(1,101) if oddDigitSumLessThen15(x)])
# prettyListChecker([x for x in range(1,101) if oddDigitSum(x)])

# Task: find the specialised Four-digit numbers
# Find and list all the 4-digit numbers in decimal notation that have the property
# that:
# the sum of their four digits = the sum of their digits when represented in duodecimal (base 12) notation
# and:
# the sum of their four digits = the sum of their digits when represented in duodecimal (base 16) notation


# Input: None

# Output: All the four-digit numbers 
# that satisfy the requirement (in strictly increasing order)
# each on a separate line, with no leading or trailing blanks
# ending with a new-line character
# no blank lines in the output


from sys import stdin, stdout

lLimit = 1000 # inclusive bound
uLimit = 9999

def digitSum(number, base):
    sum = 0
    remainder = int(number%base)
    factor = number
    while factor != 0:
        # if remainder != 0:
        sum += remainder
        # else:
        #     sum += 1
        factor = int(factor / base)
        remainder = int(factor % base)
    sum += remainder
    
    return sum

for i in range(lLimit,uLimit+1):
    if (digitSum(i,10)==digitSum(i,12)==digitSum(i,16)):
        stdout.write("%d\n" % i)



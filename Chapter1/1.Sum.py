# Task: find the sum of all integer numbers lying between 1 and N inclusive

# Input: a single *integer* N that is not greated than 10,000 by its absolute value

# Output: A single *integer* N that is the sum of 
# all integer numbers lying between 1 and N inclusive

# Submitted to Ural 1068


from sys import stdin, stdout

N = int(stdin.read())

limit = 10000

if N > 0 and abs(N) <= limit:
    stdout.write( '%d' % int(N*(1+N)/2))
elif N <= 0 and abs(N) <= limit:
    stdout.write( '%d' % int(N*(1-N)/2+1))

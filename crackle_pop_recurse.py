"""This program will:
Print the numbers from 1 to 100 (inclusive).
HOWEVER, if a number is divisible by 3, it'll print "Crackle".
If it is divisible by 5, it'll print "Pop"
If it is divisible by both 3 AND 5, it'll print "CracklePop".
At the end, we'll have a nice bowl of Rice Krispies to celebrate!
"""

def crackle_pop(end):
    for n in range (1, end):
        if n % 3 == 0 and n % 5 == 0:
            print("CracklePop")
        elif n % 3 == 0:
            print("Crackle")
        elif n % 5 == 0:
            print("Pop")
        else:
            print(n)

if __name__ == '__main__':
    crackle_pop(101)

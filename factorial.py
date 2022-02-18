import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    nums = sys.argv[1:]
    print("Computing factorial of ", nums)

    for i in nums:
        print("factorial of {} is {}".format(i, factorial(int(i))))
    

# def isPrime(last_prime: int):
#     guess = last_prime + 1
#     for i in range(2, round(guess/2)):
#         if guess % i == 0:
#             return isPrime(guess)
#     return guess
        
# def primeGen(maxNum: int):
#     i = 0
#     while i <= maxNum:
#         i = isPrime(i)
#         if i <= maxNum:
#             yield i 

# for i in primeGen(500):
#     print(i)

# nums = (x for x in range(5))

# print(nums)


print([[i for i in range(j)] for j in range(4)])

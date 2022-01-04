# Optimised version

def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "FizzBuzz"
    if input % 5 == 0:
        return "Buzz" # elif can also be used
    if input % 3 == 0: # elif can also be used
        return "Fizz"
    return input

print(fizz_buzz(3))

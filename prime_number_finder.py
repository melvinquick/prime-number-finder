# Rules for finding Prime Numbers
## Aside from 2, no even number is Prime
## If the sum of the digits is divisible by 3, then the number will be divisble by 3
## If the number end with 0 or 5, then it will be divisible by 5
## Double the last digit and subtract it from the rest of the number... If the answer is divisible by 7, the original number will be divisible by 7... For instance, if the number is 161, take the last digit (1), double it, then subtract it from the rest of the number (16)... If the answer is divisible by 7, then so is the original number... In this case the answer is 14, 14 is divisible by 7, so 161 is also
## Add alternate digits and subtract it from the difference of the next sum of alternate digits... For instance, if the number is 574652, add 5+4+5=14 and 7+6+2=15... If the difference i.e. 1 is divisible by 11, then the number will be divisible by 11... In this case, clearly the number is not divisible by 11
## Semiprimes are not true Primes and need to be ruled out by checking a number against the square of each Prime that was already added to the prime list... For example, 169 is the product of 13*13, so it's not Prime, it's Semiprime
## Squarefree Primes are an extension of Semiprimes where the number is the product of two unique Primes from the Prime list... For example, 221 is the product of 13*17, so it's not Prime, it's a Squarefree Prime


# Function to determine the sum of the digits of the number
def digit_sum_func(number):
    ## Local Variables
    digit_sum = 0
    digits = str(number)

    ## Local Main Code
    for digit in digits:
        digit_sum += int(digit)
    return digit_sum


# Function to check last digit of the number
def last_digit_func(number):
    ## Local Variables / Local Main Code
    last_digit = int(str(number)[-1:])
    return last_digit


# Function to check for the divisible by 7 condition
def seven_check_func(number):
    ## Local Variables / Local Main Code
    last_digit = int(str(number)[-1:])
    new_number_1 = int(str(number)[:-1])
    new_number_2 = new_number_1 - (2 * last_digit)
    return new_number_2


# Function to check for the divisible by 11 condition
def eleven_check_func(number):
    ## Local Variables / Local Main Code
    new_number_1 = int(str(number)[0::2])
    new_number_1 = digit_sum_func(new_number_1)
    new_number_2 = int(str(number)[1::2])
    new_number_2 = digit_sum_func(new_number_2)
    new_number_3 = abs(new_number_1 - new_number_2)
    return new_number_3


# Function to check for Semiprimes
def semiprime_check_func(number):
    ## Local/Global Variables
    global prime_list

    ##Local Main Code
    for prime in prime_list:
        if number == prime * prime:
            return True
    return False


# Function to check for Squarefree Primes
def squarefree_prime_check_func(number):
    ## Local/Global Variables
    counter = 0
    global prime_list

    ## Local Main Code
    for prime in prime_list:
        counter = 0
        while counter <= len(prime_list) - 1:
            if number == prime * prime_list[counter]:
                return True
            counter += 1
    return False


# Function to determine if a number is Prime or not
def prime_check_func(number):
    ## Local/Global Variables
    digit_sum = 0
    seven_check = 0
    eleven_check = 0
    global starting_prime_list
    global prime_list
    global end_digit_fail_list
    global is_semiprime
    global is_squarefree_prime

    ## Local Main Code
    if number in starting_prime_list:
        return True

    if last_digit_func(number) in end_digit_fail_list:
        return False

    digit_sum = digit_sum_func(number)

    if digit_sum % 3 == 0:
        return False
    
    seven_check = seven_check_func(number)

    if seven_check % 7 == 0:
        return False

    eleven_check = eleven_check_func(number)

    if eleven_check % 11 == 0:
        return False
    
    is_semiprime = semiprime_check_func(number)

    if is_semiprime == True:
        return False

    is_squarefree_prime = squarefree_prime_check_func(number)

    if is_squarefree_prime == True:
        return False

    prime_list.append(number)

    return True


# Function for getting the last number you checked and starting up the finder from there
def get_startup_number_func():
    ## Local Variables / Local Main Code
    startup_number_file = open("current_number.txt", "r")
    startup_number = int(startup_number_file.read())
    startup_number_file.close()
    return startup_number


# Function for setting the last number you checked
def set_ending_number_func(number):
    ## Local Variables / Local Main Code
    ending_number_file = open("current_number.txt", "w")
    ending_number_file.write(str(number))
    ending_number_file.close()
    return


# Function to store a found Prime in a file
def store_prime_func(number):
    ## Local Variables / Local Main Code
    new_prime_file = open("prime_numbers.txt", "a")
    new_prime_file.write(str(number))
    new_prime_file.write("\n")
    new_prime_file.close()
    return


# Function to retrieve the current Prime List at the beginning of code execution
def get_prime_list_func():
    ## Local Variables
    current_prime_list = []

    ## Local Main Code
    prime_numbers_file = open("prime_numbers.txt", "r")
    for prime in prime_numbers_file:
        current_prime_list.append(int(prime))
    prime_numbers_file.close()
    return current_prime_list


# Global Variables
starting_prime_list = [2,3,5,7,11,13,17,19,23,29]
prime_list = get_prime_list_func()
end_digit_fail_list = [0,2,4,5,6,8]
current_number = get_startup_number_func()
is_prime = False
is_semiprime = False
is_squarefree_prime = False
keep_iterating = True


# Main Code
if __name__ == "__main__":
    while keep_iterating:
        is_prime = prime_check_func(current_number)

        if is_prime == True:
            store_prime_func(current_number)

        current_number += 1
        set_ending_number_func(current_number)
for num in range(2,101):
    is_prime = True
    for factor in range(2,num):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num)
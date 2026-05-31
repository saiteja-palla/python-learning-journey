def is_prime(num):
    count = 1
    if num != 1:
        for i in range(2, num+1):
            if num % i == 0:
                count += 1
        if count < 2:
            return True
    return False
    
print(is_prime(73))
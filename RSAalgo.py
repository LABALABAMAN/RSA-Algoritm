from math import gcd


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


# Get p and q
p = int(input("Enter p value: "))
q = int(input("Enter q value: "))

# Validate p and q
if not is_prime(p) or not is_prime(q):
    print("p and q must be prime numbers.")
    exit()

if p == q:
    print("p and q must be different.")
    exit()


# Calculate n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)

print(f"n = {n}")
print(f"phi(n) = {phi}")


# Get e
e = int(input("Choose e value (3, 15, 17, 65537): "))

if gcd(e, phi) != 1:
    print("e and phi(n) must be coprime.")
    exit()


# Calculate d
d = pow(e, -1, phi)

print(f"Public key  = ({e}, {n})")
print(f"Private key = ({d}, {n})")


while True:

    ask = input("Decrypt or encrypt? (d/e): ").lower()

    if ask == "d":

        crypt = int(input("Crypted number: "))

        decrypted = pow(crypt, d, n)

        print("Decrypted is:", decrypted)

        break

    elif ask == "e":

        number = int(input("Put what number you want to crypt: "))

        if number < 0 or number >= n:
            print(f"Number must be between 0 and {n - 1}.")
            continue

        encrypted = pow(number, e, n)

        print("Encrypted is:", encrypted)

        break

    else:
        print("Enter valid command.")
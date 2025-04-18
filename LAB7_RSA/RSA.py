def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def RSA(p, q, msg):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Finding 'e' such that gcd(e, phi) = 1
    for i in range(2, phi):
        if gcd(i, phi) == 1:  # Fixed comparison operator
            e = i
            break

    # Finding 'd' such that (d * e) % phi = 1
    j = 1  # Start from 1 instead of 0 to avoid infinite loop
    while True:
        if (j * e) % phi == 1:  # Fixed comparison operator
            d = j
            break
        j += 1

    # Encrypting the message
    c = (msg ** e) % n
    print("Encrypted message:", c)

    # Decrypting the message
    decrypted_msg = (c ** d) % n  # Fixed variable name
    print("Decrypted message:", decrypted_msg)

# Taking user input
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
msg = int(input("Enter a message: "))

RSA(p, q, msg)

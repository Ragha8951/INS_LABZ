import math  # Importing the math module for power calculations

# Step 1: Input prime number (q) and primitive root (a)
q = int(input("Enter a prime number: "))  # A large prime number
a = int(input("Enter a primitive root: "))  # A primitive root of q

# Step 2: Input private keys (Xa for A, Xb for B)
Xa = int(input("Enter the private key of A: "))  # Secret key chosen by user A
Xb = int(input("Enter the private key of B: "))  # Secret key chosen by user B

# Step 3: Compute public keys using (a^X mod q)
Ya = (math.pow(a, Xa) % q)  # Public key of A (sent to B)
Yb = (math.pow(a, Xb) % q)  # Public key of B (sent to A)

print("Public key of A:", Ya)
print("Public key of B:", Yb)

# Step 4: Compute the shared secret key
Ka = (math.pow(Yb, Xa) % q)  # Key computed by A using B’s public key
Kb = (math.pow(Ya, Xb) % q)  # Key computed by B using A’s public key

print("Shared key for A:", Ka)
print("Shared key for B:", Kb)

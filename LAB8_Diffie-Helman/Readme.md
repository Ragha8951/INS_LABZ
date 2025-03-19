# Diffie-Hellman Key Exchange

## Live Demo
[Run on Google Colab](https://colab.research.google.com/drive/1Gx1XE5r324ANN6zyIEZE61DH0DaIM79a?usp=sharing)

## Features
- Implements Diffie-Hellman key exchange protocol.
- Generates public and private keys for secure communication.
- Computes a shared secret key between two users.
- Uses modular exponentiation for key computation.

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of cryptographic key exchange.
- Google Colab access (for running the script online).

## How It Works
1. **Input Prime Number & Primitive Root:**
   - User inputs a prime number `q` and its primitive root `a`.
2. **Choose Private Keys:**
   - Each user (A & B) selects a private key (`Xa` and `Xb`).
3. **Compute Public Keys:**
   - Public keys are generated as `Ya = (a^Xa) % q` and `Yb = (a^Xb) % q`.
4. **Exchange Public Keys:**
   - Users share their public keys with each other.
5. **Compute Shared Secret Key:**
   - Both users compute the shared key using:
     - `Ka = (Yb^Xa) % q` (computed by A)
     - `Kb = (Ya^Xb) % q` (computed by B)
6. **Result:**
   - Both A & B obtain the same secret key for secure communication.

## Example Usage
```bash
Enter a prime number: 23
Enter a primitive root: 5
Enter the private key of A: 6
Enter the private key of B: 15
Public key of A: 8.0
Public key of B: 19.0
Shared key for A: 2.0
Shared key for B: 2.0
```

## Real-Life Applications
- **Secure Key Exchange:** Used in SSL/TLS protocols for encrypted communication.
- **Cryptographic Systems:** Forms the foundation of many secure encryption algorithms.
- **Blockchain Security:** Helps in establishing secure transactions.
- **Messaging Apps:** Enables end-to-end encryption for secure messaging.

## Notes
- The chosen prime number `q` should be large for stronger security.
- The primitive root `a` must be carefully selected.
- The script uses `math.pow()`, which may introduce floating-point inaccuracies. Consider using modular exponentiation for better precision.

## Future Enhancements
- Implement modular exponentiation for accurate computations.
- Add user authentication to prevent man-in-the-middle attacks.
- Extend the implementation for group key exchange.

## Contribution
Contributions are welcome! If you find any issues or have suggestions, feel free to create a pull request or open an issue on GitHub.

## Author
**GitHub:** [@Ragha8951](https://github.com/Ragha8951)  
**Email:** [ragha8951@gmail.com](mailto:ragha8951@gmail.com)

Thank you for visiting ❤️


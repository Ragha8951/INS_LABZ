# RSA Encryption & Decryption

## Live Demo
[Run on Google Colab](https://colab.research.google.com/drive/16rGY8POX8nud4kACCSHYGv859oUA04iC?usp=sharing)

## Features
- Implements RSA encryption and decryption.
- Uses two prime numbers to generate public and private keys.
- Encrypts and decrypts a numerical message.
- Demonstrates fundamental cryptographic principles.

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of cryptographic concepts.
- Google Colab access (for running the script online).

## How It Works
1. **Input Prime Numbers:**
   - The user provides two prime numbers, `p` and `q`.
2. **Compute RSA Parameters:**
   - `n = p * q`
   - `phi(n) = (p - 1) * (q - 1)`
3. **Find Public Key `e`:**
   - Selects the smallest integer `e` such that `gcd(e, phi) = 1`.
4. **Compute Private Key `d`:**
   - Finds `d` such that `(d * e) % phi = 1`.
5. **Encrypt the Message:**
   - Uses the formula `c = (msg ^ e) % n`.
6. **Decrypt the Message:**
   - Uses the formula `decrypted_msg = (c ^ d) % n`.

## Example Usage
```bash
Enter the value of p: 11
Enter the value of q: 13
Enter a message: 9
Encrypted message: 19
Decrypted message: 9
```

## Real-Life Applications
- **Secure Communication:** Encrypts messages for confidentiality.
- **Digital Signatures:** Used to verify the authenticity of messages.
- **Online Transactions:** Protects sensitive financial data.
- **Authentication Systems:** Provides secure user verification.

## Notes
- `p` and `q` must be prime numbers for correct RSA key generation.
- The message should be a numeric value within the range of `n`.
- This implementation is a basic demonstration and should not be used for real-world security applications.

## Future Enhancements
- Improve key generation for larger prime numbers.
- Implement a more efficient modular exponentiation method.
- Extend support for string-based encryption.

## Contribution
Contributions are welcome! If you find any issues or have suggestions, feel free to create a pull request or open an issue on GitHub.

## Author
**GitHub:** [@Ragha8951](https://github.com/Ragha8951)  
**Email:** [ragha8951@gmail.com](mailto:ragha8951@gmail.com)

Thank you for visiting ❤️


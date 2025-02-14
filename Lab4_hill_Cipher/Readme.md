# Hill Cipher Encryption & Decryption

[**Live Demo**](https://colab.research.google.com/drive/1enFY-QXlBQzNO8q0AmcptR06zRpY9ho6?usp=sharing)

This Python script implements the Hill Cipher, a polygraphic substitution cipher that encrypts blocks of letters using matrix multiplication.

## Features

- Encrypts and decrypts messages using matrix-based transformations.
- Handles uppercase letters and ignores spaces.
- Pads plaintext with 'X' if necessary to fit the matrix size.
- Uses modular inverse for decryption.

## Prerequisites

- Python 3.x installed on your system.
- NumPy library installed (`pip install numpy`).
- Basic knowledge of running Python scripts.

## How It Works

- The plaintext is converted into numerical vectors using their ASCII values.
- Encryption: The vectors are multiplied by a key matrix and taken modulo 26.
- Decryption: The ciphertext is processed using the modular inverse of the key matrix.

## How to Use

1. Run the Python script.
2. Enter the plaintext you want to encrypt.
3. The program will return:
   - Encrypted text (ciphertext).
   - Decrypted text (original plaintext).

## Example Usage

```
Enter the plain text: HELLO
Encrypted: ZEBBW
Decrypted: HELLOX
```

## Notes

- The key matrix must be invertible modulo 26.
- Only uppercase English letters are supported.
- The plaintext length should be a multiple of the matrix size (padding is added if necessary).

## Future Enhancements

- Extend support for larger key matrices.
- Implement error handling for invalid inputs.
- Create a GUI version for user-friendly interaction.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue on GitHub.

## Author

GitHub: [@Ragha8951](https://github.com/Ragha8951)  
Email: [ragha8951@gmail.com](mailto:ragha8951@gmail.com)

Thank you for visiting ❤️


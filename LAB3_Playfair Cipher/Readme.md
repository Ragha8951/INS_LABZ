# Playfair Cipher Encryption

[**Live Demo**](https://colab.research.google.com/drive/19D-APeSvt0z2zJBoyNnlp7rCK5RqLj27?usp=sharing)

This Python script implements the Playfair Cipher, a classical encryption technique that encrypts digraphs (pairs of letters) using a 5x5 matrix.

## Features

- Encrypts messages using the Playfair Cipher.
- Removes spaces and replaces 'J' with 'I' as per Playfair rules.
- Automatically pads odd-length plaintext with 'X'.
- Handles key processing to create a 5x5 matrix with unique characters.

## Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

## How It Works

- A 5x5 matrix is generated from the keyword, ensuring unique letters (excluding 'J').
- The plaintext is converted into digraphs (pairs of letters).
- The rules of the Playfair Cipher are applied:
  - If both letters are in the same row, they are replaced with the next letter in the row.
  - If both letters are in the same column, they are replaced with the next letter in the column.
  - Otherwise, they form a rectangle and swap positions diagonally.

## How to Use

1. Run the Python script.
2. Enter the plaintext you want to encrypt.
3. Provide a keyword for the cipher matrix.
4. The program will return the encrypted message.

## Example Usage

```
Enter the plain text: HELLO WORLD
Enter the Keyword: SECRET
Encrypted: DMBBX UVTLE
```

## Notes

- The substitution is case-insensitive; all letters are converted to uppercase.
- Spaces and 'J' are handled automatically.
- Padding is added if necessary to ensure even-length input.

## Future Enhancements

- Implement decryption functionality.
- Enhance user interface for better interaction.
- Allow custom padding characters instead of 'X'.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue on GitHub.

## Author

GitHub: [@Ragha8951](https://github.com/Ragha8951)  
Email: [ragha8951@gmail.com](mailto:ragha8951@gmail.com)

Thank you for visiting ❤️


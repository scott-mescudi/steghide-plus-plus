

```markdown
# Steghide++

Steghide++ is a Python utility for performing steganography operations using Steghide. Steghide is a steganography program that is used to hide data in various kinds of image and audio files. This utility provides a user-friendly interface to embed and extract hidden data from images, generate random passwords, and more.

## Requirements

Before using Steghide++, ensure you have the following dependencies installed:

- Steghide
- Tesseract-OCR
- Python 3.x

To install the required Python packages, run the following command:

```
python requirements.py
```

This command will install the necessary Python packages specified in the `requirements.py` file.

## Usage Instructions

1. **Encrypt using password:** Embeds data into an image using a passphrase.
2. **Decrypt using password:** Extracts hidden data from an image using a passphrase.
3. **Encrypt and print binary image:** Encrypts coverfile and prints passphrase in a binary image.
4. **Decrypt using binary image:** Extracts hidden data from an image using a binary image.
5. **Generate a random password:** Generate a variable length password with ASCII characters.
6. **Help:** Display the help page.

## Important Note

Please do not delete the following files:

- **arial.ttf:** This file is required for printing text on images. Deleting it may cause the program to fail when generating binary images.
- **black.png:** This image is used as a background for generating binary images. Removing it may lead to errors during binary image creation.

Deleting these files may cause the program to malfunction or produce unexpected results. It is recommended to keep them in the same directory as the program (`steghide++.py`).

## How to Use

1. Clone the repository or download the `steghide++.py` file to your local machine.
2. Ensure you have met the requirements mentioned above.
3. Run the `requirements.py` file to install the necessary Python packages.
4. Execute `steghide++.py` in your terminal or command prompt.
5. Follow the on-screen instructions to perform the desired steganography operation.

## Additional Information

For more information on steganography and how to use this utility, refer to the help page provided within the program.

If you encounter any issues or have suggestions for improvement, feel free to reach out to the author.

Enjoy using Steghide++ for your steganography needs!
'''




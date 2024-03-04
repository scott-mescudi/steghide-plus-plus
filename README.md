# Steganography Utility

This utility provides a set of functions to perform steganography operations using steghide. It allows you to embed and extract hidden data within image files using passwords or binary images.

## Setup Instructions

Before using this utility, ensure that you have the following dependencies installed:

- [Steghide](https://github.com/StefanoDeVuono/steghide)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

If these dependencies are not installed, the utility will attempt to install them automatically when executed.

## Usage

### Encrypt using password (Option 1)

This option embeds data into an image using a passphrase.

Usage:
```python
python steganography_utility.py
```

### Decrypt using password (Option 2)

This option extracts hidden data from an image using a passphrase.

Usage:
```python
python steganography_utility.py
```

### Decrypt using binary image (Option 3)

This option extracts hidden data from an image using a binary image.

Usage:
```python
python steganography_utility.py
```

### Help (Option 4)

Displays the help page with usage instructions.

Usage:
```python
python steganography_utility.py
```

## Additional Notes

- Ensure that the cover file is not smaller than the embedded file.
- If files are in the same directory as the program, you can simply type the file names.
- Only `.wav` audio files can be used to embed files into audio.

## Authors

This utility was created by [goslar61](https://github.com/goslar61). If you have any questions or suggestions, feel free to reach out.
## Additional Notes

- Ensure that the cover file is not smaller than the embedded file.
- If files are in the same directory as the program, you can simply type the file names.
- Only `.wav` audio files can be used to embed files into audio.

"""this is my first ever python project after 2 weeks of learning


#made by goslar61
import subprocess
import pytesseract
from PIL import Image
import time
from colorama import init, Fore
from PIL import Image, ImageDraw, ImageFont

# Initialize colorama
init(autoreset=True)

def binary_img_translate(image_path, binary_path):
    image = Image.open(binary_path)
    text = pytesseract.image_to_string(image)
    binary = text
    normal = "".join(chr(int(c, 2)) for c in binary.split())
    command = ["steghide", "extract", "-sf", image_path, "-p", normal]

    try:
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # If the command runs successfully, print the output in green color
        print(Fore.GREEN + "Success!")
    except subprocess.CalledProcessError as e:
        # If the command fails, print the error in red color
        print(Fore.RED + "Error:", e)

def print_binary_image(image_path, data_file_path, passphrase):
    command = ["steghide", "embed", "-cf", image_path, "-ef", data_file_path, "-p", passphrase]

    try:
    
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # If the command runs successfully, print the output in green color
        print(Fore.GREEN + "Success!")
    except subprocess.CalledProcessError as e:
        # If the command fails, print the error in red color
        print(Fore.RED + "Error:", e)

    str = passphrase
    res = ''.join(format(ord(i), '08b') for i in str)
    #image will have max 108 characters on it
    image = Image.open("/media/astr0/COCK/python/steghide++/black.png") ## enter path you want to use to write text on
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype("/media/astr0/COCK/python/steghide++/arial.ttf", 25) ##enter font path you want to use to write text with
    text = res
    textpos = (0, 0)
    text_color = (255, 255, 255) ## enter color you want the text 2 be

    d.text(textpos, text, font=font, fill=text_color)
    image.save("binary_image.png")
    print(Fore.YELLOW + "image saved under binary_image.png")



def embed_data_with_steghide(image_path, data_file_path, passphrase):
    # Construct the steghide command
    command = ["steghide", "embed", "-cf", image_path, "-ef", data_file_path, "-p", passphrase]

    try:
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # If the command runs successfully, print the output in green color
        print(Fore.GREEN + "Success!")
    except subprocess.CalledProcessError as e:
        # If the command fails, print the error in red color
        print(Fore.RED + "Error:", e)

def extract_data_with_steghide(image_path, passphrase):
    # Construct the steghide command
    command = ["steghide", "extract", "-sf", image_path, "-p", passphrase]

    try:
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Print the extracted file location in green color
        print(Fore.GREEN + "Success!")
    except subprocess.CalledProcessError as e:
        # If the command fails, print the error in red color
        print(Fore.RED + "Error:", e)


def install_or_update_steghide():
    try:
        result = subprocess.run(["steghide", "--version"], capture_output=True, text=True)
        if "steghide" in result.stdout:
           print(Fore.GREEN + "Steghide is already installed")
          
    except Exception as e:
        print(Fore.YELLOW + "Steghide is not installed. Installing...")
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "steghide"])
        print(Fore.YELLOW + "Steghide installed successfully.")
                    
        

def install_or_update_tesseract():
    try:
        result = subprocess.run(["tesseract", "--version"], capture_output=True, text=True)
        if 'tesseract' in result.stdout:
            print(Fore.GREEN +"tesseract-ocr is already installed")
    except Exception as e:
        print(Fore.YELLOW + "Tesseract-OCR is not installed. Installing...")
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "tesseract-ocr"])
        print(Fore.YELLOW + "Tesseract-OCR installed successfully.")


install_or_update_steghide()
install_or_update_tesseract()

print(Fore.MAGENTA + """
                                                                                                                                                                                             
                                                                                                                       dddddddd                                                              
                          tttt                                                 hhhhhhh               iiii              d::::::d                                                              
                       ttt:::t                                                 h:::::h              i::::i             d::::::d                                                              
                       t:::::t                                                 h:::::h               iiii              d::::::d                                                              
                       t:::::t                                                 h:::::h                                 d:::::d                            +++++++              +++++++       
    ssssssssss   ttttttt:::::ttttttt        eeeeeeeeeeee       ggggggggg   gggggh::::h hhhhh       iiiiiii     ddddddddd:::::d     eeeeeeeeeeee           +:::::+              +:::::+       
  ss::::::::::s  t:::::::::::::::::t      ee::::::::::::ee    g:::::::::ggg::::gh::::hh:::::hhh    i:::::i   dd::::::::::::::d   ee::::::::::::ee         +:::::+              +:::::+       
ss:::::::::::::s t:::::::::::::::::t     e::::::eeeee:::::ee g:::::::::::::::::gh::::::::::::::hh   i::::i  d::::::::::::::::d  e::::::eeeee:::::ee +++++++:::::+++++++  +++++++:::::+++++++ 
s::::::ssss:::::stttttt:::::::tttttt    e::::::e     e:::::eg::::::ggggg::::::ggh:::::::hhh::::::h  i::::i d:::::::ddddd:::::d e::::::e     e:::::e +:::::::::::::::::+  +:::::::::::::::::+ 
 s:::::s  ssssss       t:::::t          e:::::::eeeee::::::eg:::::g     g:::::g h::::::h   h::::::h i::::i d::::::d    d:::::d e:::::::eeeee::::::e +:::::::::::::::::+  +:::::::::::::::::+ 
   s::::::s            t:::::t          e:::::::::::::::::e g:::::g     g:::::g h:::::h     h:::::h i::::i d:::::d     d:::::d e:::::::::::::::::e  +++++++:::::+++++++  +++++++:::::+++++++ 
      s::::::s         t:::::t          e::::::eeeeeeeeeee  g:::::g     g:::::g h:::::h     h:::::h i::::i d:::::d     d:::::d e::::::eeeeeeeeeee         +:::::+              +:::::+       
ssssss   s:::::s       t:::::t    tttttte:::::::e           g::::::g    g:::::g h:::::h     h:::::h i::::i d:::::d     d:::::d e:::::::e                  +:::::+              +:::::+       
s:::::ssss::::::s      t::::::tttt:::::te::::::::e          g:::::::ggggg:::::g h:::::h     h:::::hi::::::id::::::ddddd::::::dde::::::::e                 +++++++              +++++++       
s::::::::::::::s       tt::::::::::::::t e::::::::eeeeeeee   g::::::::::::::::g h:::::h     h:::::hi::::::i d:::::::::::::::::d e::::::::eeeeeeee                                            
 s:::::::::::ss          tt:::::::::::tt  ee:::::::::::::e    gg::::::::::::::g h:::::h     h:::::hi::::::i  d:::::::::ddd::::d  ee:::::::::::::e                                            
  sssssssssss              ttttttttttt      eeeeeeeeeeeeee      gggggggg::::::g hhhhhhh     hhhhhhhiiiiiiii   ddddddddd   ddddd    eeeeeeeeeeeeee                                            
                                                                        g:::::g                                                                                                              
                                                            gggggg      g:::::g                                                                                                              
                                                            g:::::gg   gg:::::g                                                                                                              
                                                             g::::::ggg:::::::g                                                                                                              
                                                              gg:::::::::::::g                                                                                                               
                                                                ggg::::::ggg                                                                                                                 
                                                                   gggggg                                                                                                                      
""")
print(Fore.YELLOW + """\n
[1] Encrypt using password --- Uses password instead of binary image.
[2] Decrypt using password --- Uses password instead of binary image.
[3] Encypt and print binary image --- Encypts coverfile and prints passphrase in a binary image
[4] Decrypt using binary image --- Takes binary image and decrypts cover file.
[5] Help
""")

options = ["1", "2", "3", "4", "5"]

while True:
    option = input("\nWhat would you like to do today: ")
    if option not in options:
        print(Fore.RED + "\nError: Invalid input. Please enter a number.")
    else:
        break


if option == "1":
    print(Fore.YELLOW + "[1] Encrypt using password --- Uses password instead of binary image.")
    image_path = input("Enter the path to the image file: ")
    data_file_path = input("Enter the path to the data file: ")
    passphrase = input("Enter the passphrase (optional): ")
    embed_data_with_steghide(image_path, data_file_path, passphrase)

elif option == "2":
    print(Fore.YELLOW + "[2] Decrypt using password --- Uses password instead of binary image.")
    image_path = input("Enter the path to the image file: ")
    passphrase = input("Enter the passphrase: ")
    extract_data_with_steghide(image_path, passphrase)
elif option == "3":
    print(Fore.YELLOW + "[3] Encypt and print binary image --- Encypts coverfile and prints passphrase in a binary image.")
    image_path = input("Enter the path to the image file: ")
    data_file_path = input("Enter the path to the data file: ")
    passphrase = input("Enter the passphrase (Max 10 char): ")
    print_binary_image(image_path, data_file_path, passphrase)
elif option == "4":
    print(Fore.YELLOW + "[4] Decrypt using binary image --- Takes binary image and decrypts cover file.")
    image_path = input("Enter the path to the image file: ")
    binary_path = input("Enter the path to the binary image: ")
    binary_img_translate(image_path, binary_path)

elif option == "5":
    print(Fore.CYAN + """
**Steganography Utility Help Page:**

This utility allows you to perform steganography operations using steghide.

**Options:**

1. **Encrypt using password:** Embeds data into an image using a passphrase.
2. **Decrypt using password:** Extracts hidden data from an image using a passphrase.
3. **Encrypt and print binary image:** Encrypts cover file and prints passphrase in a binary image.
4. **Decrypt using binary image:** Extracts hidden data from an image using a binary image.
5. **Help:** Display this help page.

---

**Notes:**

- **Encrypt using password (Option 1):**
  - Prompts for the path to the image file and the data file.
  - Optionally, you can provide a passphrase for additional security.

- **Decrypt using password (Option 2):**
  - Prompts for the path to the image file and the passphrase.
  - Extracts hidden data from the image using the provided passphrase.

- **Encrypt and print binary image (Option 3):**
  - Prompts for the path to the image file and the data file.
  - Optionally, you can provide a passphrase (max 10 characters) for additional security.
  - Generates a binary image with the passphrase encoded and saves it as 'binary_image.png'.

- **Decrypt using binary image (Option 4):**
  - Prompts for the path to the image file and the binary image file.
  - Extracts hidden data from the image using the provided binary image.

- **General Notes:**
  - Ensure the cover file is not smaller than the embedded file.
  - If files are in the same directory as the program, you can simply type the file names.
  - Only `.wav` audio files can be used to embed files into audio.

---

**Additional Information:**

- **Dependencies:**
  - This utility requires steghide and tesseract-ocr to be installed.
  - If not installed, the utility will attempt to install them automatically.
""")


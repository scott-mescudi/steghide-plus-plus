#made by goslar61
import subprocess
from colorama import init, Fore
import time
import os
# Initialize colorama
init(autoreset=True)

def print_binary_image(image_path, data_file_path, passphrase):
    from PIL import Image, ImageDraw, ImageFont
    command = ["steghide", "embed", "-cf", image_path, "-ef", data_file_path, "-p", passphrase]
  
    try:
      result = subprocess.run(command, capture_output=True, text=True, check=True)
    
      str = passphrase
      res = ''.join(format(ord(i), '08b') for i in str)
      #image will have max 108 characters on it
      image = Image.open("/media/astr0/COCK/steghide++/black.png") ## enter path you want to use to write text on
      d = ImageDraw.Draw(image)
      font = ImageFont.truetype("/media/astr0/COCK/steghide++/arial.ttf", 25) ##enter font path you want to use to write text with
      text = res
      textpos = (0, 0)
      text_color = (255, 255, 255) ## enter color you want the text 2 be

      d.text(textpos, text, font=font, fill=text_color)
      image.save("binary_image.png")
      print(Fore.GREEN + "Success!")
      print(Fore.YELLOW + "image saved under binary_image.png")
    except subprocess.CalledProcessError as e:
      # If the command fails, print the error in red color
      print(Fore.RED + "Error: file not found")

   
   


def binary_img_translate(image_path, binary_path):
    from PIL import Image, ImageDraw, ImageFont
    import pytesseract
    try:
      image = Image.open(binary_path)
      text = pytesseract.image_to_string(image)
      binary = text
      normal = ""
      
      # Split the binary string into chunks of 8 characters
      for chunk in [binary[i:i+8] for i in range(0, len(binary), 8)]:
          try:
              # Convert each chunk to an integer and then to a character
              normal += chr(int(chunk, 2))
          except ValueError:
              # Handle non-convertible chunks gracefully (you can add your own error handling logic here)
              pass
      
      command = ["steghide", "extract", "-sf", image_path, "-p", normal]

      try:
          # Execute the command
          result = subprocess.run(command, capture_output=True, text=True, check=True)
          # If the command runs successfully, print the output in green color
          print(Fore.GREEN + "Success!")
      except subprocess.CalledProcessError as e:
          # If the command fails, print the error in red color
          print(Fore.RED + "Error:", e)
    except FileNotFoundError:
        print(Fore.RED + "Error: file not found")



    



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
        print(Fore.RED + "Error: file not found")

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
        print(Fore.RED + "Error: file not found")

def password_gen():
  import random
  try:
    init(autoreset=True)
    numbers = list(range(1, 10))
    uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabc")
    lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    combined_list = numbers + uppercase_letters + lowercase_letters + special_characters
    new = []
    
    q = input("password length: ")

    
    for i in range(int(q)):
      new.append(str(random.choice(combined_list)))
    password =  str(''.join(new))
    
    print("\nPassword of " + Fore.YELLOW + str(q) + Fore.WHITE + " characters is " + Fore.YELLOW + password + "\n")
  except ValueError:
      print(Fore.RED + "please enter a number ")
      time.sleep(1)
      password_gen()

def help_page():
    print(Fore.CYAN + """
**Steganography Utility Help Page:**

This utility allows you to perform steganography operations using steghide.

**Options:**

1. **Encrypt using password:** Embeds data into an image using a passphrase.
2. **Decrypt using password:** Extracts hidden data from an image using a passphrase.
3. **Encrypt and print binary image:** Encrypts coverfile and prints passphrase in a binary image.
4. **Decrypt using binary image:** Extracts hidden data from an image using a binary image.
5. **Generate a random password:** Generate a variable length password with ASCII characters.
6. **Help:** Display this help page.

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

- **Generate a random password (Option 5):**
  - Prompts for the desired length of the password.
  - Generates a random password of the specified length.

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
[5] Generate a random password --- Generate a variable length password with ascii characters
[6] Help
""")

options = ["1", "2", "3", "4", "5", "6"]

while True:
    option = input("\nWhat would you like to do today: ")
    if option not in options:
        print(Fore.RED + "\nError: Invalid input. Please enter a number.")
    else:
        break



def validate_file_path(prompt):
    while True:
        file_path = input(prompt)
        if not os.path.exists(file_path):
            print(Fore.RED + f"Error: File '{file_path}' not found.")
        else:
            return file_path

def validate_image_path(prompt):
    while True:
        image_path = input(prompt)
        if not os.path.exists(image_path):
            print(Fore.RED + f"Error: Image file '{image_path}' not found.")
        elif not image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            print(Fore.RED + "Error: Invalid image format. Supported formats are PNG, JPG, JPEG, BMP, and GIF.")
        else:
            return image_path

def validate_passphrase(prompt):
    while True:
        passphrase = input(prompt)
        if len(passphrase) > 10:
            print(Fore.RED + "Error: Passphrase must be maximum 10 characters.")
        else:
            return passphrase


if option == "1":
    print(Fore.YELLOW + "[1] Encrypt using password --- Uses password instead of binary image.")
    image_path = validate_image_path("Enter the path to the image file: ")
    data_file_path = validate_file_path("Enter the path to the data file: ")
    passphrase = input("Enter the passphrase (optional): ")
    embed_data_with_steghide(image_path, data_file_path, passphrase)


elif option == "2":
    print(Fore.YELLOW + "[2] Decrypt using password --- Uses password instead of binary image.")
    image_path = validate_image_path("Enter the path to the image file: ")
    passphrase = input("Enter the passphrase: ")
    extract_data_with_steghide(image_path, passphrase)


elif option == "3":
    print(Fore.YELLOW + "[3] Encrypt and print binary image --- Encrypts cover file and prints passphrase in a binary image.")
    image_path = validate_image_path("Enter the path to the image file: ")
    data_file_path = validate_file_path("Enter the path to the data file: ")
    passphrase = validate_passphrase("Enter the passphrase (Max 10 characters): ")
    print_binary_image(image_path, data_file_path, passphrase)


elif option == "4":
    print(Fore.YELLOW + "[4] Decrypt using binary image --- Takes binary image and decrypts cover file.")
    image_path = validate_image_path("Enter the path to the image file: ")
    binary_path = validate_file_path("Enter the path to the binary image: ")
    binary_img_translate(image_path, binary_path)


elif option == "5":
    print(Fore.YELLOW + "[5] Generate a random password --- Generate a variable length password with ASCII characters.")
    password_gen()

elif option == "6":
    help_page()

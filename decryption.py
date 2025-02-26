import cv2

def decrypt_image(image_path, password_file):
    # Load the encrypted image (lossless PNG format)
    img = cv2.imread(image_path)
    if img is None:
        print("Encrypted image not found!")
        return

    # Retrieve the stored password from file
    try:
        with open(password_file, "r") as f:
            correct_pass = f.read().strip()
    except FileNotFoundError:
        print("Password file not found!")
        return

    # Ask user for the decryption passcode
    pas = input("Enter passcode for Decryption: ")
    if pas != correct_pass:
        print("Incorrect passcode. Access denied!")
        return

    # Ask user for the secret message length
    try:
        length = int(input("Enter secret message length: "))
    except ValueError:
        print("Invalid length input!")
        return

    message = ""
    n = 0  # row index
    m = 0  # column index
    z = 0  # channel index

    # Read the embedded message from the image
    for i in range(length):
        # Check if we are within image boundaries
        if n >= img.shape[0] or m >= img.shape[1]:
            print("Reached image boundary before reading the full message.")
            break
        # Read the pixel channel value and convert it back to a character
        message += chr(img[n, m, z])
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", message)

if __name__ == "__main__":
    image_path = "kitten_encrypted.png"  # Path to the encrypted image
    password_file = "passcode.txt"  # Path to the password file
    decrypt_image(image_path, password_file)
import cv2

def encrypt_image(image_path, message, password, output_path):
    img = cv2.imread(image_path)  # Load the image
    if img is None:
        print("Cover image not found!")
        return

    # Save the password to a file (for demonstration purposes only)
    with open("passcode.txt", "w") as f:
        f.write(password)

    # Embed the message into the image
    n = 0  # row index
    m = 0  # column index
    z = 0  # channel index (0=Blue, 1=Green, 2=Red in OpenCV)

    for char in message:
        # Check if we are within image boundaries
        if n >= img.shape[0] or m >= img.shape[1]:
            print("Message is too long for the image!")
            break
        # Write the ASCII value of the character into the chosen pixel channel
        img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % 3

    # Save the encrypted image as PNG to avoid lossy compression
    cv2.imwrite(output_path, img)
    print(f"Secret message embedded into image and saved as {output_path}")
    print(f"Remember the message length: {len(message)}")

if __name__ == "__main__":
    image_path = "kitten.jpg"  # Path to the cover image
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    output_path = "kitten_encrypted.png"  # Output file name
    encrypt_image(image_path, message, password, output_path)
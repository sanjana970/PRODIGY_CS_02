from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_img = Image.new(img.mode, img.size)
    
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple(p ^ key for p in pixel)  # Perform XOR operation with the key
            encrypted_img.putpixel((x, y), encrypted_pixel)
    
    encrypted_img.show()
    encrypted_img.save("encrypted_image.png")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    decrypted_img = Image.new(img.mode, img.size)
    
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            decrypted_pixel = tuple(p ^ key for p in pixel)  # Perform XOR operation with the key
            decrypted_img.putpixel((x, y), decrypted_pixel)
    
    decrypted_img.show()
    decrypted_img.save("decrypted_image.png")

def main():
    while True:
        choice = input("Enter 'e' to encrypt an image, 'd' to decrypt an image, or 'q' to quit: ").lower()
        if choice == 'q':
            print("Exiting program.")
            break
        elif choice == 'e':
            image_path = input("Enter the path to the image to encrypt: ")
            key = int(input("Enter the encryption key (a number between 0 and 255): "))
            encrypt_image(image_path, key)
        elif choice == 'd':
            image_path = input("Enter the path to the image to decrypt: ")
            key = int(input("Enter the decryption key (the same number used for encryption): "))
            decrypt_image(image_path, key)
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if _name_ == "_main_":
    main()
from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    """
    Encrypt an image by applying a simple mathematical operation on each pixel.
    :param image_path: Path to the image file.
    :param key: Integer key used to manipulate pixel values.
    :return: Encrypted image.
    """
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Apply encryption (add the key to the pixel values)
    encrypted_array = img_array + key
    
    # Ensure pixel values stay within the valid range [0, 255]
    encrypted_array = np.clip(encrypted_array, 0, 255)
    
    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    
    return encrypted_image

def decrypt_image(encrypted_image, key):
    """
    Decrypt the image by reversing the encryption operation.
    :param encrypted_image: Encrypted image.
    :param key: Integer key used to manipulate pixel values.
    :return: Decrypted image.
    """
    img_array = np.array(encrypted_image)
    
    # Reverse the encryption (subtract the key from the pixel values)
    decrypted_array = img_array - key
    
    # Ensure pixel values stay within the valid range [0, 255]
    decrypted_array = np.clip(decrypted_array, 0, 255)
    
    # Convert back to image
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    
    return decrypted_image

if __name__ == "__main__":
    print("🔄 Running the script...")

    # Correct image path
    image_path = "C:/Users/radha/OneDrive/Desktop/PRODIGY_CS_02/image.jpg"  # Updated image path
    key = 50  # Encryption key, you can change this value

    if not os.path.exists(image_path):
        print("❌ Image 'image.jpg' not found in current folder.")
    else:
        print("✅ Image found. Encrypting now...")

        # Encrypt the image
        encrypted_image = encrypt_image(image_path, key)
        encrypted_image.save('encrypted_image.jpg')
        encrypted_image.show()

        # Decrypt the image
        decrypted_image = decrypt_image(encrypted_image, key)
        decrypted_image.save('decrypted_image.jpg')
        decrypted_image.show()

        print("✅ Done! Encrypted and decrypted images saved.")

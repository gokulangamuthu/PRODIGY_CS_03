from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size

    # Convert the image to RGB mode
    rgb_image = image.convert('RGB')

    # Create a new image for encrypted pixels
    encrypted_image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel at (x, y)
            r, g, b = rgb_image.getpixel((x, y))

            # Perform pixel manipulation using the encryption key
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            # Set the modified pixel in the new image
            encrypted_image.putpixel((x, y), (r, g, b))

    # Save the encrypted image
    encrypted_image.save("encrypted_image.png")

    print("Image encrypted successfully!")

# Example usage:
image_path = "images.jpg"
encryption_key = 50
encrypt_image(image_path, encryption_key)

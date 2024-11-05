from openai import OpenAI
from PIL import Image
import io

# Set your OpenAI API key (replace with your actual key)
Api_Key = "APIKEY"
Image_Path = "image.png"

def generate_image_from_prompt(prompt):
    """Generates an image using DALL-E and returns the image data."""
    try:
        print("Generating image...")
        client = OpenAI(api_key=Api_Key)

        response = client.images.generate(
          model="dall-e-2",
          prompt=prompt,
          size="1024x1024",
          quality="standard",
          n=1,
        )

        image_url = response.data[0].url
                # Download the image data from the URL
        import requests
        img_data = requests.get(image_url).content
        with open(Image_Path, 'wb') as handler:
            handler.write(img_data)
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def image_to_ascii(width=80):
    """Converts image data to ASCII art."""
    try:
        print("Converting image to ASCII...")
        img = Image.open(Image_Path).convert("L")  # Convert to grayscale
        img.thumbnail((width, width * img.height // img.width)) # Resize proportionally

        ascii_chars = "@%#*+=-:. "  # Characters for different brightness levels
        ascii_art = ""
        for y in range(img.height):
            for x in range(img.width):
                pixel_value = img.getpixel((x, y))
                char_index = int(pixel_value / 256 * len(ascii_chars))
                ascii_art += ascii_chars[char_index]
            ascii_art += "\n"
        return ascii_art
    except Exception as e:
        return f"Error converting image: {e}"

if __name__ == "__main__":
    prompt = input("Enter a description for the image you want: ")
    generate_image_from_prompt(prompt)

    ascii_art = image_to_ascii()
    
    print(ascii_art)
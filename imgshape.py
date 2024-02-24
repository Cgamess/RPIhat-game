def process_image(image_path):
    try: from pillow import image as PILImage
    except: from sense_hat import Image as PILImage
    # Open the image using the alias
    img = PILImage.open(image_path)

    # Get the size of the image
    width, height = img.size

    # Determine the value of n
    n = int((width.bit_length() - 1) / 8)

    # Initialize the dictionary to store 8x8 chunks
    chunks_dict = {}

    # Process the image and store chunks in the dictionary
    for y in range(0, height, 8):
        for x in range(0, width, 8):
            chunk = img.crop((x, y, x + 8, y + 8))
            idvalue = (x // 8, y // 8)
            chunks_dict[(idvalue[0], idvalue[1], n)] = chunk

    # Close the image
    img.close()

    return chunks_dict


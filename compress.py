import xml.etree.ElementTree as ET
import base64
from PIL import Image
from io import BytesIO

# Version 1: Read input.svg and print it to the console
# Version 2: Find all the image tag and print them to the console
# Version 3: Extract the image href and print them to the console
# Version 4: Extract the image href and print the data type and data to the console
# Version 5: Convert the base64 data to binary and print the binary data to the console
# Version 6: Convert the binary data to an Image object and display the image
# Version 7: Convert the Image object to webp format and print the webp data to the console
# Version 8: Convert the webp data to base64 and print the base64 data to the console


def main():
    tree = ET.parse('input.svg')
    root = tree.getroot()

    for elem in root.iter():
        if elem.tag.endswith('image'):
            href_data = elem.attrib['href'].split(',')
            data_base64_bytes = href_data[1].encode('ascii')

            data_bytes = base64.b64decode(data_base64_bytes)

            img = Image.open(BytesIO(data_bytes))
            
            webp_data = BytesIO()
            img.save(webp_data, format='webp')
            
            webp_data_base64 = base64.b64encode(webp_data.getvalue()).decode('ascii')
            
            print(webp_data_base64)


if __name__ == "__main__":
    main()

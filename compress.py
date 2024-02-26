import xml.etree.ElementTree as ET
import base64

# Version 1: Read input.svg and print it to the console
# Version 2: Find all the image tag and print them to the console
# Version 3: Extract the image href and print them to the console
# Version 4: Extract the image href and print the data type and data to the console
# Version 5: Convert the base64 data to binary and print the binary data to the console
def main():
    tree = ET.parse('input.svg')
    root = tree.getroot()
    
    for elem in root.iter():
        if elem.tag.endswith('image'):
            href_data = elem.attrib['href'].split(',')
            data_type = href_data[0].split(';')[0].split(':')[1].split('/')[1]
            data_base64_bytes = href_data[1].encode('ascii')
            
            data_bytes = base64.b64decode(data_base64_bytes)
            
            print(data_bytes)

if __name__ == "__main__":
    main()

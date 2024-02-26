import xml.etree.ElementTree as ET

# Version 1: Read input.svg and print it to the console
# Version 2: Find all the image tag and print them to the console
# Version 3: Extract the image href and print them to the console
def main():
    tree = ET.parse('input.svg')
    root = tree.getroot()
    
    for elem in root.iter():
        if elem.tag.endswith('image'):
            print(elem.attrib['href'])

if __name__ == "__main__":
    main()

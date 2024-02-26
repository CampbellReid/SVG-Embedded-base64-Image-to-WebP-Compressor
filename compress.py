import xml.etree.ElementTree as ET

# Version 2: Find all the image tag and print them to the console
def main():
    tree = ET.parse('input.svg')
    root = tree.getroot()
    
    for elem in root.iter():
        if elem.tag.endswith('image'):
            print(elem.tag, elem.attrib)

if __name__ == "__main__":
    main()

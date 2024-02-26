import xml.etree.ElementTree as ET

# Version 1: Read input.svg and print it to the console
def main():
    tree = ET.parse('input.svg')
    root = tree.getroot()
    print(ET.tostring(root, encoding='utf8').decode('utf8'))

if __name__ == "__main__":
    main()

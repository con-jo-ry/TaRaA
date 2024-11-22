import xml.etree.ElementTree as ET

def validate_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        print("XML is well-formed and valid")
        return True
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
        return False

# Usage
validate_xml("tvb_g.xml")

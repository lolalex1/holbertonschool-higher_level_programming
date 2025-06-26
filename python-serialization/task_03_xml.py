#!/usr/bin/python3
"""Module to serialize and deserialize dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML and save to the given filename."""
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        with open(filename, 'wb') as xml_file:
            tree.write(xml_file, encoding='utf-8', xml_declaration=True)
    except (IOError, ET.ParseError):
        pass


def deserialize_from_xml(filename):
    """Deserialize XML file content into a dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}

    except (IOError, ET.ParseError):
        return None

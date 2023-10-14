import xmlschema

def main():
    root_elements = xmlschema.XMLSchema('../sample/jmx.xsd').root_elements
    for ele in root_elements:
        print_children_element(ele, 0)


def print_children_element(element:xmlschema.XsdElement, depth):
    indent = ''
    for _ in range(depth):
        indent = indent + '    '
    
    print(indent, element.local_name or 'any', sep='', end=None if len(element.attributes) == 0 else '')
    for attrib in element.attributes.keys():
        print('\t', attrib, '\t', element.attributes[attrib].type.enumeration or '', sep='')

    for ele in element.iterchildren():
        print_children_element(ele, depth + 1)

if __name__ == "__main__":
    main()
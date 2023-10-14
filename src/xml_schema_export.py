import xmlschema

def main():
    root_elements = xmlschema.XMLSchema('../sample/jmx.xsd').root_elements
    for ele in root_elements:
        print_children_element(ele, 0)


def print_children_element(element:xmlschema.XsdElement, depth):
    indent = ''
    for _ in range(depth):
        indent = indent + '    '
    print(indent, element.local_name or 'any', sep='')

    for ele in element.iterchildren():
        print_children_element(ele, depth + 1)

if __name__ == "__main__":
    main()
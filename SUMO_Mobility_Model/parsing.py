from xml.etree.ElementTree import parse

# tree = parse('./data/trace_dump.xml')
tree = parse('sumoTrace.xml')
root = tree.getroot()

timestep =root.find("timestep/vehicle").attrib

print(timestep)
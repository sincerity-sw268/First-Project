from xml.etree.ElementTree import parse
import random
# tree = parse('./data/trace_dump.xml')
tree = parse('sumoTrace.xml')
root = tree.getroot()

timestep =root.find("timestep/vehicle").attrib

print(timestep)

print(random.seed(42))
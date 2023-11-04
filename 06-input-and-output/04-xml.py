import xml.etree.ElementTree as ET

root = ET.fromstring('''
<data>
  <country name="Italy">
    <rank>42</rank>
    <year>1861</year>
  </country>
</data>
''')

print(root[0][1].text) # '1861'
print(ET.dump(root)) # prints the xml + 'None': why? See below
ET.dump(root) # dumps to stdout
print(ET.tostring(root)) # prints the binary string
print(ET.tostring(root).decode()) # prints the string

tree = ET.parse('countries.xml')
root = tree.getroot()

print(root.tag) # 'data'
print(root.attrib) # '{}'

for child in root:
  print(child.tag, child.attrib)
# country {'name': 'Liechtenstein'}
# country {'name': 'Singapore'}
# country {'name': 'Panama'}

for element in root.findall('./country[@name="Liechtenstein"]/neighbor'): # XPath
  print(element.attrib['name'])

# For more info on XPath @see https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support

# For non-blocking parsing @see https://docs.python.org/3/library/xml.etree.elementtree.html#pull-api-for-non-blocking-parsing

for rank in root.iter('rank'):
  new_rank = int(rank.text) + 1
  rank.text = str(new_rank) # update content
  rank.set('updated', 'true') # update an attribute

print(root[0][0].text)
print(root[0][0].attrib['updated'])

tree.write('updated_countries.xml')

for country in root.findall('country'): # findall creates a new list so we can safely remove elements from the document
  rank = int(country.find('rank').text)
  if rank > 50:
    root.remove(country) # remove an element

tree.write('updated_countries.xml')

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)

# For extra features of XML @see https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml-with-namespaces

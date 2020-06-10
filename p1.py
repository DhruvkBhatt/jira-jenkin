import json as j

d={
  "Name" : "Rani",
  "Designation" : "PHP Developer",
  "Salary" : 98000,
  "Age":27,
  "Projects" : [
          {"Topic":"Smart Ambulance","Category":"Android Application","Months":2},
          {"Topic":"AST","Category":"Embedded System","Months":1},
          {"Topic":"Plant Nursery","Category":"Website","Months":3}
  ]
}

print(d)

import xml.etree.cElementTree as e
r = e.Element("Employee")
e.SubElement(r,"Name").text = d["Name"]
e.SubElement(r,"Designation").text = d["Designation"]
e.SubElement(r,"Salary").text = str(d["Salary"])
e.SubElement(r,"Age").text = str(d["Age"])
project = e.SubElement(r,"Projects")
for z in d["Projects"]:
  e.SubElement(project,"Topic").text = z["Topic"]
  e.SubElement(project,"Category").text = z["Category"]
  e.SubElement(project,"Months").text = str(z["Months"])
a = e.ElementTree(r)
a.write("json_to_xml.xml")
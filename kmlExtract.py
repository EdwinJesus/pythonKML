import xml.etree.ElementTree as ET
import os

def saveFile(text,file):
    cvs = open(file,"w+")
    cvs.write(text)
    cvs.close()

pathSave = ""
path = ""

tree = ET.parse(path+"name.kml")

root = tree.getroot()

folderStrings = tree.findall('.//{http://www.opengis.net/kml/2.2}Document')

print("Begin")

for folder in folderStrings:
    name = folder.find("{http://www.opengis.net/kml/2.2}name")

    print(name.text)

    placemark = folder.findall("{http://www.opengis.net/kml/2.2}Placemark")

    for place in placemark:
        name = place.find("{http://www.opengis.net/kml/2.2}name")        
        print(name.text)
        poligons = place.findall("{http://www.opengis.net/kml/2.2}Polygon")
        #print(poligons)
        for point in poligons:
            outer =  point.findall("{http://www.opengis.net/kml/2.2}outerBoundaryIs")
            
            for gps in outer:
                linearRing = gps.findall("{http://www.opengis.net/kml/2.2}LinearRing")
                print("linearRing")
                print(linearRing)
                for linear in linearRing:
                    coor = linear.find("{http://www.opengis.net/kml/2.2}coordinates")

                    coordenadasClean = coor.text.strip().replace("\n","").replace("\t","").replace(",", " ").replace("0 -", ",-").replace(" 0", "").replace(" ,-", ",-").strip()

                    saveFile(coordenadasClean,pathSave+name.text+".txt")

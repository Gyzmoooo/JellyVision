import subprocess
import os
import xml.etree.ElementTree as ET
import git

porta = 322
password = "masbeppe09"
ipRpi = "192.168.139.207"
photoFolder = "/home/pablo/Desktop/Code2k24/jellyVision/photos"
toSaveLocation = "C:\\Users\\Admin\\Desktop\\hackatonMain"

def transferFromPi(porta, password, ipRpi, photoFolder, toSaveLocation):
    comando = f"echo y | pscp -r -P {porta} -pw {password} pablo@{ipRpi}:{photoFolder} {toSaveLocation}"
    subprocess.run(comando, shell=True)

def create_xml_file(filename, folder, img_filename, path, width, height, object_name, xmin, ymin, xmax, ymax):
    root = ET.Element("annotation")
    
    ET.SubElement(root, "folder").text = folder
    ET.SubElement(root, "filename").text = img_filename
    ET.SubElement(root, "path").text = path
    
    source = ET.SubElement(root, "source")
    ET.SubElement(source, "database").text = "Unknown"
    
    size = ET.SubElement(root, "size")
    ET.SubElement(size, "width").text = str(width)
    ET.SubElement(size, "height").text = str(height)
    ET.SubElement(size, "depth").text = str(3.0)
    
    ET.SubElement(root, "segmented").text = "0"
    
    obj = ET.SubElement(root, "object")
    ET.SubElement(obj, "name").text = object_name
    ET.SubElement(obj, "pose").text = "Unspecified"
    ET.SubElement(obj, "truncated").text = "0"
    ET.SubElement(obj, "difficult").text = "0"
    
    bndbox = ET.SubElement(obj, "bndbox")
    ET.SubElement(bndbox, "xmin").text = str(xmin)
    ET.SubElement(bndbox, "ymin").text = str(ymin)
    ET.SubElement(bndbox, "xmax").text = str(xmax)
    ET.SubElement(bndbox, "ymax").text = str(ymax)
    
    tree = ET.ElementTree(root)
    tree.write(filename)



for i in os.listdir(f'{toSaveLocation}\\photos'):
    os.rename(f'{toSaveLocation}\\photos\\{i}', f'{toSaveLocation}\\photos\\45,491661_12,240957_{i}')
    name = f'{toSaveLocation}\\photos\\45,491661_12,240957_{i}'.strip('jpg')

create_xml_file(f'{name}.xml', 'a', f'{name}.jpg', 'a', 720, 720, 'pelagia', 170.0, 140.0, 580.0, 550.0 )

def commitGit():
    xmlToCommit = (f'{name}.xml')

    repo_url = "https://github.com/Gyzmoooo/JellyVision/tree/main/xmlData"




'''
def git():
    print('a')

if __name__ == "__main__":
    transferFromPi(porta, password, ipRpi, photoFolder, toSaveLocation)
    for i in os.listdir(f'{toSaveLocation}\\photos'):
        os.rename(f'{toSaveLocation}\\photos\\{i}', f'{toSaveLocation}\\photos\\45,491661_12,240957_{i}')
        name = f'{toSaveLocation}\\photos\\45,491661_12,240957_{i}'.strip('jpg')
        create_xml_file(f'{name}.xml', 'a', f'{name}.jpg', 'a', 720, 720, 'pelagia', 170.0, 140.0, 580.0, 550.0 )
'''

import random 
import xml.etree.ElementTree as ET
from xml.dom import minidom

def make_regression(n_samples=150, n_features =1, noise=42, random_state=42):
    # Set the seed for reproducibility
    random.seed(random_state)

    x = []
    y = []

    for _ in range(n_samples):
        features = [random.uniform(-10, 10) for _ in range(n_features)]
        target = sum(features) + random.gauss(0, noise) #Linear relationship with added Gaussian noise

        x.append(features)
        y.append(target)

    return x, y

choice = input("Would you like to generate a random regression data? (yes/no): ")

if choice == 'yes':
    file_name = input('Enter file name: ')

    x, y = make_regression(n_samples=150, n_features=1, noise=42, random_state=42)

    root = ET.Element('Dataset')

    for features, target in zip(x, y):
        sample =ET.SubElement(root, 'Sample')
        for i, feature in enumerate(features):
            ET.SubElement(sample, f'Feature{i+1}').text = f'{feature:.2f}'
        ET.SubElement(sample, 'Target').text = f'{target:.2f}'

    tree = ET.ElementTree(root)
    
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "     ")

    with open(f'{file_name}.xml', 'w') as file:
        file.write(xml_str)
    
    print("Data has been written to 'regression_data.xml'")

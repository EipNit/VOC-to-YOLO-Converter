import os
import xml.etree.ElementTree as ET


def get_class_list(input_dir):
    """
    Extract a list of unique class names from VOC XML files.

    Parameters:
    - input_dir: Directory containing VOC XML files.

    Returns:
    - class_list: List of unique class names.
    """
    classes = set()

    for filename in os.listdir(input_dir):
        if not filename.endswith('.xml'):
            continue

        tree = ET.parse(os.path.join(input_dir, filename))
        root = tree.getroot()

        for obj in root.iter('object'):
            class_name = obj.find('name').text
            classes.add(class_name)

    return sorted(list(classes))


def voc_to_yolo(input_dir, output_dir, class_list):
    """
    Convert VOC format annotations to YOLO format.

    Parameters:
    - input_dir: Directory containing VOC XML files.
    - output_dir: Directory to save YOLO TXT files.
    - class_list: List of class names in the order they appear in the YOLO model.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if not filename.endswith('.xml'):
            continue

        tree = ET.parse(os.path.join(input_dir, filename))
        root = tree.getroot()

        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        with open(os.path.join(output_dir, filename.replace('.xml', '.txt')), 'w') as f:
            for obj in root.iter('object'):
                difficult = obj.find('difficult').text
                if int(difficult) == 1:
                    continue

                class_name = obj.find('name').text
                if class_name not in class_list:
                    continue

                class_id = class_list.index(class_name)

                bndbox = obj.find('bndbox')
                xmin = float(bndbox.find('xmin').text)
                ymin = float(bndbox.find('ymin').text)
                xmax = float(bndbox.find('xmax').text)
                ymax = float(bndbox.find('ymax').text)

                x_center = (xmin + xmax) / 2.0 / width
                y_center = (ymin + ymax) / 2.0 / height
                box_width = (xmax - xmin) / width
                box_height = (ymax - ymin) / height

                f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")


# Usage example
input_dir = 'Annotations'
output_dir = 'labels'

# Automatically generate the class list
class_list = get_class_list(input_dir)
print("Class List:", class_list)

voc_to_yolo(input_dir, output_dir, class_list)

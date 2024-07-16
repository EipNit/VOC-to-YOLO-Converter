VOC to YOLO Converter

This script converts PASCAL VOC format annotations to YOLO format. It reads the XML files of annotations from a specified directory, extracts the class names, and converts the bounding box coordinates to the YOLO format.
Features

    Extracts unique class names from VOC XML files.
    Converts VOC format annotations to YOLO format.
    Skips difficult objects (as specified in the VOC annotations).

Requirements

    Python 3.x
    Libraries: os, xml.etree.ElementTree

Usage

    Place your VOC XML annotation files in a directory (e.g., Annotations/).

    Run the script:

    python

    python voc2yolo.py

    By default, the script will:
        Read the XML files from the Annotations directory.
        Save the converted YOLO TXT files in the labels directory.

Script Details
get_class_list(input_dir)

Extracts a list of unique class names from VOC XML files.

    Parameters:
        input_dir: Directory containing VOC XML files.
    Returns:
        class_list: List of unique class names.

voc_to_yolo(input_dir, output_dir, class_list)

Converts VOC format annotations to YOLO format.

    Parameters:
        input_dir: Directory containing VOC XML files.
        output_dir: Directory to save YOLO TXT files.
        class_list: List of class names in the order they appear in the YOLO model.

Example Usage in Script

The script includes an example usage:

python

input_dir = 'Annotations'
output_dir = 'labels'

# Automatically generate the class list
class_list = get_class_list(input_dir)
print("Class List:", class_list)

voc_to_yolo(input_dir, output_dir, class_list)

License

This project is licensed under the MIT License.

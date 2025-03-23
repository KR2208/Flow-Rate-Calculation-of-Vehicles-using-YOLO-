import os
from bs4 import BeautifulSoup
# set width, height and names
width = 1280
height = 964
names = ['bicycle', 'bus', 'traffic sign' , 'train' , 'motorcycle' , 'car' , 'traffic light' , 'person' , 'vehicle fallback' , 'truck' , 'autorickshaw' , 'animal' , 'caravan' , 'rider' , 'trailer']


def copy_and_rename_files(base_dir, new_dir):
    # Walk through the base directory
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            # Construct the full file path
            full_file_path = os.path.join(root, file)
            
            # Get the relative path from the base directory and replace os separator with "-"
            file = os.path.relpath(full_file_path, base_dir)
            if "xml" not in file:
                print("Shit ",file)
                continue
            with open(full_file_path, 'r') as f:
                data = f.read()

            # parse file
            Bs_data = BeautifulSoup(data, "xml")

            # get annotations
            annotations = Bs_data.find('annotation')

            # get objects
            objects = annotations.find_all('object')

            converted = ''

            # iterate objects
            for object in objects:
                #get current items
                name = object.find('name').contents[0]
                bndbox = object.find('bndbox')
                xmin = int(bndbox.find('xmin').contents[0])
                ymin = int(bndbox.find('ymin').contents[0])
                xmax = int(bndbox.find('xmax').contents[0])
                ymax = int(bndbox.find('ymax').contents[0])
                
                #convert them accordingly
                w = (xmax-xmin) / width
                h = (ymax-ymin) / height
                x = ((xmin + xmax)/2) / width
                y = ((ymin + ymax)/2) / height
                i = names.index(name)
                converted = converted + "{} {:.6f} {:.6f} {:.6f} {:.6f}\n".format(i, x, y, w, h)
            
            new = os.path.join(new_dir, file.replace(".xml",".txt"))

            # write the new file with a replacement to txt
            with open(new, "w") as f:
                f.write(converted[:-1])

            print(new," Done")

# Example usage
base_dir = 'IDD_Detection_post/annotation'
new_dir = 'IDD_Detection_post/yolo-annotation'
copy_and_rename_files(base_dir, new_dir)

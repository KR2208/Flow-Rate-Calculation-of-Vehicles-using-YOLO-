import os

images = 'IDD_Detection_post/images'
annotations = 'IDD_Detection_post/yolo-annotation'

img_list = os.listdir(images)
ann_list = os.listdir(annotations)

ann_full = ""
img_full = ""

for ann in ann_list:
    img = ann.replace("txt","jpg")
    if img in img_list:
        ann_full = ann_full + os.path.join(annotations,ann) + "\n"
        img_full = img_full + os.path.join(images,img) + "\n"
        print(img)
    
with open("images.txt", 'w') as f:
    f.write(img_full) 

with open("annotation.txt", 'w') as f:
    f.write(ann_full)
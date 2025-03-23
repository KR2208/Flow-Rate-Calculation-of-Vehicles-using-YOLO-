from bs4 import BeautifulSoup

# set width, height and names
width = 1280
height = 964
names = ['bicycle', 'bus', 'traffic sign' , 'train' , 'motorcycle' , 'car' , 'traffic light' , 'person' , 'vehicle fallback' , 'truck' , 'autorickshaw' , 'animal' , 'caravan' , 'rider' , 'trailer']

# file name here
file = '000060_r.xml'

# read file
with open(file, 'r') as f:
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
	print("{}, {}, {}, {}, {}".format(name, xmin, ymin, xmax, ymax))
	
    #convert them accordingly
	w = (xmax-xmin) / width
	h = (ymax-ymin) / height
	x = ((xmin + xmax)/2) / width
	y = ((ymin + ymax)/2) / height
	i = names.index(name)
	print("{} {:.6f} {:.6f} {:.6f} {:.6f}".format(i, x, y, w, h))
	converted = converted + "{} {:.6f} {:.6f} {:.6f} {:.6f}\n".format(i, x, y, w, h)

# write the new file with a replacement to txt
with open(file.replace(".xml",".txt"), "w") as f:
	f.write(converted[:-1])
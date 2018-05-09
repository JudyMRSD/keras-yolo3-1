import xml.etree.ElementTree as ET
import glob
import os

classes = ["car"]
Train_One_Class = True

def convert_annotation(in_file, out_file):
    tree=ET.parse(in_file)
    root = tree.getroot()
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        if Train_One_Class == True:
            cls_id = 0
        else:
            cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        #print("b", b)
        #print("box data: ", " " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
        out_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

def sortKeyFunc(s):
    return(int(os.path.basename(s)[:-4]))

wd = os.getcwd()
print("wd", wd)
img_dir = wd+"/train_data/fifth_dataset/images_may4/"
ann_dir = wd+"/train_data/fifth_dataset/annotations_may4/"
out_file = open(wd+"/train_data/train.txt", 'w')

print("img_dir", img_dir)
print("ann_dir", ann_dir)
print("out_file", out_file)
image_names = sorted(glob.glob(img_dir + "*.jpg"), key = sortKeyFunc)
print("image_names",image_names)



for img_path in image_names:
    print("img_path", img_path)
    out_file.write(img_path)

    base = os.path.basename(img_path)
    print("base", base)
    voc_anno_path = ann_dir+ os.path.splitext(base)[0] + '.xml'

    print("voc_anno_path", voc_anno_path)

    convert_annotation(voc_anno_path, out_file)
    out_file.write('\n')
out_file.close()
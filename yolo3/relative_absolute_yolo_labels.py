import glob

# relative_to_absolute:
# input :
# standard yolo3 format:  https://pjreddie.com/darknet/yolo/
# x, y, width, and height are relative to the image's width and height
# one label(.txt) per image(.jpg)
# input file format: <object-class> <x> <y> <width> <height>
# remove 0.txt if label is from the labeling GUI (first file is static cars' labels)
# output:
# One row for one image;
# Row format: image_file_path box1 box2 ... boxN;
# Box format: x_min,y_min,x_max,y_max,class_id (no space).
class LabelConverter():
    def __init__(self):
        self.a = 0
    def relative_to_absolute(self, input_dir, output_dir):
        label_files = sorted(glob.glob(input_dir + '*.txt'))
        for f in label_files:
            print("filename", f)

def main():
    converter= LabelConverter()
    input_label_dir = "./train_data/bbox_relative/"
    img_dir = "./train_data/images"
    converter.relative_to_absolute(input_label_dir, img_dir, output_dir)

if __name__ == '__main__':
    main()
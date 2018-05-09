import cv2
import os

class Plot_Train_Bbox:
    def __init__(self):
        self.a = 0

    def plot_training_instances(self, train_ints, train_labels ):
        print("train_ints[0]['object'] ", train_ints[0]['object']) # train_ints[0]['object']  [{'name': 'car', 'xmin': 3183, 'ymin': 1337, 'xmax': 3292, 'ymax': 1408}, {'name': 'car', 'xmin': 2487, 'ymin': 2079, 'xmax': 2536, 'ymax': 2183}, {'name': 'car', 'xmin': 2394, 'ymin': 2103, 'xmax': 2451, 'ymax': 2244}, {'name': 'car', 'xmin': 2477, 'ymin': 1919, 'xmax': 2534, 'ymax': 2040}, {'name': 'car', 'xmin': 2400, 'ymin': 1929, 'xmax': 2450, 'ymax': 2044}, {'name': 'car', 'xmin': 2161, 'ymin': 1482, 'xmax': 2272, 'ymax': 1531}, {'name': 'car', 'xmin': 2745, 'ymin': 1286, 'xmax': 2869, 'ymax': 1352}, {'name': 'car', 'xmin': 2543, 'ymin': 1158, 'xmax': 2642, 'ymax': 1245}, {'name': 'car', 'xmin': 2447, 'ymin': 836, 'xmax': 2499, 'ymax': 937}, {'name': 'car', 'xmin': 2278, 'ymin': 893, 'xmax': 2331, 'ymax': 1008}, {'name': 'car', 'xmin': 2216, 'ymin': 749, 'xmax': 2263, 'ymax': 865}, {'name': 'car', 'xmin': 2281, 'ymin': 552, 'xmax': 2325, 'ymax': 658}]
        print("train_ints[0]['filename'] ", train_ints[0]['filename']) # train_ints[0]['filename']  ./training_data/aerial/images_may4/2300.jpg
        print("train_labels", train_labels) # {'car': 159, 'bus': 3}

        num_imgs = len(train_ints)
        for i in range(0, num_imgs):
            image_path = train_ints[i]['filename']
            print("img_path", image_path)
            image = cv2.imread(image_path)
            for box in train_ints[i]['object']:
                name = box['name']
                xmin = box['xmin']
                ymin = box['ymin']
                xmax = box['xmax']
                ymax = box['ymax']
                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)
                cv2.putText(image,
                            name,
                            (xmin, ymin - 13),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1e-3 * image.shape[0],
                            (0, 255, 0), 2)
            base = os.path.basename(image_path)
            out_path = './plot_training/'+base[:-4] + '_detected' + base[-4:]
            cv2.imwrite(out_path, (image).astype('uint8'))

    def plot_training_resized(self, base_image_path, image, boxes):

        for box in boxes:
            name = box[4]
            xmin = box[0]
            ymin = box[1]
            xmax = box[2]
            ymax = box[3]
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)
            # cv2.putText(image,
            #             name,
            #             (xmin, ymin - 13),
            #             cv2.FONT_HERSHEY_SIMPLEX,
            #             1e-3 * image.shape[0],
            #             (0, 255, 0), 2)
        out_path = './train_log_dir/'+base_image_path + '_detected' + ".jpg"
        cv2.imwrite(out_path, (image).astype('uint8'))

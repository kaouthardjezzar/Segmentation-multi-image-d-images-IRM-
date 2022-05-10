import os 

TRAIN_IMAGE_PATH = "/home/kawther/Segmentation-multi-image-d-images-IRM-/Br35H-Mask-RCNN/TRAIN"
VAL_IMAGE_PATH = "/home/kawther/Segmentation-multi-image-d-images-IRM-/Br35H-Mask-RCNN/VAL"
TEST_IMAGE_PATH = "/home/kawther/Segmentation-multi-image-d-images-IRM-/Br35H-Mask-RCNN/TEST"

TRAIN_ANNOT_FILE = os.path.join(TRAIN_IMAGE_PATH,"annotations_train.json")
VAL_ANNOT_FILE = os.path.join(VAL_IMAGE_PATH,"annotations_val.json")
TEST_ANNOT_FILE = os.path.join(TEST_IMAGE_PATH,"annotations_test.json")

TRAIN_ANNOT_DIR = "/home/kawther/Segmentation-multi-image-d-images-IRM-/Br35H-Mask-RCNN/TRAIN_ANNOT"
VAL_ANNOT_DIR = "/home/kawther/Segmentation-multi-image-d-images-IRM-/Br35H-Mask-RCNN/VAL_ANNOT"
TEST_ANNOT_DIR = "/home/kawther/Segmentation-multi-image-d-images-IRM-/Br35H-Mask-RCNN/TEST_ANNOT"
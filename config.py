import os 


# Put your path to the Br35H-MASK-RCNN folder
BASE_PATH = "/home/kawther/Segmentation-multi-image-d-images-IRM-/Br35H-Mask-RCNN"

TRAIN_IMAGE_PATH = os.path.join(BASE_PATH, "TRAIN")
VAL_IMAGE_PATH = os.path.join(BASE_PATH, "VAL")
TEST_IMAGE_PATH = os.path.join(BASE_PATH, "TEST")

TRAIN_ANNOT_FILE = os.path.join(TRAIN_IMAGE_PATH,"annotations_train.json")
VAL_ANNOT_FILE = os.path.join(VAL_IMAGE_PATH,"annotations_val.json")
TEST_ANNOT_FILE = os.path.join(TEST_IMAGE_PATH,"annotations_test.json")

TRAIN_ANNOT_DIR = os.path.join(BASE_PATH, "TRAIN_ANNOT")
VAL_ANNOT_DIR = os.path.join(BASE_PATH, "VAL_ANNOT")
TEST_ANNOT_DIR = os.path.join(BASE_PATH, "TEST_ANNOT")
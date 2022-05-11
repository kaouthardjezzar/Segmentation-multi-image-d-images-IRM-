# json annotation file to img annotation
import json
import cv2
import glob
import numpy as np
import os

def json_annot_to_png_annot (annotation_directory, images_path, annotaion_file):
    if not os.path.exists(annotation_directory):
        os.makedirs(annotation_directory)
    # read json annotation file
    with open(annotaion_file) as json_file:
        data = json.load(json_file)
    # loading images
    train_images = [f for f in os.listdir(images_path) if f.endswith('.jpg')]
    for img in train_images:
        image = cv2.imread(os.path.join(images_path,img))
        try:
            dimensions= image.shape
            print("checked for shape".format(image.shape))
        except AttributeError:
            print("shape not found")
        file_name = str(img).replace(".jpg", "")
        os.chdir(annotation_directory)
        tmp = np.zeros(dimensions).astype('uint8')
        for d in data:
            if file_name == data[d]['filename'].replace(".jpg",""):
                if len(data[d]['regions'][0]['shape_attributes']) == 3:
                    x_pixels = data[d]['regions'][0]['shape_attributes']['all_points_x']
                    y_pixels = data[d]['regions'][0]['shape_attributes']['all_points_y']
                    pts = []
                    for i in range(len(x_pixels)):
                        pts.append([x_pixels[i], y_pixels[i]])
                    ptss = np.array(pts)
                    ptss = ptss.reshape((-1, 1, 2))
                    isClosed = True
                    tmp = cv2.fillPoly(tmp, [ptss], (255,255,255))
                elif len(data[d]['regions'][0]['shape_attributes']) == 6:
                    center_coordinates = (data[d]['regions'][0]['shape_attributes']['cx'],
                                            data[d]['regions'][0]['shape_attributes']['cy'])
                    axesLength = (int(data[d]['regions'][0]['shape_attributes']['rx']),
                                    int(data[d]['regions'][0]['shape_attributes']['ry']))
                    angle = data[d]['regions'][0]['shape_attributes']['theta']
                    startAngle = 0
                    endAngle = 360
                    tmp = cv2.ellipse(tmp,
                                        center_coordinates,
                                        axesLength,
                                        angle,
                                        startAngle,
                                        endAngle,
                                        (255,255,255),
                                        thickness=-1)

        cv2.imwrite("{}.png".format(file_name), tmp.astype('uint8'))
        

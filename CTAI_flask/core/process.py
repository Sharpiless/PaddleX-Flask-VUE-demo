import os

import cv2


def data_in_one(inputdata):
    if not inputdata.any():
        return inputdata
    inputdata = (inputdata - inputdata.min()) / (inputdata.max() - inputdata.min())
    return inputdata


def pre_process(data_path):
    file_name = os.path.split(data_path)[1].split('.')[0]
    return data_path, file_name


def last_process(file_name):
    image = cv2.imread(f'./tmp/ct/{file_name}.png')
    mask = cv2.imread(f'./tmp/mask/{file_name}_mask.png', 0)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imwrite('./tmp/draw/{}.png'.format(file_name), image)

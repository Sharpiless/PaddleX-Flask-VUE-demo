import numpy as np
import cv2

rate = 0.5

def predict(dataset, model):
    global img_y
    x = dataset[0].replace('\\', '/')
    file_name = dataset[1]
    print(x)
    print(file_name)
    img_y = model.predict(x)['label_map']
    img_y = img_y * 255
    img_y = img_y.astype(np.int)
    cv2.imwrite(f'./tmp/mask/{file_name}_mask.png', img_y,
                (cv2.IMWRITE_PNG_COMPRESSION, 0))


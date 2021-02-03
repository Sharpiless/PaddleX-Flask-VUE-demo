# 基于Paddle+Flask的眼部医疗辅助系统（前后端分离）

视频链接：https://www.bilibili.com/video/BV1k54y1s7j9

# 1. 项目简介：

本项目基于PaddleX提供的FastSCNN语义分割模型，在眼部图像视盘分割数据集上进行训练，并开发了前后端分离项目。

后端代码基于Flask开发，前端WEB界面基于VUE开发。

![](https://ai-studio-static-online.cdn.bcebos.com/936a7f88ceac4085924961e023e0b974e38138def41444dfaf6a58cec091ec4d)

# 2. 训练语义分割模型：



```python
! pip install paddlex -i https://mirror.baidu.com/pypi/simple
```

    done
    [?25h  Created wheel for pycocotools: filename=pycocotools-2.0.2-cp37-cp37m-linux_x86_64.whl size=278368 sha256=69425bf5985e5aa2c1a6c475a0d5e5975b3e5e5a024bda6e4573d07ccae57a21
      Stored in directory: /home/aistudio/.cache/pip/wheels/fb/44/67/8baa69040569b1edbd7776ec6f82c387663e724908aaa60963
    Successfully built pycocotools
    Installing collected packages: paddleslim, xlwt, colorama, shapely, paddlehub, pycocotools, paddlex
      Found existing installation: paddlehub 1.6.0
        Uninstalling paddlehub-1.6.0:
          Successfully uninstalled paddlehub-1.6.0
    Successfully installed colorama-0.4.4 paddlehub-1.8.3 paddleslim-1.1.1 paddlex-1.3.4 pycocotools-2.0.2 shapely-1.7.1 xlwt-1.3.0



```python
! wget https://bj.bcebos.com/paddlex/datasets/optic_disc_seg.tar.gz
! tar xzf optic_disc_seg.tar.gz
```

    --2021-01-23 08:11:17--  https://bj.bcebos.com/paddlex/datasets/optic_disc_seg.tar.gz
    Resolving bj.bcebos.com (bj.bcebos.com)... 182.61.200.229, 182.61.200.195, 2409:8c00:6c21:10ad:0:ff:b00e:67d
    Connecting to bj.bcebos.com (bj.bcebos.com)|182.61.200.229|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 19077558 (18M) [application/octet-stream]
    Saving to: ‘optic_disc_seg.tar.gz’
    
    optic_disc_seg.tar. 100%[===================>]  18.19M  29.0MB/s    in 0.6s    
    
    2021-01-23 08:11:18 (29.0 MB/s) - ‘optic_disc_seg.tar.gz’ saved [19077558/19077558]
    



```python
# 设置使用0号GPU卡（如无GPU，执行此代码后仍然会使用CPU训练模型）
import matplotlib
matplotlib.use('Agg') 
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import paddlex as pdx
```

    2021-01-23 08:11:24,888-INFO: font search path ['/opt/conda/envs/python35-paddle120-env/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf', '/opt/conda/envs/python35-paddle120-env/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/afm', '/opt/conda/envs/python35-paddle120-env/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/pdfcorefonts']
    2021-01-23 08:11:25,242-INFO: generated new fontManager



```python
from paddlex.seg import transforms
train_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.Resize(target_size=512),
    transforms.RandomPaddingCrop(crop_size=500),
    transforms.Normalize()
])
eval_transforms = transforms.Compose([
    transforms.Resize(512),
    transforms.Normalize()
])
```


```python
train_dataset = pdx.datasets.SegDataset(
    data_dir='optic_disc_seg',
    file_list='optic_disc_seg/train_list.txt',
    label_list='optic_disc_seg/labels.txt',
    transforms=train_transforms,
    shuffle=True)
eval_dataset = pdx.datasets.SegDataset(
    data_dir='optic_disc_seg',
    file_list='optic_disc_seg/val_list.txt',
    label_list='optic_disc_seg/labels.txt',
    transforms=eval_transforms)
```

    2021-01-23 08:11:39 [INFO]	267 samples in file optic_disc_seg/train_list.txt
    2021-01-23 08:11:39 [INFO]	76 samples in file optic_disc_seg/val_list.txt



```python
num_classes = len(train_dataset.labels)
num_classes
```




    2




```python
num_classes = len(train_dataset.labels)
model = pdx.seg.FastSCNN(num_classes=num_classes)
model.train(
    num_epochs=40,
    train_dataset=train_dataset,
    train_batch_size=4,
    eval_dataset=eval_dataset,
    learning_rate=0.01,
    save_interval_epochs=1,
    save_dir='output/',
    use_vdl=True)
```


```python
!paddlex --export_inference --model_dir=./output/best_model --save_dir=./inference_model --fixed_input_shape=[512,512]
```

    W0123 08:16:03.194139  1332 device_context.cc:252] Please NOTE: device: 0, CUDA Capability: 70, Driver API Version: 10.1, Runtime API Version: 9.0
    W0123 08:16:03.199599  1332 device_context.cc:260] device: 0, cuDNN Version: 7.6.
    2021-01-23 08:16:06 [INFO]	Model[FastSCNN] loaded.
    2021-01-23 08:16:06 [INFO]	Model for inference deploy saved in ./inference_model.


# 3. 模型预测

使用模型进行预测，同时使用`pdx.seg.visualize`将结果可视化，可视化结果将保存到`./output/deeplab`下，其中`weight`代表原图的权重，即mask可视化结果与原图权重因子。


```python
import paddlex as pdx
model = pdx.deploy.Predictor('inference_model')
image_name = 'optic_disc_seg/JPEGImages/H0005.jpg'
result = model.predict(image_name)
pdx.seg.visualize(image_name, result, weight=0.4, save_dir='./output/deeplab')
```

    2021-01-23 08:16:45 [INFO]	The visualized result is saved as ./output/deeplab/visualize_H0005.jpg



```python
!zip -r inference_model/ weights.zip
```

    	zip warning: name not matched: weights.zip
    
    zip error: Nothing to do! (try: zip -r inference_model/ . -i weights.zip)


# 4. 启动WEB应用：

在 Flask 项目下运行以下代码启动后端：
```
python app.py
```

在 VUE 项目下运行以下代码安装依赖：
```
npm run serve
```
运行以下代码启动前端：
```
npm run serve
```

然后在浏览器打开Localhost即可：

![](https://ai-studio-static-online.cdn.bcebos.com/fbd0e4b62a3a435a9afa683456bfebb3ef173c5794854576ad0279aefa2e5bdb)

# 我的公众号：

感兴趣的同学关注我的公众号——可达鸭的深度学习教程：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127153004430.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)

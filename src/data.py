import random

import torch
import torchvision.transforms.functional as tf


def transforms(x, y):
    x = list(tf.five_crop(x, 512))
    y = list(tf.five_crop(y, 512))

    for i in range(len(x)):
        if random.random() > 0.5:
            x[i] = tf.hflip(x[i])
            y[i] = tf.hflip(y[i])

        if random.random() > 0.5:
            x[i] = tf.vflip(x[i])
            y[i] = tf.vflip(y[i])

        if random.random() > 0.5:
            angle = random.randint(-30, 30)
            x[i] = tf.rotate(x[i], angle)
            y[i] = tf.rotate(y[i], angle)

    x = torch.stack([tf.to_tensor(crop) for crop in x])
    y = torch.stack([tf.to_tensor(crop) for crop in y])
    
    # Replace all nonzero values with 1
    y[y!=0] = 1

    return x, y


def collate(batch):
    data = torch.cat([item[0] for item in batch])
    target = torch.cat([item[1] for item in batch])
    return data, target

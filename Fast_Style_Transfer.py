import argparse

def stylize(content_image_path,style_image_path,output_dir):
    import tensorflow_hub as hub
    import tensorflow as tf
    from matplotlib import pyplot as plt
    import numpy as np
    import cv2

    model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)

    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
    output_image_path = output_dir + 'generated_img.jpg'
    cv2.imwrite(output_image_path, cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))

def load_image(img_path):
    import tensorflow as tf
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img


if __name__== "__main__":
    parser = argparse.ArgumentParser()
    # content_image=""
    # style_image=""
    # output_dir=""
    parser.add_argument('--ci', required=True,help='Path for Content images')
    parser.add_argument('--si', required=True,help='Path for Style images')
    parser.add_argument('--o',required=True,help='Path for Output/Stylized images')

    values = parser.parse_args()

    stylize(values.ci,values.si,values.o)
# Creating Art through Neural Style Transfer

link to medium article : https://ashutosh-saxena.medium.com/creating-art-through-neural-style-transfer-5e51e559fef9

Ever wish you could paint like Picasso or Van Gogh!?.

This is known as neural style transfer! This is a technique outlined in Leon A. Gatys’ paper, A Neural Algorithm of Artistic Style, which is a great read, and you should definitely check it out.

Neural style transfer is an optimization technique used to take three images, a content image, a style reference image (such as an artwork by a famous painter), and the input image you want to style — and blend them together such that the input image is transformed to look like the content image, but “painted” in the style of the style image.

For example, let’s take an image of this turtle and Katsushika Hokusai’s The Great Wave off Kanagawa:
![image](https://user-images.githubusercontent.com/58273769/115754767-2e3e2000-a3ba-11eb-891a-34d3b5777a32.png)

What will happen if Hokusai decided to add the texture or style of his waves to the image of the turtle? Something like this?

![image](https://user-images.githubusercontent.com/58273769/115754839-4150f000-a3ba-11eb-9210-a2ba9ae0c901.png)

Style transfer is a fun and interesting technique that showcases the capabilities and internal representations of neural networks.

The principle of neural style transfer is to define two distance functions, one that describes how different the content of two images are, Lcontent, and one that describes the difference between the two images in terms of their style, Lstyle.

Then, given three images, the desired style image, the desired content image, and the input image (initialized with the content image), we try to transform the input image to minimize the content distance with the content image and its style distance with the style image.

### Model

In this case, we load VGG16 and feed in our input tensor to the model. This will allow us to extract the feature maps (and subsequently the content and style representations) of the content, style, and generated images.

We use VGG19, as suggested in the paper. In addition, since VGG16 is a relatively simple model (compared with ResNet, Inception, etc) the feature maps actually work better for style transfer.

### Trying it Yourself ?

The Normal version takes quite a lot of time to do a single iteration (30-40 sec on GTX 1050)

To run the "Fast-Style-Transfer" :

```python Fast_Style_Transfer.py --ci = '<path of content image>' --si = '<path of style image>' --o = '<output directory>```

Citation :
- Leon A. Gatys’ paper : https://arxiv.org/abs/1508.06576

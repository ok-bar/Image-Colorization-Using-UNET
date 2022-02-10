# Image-Colorization-Using-UNET

The goal of this project is to colorize black-and-white images, which was a difficult task a few years ago but has recently become easier with the rise of deep learning. Colorization can be done quite well using Photoshop, but it requires little knowledge. 
Furthermore, depending on the number of images you have, it can take hours or even days. To achieve the desired look, a wide variety of color combinations are required. The first step in colorizing images is to convert them from RGB to grayscale, which will then be used as input(grayscale) and output(RGB). 
Using Unet architecture , the model learns how to colorize images.

The first task is taking a dataset of RGB images which will be used as the output and change it to GRAY scale images which will be act as the input. Then the model can learn to transform a gray scale image to rgb image.
![F7438F83-05B3-452F-9BAE-68F9BDBFF83D_1_105_c](https://user-images.githubusercontent.com/51881832/153343096-9a7a5005-1dd5-4117-9c0b-e97ec62f3a1f.jpeg)

After the transform:

![C38297EF-3A2E-4CA6-86E8-0480FE93522C_1_105_c](https://user-images.githubusercontent.com/51881832/153343407-9c1cf259-845b-4dc4-ab1f-c9bc7509170a.jpeg)

To train the model i used Unet with VGG16 backbone, but unfreezed all layers since the task is different:
![image](https://user-images.githubusercontent.com/51881832/153343932-57d64de8-d9e1-4b49-a2fa-c314320ab4ef.png)


After 9 epochs the model stop learning:


![08572149-9449-43C1-9FC8-091008D18F52_1_105_c](https://user-images.githubusercontent.com/51881832/153344928-7f259815-6e9d-4ccd-b321-d8d05461e9f3.jpeg)

![5A8E3F72-58CD-4ADC-800C-460AE372E0D0_1_105_c](https://user-images.githubusercontent.com/51881832/153345606-cf90ced6-6ea3-4c79-8aec-dac79278a889.jpeg)

Then I compared between the true image, the gray scale image and the predictions:
![955B942C-7763-498D-B7F0-7FDC5D8BA6F3_1_105_c](https://user-images.githubusercontent.com/51881832/153345916-8f8f01e7-7a43-467c-89f1-55c3273ef2ca.jpeg)

To conclude,the model performed poorly when asked to colorize a grayscale image. Many papers use a LAB image instead of an RGB image because two numbers (a,b) are easier to predict than three. I tried it as well, but the results are nearly identical. Even if more images are used, it will be extremely difficult for any model to predict the color of the eyes, hair, and skin tone. Using GAN as a solution to this problem is an ideal option. With GAN, the model can predict whether an image is "real" in terms of colorization.

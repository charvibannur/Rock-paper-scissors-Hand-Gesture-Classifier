from collections import Counter
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def load_image(img_path, show=False):
    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor


if __name__ == "__main__":

    # load model
    model = load_model(r"model_trained.h5")

    # image path
    img_path = r'image.jpg'

    # load a single image
    new_image = load_image(img_path)

    # plot image
    image = Image.open(img_path)
    image.show()

    # check prediction
    pred = model.predict(new_image)
    percentage = (pred * 100).astype('int64')
    for i in percentage:
        per={}
        per.update({'Rock':i[1]})
        per.update({'Paper': i[0]})
        per.update({'Scissors':i[2]})

    # To display the three most probable classes

    k= Counter(per)
    high = k.most_common(3)
    for i in high:
        print(i[0]," :",i[1],"%")

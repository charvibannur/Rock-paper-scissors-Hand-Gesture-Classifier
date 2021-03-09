Image Classifier using CNN
what is a CNN?
what is CNN – as we know its a machine learning algorithm for machines to understand the features of the image with foresight and remember the features to guess whether the name of the new image fed to the machine.

This model is used to classify basic hand gestures used in the game-rock paper scissors.

About the dataset

Rock Paper Scissors is a dataset containing 2,892 images of diverse hands in Rock/Paper/Scissors poses. It contains images from a variety of different hands, from different races, ages and genders, posed into Rock / Paper or Scissors and labelled as such. These images have all been generated using CGI techniques as an experiment in determining if a CGI-based dataset can be used for classification against real images.

Note that all of this data is posed against a white background.

Each image is 300×300 pixels in 24-bit color.

About the model

The model is a vanilla CNN model. The feature extraction part of the model contains 5 layers with 3 convolutional 2D layers and 2 maxpooling layers. Then comes the neural network which, firstly flattens the images. The neural network consists of 3 layers with the output layer being a soft max layer with 3 neurons.
The optimiser we use is adam, as it offers more accuracy and is best suited for classification models.

Another technique used was Data augmentation.Data augmentation in data analysis are techniques used to increase the amount of data by adding slightly modified copies of already existing data or newly created synthetic data from existing data.

Members:
Charvi Bannur:https://github.com/charvibannur
Gagan Goutham:https://discord.com/channels/818498368502235177/818498368502235180/818890091438931998
Amitram Achunala:




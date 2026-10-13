# Fashion MNIST dataset with PCA

In this project I have applied PCA(Principal Component Anylasis) in [Fashion MNIST dataset](https://www.kaggle.com/datasets/zalando-research/fashionmnist) in Kaggle. This markdown is just the overview of the project I have given more detail about PCA in my [notes](https://github.com/gitbhusalhubpramish/ml-notes/tree/main/0.009%20PCA). 

<img src="visual.jpg"/>

This image is just the final visulization of the PCA model.

## Small intro to PCA

Sooo..., PCA is a unsupervised meachine learning algorithm which helps us to reduce diamentions of our data. It finds the corelation or covariance of data then makes a vector which transfer the data where it include the info of most of the feature. There are $n$ number of Principal component in a PCA where $n$ is the number of feature but we can visulize the data or get  around 80% of the data after applying this.

## Feature

This project was made by me to understand PCA from scratch so it's main feature is it has PCA applied from scratch but also:

- PCA from scratch
- Numpy for maths and matrix calculation
- Data visulization
- Reduces or transforms 785 feature so we can visulize it from **2 features**.

## Tech-Stack

This project mostly(almost all) uses python liberies or technology related to math and datascience. I've used:

- Numpy for calculation
- matplotlib for datavisulization
- streamlit for hosting and building app
- Pandas for csv and data manipulation

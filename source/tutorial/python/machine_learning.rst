Machine Learning
================
This page is supposed to gather all the "wisdom" I have so far in Machine Learning.

What do I need to start?
------------------------
Data
````
* A representative set of data (the more complex the problem, the more data)
* A label for each dataset, that describes the data

#. Data & labels must be divided into

    * training data
    * training labels
    * validation data
    * validation labels

    where the training data is usually about 75% of the data, 25 % for validation

    Additionally you might reserve some for testing (60 % training, 20 % validation,
    20 % testing)

        * test data
        * test labels

#. Transform data into tensors (1D, 2D, 3D, or more):

    * 2D: Vector data (samples, data_values)
    * 3D: Timeseries data or sequence data (samples, time_or_sequence, data_values)
    * 4D: Image data (samples, height_index, width_index, color_channel_values)
    * 5D: Video data (samples, frame, height_index, width_index, color_channel_values)

#. One-Hot Encode the labels: 2D tensor (sample, label):

    * Label tensore shape must be (amount_of_data_samples, amount_of_classes)

#.




Amount and size of hidden layers
--------------------------------
Selecting the amount and the size of hidden layers within a model is crucial:

* too few layers or too few nodes -> information loss, resulting in bad accuracy (underfitting)
* too many layers or too many nodes -> slow training, overfitting

The goal is to create a model, which has a good accuracy on test data

If the model is too smart, in other words, is too much tailored onto the training data,
it will not perform well on test data, but perfect on the training data -> overfitting.

A model must be smart enough to deal with typical data, but not "too smart", consequently
performing bad on new data.

**Rule of thumb**

* As a starting point, the amount of nodes in a hidden layer should be the **average
between the nodes of the previous layer and the proceeding layer**.
* Start with two hidden layers, working your way up to see if it improves on accuracy

More information:
https://www.heatonresearch.com/2017/06/01/hidden-layers.html

Selection of the loss functions
-------------------------------
:categorical_crossentropy:

    Measures the distance between the classifier’s predictions and the labels.
    The lower the loss, the better the classifier. Also referred to as *Cross-Entropy*.

    **Suitable for**: Good choice for categorical data ("Does this dataset belong
    to a certain category?")
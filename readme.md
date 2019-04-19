#OCR with Tensorflow#
##dataGen.py##
This file is intended to creat a dataset that can be used to train the tensor model. That said
I ran into issues with formatting the image where it would cut of the first few letters of the
string, otherwise it works pretty well.
##main.py##
This is the main python file. It begins with putting all of the PNGs into an array, along with
an array of keys that correspond to the values in the training set. After creating the arrays
it puts them into the tensorflow model. Right now I am having trouble with the shape of the
model.
#Running the Code#
Right now all you should have to do is run main.py, but you also need to put an image in there.
You can run it on a file by calling model.predict(fileName.png) If you add this bit of code it
will predict the value of the number in the image. One important thing is that the image has
the dimensions(1200, 900).

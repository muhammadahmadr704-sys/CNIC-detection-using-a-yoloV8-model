# ID card detection using Yolov8 model
--------------------------------------
Yes obviously this a big project so this was divided into chunks and I was given the part where I had to correctly detect the pose of the card and then crop it out so that the information on that card is extracted and sent forward to verify through the servers.
Other parts of this project were best frame detection from a captured video and one was to read the signatures on the ID card.
One team member was assigned the part to clearly detect and separate fingers using correct pose detection and then the company's algorithm was used to extract fingerprint information and sent forward to cross check through the government. 
So far the whole scenario has been explained.
------------------------------------
My task included preparing pictures of random ID cards in random orientations and then clearly annotate and label them to prepare the dataset to be fed to the model we will be training.
Then the whole prepared dataset was used to train a Yolov8 model using 20-80 EPOCHS on different sizes of v8 mdoel to compare and check if the cost of increasing model size is any fruitful or not.
In my case, both increasing the model size and dataset size initially lead to significant improvement in results but later the model size did not show any further improvement for increase in size when the dataset was almost doubled. Then we cleaned ( filtered ) the dataset and then again increased it and that lead to very good results in finding the correct pose of a card being held in hands.
------------------------------------
Final code, model and supporting results are uploaded here
------------------------------------
If you have reached this far here, feel free to contact me and I'll be happy to collaborate whereever you need.

# SVM-handwriting-recognition
Project involving Support Vector Machine to classificate handwriting letters from NIST Special Database 19. <br>
<br>
## Steps todo: <br>
1. Download dataset from: https://s3.amazonaws.com/nist-srd/SD19/by_class.zip <br>
2. Unzip it <br>
3. Run resize_alphabet.py - it will centered photos at sign and change the resolution to 12x12 pixels and chose about 1500 of examples for each sign (randomly) <br>
4. Run train_model.py - it will show the accuracy of model, and save it with teh name 'finalized_model.sav' (at repozitory i uploaded mine model with accuracy eauals 70%) <br>
5. Use jupyter notebook to check online how it works - just load model <br>
6. Ich you want to check your own letters - look for svm.png and make file similar to this. Letter run cut.py and test the results with notebook

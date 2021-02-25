model = Sequential()   
model.add(Convolution1D(64, 5, activation='relu', padding='same'))    
model.add(Dropout(0.2))    
model.add(MaxPooling1D())    
model.add(Flatten())    
model.add(Dense(100, activation='relu'))    
model.add(Dropout(0.7))    
model.add(Dense(1, activation='sigmoid'))    
model.compile(loss="binary_crossentropy", optimizer='adam',  metrics=['accuracy'])    
model.fit(X, y, nb_epoch=20)
model.summary()
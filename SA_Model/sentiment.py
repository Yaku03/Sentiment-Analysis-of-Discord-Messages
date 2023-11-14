import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle5 as pickle

data = pd.read_csv('../Datasets/backup.csv') 
data['value'] = data['sentiment'].apply(lambda x: 'positive' if x > 0
                                        else 'negative' if x < 0
                                        else 'neutral')
data = data[['text', 'value']]
data = data.sample(frac=1).reset_index(drop=True)

t = tf.keras.preprocessing.text.Tokenizer(num_words=5000, oov_token='<OOV>')
t.fit_on_texts(data['text'])
word_index = t.word_index
seq = t.texts_to_sequences(data['text'])
pad = tf.keras.preprocessing.sequence.pad_sequences(seq, truncating='post')
labels = pd.get_dummies(data['value']).values

x_train, x_test, y_train, y_test = train_test_split(pad, labels, test_size=0.2)

callback = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=2)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Embedding(5000, 100, input_length=76))
model.add(tf.keras.layers.Conv1D(6, 5, activation='relu'))
model.add(tf.keras.layers.GlobalMaxPooling1D())
model.add(tf.keras.layers.Dense(6, activation='relu', input_shape=(1, )))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(3, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train, epochs=10, batch_size=16, validation_data=(x_test, y_test), callbacks=[callback])

y_pred = np.argmax(model.predict(x_test), axis=-1)
print("Accuracy: ", accuracy_score(np.argmax(y_test, axis=-1), y_pred))

model.save('missed_connections.h5')
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(t, handle, protocol=pickle.HIGHEST_PROTOCOL)
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split # membagi dataset menjadi set pelatihan dan pengujian
from sklearn.metrics import accuracy_score # menghitung akurasi prediksi model
import numpy as np # untuk memanipulasi data dalam bentuk array


data_dict = pickle.load(open('./data.pickle', 'rb')) # memuat dataset yang disimpan dalam file 'data.pickle'

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels) # membagi data train dan data test

model = RandomForestClassifier()

model.fit(x_train, y_train) # melatih model menggunakan data latih

y_predict = model.predict(x_test) # menggunakan model yang telah dilatih untuk memprediksi label gestur tangan dari data uji

score = accuracy_score(y_predict, y_test) # menghitung hasil prediksi dengan label asli dari data test

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('model.p', 'wb') 
pickle.dump({'model': model}, f)
f.close()

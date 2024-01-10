import numpy as np
import pickle

f = open('data.pickle', 'rb')
data = pickle.load(f)
f.close()

data = np.asarray(data['data'])
labels = np.asarray(data['labels'])

data_dict = {'data': data, 'labels': labels}
print(data_dict['data'])
print(data_dict['labels'])

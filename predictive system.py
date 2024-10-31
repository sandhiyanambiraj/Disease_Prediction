import numpy as np
import pickle 

loaded_model=pickle.load(open('C:/Users/Santhiya/OneDrive/diabetes prediction/trained_model.sav','rb'))

input_data=(5,166,72,19,175,25.8,0.587,51)

input_data_as_numpy_array=np.asarray(input_data)

input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)


prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print("the person is not diabetes")
else:
  print("the person is diabetes")

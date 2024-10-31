

import numpy as np 
import pickle 
import streamlit as st

loaded_model=pickle.load(open('C:/Users/Santhiya/OneDrive/diabetes prediction/trained_model.sav','rb'))



def diabetes_prediction(input_data):
    

    input_data_as_numpy_array=np.asarray(input_data)

    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)


    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
       return "the person is not diabetes"
    else:
      return  "the person is diabetes" 
  
    
  
def main():
    
    
    st.title("diabetes prediction web app")
    
    # gettting the input data from the user
    Pregnancies = st.text_input("number  of  Pregnancies")
    Glucose = st.text_input("Glucose level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("SkinThickness Value")
    Insulin = st.text_input("Insulin level")
    BMI = st.text_input("BMI Value")
    Diabetespedigreefunction = st.text_input("Diabetespedigreefunction Value")
    Age = st.text_input("Age of the person")
    
    
    
    # code for prediction
    
    diagonsis =''
    if st.button("Diabetes Test Result"):
        diagonsis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI, Diabetespedigreefunction, Age])
        
    st.success(diagonsis)
    
if __name__ == "__main__":
    main()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
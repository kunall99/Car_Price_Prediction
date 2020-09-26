
import pickle
import numpy as np
import streamlit as st

pickle_in = open("random_forest_regression_model.pkl", "rb")
classifier = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual):
    prediction = classifier.predict([[Present_Price, Kms_Driven, Owner, Year, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
    return prediction


def main():
    st.title("Car Price Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Car Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    #Year = st.text_input("Which year model", "Type Here")
    Year = st.number_input("Which year model",value=1)
    #st.write(type(Year))
    Year = 2020-Year
    Present_Price = st.number_input("Purchased Price(in lakhs)", value=1.0)
    Kms_Driven = st.number_input("kilometers already drive", value=1)
    Kms_Driven = np.log(Kms_Driven)
    #st.write(Kms_Driven)
    Owner = st.number_input("Past owner (0/1/2)", value=1)

    Fuel_Type = st.selectbox(
        'Select Fuel Type',
        ('Diesel', 'Petrol')
    )
    if (Fuel_Type == 'Diesel'):
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 1
    else:
        Fuel_Type_Petrol = 1
        Fuel_Type_Diesel = 0
    #st.write(type(Fuel_Type_Petrol))
    Seller_Type = st.selectbox(
        'Select seller type',
        ('Dealer', 'Individual')
    )
    if (Seller_Type == 'Individual'):
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0
    #st.write(Seller_Type_Individual)
    Transmission_Mannual = st.selectbox(
        'Select Transmission type',
        ('Automatic', 'Manual')
    )
    if (Transmission_Mannual == 'Mannual'):
        Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual)
    if result=='0':
        st.text("Sorry you cannot sell the car")
    else:
        st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()
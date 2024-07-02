import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import streamlit
streamlit.subheader("Know you service provider and which country")
a = streamlit.text_input("Enter your phone number: ", placeholder="Please Enter your input with countrycode eg+91-9087")
button = streamlit.button("Press it")


if button:
    phone = phonenumbers.parse(a)
    b = (carrier.name_for_number(phone, "en"))
    c = (geocoder.country_name_for_number(phone, "en"))
    streamlit.text(f"Service Provider - {b}")
    streamlit.text(f"Country-  {c}")


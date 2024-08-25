import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote
import json
st.title("                             Practo Data Scraping  🧑‍⚕️                          ")
city_name = st.text_input("Enter a city name:")
specialist=[' ',"Dentist",
    "General Physician",
    "Pediatrician",
    "Ayurveda",
    "Orthopedist",
    "Gynecologist/obstetrician",
    "Gynecologist",
    "Homeopath",
    "Cardiologist",
    "General Surgeon",
    "Ophthalmologist",
    "Ophthalmologist/ Eye Surgeon",
    "Dermatologist/cosmetologist",
    "Spa",
    "Dermatologist",
    "Oral Surgeon",
    "Physiotherapist",
    "Dental Surgeon",
    "Urologist",
    "Ear-nose-throat (ent) Specialist",
    "Orthodontist",
    "Diabetologist",
    "Psychiatrist",
    "Endodontist"
    ]

doctor_speciality = st.selectbox("Select a specialist:", specialist)
def scraping(city,speciality):
    params={
    "word":speciality,"autocompleted":True,"category":"subspeciality"
}
    json_str = json.dumps([params])

# URL encode the JSON string
    encoded_json_str = quote(json_str)

# Construct query string
    querystring =f'?results_type=doctor&q={encoded_json_str}&city={city}'
    
    base_url = f"https://www.practo.com/search/doctors"
    full_url=base_url+querystring
    page = 1
    doctors_list = {'name':[],
                     'profile':[],
                      'recommendations':[],
                      'consultation':[],
                      'experience':[],
                      'locality':[]                      
                    }  # Column headers

    while True:
        url = f"{full_url}&page={page}"
       
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all doctor name elements (update as needed)
        doctor_elements = soup.find_all('h2', class_='doctor-name') # Update class accordingly
        profile_sections = soup.find_all('div', class_='info-section')
        recommendation_section=soup.find_all('span',attrs={"data-qa-id":"doctor_recommendation"})
        consultation_fee=soup.find_all('span',attrs={"data-qa-id":"consultation_fee"})
        Experience=soup.find_all('div',attrs={"data-qa-id":"doctor_experience"})
        locality=soup.find_all('span',attrs={"data-qa-id":"practice_locality"})
        if not doctor_elements:
            break
       
        else:
           
           
           # Iterate through each doctor element
           for doctor, profile,rec,fee,exp,loc in zip(doctor_elements, profile_sections,recommendation_section,consultation_fee,Experience,locality):
                   
           # Extract name
                name = doctor.get_text(strip=True)
        
           # Extract profile link
                profile_link = profile.find('a', href=True)
                if profile_link:
                    href = profile_link['href']
                    href="https://www.practo.com/"+href
                else:
                    href = "No link found"
           # Extract doctor recommendation
                recommend=rec.get_text(strip=True)
            #Extract consultation fees
                consultation=fee.get_text(strip=True)
            #Extract doctor's experience
                exper=exp.get_text(strip=False)
            #Extract doctor's locality
                local=loc.get_text(strip=True)
                local=local+city
        # Append the name and href to the list
                doctors_list['name'].append(name)
                doctors_list['profile'].append(href)
                doctors_list['recommendations'].append(recommend)
                doctors_list['consultation'].append(consultation)
                doctors_list['experience'].append(exper)
                doctors_list['locality'].append(local)

        page += 1  # Go to the next page
    s=str(len(doctors_list['name']))
    st.header(s+" Doctors Available")
    return doctors_list,s
container_css="""
<style>
.container {
    height:180px;
    width:800px;
    background-color:white;
    margin-top: 20px;
    border:2px solid #7e888c;
    border-radius: 5px;
    box-sizing: border-box;
    padding:20px;
    
}

.my-button {
background-color: #000000; 
padding: 10px 20px;    
border: none;           
border-radius: 5px;     
cursor: pointer;        
text-decoration: none;  
font-size: 16px;
margin-left:700px;

}

.my-button:hover {
text-decoration:none;
}
</style>
"""
st.markdown(container_css, unsafe_allow_html=True)    
if st.button("scrape_data"):
    doctors,s=scraping(city_name,doctor_speciality)
    for i,(name,rec,link,exp,loc) in enumerate(zip(doctors['name'],doctors['recommendations'],doctors['profile'],doctors['experience'],doctors['locality'])):
        with st.container(): 
            st.markdown(f'''<div class="container">
                        <h3>{name}</h3>
                        <span>Speciality:{doctor_speciality}</span>
                        <span style="margin-left:40px">Experience:{exp}</span>
                        <span style="margin-left:40px">Locality:{loc}</span>
                        <div style="display:inline-block">Average Ratings:{rec}
                        <a href="{link}" target="_blank" class="my-button" style="color:white">Visit</a></div>
                        </div>''',unsafe_allow_html=True)
       

   



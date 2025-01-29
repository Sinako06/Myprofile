# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:22:03 2025

@author: Masthe
"""
#Import the library
import streamlit as st
import pandas as pd
#Title of the app
st.title("Researcher Profile Page")

#Collect the basic info
name= "Sinako Ngcwangu"
field= "Metallurgy"
institute= "Tshwane University of Technology"

#Display Basic Profile Info
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institute}")

#Add a section for publication
st.header("Publications")
upload_file= st.file_uploader("Upload a CSV of Publications", type= "csv")

if upload_file:
    publications= pd.read_csv(upload_file)
    st.dataframe(publications)
    
    #Add filtering for your keyword
    keyword= st.text_input("filter by word"," ")
    if keyword:
        filtered= publications[publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")
        
#Add a section for visualizing publication trends
st.header("Publication Trends")
if upload_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "sinakosomeleze@gmail.com"
st.write(f"You can reach {name} at {email}.") 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

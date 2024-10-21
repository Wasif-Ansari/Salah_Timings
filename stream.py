import streamlit as st
import pandas as pd
import openpyxl

# Load the Excel file
file_path = 'NAMAZ TIMINGS.xlsx'
# excel_data = pd.read_excel(file_path)

# st.table(pd.DataFrame({'Prayer': [ansar_prayer_name], 'Time': [ansar_time]}))


st.title("Namaz Timings")

st.subheader("NOORANI Timings")

noorani_prayer_names = ['FAJAR', 'ZOHAR', 'ASAR', 'MAGHRIB', 'ISHA']

wb = openpyxl.load_workbook(file_path)
sheet = wb['Sheet1']

C1 = sheet['C2'] # read direct value in cell C1
noorani_time = [str(sheet[f"B{i}"].value)[:-3] for i in range(2,7)]

st.table(pd.DataFrame({'Prayer': noorani_prayer_names, 'Time': noorani_time}))



st.subheader("ANSAR Timings")

ansar_time = [str(sheet[f"D{i}"].value)[:-3] for i in range(2,7)]

st.table(pd.DataFrame({'Prayer': noorani_prayer_names, 'Time': ansar_time}))


st.subheader("MARKAZ Timings")

markaz_time = [str(sheet[f"F{i}"].value)[:-3] for i in range(2,7)]

st.table(pd.DataFrame({'Prayer': noorani_prayer_names, 'Time': markaz_time} ))

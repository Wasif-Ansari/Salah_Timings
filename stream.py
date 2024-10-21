# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1yDAJ-TICOgxF4AMY8FU8bYnplt-KAHplllWqyZdEy50/edit?gid=1569312511#gid=1569312511"
# url = "https://docs.google.com/spreadsheets/d/1yDAJ-TICOgxF4AMY8FU8bYnplt-KAHplllWqyZdEy50/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url)
# st.dataframe(data)



df = pd.DataFrame(data)

st.title("Namaz Timings")

st.subheader("NOORANI Timings")

prayer_names = ['FAJAR', 'ZOHAR', 'ASAR', 'MAGHRIB', 'ISHA']
noorani_time = [df.iloc[i, 2] for i in range(2,7)]

st.table(pd.DataFrame({'Prayer': prayer_names, 'Time': noorani_time}))


st.subheader("ANSAR Timings")

ansar_time = [df.iloc[i, 5] for i in range(2,7)]

st.table(pd.DataFrame({'Prayer': prayer_names, 'Time': ansar_time}))


st.subheader("MARKAZ Timings")


markaz_time = [df.iloc[i, 8] for i in range(2,7)]

st.table(pd.DataFrame({'Prayer': prayer_names, 'Time': markaz_time}))


st.write("Copyright &copy; Wasif Ansari")


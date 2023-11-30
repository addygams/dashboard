import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# from babel.numbers import format_currency
# import plotly.figure_factory as ff
# import plotly.express as px
sns.set(style='dark')

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

st.header('Projek Analisis Data :sparkles:')

df = pd.read_csv("all_data.csv")
st.write(df)

st.subheader('Statistik Data')
st.write(df.describe())

df_2011 = df[df['yr'] == 0]
df_2012 = df[df['yr'] == 1]

count_2011 = df_2011.groupby(['month'])['count'].sum().reset_index()
count_2012 = df_2012.groupby(['month'])['count'].sum().reset_index()

st.subheader('Perkembangan Jumlah Peminjaman Sepeda Tiap Bulan (Tahun 2011)')
st.line_chart(count_2011, x="month", y="count")

st.subheader('Perkembangan Jumlah Peminjaman Sepeda Tiap Bulan (Tahun 2012)')
st.line_chart(count_2012, x="month", y="count")

st.subheader('Perbandingan Jumlah Peminjaman Sepeda Tiap Bulan (2011 vs 2012)')
plt.figure(figsize=(10, 6))
plt.bar(count_2011['month'] - 0.2, count_2011['count'], width=0.4, label='2011', color='skyblue')
plt.bar(count_2012['month'] + 0.2, count_2012['count'], width=0.4, label='2012', color='lightgreen')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Peminjaman')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

jml_2011 = df[df['yr'] == 0].groupby(['month', 'jenis_hari'])['count'].sum().reset_index()
avg_2011 = df[df['yr'] == 0].groupby(['month', 'jenis_hari'])['count'].mean().reset_index()

jml_2012 = df[df['yr'] == 1].groupby(['month', 'jenis_hari'])['count'].sum().reset_index()
avg_2012 = df[df['yr'] == 1].groupby(['month', 'jenis_hari'])['count'].mean().reset_index()

st.subheader('Perbandingan Jumlah Peminjaman Sepeda antara Hari Kerja dan Hari Libur (Tahun 2011)')
plt.figure(figsize=(14, 8))
sns.barplot(x='month', y='count', hue='jenis_hari', data=jml_2011, palette='viridis')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Peminjaman')
plt.legend(title='Jenis Hari')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot()

st.subheader('Perbandingan Jumlah Peminjaman Sepeda antara Hari Kerja dan Hari Libur (Tahun 2012)')
plt.figure(figsize=(14, 8))
sns.barplot(x='month', y='count', hue='jenis_hari', data=jml_2012, palette='viridis')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Peminjaman')
plt.legend(title='Jenis Hari')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot()

st.subheader('Perbandingan Rata-rata Jumlah Peminjaman Sepeda antara Hari Kerja dan Hari Libur (Tahun 2011)')
plt.figure(figsize=(14, 8))
sns.barplot(x='month', y='count', hue='jenis_hari', data=avg_2011, palette='viridis')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Peminjaman')
plt.legend(title='Jenis Hari')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot()


st.subheader('Perbandingan Rata-rata Jumlah Peminjaman Sepeda antara Hari Kerja dan Hari Libur (Tahun 2012)')
plt.figure(figsize=(14, 8))
sns.barplot(x='month', y='count', hue='jenis_hari', data=avg_2012, palette='viridis')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Peminjaman')
plt.legend(title='Jenis Hari')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot()

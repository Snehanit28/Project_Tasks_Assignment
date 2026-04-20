import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Titanic Survival Analysis Dashboard")

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

st.write("Dataset Preview")
st.dataframe(df.head())

# Survival count
st.subheader("Survival Count")
fig, ax = plt.subplots()
sns.countplot(data=df, x='Survived', ax=ax)
st.pyplot(fig)

# Survival by gender
st.subheader("Survival by Gender")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='Sex', hue='Survived', ax=ax2)
st.pyplot(fig2)

# Age distribution
st.subheader("Age Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(df['Age'].dropna(), kde=True, ax=ax3)
st.pyplot(fig3)

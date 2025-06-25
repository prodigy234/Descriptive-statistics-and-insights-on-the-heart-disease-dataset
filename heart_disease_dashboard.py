# 📊 Advanced Interactive Heart Disease Risk Dashboard
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from scipy.stats import ttest_ind

# Page Configuration
st.set_page_config(page_title="Heart Disease Analytics Dashboard", layout="wide", page_icon="🫀")
st.title("🫀 Advanced Heart Disease Risk Analysis Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('heart_disease.csv')
    return df

df = load_data()

# Preprocessing
df.fillna(df.median(numeric_only=True), inplace=True)

# Encoding Categorical Variables
cat_cols = df.select_dtypes(include='object').columns.drop("Heart Disease Status")
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Sidebar Filters
st.sidebar.header("🔍 Filter Dataset")
age_range = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (30, 70))
filtered_df = df[(df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])]

# EDA Section
st.subheader("📈 Exploratory Data Analysis")
col1, col2 = st.columns(2)

with col1:
    st.write("**Heart Disease Status Distribution**")
    fig = px.pie(filtered_df, names='Heart Disease Status', title='Heart Disease Status Distribution')
    st.plotly_chart(fig)

with col2:
    st.write("**Gender Distribution**")
    fig = px.histogram(filtered_df, x='Gender', color='Heart Disease Status', barmode='group', title='Gender vs Heart Disease')
    st.plotly_chart(fig)

# Correlation Heatmap
st.subheader("🔗 Feature Correlation")
numeric_df = filtered_df.select_dtypes(include=np.number)
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), cmap='coolwarm', annot=False, ax=ax)
st.pyplot(fig)

# PCA Section
st.subheader("📉 PCA - Dimensionality Reduction")
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_df.drop(columns=["Age"]))
pca = PCA(n_components=5)
pca_result = pca.fit_transform(scaled_data)
explained = pca.explained_variance_ratio_
st.bar_chart(pd.Series(explained, index=[f'PC{i+1}' for i in range(len(explained))]))

# Insights
st.subheader("💡 Key Insights")
col1, col2 = st.columns(2)
with col1:
    st.metric("Avg. BMI", f"{filtered_df['BMI'].mean():.2f}")
    st.metric("Avg. Blood Pressure", f"{filtered_df['Blood Pressure'].mean():.2f}")
    st.metric("Diabetes Rate", f"{filtered_df['Diabetes'].value_counts(normalize=True).get(1,0)*100:.2f}%")

with col2:
    st.metric("Heart Disease Rate", f"{filtered_df['Heart Disease Status'].value_counts(normalize=True).get('Yes',0)*100:.2f}%")
    st.metric("High Cholesterol Rate", f"{filtered_df['Cholesterol Level'].mean():.2f}")
    st.metric("Avg. Stress Level", filtered_df['Stress Level'].mode()[0] if not filtered_df['Stress Level'].mode().empty else "Unknown")

# Advanced Visuals
st.subheader("📊 Comparative Health Indicators")
compare_col = st.selectbox("Select feature to compare by Heart Disease Status", options=numeric_df.columns)
fig = px.box(filtered_df, x='Heart Disease Status', y=compare_col, color='Heart Disease Status', title=f'{compare_col} Distribution')
st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("# About the Developer")

st.image("my_image.jpg", width=150)
st.markdown("## **Kajola Gbenga**")

st.markdown(
    """
\U0001F4C7 Certified Data Analyst | Certified Data Scientist | Certified SQL Programmer | Mobile App Developer | AI/ML Engineer

\U0001F517 [LinkedIn](https://www.linkedin.com/in/kajolagbenga)  
\U0001F4DC [View My Certifications & Licences](https://www.datacamp.com/portfolio/kgbenga234)  
\U0001F4BB [GitHub](https://github.com/prodigy234)  
\U0001F310 [Portfolio](https://kajolagbenga.netlify.app/)  
\U0001F4E7 k.gbenga234@gmail.com
"""
)

st.markdown("✅ Created using Python and Streamlit")
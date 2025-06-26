# 🫀 Advanced Heart Disease Risk Analysis Dashboard

This project is a robust and interactive Streamlit dashboard that analyzes heart disease risks using real-world medical data. It provides exploratory data analysis, feature correlation, dimensionality reduction using PCA, and various statistical insights to help uncover patterns related to heart disease.

---

This Heart Disease Risk Analytics Dashboard which I built for advanced cardiovascular insights can be accessed live on Streamlit [Here](https://heartanalytics.streamlit.app/)

---

## 📬 Author

**Gbenga Kajola**

[LinkedIn](https://www.linkedin.com/in/kajolagbenga)

[Portfolio](https://kajolagbenga.netlify.app)

[Certified_Data_Scientist](https://www.datacamp.com/certificate/DSA0012312825030)

[Certified_Data_Analyst](https://www.datacamp.com/certificate/DAA0018583322187)

[Certified_SQL_Database_Programmer](https://www.datacamp.com/certificate/SQA0019722049554)

---

## 📊 Project Overview

This dashboard provides an end-to-end data exploration of heart disease risk indicators across different demographics and behavioral profiles. The tool allows users to:

- Filter patient records by **age range**.
- Explore visual **distributions of disease, gender, and lifestyle** factors.
- Analyze **correlations** among medical variables.
- Apply **PCA** for dimensionality reduction.
- Reveal **key health metrics and patterns**.
- Compare indicators **across heart disease statuses**.
- Understand how factors like **cholesterol, BMI, blood pressure**, and **stress levels** impact heart health.

---

## 📂 Dataset Overview

The dataset, `heart_disease.csv`, contains patient information such as:
## 🧾 Dataset Description

The dataset used for this dashboard contains patient medical and behavioral records across the following 21 features:

| Column                   | Description                                |
|--------------------------|--------------------------------------------|
| Age                      | Age of the individual                      |
| Gender                   | Gender (Male/Female)                       |
| Blood Pressure           | Systolic blood pressure                    |
| Cholesterol Level        | Total cholesterol                          |
| Exercise Habits          | Level of physical activity (Low/High)      |
| Smoking                  | Smoking status                             |
| Family Heart Disease     | Family history of heart disease            |
| Diabetes                 | Diabetes status                            |
| BMI                      | Body Mass Index                            |
| High Blood Pressure      | Hypertension diagnosis                     |
| High LDL Cholesterol     | LDL cholesterol status                     |
| Alcohol Consumption      | Frequency of alcohol intake                |
| Stress Level             | Self-reported stress level                 |
| Sleep Hours              | Average hours of sleep per day             |
| Sugar Consumption        | Sugar intake level                         |
| Triglyceride Level       | Triglyceride measurement                   |
| Fasting Blood Sugar      | Fasting blood sugar                        |
| CRP Level                | C-reactive protein level (inflammation)    |
| Homocysteine Level       | Homocysteine biomarker (risk indicator)    |
| Heart Disease Status     | Target variable (Yes/No)                   |

---

## 🧠 Features & Functionalities

### ✅ Interactive Filtering
- Users can select an **age range** via a sidebar slider to focus on relevant data.

### ✅ Exploratory Visualizations
- **Pie chart** showing the distribution of heart disease cases.
- **Histogram** comparing gender distribution by heart disease status.
- **Heatmap** of correlations among numerical variables.
- **Box plots** to compare specific features (e.g., cholesterol, BMI) by disease status.

### ✅ PCA Analysis
- Reduces the complexity of the data.
- Displays the **explained variance ratio** using bar charts.

### ✅ Key Metrics Display
- Dynamically calculated average values and rates such as:
  - Heart disease rate
  - High cholesterol rate
  - Diabetes rate
  - Stress level and average BMI

## 🚀 Features of the Dashboard

### 🔍 Sidebar Filters
- Filter data by **Age Range** to focus on specific demographic segments.

### 📈 Exploratory Data Analysis (EDA)
- **Heart Disease Distribution**: Pie chart of individuals with and without heart disease.
- **Gender vs Heart Disease**: Histogram comparing gender-based heart disease occurrences.

### 🔗 Feature Correlation
- Correlation heatmap to identify relationships between numerical features.

### 📉 PCA - Dimensionality Reduction
- Principal Component Analysis (PCA) applied to standardize and reduce dimensions.
- Visualized using a bar chart to explain variance captured by each component.

### 💡 Key Health Insights
- Metrics for **Average BMI**, **Blood Pressure**, **Diabetes Rate**, **Heart Disease Rate**, **Cholesterol Level**, and **Stress Level**.

### 📊 Comparative Health Indicators
- Boxplot to compare health features (e.g., BMI, Blood Pressure) against heart disease status.

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas, NumPy** – Data manipulation
- **Seaborn, Matplotlib, Plotly** – Data visualization
- **Scikit-learn** - (for Label Encoding, Scaling, PCA)
- **Scipy** - (for statistical testing)

---

## 🧪 Sample Insights From the Dashboard

- Majority of heart disease patients are **within the 50–70 age range**.
- **Higher BMI and cholesterol levels** correlate with increased risk.
- **Male gender** shows a slightly higher tendency toward heart disease.
- **Stress and lifestyle** factors (smoking, exercise habits) play significant roles in patient health.

---

## 📦 How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/prodigy234/Heart_Disease_Risk_Analysis_Dashboard.git
    cd heart-disease-dashboard
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Launch the dashboard:
    ```bash
    streamlit run heart_disease_dashboard.py
    ```

Make sure the `heart_disease.csv` file is in the same directory as your `heart_disease_dashboard.py` script.

---

## 📥 Report Download Feature

The dashboard includes a button to download a full Word-format analytics report summarizing findings. 

---

## 📬 Contact

For feedback or collaborations, reach out at:

📧 **k.gbenga234@gmail.com**

---

## ✅ Project Highlights

- End-to-end EDA
- Streamlit UI Interactivity
- Modular Code for Deployment
- Clean visualizations with real-world health data
- Ideal for presentations, health research, or predictive modeling extensions

---

## 📌 To-Do / Future Improvements

- Add ML model for predicting heart disease likelihood
- Enable downloadable reports (PDF/CSV)
- Integrate live data sources (e.g., via API)
- Include user authentication for health professionals

---

## ✅ License

This project is open-source and freely available for educational and research purposes. It is licensed under the MIT License. You are free to use, modify, and distribute it with proper attribution.
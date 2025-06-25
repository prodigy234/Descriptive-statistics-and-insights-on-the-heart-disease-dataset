# 🫀 Advanced Heart Disease Risk Analysis Dashboard

This project is a robust and interactive Streamlit dashboard that analyzes heart disease risks using real-world medical data. It provides exploratory data analysis, feature correlation, dimensionality reduction using PCA, and various statistical insights to help uncover patterns related to heart disease.

---

## 📬 Author

**Gbenga Kajola**

[LinkedIn](https://www.linkedin.com/in/kajolagbenga)

[Portfolio](https://kajolagbenga.netlify.app)

[Certified_Data_Scientist](https://www.datacamp.com/certificate/DSA0012312825030)

[Certified_Data_Analyst](https://www.datacamp.com/certificate/DAA0018583322187)

[Certified_SQL_Database_Programmer](https://www.datacamp.com/certificate/SQA0019722049554)

---

## 📂 Dataset Overview

The dataset, `heart_disease.csv`, contains patient information such as:
- Age
- Gender
- BMI (Body Mass Index)
- Blood Pressure
- Cholesterol Level
- Diabetes Status
- Stress Level
- Heart Disease Status (Target variable)

---

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
- **Pandas, NumPy**
- **Seaborn, Matplotlib, Plotly**
- **Scikit-learn** (for Label Encoding, Scaling, PCA)
- **Scipy** (for statistical testing)

## 📦 How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/prodigy234/heart-disease-dashboard.git
    cd heart-disease-dashboard
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Launch the dashboard:
    ```bash
    streamlit run app.py
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

## ✅ License

This project is licensed under the MIT License. You are free to use, modify, and distribute it with proper attribution.

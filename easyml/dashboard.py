import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from easyml.train import train

# Define dataset path and target variable (Replace with your actual dataset)
DATA_PATH = "data.csv"
TARGET_COLUMN = "price"
MODELS_TO_TEST = ["random_forest", "xgboost", "logistic_regression"]

# Train models and store results
performance_results = []
for model in MODELS_TO_TEST:
    _, result = train(DATA_PATH, TARGET_COLUMN, algorithm=model)
    performance_results.append(result)

# Convert performance results into a DataFrame
df_results = pd.DataFrame(performance_results)

# Streamlit UI
st.title("📊 EasyML: Model Performance Dashboard")

st.write("This dashboard compares the performance of ML models tested with EasyML.")

# Display results
st.write("### Model Performance")
st.dataframe(df_results)

# Visualization
st.write("### Performance Comparison")

# Get the metric column dynamically
metric_column = df_results.columns[1]

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x="Model", y=metric_column, data=df_results, ax=ax)
ax.set_title("Model Performance Comparison")
ax.set_ylabel(metric_column)
st.pyplot(fig)

st.success("Models trained and compared successfully! 🚀")

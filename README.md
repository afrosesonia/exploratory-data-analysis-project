# exploratory-data-analysis-project
The goal of this project is to understand underlying patterns in healthcare data through data cleaning, statistical analysis, visualization, and insight generation using Python

Overview:

This project presents a comprehensive Exploratory Data Analysis (EDA) of a healthcare dataset obtained from Kaggle. The dataset contains synthetic patient healthcare records, including demographic information, medical conditions, hospital stay details, billing amounts, insurance providers, and test results.

DataSource:
https://www.kaggle.com

Objectives:
- Perform data cleaning and preprocessing  
- Explore patient demographics and medical conditions  
- Analyze billing patterns and insurance providers  
- Visualize healthcare trends using charts  
- Extract meaningful insights from the data 

Data Cleaning & Preprocessing:
- Checked for missing and duplicate values  
- Converted date columns to datetime format  
- Converted categorical variables to appropriate data types  
- Created a new feature: Length of Stay (Discharge Date − Admission Date)

Findings:
- Most patients fall within the 30–60 age group
- Female patients slightly outnumber male patients
- Blood types O+ and A+ are the most common
- Chronic conditions such as diabetes and hypertension are highly prevalent
- Patient admissions show seasonal trends
- Billing amounts are right-skewed, with a small number of high-cost cases
- Insurance providers significantly influence billing amounts
- Most hospital stays are short (1–5 days)
- Age has a moderate correlation with billing amount and length of stay
- Older patients are more likely to have chronic medical conditions
- Chronic and severe conditions generally result in higher healthcare costs
- The dataset overall shows a fairly balanced gender representation
- A small number of hospitals handle significantly more admissions
- Emergency admissions are more common for acute and severe conditions. 

This exploratory data analysis provides valuable insights into healthcare utilization, patient demographics, and cost patterns.  
The results can support healthcare decision-making, cost optimization, and future predictive modeling tasks.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)

# Load dataset
df = pd.read_csv("../HealthcareDataset/modified_healthcare_dataset.csv")

# Inspect Dataset
print(df.columns)
print(df.head())
print(df.tail())
print(df.describe)

# Identify missing values
df.isnull().sum()

# Handle missing values
df = df.dropna()

# Convert column types (dates, categories)
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])

categorical_cols = ['Gender', 'Blood Type', 'Medical Condition', 
                    'Insurance Provider', 'Test Results']

for col in categorical_cols:
    df[col] = df[col].astype('category')

df['Length of Stay'] = (df['Discharge Date'] - df['Date of Admission']).dt.days

#####
sns.histplot(df['Age'], kde=True)
plt.title("Age Distribution of Patients")
plt.show()
#####
sns.countplot(data=df, x='Gender')
plt.title("Gender Distribution")
plt.show()
#####
sns.countplot(data=df, x='Blood Type')
plt.title("Blood Type Distribution")
plt.show()
#####
df['Medical Condition'].value_counts().nlargest(10).plot(kind='bar')
plt.title("Top 10 Medical Conditions")
plt.show()
#####
df.set_index('Date of Admission').resample('ME').size().plot()
plt.title("Monthly Admissions Over Time")
plt.show()
#####
sns.boxplot(y=df['Billing Amount'])
plt.title("Billing Amount Distribution")
plt.show()
#####
sns.barplot(data=df, x='Insurance Provider', y='Billing Amount')
plt.xticks(rotation=45)
plt.title("Average Billing Amount by Insurance Provider")
plt.show()
#####
sns.histplot(df['Length of Stay'], bins=30, kde=True)
plt.title("Length of Hospital Stay")
plt.show()
#####
sns.heatmap(df.select_dtypes('number').corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
#####
sns.boxplot(data=df, x='Medical Condition', y='Age')
plt.xticks(rotation=90)
plt.title("Age Distribution by Medical Condition")
plt.show()

#####
avg_spending_condition = (
    df.groupby('Medical Condition')['Billing Amount']
    .mean()
    .sort_values(ascending=False)
)

avg_spending_condition.plot(kind='bar')
plt.title("Average Billing Amount by Medical Condition")
plt.ylabel("Average Billing Amount")
plt.show()

#####
gender_condition = (
    df.groupby(['Medical Condition', 'Gender'])
    .size()
    .unstack()
)
gender_condition.plot(kind='bar', stacked=True)
plt.title("Gender Distribution by Medical Condition")
plt.ylabel("Number of Patients")
plt.show()

#####
df['Hospital'].value_counts().plot(kind='bar')
plt.title("Number of Admissions per Hospital")
plt.ylabel("Number of Admissions")
plt.show()

#####
admission_condition = (
    df.groupby(['Medical Condition', 'Admission Type'])
    .size()
    .unstack()
)

admission_condition.plot(kind='bar', stacked=True)
plt.xticks(rotation=90)
plt.title("Admission Type Distribution Across Medical Conditions")
plt.ylabel("Number of Admissions")
plt.show()

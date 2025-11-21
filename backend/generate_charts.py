import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_csv('cleaned_data.csv')

# Keep features for correlation etc
keep_features = [
    "Number_of_casualties", "Cause_of_accident", "Day_of_week", "Type_of_vehicle",
    "Area_accident_occured", "Age_band_of_driver", "Driving_experience",
    "Number_of_vehicles_involved", "Time_Period", "Types_of_Junction"
]
keep_features_target = keep_features + ["Accident_severity"]

# Make sure charts directory exists
charts_dir = "static_charts"
os.makedirs(charts_dir, exist_ok=True)

# ---- DARK MODE -- GLOBAL STYLE ----
plt.style.use("dark_background")
sns.set_context('notebook', font_scale=1.18)

plt.rcParams['axes.labelcolor'] = '#e3eafc'
plt.rcParams['xtick.color'] = '#e3eafc'
plt.rcParams['ytick.color'] = '#e3eafc'
plt.rcParams['text.color'] = '#f7faff'
plt.rcParams['axes.titlecolor'] = '#aeefff'
plt.rcParams['figure.facecolor'] = '#22223b'

# 1. Severity Distribution
plt.figure(figsize=(6,4))
sns.countplot(y='Accident_severity', data=df, order=df['Accident_severity'].value_counts().index, palette="mako")
plt.title('Accident Severity Distribution', color='#97cdf2')
plt.tight_layout()
plt.savefig(f"{charts_dir}/severity_distribution.png")
plt.close()

# 2. Top 10 Causes of Accidents
plt.figure(figsize=(9,4.5))
sns.countplot(y='Cause_of_accident', data=df, order=df['Cause_of_accident'].value_counts().index[:10], palette="crest")
plt.title('Top 10 Causes of Accidents', color='#97cdf2')
plt.tight_layout()
plt.savefig(f"{charts_dir}/top10_causes.png")
plt.close()

# 3. Severity by Time Period
plt.figure(figsize=(6.5,4))
sns.countplot(x='Time_Period', hue='Accident_severity', data=df, palette="Set2")
plt.title('Accident Severity by Time Period', color='#97cdf2')
plt.xlabel('Time Period', color='#e3eafc')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(f"{charts_dir}/time_period_severity.png")
plt.close()

# 4. Severity by Weather Condition
plt.figure(figsize=(8,4))
sns.countplot(x='Weather_conditions', hue='Accident_severity', data=df, palette="Set1")
plt.title('Severity by Weather Condition', color='#97cdf2')
plt.xlabel('Weather Conditions', color='#e3eafc')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(f"{charts_dir}/weather_severity.png")
plt.close()

# 5. Number of Casualties by Severity
plt.figure(figsize=(7.5,4))
sns.histplot(df, x='Number_of_casualties', hue='Accident_severity', multiple='stack', bins=df['Number_of_casualties'].max(), palette='Set3')
plt.title('Number of Casualties by Severity', color='#97cdf2')
plt.xlabel('Number of Casualties', color='#e3eafc')
plt.tight_layout()
plt.savefig(f"{charts_dir}/casualties_severity.png")
plt.close()

# 6. Feature Importance (if you have 'feature_importance.csv' as DataFrame)
try:
    feature_importance = pd.read_csv('feature_importance.csv')
    plt.figure(figsize=(8, 5))
    sns.barplot(
        y='Feature', x='Importance',
        data=feature_importance.sort_values('Importance', ascending=True).tail(15),
        palette="viridis")
    plt.title('Top 15 Most Important Features', color='#97cdf2')
    plt.xlabel('Importance', color='#e3eafc')
    plt.tight_layout()
    plt.savefig(f"{charts_dir}/feature_importance.png")
    plt.close()
except Exception as e:
    print("Skipped feature importance chart:", str(e))

# 7. Heatmap: Accident Severity vs Top 10 Causes of Accident
plt.figure(figsize=(10, 6))
top10_causes = df['Cause_of_accident'].value_counts().index[:10]
pivot = df[df['Cause_of_accident'].isin(top10_causes)].pivot_table(
    index='Cause_of_accident', columns='Accident_severity', aggfunc='size', fill_value=0
)
sns.heatmap(pivot, annot=True, fmt='d', cmap='mako', linewidths=.5, linecolor='#22223b')
plt.title('Heatmap: Severity vs Top 10 Causes', color='#97cdf2')
plt.xlabel('Accident Severity', color='#e3eafc')
plt.ylabel('Cause of Accident', color='#e3eafc')
plt.tight_layout()
plt.savefig(f"{charts_dir}/heatmap_severity_cause.png")
plt.close()

# 8. Heatmap: Accident Severity by Light Conditions
plt.figure(figsize=(8, 5))
pivot_light = df.pivot_table(
    index='Light_conditions', columns='Accident_severity', aggfunc='size', fill_value=0
)
sns.heatmap(pivot_light, annot=True, fmt='d', cmap='rocket', linewidths=.5, linecolor='#22223b')
plt.title('Heatmap: Severity by Light Conditions', color='#97cdf2')
plt.xlabel('Accident Severity', color='#e3eafc')
plt.ylabel('Light Conditions', color='#e3eafc')
plt.tight_layout()
plt.savefig(f"{charts_dir}/heatmap_severity_light.png")
plt.close()

# 9. Correlation Matrix: Selected Features
encoded_df = df[keep_features_target].copy()
for col in keep_features_target:
    if encoded_df[col].dtype == 'object':
        encoded_df[col] = encoded_df[col].astype('category').cat.codes

corr = encoded_df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='mako', center=0,
            annot_kws={"color":'#c9f6fb'})
plt.title('Correlation Matrix: Selected Features', color='#97cdf2')
plt.tight_layout()
plt.savefig(f"{charts_dir}/corr_matrix.png")
plt.close()

print("✓ All charts have been generated in the /static_charts directory.")

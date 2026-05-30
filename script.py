# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# %%
df = pd.read_csv("dataset.csv")

# %% [markdown]
# # TASK 1 : Data Collection and understanding it

# %%
print(df.head())  #Prints first 5 rows

# %%
print(df.info()) 

# %%
print(df.shape) #Prints the number of rows and columns in the Dataset

# %%
print(df.columns)

# %% [markdown]
# # TASK 2 : Data Cleaning & Preprocessing

# %%
print(df.isnull().sum())

# %%
print(df.duplicated().sum())

# %%
df = df.drop_duplicates()
print("Duplicates Removed Successfully")

# %%
# sum() counts total missing values column-wise

# isnull() identifies missing values
# duplicated() identifies duplicate rows
# drop_duplicates() removes duplicate rows

# %% [markdown]
# # TASK 3 : Exploratory Data Analysis (EDA)

# %%
print(df["status"].value_counts())  #Unique values and their count in "status" column

# %% [markdown]
# ### Average of Columns

# %%
print("Average Text Length:")
print(df["text_length"].mean())

print("Average Word Count:")
print(df["word_count"].mean())

print("Average Polarity:")
print(df["polarity"].mean())

print("Average Subjectivity:")
print(df["subjectivity"].mean())

# %% [markdown]
# ###

# %%
# Top Mental Health Categories
print("Top Categories:")
print(df["status"].value_counts().head())

# %% [markdown]
# ### EDA insights 

# %%
print("1. Some mental health categories appear more frequently.")
print("2. Text length varies across different categories.")
print("3. Word count differs based on emotional expression.")
print("4. Sentiment polarity helps understand emotional tone.")
print("5. Subjectivity analysis shows personal emotional expression.")

# %% [markdown]
# # TASK 4 : Data Visualization

# %% [markdown]
# Mental Health Category Distribution

# %%
plt.figure(figsize=(12,5))
sns.countplot(x="status", data=df)
plt.title("Mental Health Category Distribution")
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# Polarity Distribution

# %%
plt.figure(figsize=(8,5))
sns.histplot(df["polarity"], bins=20)
plt.title("Sentiment Polarity Distribution")
plt.show()

# %% [markdown]
# Word Count by Category

# %%
plt.figure(figsize=(12,5))
sns.boxplot(x="status", y="word_count", data=df)
plt.title("Word Count by Mental Health Category")
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# Correlation Heatmap

# %%
plt.figure(figsize=(10,6))
sns.heatmap(
    df[
        [
            "text_length",
            "word_count",
            "polarity",
            "subjectivity"
        ]
    ].corr(),
    annot=True
)
plt.title("Feature Correlation Heatmap")
plt.show()

# %% [markdown]
# Wordcloud Visualization

# %%
text = " ".join(df["text"].astype(str))
wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color="white"
).generate(text)

plt.figure(figsize=(12,5))
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Most Common Words in Dataset")
plt.show()

# %% [markdown]
# # TASK 5 : Final insights

# %% [markdown]
# Most Common Category 

# %%
most_common_category = df["status"].value_counts().idxmax()
print("Most Common Mental Health Category:",most_common_category)

# %% [markdown]
# Average Word Count

# %%
avg_word_count = df["word_count"].mean()
print("Average Word Count:",avg_word_count)

# %% [markdown]
# Number of High and Low Polarity Text

# %%
# High Polarity Text Count
positive = df[df["polarity"] > 0.5]
print("Number of Highly Positive Texts:",len(positive))

# Low Polarity Text Count
negative = df[df["polarity"] < 0]
print("Number of Negative Texts:",len(negative))

# %% [markdown]
# Keyword Analysis

# %%
# Convert keyword columns to binary values
# 1 = keyword present, 0 = keyword absent

keyword_columns = [
    "has_suicidal_keyword",
    "has_stress_keyword",
    "has_help_keyword"
]

for col in keyword_columns:
    df[col] = df[col].isin(["1", "True"]).astype(int)

# Percentage of texts containing keywords
print(f"Suicidal Keyword Present: {df['has_suicidal_keyword'].mean()*100:.2f}%")
print(f"Stress Keyword Present: {df['has_stress_keyword'].mean()*100:.2f}%")
print(f"Help Keyword Present: {df['has_help_keyword'].mean()*100:.2f}%")



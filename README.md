# Mental Health Text Analysis using NLP

## Project Overview

This project focuses on analyzing mental health related text data using basic Natural Language Processing (NLP) techniques.

The dataset contains text entries along with engineered features such as text length, word count, sentiment polarity, subjectivity, and keyword indicators. The goal of this project is to explore patterns in mental health related text and generate meaningful insights through data analysis and visualization.

This project was completed as part of my Data Science Internship at Decode Labs.

---

## Dataset

Dataset Source:

https://www.kaggle.com/datasets/priyangshumukherjee/mental-health-text-classification-dataset

Dataset used:

- mental_heath_feature_engineered.csv

Key Features:

- Text
- Status (Mental Health Category)
- Text Length
- Word Count
- Sentiment Polarity
- Subjectivity
- Suicidal Keyword Indicator
- Stress Keyword Indicator
- Help Keyword Indicator

---

## Libraries Used

- Pandas
- Matplotlib
- Seaborn
- WordCloud

---

## Project Tasks

### Task 1: Dataset Understanding

- Loaded and explored the dataset
- Examined dataset structure
- Checked columns and data types

### Task 2: Data Cleaning

- Checked missing values
- Checked duplicate records
- Removed duplicate entries

### Task 3: Exploratory Data Analysis

- Analyzed category distribution
- Examined text length and word count
- Studied sentiment polarity and subjectivity
- Generated observations from the dataset

### Task 4: Data Visualization

Created the following visualizations:

- Mental Health Category Distribution
- Sentiment Polarity Distribution
- Word Count by Mental Health Category
- Feature Correlation Heatmap
- WordCloud of Common Words

### Task 5: Text Pattern Analysis

- Identified most common mental health category
- Analyzed positive and negative text counts
- Examined keyword occurrence percentages
- Generated project insights

---

## Key Insights

- Certain mental health categories appear more frequently than others.
- Message length varies across categories.
- Sentiment polarity helps identify emotional tone in text.
- Keyword analysis highlights the presence of stress, help, and suicidal expressions.
- WordCloud visualization provides an overview of commonly used words.

---

## How to Run

Install required libraries:

```bash
pip install pandas matplotlib seaborn wordcloud
```

Run the notebook:

```bash
jupyter notebook
```

Open:

```text
Project2.ipynb
```

and run all cells.

---

## Repository Structure

```text
Decode-Labs-Project-2/
│
├── dataset.csv
├── Project2.ipynb
├── script.py
└── README.md
```

---

## Learning Outcomes

Through this project, I learned:

- Basic NLP concepts
- Text data analysis
- Sentiment analysis interpretation
- Data visualization using Python
- Extracting insights from text-based datasets

---

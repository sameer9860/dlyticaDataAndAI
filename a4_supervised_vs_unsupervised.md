# Assignment 4 - Supervised vs Unsupervised Learning

**Name:** Samir Khatiwada

**Date:** June 18, 2026

## PART A - EXPLAIN IN YOUR OWN WORDS

### 1. Supervised Learning vs Unsupervised Learning

**Supervised Learning:**

Supervised learning is a type of machine learning where the training data contains labels (correct answers). The model learns from the input data and the known answers so it can predict the correct output for new data.

**Unsupervised Learning:**

Unsupervised learning is a type of machine learning where the training data does not contain labels. The model tries to find patterns, groups, or relationships in the data by itself.

### 2. Real-Life Analogies

**Supervised Learning Analogy:**

Studying for an exam using a book that includes both questions and answer keys. You learn by comparing your answers with the correct ones.

**Unsupervised Learning Analogy:**

Organizing a large collection of photos into groups without any instructions. You group similar photos together based on what you notice.

### 3. Classification vs Regression

Both classification and regression are supervised learning methods because they use labeled data.

* **Classification** predicts categories or classes, such as spam/not spam or cat/dog/bird.
* **Regression** predicts numerical values, such as house prices or temperatures.

## PART B - CLASSIFY EACH SCENARIO

| Real-world Task                                                              | Learning Type | Type           |
| ---------------------------------------------------------------------------- | ------------- | -------------- |
| Predict tomorrow's temperature from weather data                             | Supervised    | Regression     |
| Group 10,000 customers into similar segments (no labels given)               | Unsupervised  | N/A            |
| Decide if an email is spam or not spam                                       | Supervised    | Classification |
| Predict the selling price of a used car                                      | Supervised    | Regression     |
| Find unusual credit-card transactions that look like fraud (no fraud labels) | Unsupervised  | N/A            |
| Recognize whether a photo contains a cat, dog, or bird                       | Supervised    | Classification |
| Organize news articles into topic groups without being told the topics       | Unsupervised  | N/A            |

## PART C - THINK A LITTLE DEEPER

### 1. Supervised Task Example

**Task:** Predict the selling price of a used car

**Features (Inputs):**

1. Car age
2. Total kilometers driven
3. Engine size

**Label (Output):**

Selling price of the car

### 2. Why Can't We Use Unsupervised Learning to Predict an Exact House Price?

Unsupervised learning does not have labels or correct answers in the training data. Since house prices are the answers we want to predict, the model needs labeled examples, which makes it a supervised learning problem.

### 3. Five Steps of Building a Machine Learning Model

Collect Data → Prepare/Clean Data → Train Model → Evaluate Model → Make Predictions/Deploy Model

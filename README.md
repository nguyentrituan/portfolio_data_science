# WELCOME 👋🏼

I’m a Data Analyst (Ex-Business Intelligence Analyst) based in Ho Chi Minh City with a passion for discovering **customer/product insights** through data analytics. Leveraging my background in International Business Economics, I help data-driven companies tell actionable stories. I love chatting about analytics, besides sometimes I like telling a logically humorous story with many funny situations. In my spare time, I go trekking as a good way to challenge myself. 

# PORTFOLIO DATA SCIENCE 
## A/B Testing

In my experience working at leading tech companies, I've noticed that A/B testing is widely used, especially in companies and industries with large user bases such as e-commerce and gaming.

Why use A/B testing? With a large user base, companies cannot simply apply any feature they want, as doing so may carry the risk of hurting user experience and subsequently affecting the lifetime value of users. Therefore, A/B testing is necessary to control risks. Instead of applying changes to the entire user base, companies can apply them to a small group, for example, about 10% of users, and then use statistical methods to determine if there is a statistically significant difference between the control group and the variants.

In terms of methodology, I have documented it in this [Gitbook Link](https://app.gitbook.com/o/VfRPaxLWrwVO1zxPDj2s/s/iggGa4mab2uKFxO1Zj5M/). On GitHub, I provide code for both frequentist and Bayesian approaches in A/B testing.

Files consist of the following parts:
1. Frequentist Code
2. Bayesian Code

![image](https://github.com/nguyentrituan/portfolio_data_science/assets/121095339/59bb93a6-e043-41b7-ba45-e98128be6b99)


## Kaggle Competition - Prediction Interval for Birth Weight

I have had the opportunity to participate in a Kaggle competition, and we ranked in the top 10 on the leaderboard (Team: Triple Tiger).

Kaggle Competition Info https://www.kaggle.com/competitions/prediction-interval-competition-i-birth-weight/overview

**Problem:** 
In many ML contests involving regression it is not unusual to focus on what are called point predictions (expectation values) 𝑌̂  However, in this competition we are uninterested in the expectation value, but rather in producing a prediction interval, 𝐶𝛼^ . Indeed prediction intervals are often of greater practical interest than point predictions, which only form part of the story. In this competition we shall be predicting the intervals associated with birth weights.
**Goal:** To obtain the minimum average prediction interval.

**Solution:**
In the competition, I experimented with various techniques ranging from simple to complex to tune models, including KNN, Linear Regression, XGBoost Regressor, Decision Tree, and Random Forest. The results showed that the XGBoost model performed the best.

Note:
XGBoost is a decision-tree-based ensemble Machine Learning algorithm that uses a gradient boosting framework. In prediction problems involving unstructured data (images, text, etc.) artificial neural networks tend to outperform all other algorithms or frameworks. However, when it comes to small-to-medium structured/tabular data, decision tree based algorithms are considered best-in-class right now. XGBoost and Gradient Boosting Machines (GBMs) are both ensemble tree methods that apply the principle of boosting weak learners (CARTs generally) using the gradient descent architecture. However, XGBoost improves upon the base GBM framework through systems optimization and algorithmic enhancements.

![image](https://github.com/nguyentrituan/portfolio_data_science/assets/121095339/e17796bd-3fc9-48fc-bd90-fbfedf4a7793)


## Machine Learning for Marketing

This is the course for which I was certified at the Computer Center of the University of Natural Sciences. The course provided me with foundational knowledge of Machine Learning, with examples closely related to Marketing.

In this GitHub repository, I will present the code taught in the program, with simple and understandable examples that can help us better understand various machine learning algorithms. I will also present the final graduation project of the program for you to refer to.

In addition, to help you better understand how machine learning algorithms work, I have documented how machine learning runs on Excel to provide a clearer visualization. [Gitbook Link](https://app.gitbook.com/o/VfRPaxLWrwVO1zxPDj2s/s/ig7BlfmYLvYH7dyApFR1/


## Segmentation

### Concepts

One key go-to idea to uncover customer behavior is to spliting them into smaller groups that within each group they are more similar to each other.
That make the insights is cleared, comparing to doing analysis on the whole population. 

You will notice that they have done it by multiple ways in our analytics works: splitting customers by geo, app, level of values, etc.
In this hands-on, we try 3 techniques, serving that purpose: 

#### 1. Cohort

We start with **Cohort analysis**, we commonly segment customers by the date they onboard with the app/products, 
with the assumption that each snapshot of time, we acquire a group of customers (as a cohort). 
The product offerings and marketing strategies are the same, so we expect customers in the same cohort are more or less comparable. 

In fact, cohorts is not necessarily defined as the time of acquiring customers, but other given factors that make the group of customers more similar.
The cohort by the starting time of customers give a view of how the product evolve over time, and how the customer base shift over time.
 

#### 2. RFM Model

In the topic of Segmentation, we will introduce the RFM model, which is a popular model in marketing and customer segmentation for determining Customer Value (CV).


What's R, F, M?

RFM segments customers by 3 important features:

1. `Recency`: to measure how recent the last interaction with a customer
2. `Frequency`: how frequent a customer interact with the business
3. `Monetary`: the monetary value a customer generate


4. KMeans clustering




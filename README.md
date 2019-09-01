# Data Mine, Visualize, and Predict on Yelp Dataset
### Data Mining Capstone Course @UIUC

#### Author: Viraj Bhalala


## Overview:
The goal of this data mining project is to use an opportunity to synthesize the knowledge and skills we have learned from previous courses and apply them to solve real-world data mining challenges. We will work on a restaurant review data set from Yelp and mine this data set to discover interesting and useful knowledge to help people make dining decisions, including constructing a cuisine map to help people understand the landscape of different cuisines, mining popular dishes of a given cuisine, recommending (i.e., ranking) restaurants for a given dish, and predicting hygiene of a restaurant.


This capstone repo is seperated into a set of mining parts. These parts are explained more in details below

## Part 1: Data Exploration

Use LDA to topic model to extract topics from all the review text, positive and negative reviews seperately and visualize the topics to understand what people have talked about in these reviews. Use wordcloud to visualize topic clusters.

Distribution of rating stars

![Alt text](./1.DataExploration/ratingDist.png?raw=true "Title")

10 clusters(there are few more plots in notebook)
![Alt text](./1.DataExploration/cuisineCluster.png?raw=true "Title")


## Part 2: Cuisine Similarity & Clustering

In this part, we will work on mining this data set to discover knowledge about cuisines. In the Yelp dataset, businesses are tagged with categories. For example, the category "restaurant" identifies all the restaurants. Specific restaurants are also tagged with cuisines (e.g., "Indian" or "Italian"). This provides an opportunity to aggregate all the information about a particular cuisine and obtain an enriched representation of a cuisine using, for example, review text for all the restaurants of a particular cuisine. Such a representation can then be exploited to assess the similarity between two cuisines, which further enables clustering of cuisines.

The goal of this task is to mine the data set to construct a cuisine map to visually understand the landscape of different types of cuisines and their similarities using LDA and TF-IDS and visualize using heat map similarity matrix. This cuisine map can help users understand what cuisines are available and their relations, which allows for the discovery of new cuisines, thus facilitating exploration of unfamiliar cuisines

Cuisine Similarity Matrix
![Alt text](./2.CuisineSimilarity&Clustering/cuisineSimilarityMatrix.png?raw=true "Title")

## Part 3: Discover Popular Dishes
The goal of this task is to mine the data set to discover the common/popular dishes of a particular cuisine. Typically when you go to try a new cuisine, you don’t know beforehand the types of dishes that are available for that cuisine. For this task, we would like to identify the dishes that are available for a cuisine by building a dish recognizer.

In this task, we used Gensim pharses and word2vec to mine popular dishes and used word cloud to visualize it.

Below are popular dishes from Indian cuisine

Popular Dishes Word Cloud From Indian Cuisine
![Alt text](./3.DiscoverPopularDishes/cuisineWordCloud.png?raw=true "Title")

## Part 4 & 5: Dish and Restaurant Recommender

Our goal is to leverage dish names to further help people making dining decisions. People often face challenge when they have to make decision on trying new dish from cuisine they are not so familiar with as well as trying restaurants that they have never visited before. In this part, we mine popular dishes in cuisine that are liked by people using Yelp reviews. We also create visualization plots that can help people making decision.

Rating stars distribution of different restaurants associated with each popular dishes from Indian cuisine
![Alt text](./4&5.DishandRestaurantRecommender/starBarPlots.png?raw=true "Title")

Similar to above plot but distibution shown in proportion
![Alt text](./4&5.DishandRestaurantRecommender/starBarPlotProportion.png?raw=true "Title")


Rating stars distribution of different restaurants that offers chicken tikka dish from Indian cuisine
![Alt text](./4&5.DishandRestaurantRecommender/chikkenTikkaRestaurants.png?raw=true "Title")

Similar to above plot but distibution shown in proportion
![Alt text](./4&5.DishandRestaurantRecommender/chikkenTikkaRestaurantByProportion.png?raw=true "Title")


## Part 6: Restaurant Hygiene Prediction
Sometimes we make decisions beyond the rating of a restaurant. For example, if a restaurant has a high rating but it often fails to pass hygiene inspections, then this information can dissuade many people to eat there. Using this hygiene information could lead to a more informative system; however, it is often the case where we don’t have such information for all the restaurants, and we are left to make predictions based on the small sample of data points.

In this part, we are going to predict whether a set of restaurants will pass the public health inspection tests given the corresponding Yelp text reviews along with some additional information such as the locations and cuisines offered in these restaurants. Making a prediction about an unobserved attribute using data mining techniques represents a wide range of important applications of data mining.

## Task 7: Dashboard

A simple and naive dashboard application developed in Python Dash to allow user to use hygiene prediction model.

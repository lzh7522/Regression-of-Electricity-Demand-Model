# Regression-of-Electricity-Demand-Model

Brief Introduction:
=
By using regressive calculation, we aims to find the weather and social factors that affects the electricity consumption in Singapore, and construct the model.

We are doing a mathematics project to find the influence factors of the electricity consumption in Singapore. These factors are about weather, economics, social development. By using the OLS regression model in Python, we firstly find the P-values of each factors against electricity consumption, which indicate the relevance between these factors and electricity consumption. Then we delete the factor with the highest P-value. Repeat the step until all P-values are below 0.05, which suggests high relevance with electricity demand.

In this programme, OLS library will do the regreesion and automatically delete the factor with the highest P-values, until all P-values are below 0.05. The last regreesive calculation indicated the final results and coefficient in this model.

`.csv` is the Electricity Consumption Residential in Singapore and other data. <br>`p_values_hh.py` is the main Python file.

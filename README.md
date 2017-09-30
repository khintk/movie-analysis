# K-Means Clustering Movie Analysis

## What was our K-Means Clustering Movie Analysis Project?

The goal of our project was to create an algorithm using the k-means clustering method to see how well top grossing domestic movies were doing in the international marketplace.
We hoped that by clustering the movies, patterns would emerge which would show us if there were any specific types of movies that were more successful abroad.
Also, we predicted that we would see differing preferences of movie genre throughout the different regions.


## What is K-Means?
K-means is an algorithm which is used to group sets of data into a specified number of clusters.
The algorithm starts by taking in a dataset and randomly grouping the data into a certain number of groups (ie. clusters.)
Next, 1 randomly chosen centroid points is chosen for each cluster. At this point the euclidean distance formula is used to find
a point's distance from each centroid. The shortest distance decides which cluster this point will be assigned to and after this happens for each point the clusters are rearranged.
This re-arrangement process continues until all the points have settled (threshold hits 0) or the distances hit a specified floor value.
By the end of the algorithm, all points in each cluster have the shortest distance to their centroid.  


## How did we approach our project?
We started by researching how k-means algorithms worked, and the various ways it could be implemented.
Next, we began gathering our movie data and pseudo-coding our algorithm. In order to see if certain regions preferred a specific type of movie we split the international market place by continents
and then collected the gross profit from each continent of the overall top 10 movies in the world over the past 10 years. Most of the data collected is from the International Movie Database (ie. IMBd),
and for data we couldn’t locate, the cells were filled with 0. *The data does not include Antarctica because of the lack of box office reports. Also, the total gross reported for North America does not include the United States. *


## Running the program
We built our program with PyCharm. To see the result, you can run MovieAnalysisKhinCourtneyFinal.py file. This program requires a Python framework to run.

## Acknowledgments
		We would like to acknowledge our Professor Shiled Sen helping us with the project.

 Khin Kyaw & Courtney

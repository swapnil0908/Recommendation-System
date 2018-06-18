# Recommendation-System
#INTRODUCTION
A Recommendation System is an information filtering technique, which provides the users with the information, which he/she might be interested in. We see the use of recommendation systems all around us. These systems are personalizing our web experience, telling us what to buy (Amazon), which movies to watch (Netflix), whom to be friends with (Facebook) and which songs to listen (Pandora) etc. These recommendation systems leverage our shopping/ watching/ listening patterns and predict what we could like in future based on our behaviour patterns. As per the project requirement I have implemented a recommendation system based on the user based collaborative filtering method, and I have used the Pearson’s Coefficient to calculate the similarity between users. The user based collaborative filtering assumes that if certain users agree on a particular item in the past, chances are that they might agree to similar items in the future.

#ALGORITHM
1.	Read the input file and make a user by item matrix, such that each user has some rating for the items. If no rating present, then rating is 0.
2.	Find the similarity of the first user (using Pearson’s Coefficient) with all other users and store it in a map.
3.	Arrange the similar users in an order such that the most similar user is placed at the first position and the least similar user is placed in the last.
4.	For every item ‘ i ’ that user ‘ u ’ has no rating for yet, find similar users that have rated the particular item.
5.	Add the similar users preference for the item ‘ i ’, weighted by the similarity (Pearson’s Coefficient) to a running average.
6.	Repeat the step 2 to step 5 for the next user and so on for all the users, and thus we get the recommended ratings for all the items that each user had not yet given a rating for.

#CONCLUSION
•	For 943 users and 1682 items when 85% data is taken for Training set and 15% for test set, the Pearson’s Coefficient for similarity has the lowest root mean square error value when compared to Cosine similarity and Euclidean distance.
•	Collaborative Filtering can produce more personalized recommendations, when compared to content based filtering.
•	The cold start problem for new users is also taken care of by the algorithm, by taking the average of all the ratings of similar users.

#REFERENCES
•	http://recommender-systems.org/collaborative-filtering/
•	https://en.wikipedia.org/wiki/Recommender_system
•	https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0


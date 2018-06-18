import numpy as np
#import math
from collections import OrderedDict
from scipy import stats

"""
#function for calculating the similarity between 2 users, using the Pearson's Coefficient
def pearson(user1, user2):
   #calculate the mean for user1 and user2 for common rated items
    sum1 = 0
    sum2 = 0
    n = 0
    #print("user1:"+str(user1))
    #print("user2:"+str(user2))
    for i in range(len(user1)):
        if user1[i] != 0 and user2[i] != 0:
            sum1 += user1[i]
            sum2 += user2[i]
            n += 1

    #incase the users have rated no common items
    if n ==0:
        return 0.0
    #print (n)
    mean1 = float(sum1)/n
    mean2 = float(sum2)/n

    num = 0
    den1 = 0
    den2 = 0
    #print("user1 length"+str(len(user1)))
    for i in range(len(user1)):
        if user1[i] != 0 and user2[i] != 0:
            #print user1[i],mean_u1,user2[i],mean_u2
            num += (user1[i]-mean1)*(user2[i]-mean2)
            den1 += math.pow((user1[i]-mean1),2)
            den2 += math.pow((user2[i]-mean2),2)
    #print num,dem1,dem2,n
    if den1 == 0.0 or den2 == 0.0:
        return 0.0
        
    
    sim = (float(num)/math.sqrt(den1))/math.sqrt(den2)
    #print num,dem1,math.sqrt(dem1),dem2,math.sqrt(dem2),sim
    return sim
"""

#Function to find the mean of the ratings given by a user
def average(row):
    sum = 0
    n = 0
    for rating in row:
            if rating != 0 :
                sum = sum + rating
                n = n + 1
    avg = float(sum)/n
    return avg


def main():

    #number of users and items
    users = 943
    items = 1682
    #Array which contains the similarity values for each user i with each user j
    similarity = {}
    # 943 by 1682 matrix containing zeroes
    userXitem = np.zeros((users,items),dtype=int)
    #open the input file
    f1 = open('train_all_txt.txt')
    for line in f1:
            #split each line into user ID, item ID and rating
            user,item,rating = line.split()
            #store the rating in a user - item matix
            userXitem[int(user)-1][int(item)-1] = int(rating)
    #close file        
    f1.close()
    #copy the user-item matrix to another matrix
    matrix = np.copy(userXitem)
    #open the final_output file
    f2 = open("output.txt","w")
    
    i=0
    #for all users from 0-943, do the following...
    while(i<users):   
        print ("user: "+str(i+1))
        #for all users from 0-943
        for j in range(0,943):
            #find the similarity between user[i] and user[j], using pearson's coefficient and store it in an array
            similarity[j] = stats.pearsonr(userXitem[i],userXitem[j])[0]
         #arrange all the similarities in descending order   
        similarity = OrderedDict(sorted(similarity.items(),key=lambda t:t[1],reverse=True))
        #find the mean rating of the user[i]
        mean = average(userXitem[i])
        #for items from 0-1682
        for k in range(0,items):
            #if item not rated, make a and b 0.
            if(userXitem[i][k] == 0):
                a = 0.0
                b = 0.0
                
                #starting from the most similar user who has rated the item which user[i] has not rated, find the average rating
                for elem in similarity:
                    if userXitem[elem][k] != 0 and similarity[elem]>0.0: #and ccount<=100:
                        a = a + similarity[elem]*userXitem[elem][k]
                        b = b + similarity[elem]
                       
                if b==0:
                    matrix[i][k] = round(mean,0) 
                else: 
                    avg_rating = a/b
                    #store the average rating, for the item for which user[i] has not rated
                    matrix[i][k] = round(avg_rating,0)
            #print the user ID, item ID, and the rating
            f2.write(str(i+1)+" "+str(k+1)+" "+str(matrix[i][k])+"\n")
         #go to the next user i;   
        i=i+1
       
    #close output file
    f2.close()   

if __name__ == "__main__":
    main()
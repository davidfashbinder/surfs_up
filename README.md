# Climate Analysis

### Purpose of Analysis
In this analysis, we are examining the key differences between the temperatures during the months of June 2017 and December 2016.  We need to determine if the surf & ice cream shop can thrive year-round on the island of Oahu.  

### Results 

### Key Differences

![June 2017](https://github.com/davidfashbinder/surfs_up/blob/main/June.png)
![December 2016](https://github.com/davidfashbinder/surfs_up/blob/main/December.png)

-The average temperate in June was 74.94 degrees, and in December it was 71.04 degrees.  That's only a 5.2% difference between June and December.  
-The minimum temperature in December is 8 degrees lower than in June (64 in june vs. 56 in december).  That's a difference of 12.5%.
-The maximum temperature only varies by 2 degrees - 85 in June and 83 in December.  That's only a 2.35% difference.

### Summary Recommendations
Examining the summary statistics, we can see that December still brings very warm weather to Oahu, and the surf and ice cream shop should perform well.  There are colder days, with minimum temperatures in December more than 10% below those in June.  However, these statistics do not account for time of day - it should be expected that most minimum temperatures occur when the sun is down.  We also don't know how frequent the low temperatures occur in December, or how frequently the high ones do.  We can run two additional queries:

-Number of temperature readings below 69 degrees
![Number of readings below 69.0](https://github.com/davidfashbinder/surfs_up/blob/main/query1.png)
-Number of temperature readings above 74 degrees 
![Number of readings above 74.0](https://github.com/davidfashbinder/surfs_up/blob/main/query2.png)


We see that there were 481 results below 69%, which is the bottom quartile of temperatures, while there were only 399 results above 74, the top quartile.  This tells us that there are more 'colder' days in December than 'warmer'. 74 degrees also happened to be the mean temperature in June, so that means that there were 1,118 temperatures recorded in December that were less than the average temperature in June.  That number is equal to 73.7% of all December temperatures!  

While I still believe the shop will be profitable in December, we should gather more information about the temperature readings, such as time of day, if we want to dig into this data more. 

Thank you.

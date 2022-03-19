# Extra Credit
___
## The Problem:
Let’s consider a long, quiet country road with houses scattered very  sparsely along it. (We can picture the road as a 
long line segment, with  an eastern endpoint and a western endpoint.) Further, let’s suppose that  despite the bucolic
setting, the residents of all these houses are avid cell  phone users. You want to place cell phone base stations at
certain points  along the road, so that every house is within four miles of one of the base  stations.

Give an efficient algorithm that achieves this goal, using as few base  stations as possible.

## My Solution:
For this problem I started by setting up some data structures that I would be using to get my results. First,
I created an array of houses that I will use to store the locations of my houses. For example, if ```houses[0] = 2```
that would mean there is a house at mile marker two on this road. I then populated my array with some random integers
and sorted them to make it easier on myself when placing my cell towers. Then I initialize my two values ```startInterval```
and ```endInterval``` to zero, this is going to help visualize the placement of the cell towers. Then, I begin to loop
through my array of houses and check to see if they are in the current interval of my cell towers. In the first iteration
of this loop there are no cell towers, so we build our first base station four miles away from our first house. In the
next loop we check to see if the house is covered under the last cell tower. If it is then we skip it. If it isn't we 
build another cell tower 4 miles away from that house. This continues until we have reached the end of our array.

## Time Complexity:
The time complexity for this solution is O(n) since I am only looping through the collection of houses once.

## Requirements to run code:
The only requirements needed to run the code is Python at version 3.9 or greater. Since I am only using the random library
which is a part of the python standard library. There are no other external libraries needed.

### Link to Video Explanation:
[My Video explanation of the code uploaded to YouTube.](https://youtu.be/3KLrYxXKwq4)

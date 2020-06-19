#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n): as the size of the input grows the runtime will grow at the same rate 


b) O(n log n): even though it is nested loops the while loop is moving twice as fast due to the multiplier.  this makes that inner loop a log n


c) O(n): assuming bunnies is the n value with this being a recursive call it will increase at the same rate as the input grows

## Exercise II



Binary search: O(log n) I would pick the middle floor then evaluate the drop. 


If it breaks it will know that any floor above
will also break the egg essentially wiping out the need to look at those floors.  

this would become the top floor and i would start over with picking the middle floor


If it doesn't break it will know that any floor below 
will also not break the egg essentially wiping out the need to look at those floors

this would become the bottom floor and i would start over with picking the middle floor


eventually the middle floor will be the answer


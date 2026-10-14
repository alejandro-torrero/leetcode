So, having the array 

[1,2,3]

The idea is to sum the square value of each n element of the array, while alternating the sign of each elemento so that the final result is mazimized

Having those 3 values, we have
1 -> 1
2 -> 4
3 -> 9

Intutivelty, 1 being the smallest we should give that the negative value so that the result is

2 - 1 = 9 = 12

Now, this is a maximizing problem with a dynamic programming approeach, where by each element of the array we alternatate whether we sum its value or we substract its value

On that regard, we could star tby sorting the array, but my first approeach will be to start with a recursive call with an index to go trhpugh the array, and one by one we will decide to sum or to substract

In fact, the decision is at the start, after that we can only alternate, so having

[1,2,3]

There are 2 options

-1^2 + 2^2 - 3^2

1^2 - 2^2 + 3^2

Well, not really two options as the solution actually was

2^2 - 1^2 + 3^2

So, the order of the array actually matters, this introduces another consideration where we not only have an index to go trhough the array, but also we need to set an specific order.

Next approach is to sort the array, the smaller number will always be negative and depending on the last numbers we sum them. So having

[1,2,3] which is already sorted we have 3 elements, which means 2 have to be sum and 1 substract to maximize the result

3%2 = 1


[1,2,3,4]

First two will be negatives and last two will be positives

[1,2,3,4,5]

first two will be negative and last.3 will be positive.

Whenever the len divided by 2 has a remainder, it means that we will take the rounded up value of the lenght of the array


And finally, if the array has negative values, we dont really need that sign, the squqre root of n will always be positive, so apply abs before sorting

Clearly, not AI was used on this ideas markdown
Alejandro Torrero
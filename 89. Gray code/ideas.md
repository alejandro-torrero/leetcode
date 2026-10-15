# First approeach

The goal is to get any possible combination of a binary number of n digits, with n =2 the possible combinations are

[0,1,3,2]
[00,01,11,10]

We always start by zero, then the follwing gnumber of two digits has to have one bit different, thats a AND operations

00 XOR 01 = 1

With the XOR operation we can calculate exactly a difference of one bit

First, we need to know how many numbers can be on the array while considering that it will start always on 0.

total_numbers = n^2 -1

So with n=2 the maximum number of elements in the array is 2^2 = 4, where one of them is 0, so the max number that we can have is 3

Similarly, with n =3

This first approeach is wrong

# Second approach

The relation is that when n =1 we have 2 posible values on the array

Then, with n =2 we have 4 possible values

And then with 3 bits we can have 8 values

Is a realtion of how many numbers can you build with n bits. So with n=3 we have 8 possible combinations

000
001
010
011
100
101
110
111

After that we need to obtain the next one bit different value, starting by zero. At every i element we flip one bit

So, with n = 2 and i = 0

First, add n bits to i so that it complies with the rule

So we have 000 by doing 0 >> 2

Then we need to have one bit fliped, but this being the elmenet 0 theres no need to flip anything

so append 0

When i = 1

i >> 2 =
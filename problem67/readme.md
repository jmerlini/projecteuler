# Maximum Path Sum

## Problem

Given a triangle in a .txt file, find the maximum total from top to bottom. Sums are found by starting at the top and adding to it either the left child or right child and so on, until you reach the bottom.

## Example

In the following triangle, by starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

<pre>
   3
  7 4
 2 4 6
8 5 9 3</pre>

That is, 3 + 7 + 4 + 9 = 23.

**Note:** 3 + 7 + 6 + 9 is invalid since 6 is not a child of 7.

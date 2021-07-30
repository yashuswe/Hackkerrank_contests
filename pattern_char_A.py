'''Write a program to print the pattern of alphabate 'A' using symbol '*'. The middle line and height vary with user values.

check the sample test cases for more clarification

Input Format

integer value for height 
integer value for middle line position
Constraints

height > 0
position > 0
Output Format

pattern string
Sample Input 0

10
3
Sample Output 0

         *
        * *
       *****
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
*                 *
Sample Input 1

10
6
Sample Output 1

         *
        * *
       *   *
      *     *
     *       *
    ***********
   *           *
  *             *
 *               *
*                 *
Sample Input 2

5
3
Sample Output 2

    *
   * *
  *****
 *     *
*       *'''

#code by yashassvi:
h=int(input())
p=int(input())
for i in range(1,h+1):
    for j in range(h-i):
        print(" ",end="")
    for j in range(2*i-1):
        if (p == i):
            print("*",end="")
        elif (j==0 or j==(2*i-2)):
            print("*",end="")
        else:
            print(" ",end="")
    print(end="\n")
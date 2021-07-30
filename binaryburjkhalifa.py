'''Write the program to create building structure like the burj khaleefa with equivalent binary numbers

Input Format

input for the height(number of lines)

Constraints

0>=height and height<=500

Output Format

pattern with binary number

Sample Input 0

10
Sample Output 0

   0 
   1 
  10 
  11 
 100 
 101 
 110 
 111 
1000 
1001 
1010'''

#code
num=int(input())
l=len(bin(num))-2
for k in range(num+1):
    k=bin(k)[2:]
    p=len(k)
    print(' '*(l-p)+k)
    
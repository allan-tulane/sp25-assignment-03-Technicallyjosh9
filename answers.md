# CMPS 2200 Assignment 3
## Answers

**Name:**Joshua Haddad


Place all written answers from `assignment-03.md` here for easier grading.

1a) 
The bank gives a coin of the largest value that does not bring you over the total amount to be converted. Then calculate the amount you still need converted and repreat this process until the amount of money still needing converting is 0. At the end of this process you will end up with the smallest possible number of coins in your hand that add up to the same value.

1b)
Greedy Choice: In this algorithm we make a greedy choice of always choosing the coin of the largest denomination that does not go over the amount that needs to be converted. To prove that the optimal solution contains the largest denomination of coin that does not go over the amount that needs to be converted, we can take the largest denomination coin and split it up into two counts of smaller denominations, using the property that each coin is 2x larger than the next smallest coin. By using this property, we can see that by changing the largest coin into two smaller coins that add up to the same value, we now have two coins instead of one. Since our goal is to minimize the amount of coins, no solution that utilizes two smaller coins to add up to the same value as one larger coin can be optimal. Therefore, our greedy choice of choosing the coin of the largest denomination that does not go over is optimal.

Optimal Substructure Properties: In this algorithm we can see that we have an optimal substructure because, given a total value to be converted, T, our algorithm first subtracts 2^k, where 2^k is its highest value possible that is < T. After doing T - 2^k = T1, we are left with a value T1, which is the amount left to be converted. If the greedy algorithm provides the best solution, then T1 + 2^k = T also provides an optimal solution for T. Because this process can be repeated for each level, solving T1 and a coin of value 2^k is the optimal value to subtract by, we can see that adding up all the 2^ks used in this process would result in the optimal solution.


1c)
Work: W(n)= W(n/2) + 1  
At worst case number of money to be converted becomes nearly half of what it was and no parrallism occurs.
Root Dominated
W(n)= log(n)

Span:S(n)= S(n/2) + 1  
No parrallism occurs but problems gets nearly half as small each time therefor log(n).
S(n)= log(n)  


2a) Our algorithm does not work for the case in which the bank offers change in denominations of $5 $4 and $1. In the case where you are trying to convert $8 our greedy algorith would say you need 1 $5 coin and 3 $1 coins for a total of 3 coins. This is sub obtimal because if you were to use 2 $4 coins you could have 8 dollars converted with only two coins.

2b)
Optimal Substrucutre:
There exists an optial amount of coins to be handed out for every number to convert T. By creating a list of optimal coin values for every number <T you would have an optimal way of finding what T is. Because any T can be broken up into two numbers that are less than T and their optimal coin arrangments can be solved in similar way you know your solution has an optimal substructure.

2c)
def Convert(T,d):
  mem[T+1]
  mem[0] = 0
  for i in range T:
    for denominations(d) in range types of coins:
      if i - d >= 0: 
        a[i] = min(mem[i], 1 + mem[i-d]) 
  return mem[T]
  
Work: W(N)= W(N-1) +d
Loops through every number before N d times. We dont know how large d is but it would make sense for the bank to have a number of denominations that dose not scale linearly with price. Therefor
Work = W(N)

Span: S(N)= S(N-1) +1 
Function has to find minimimum for each number less than N
Span = S(N)
  In this function we loop through the outter for loop N times, and the inner for loop c times (once for each type of coins), so the work is O(N*C). We need to check the minimum value of each N value sequetially, so span is O(N)
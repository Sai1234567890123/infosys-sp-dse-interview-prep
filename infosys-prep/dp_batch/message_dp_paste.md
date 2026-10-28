i will provide 50 dp questions process like we did kumar k greedy 90 sheet like that after that i will provide 90 remaining total 140 dp questions the pattern question numberq format and question number end between is the content relate to question process it .  1q start   Education + Jobs Hiring Website - 2025© 2026 DesiQnA 2026
Desi QnA
About Us
Dynamic Programming
Tutorials
Compiler
Company-wise questions!
Hot
Tags
Categories
Dynamic-Programming | Desi QnA
Ask a question: PART 1 :
So, most of us have heard about this term “DP” a lot and have seen people in fear as soon as they listen to it.
I used to fear DP a lot too , but then I found the easiest way to master it :-)
I will share my way :-)
I will make you fall in love with this topic .
Important points:-

1. To be good at DP, all you have to do is solve classical DP-problems and their variations.
2. Recognize patterns and improve upon your thinking skills in DP.
3. Love DP, it will love you back !

There are many variations of DP and I’ll discuss them all one by one so you can become a pro!
Introduction to DP :-
To find solution to a problem, we divide the problem into sub-problems, find answers to those sub-problems , combine them to get the original answer!
That’s it!
Example:- Say I ask you to calculate :- (1+2+3+4+5) You do this:-
1)Break it into sub-problems : (1+2)+(3+4)+(5)

2. Find answers to those sub-problems: (3) + (7) + (5)
3. Combine them to get the answer to the original problem : 15.

That’s what we call dynamic programming !(Only keep this definition of dp in mind as a beginner , we will evolve it as we become pro in future tutorials) :-)
My personal trick :-
-->dp[i] usually mean the best answer to the problem till the i’th index of the array.
-->Obviously, final answer will be dp[n](where 'n' is the size of the array)
-->We cannot calculate dp[n] directly, we first need to calculate dp[1],dp[2],… and combine their results to find the value of dp[n] :-)
Problem-1 : We are given an array of integers(a[n]) . We are given multiple queries of the form : (1, i) which means we need to output the sum of all numbers from index- ‘1’ to index ‘i’ of the array.
Analysis : Running a loop for each query[O(N)] and finding the sum is a good idea but not very efficient as it takes O(N*Q) time.
Let us create a dp-array of size ‘n’.
-->dp[1]=sum of all numbers from (1,1)
-->dp[2]=sum of all numbers from (1,2)…
and so on.
Say, a[5]={4,5,3,2,1}…(assume 1-based-indexing here) So, dp[1]=4(pretty easy)…..(1)
dp[2]=4+5=9………(2)
dp[3]=4+5+3=12…..(3) and so on.
So, for any index ‘i’ ,
dp[i]=a[i]+dp[i-1],
Example:-
dp[3] = a[3] + dp[3–1] = a[3] + dp[2]= 3 + 9 =12 ….(which is same as equation…(3))
Piece of code(C++) :-
This took O(N) time!
Voila! We did it!
So, now for all the queries, all we gotta do is output the value of dp[i], which we have already pre-computed :-)
Time taken:- O(N+Q) [ O(N) for pre-computation, as we answered each query in O(1), total time taken was O(Q) ]
So you get the basic idea of DP is to make a recurrence relation ,and then run a loop ,and calculate(pre-compute) the values :-)
My aim is to start this series from a very beginner level and make you reach the advanced level :-)
Next ❯
Search
Categories
All categories
Job Opportunities(2,023)
TechNews(8)
Work Life Balance(22)
Interview-Experiences(676)
CTC (compensation details)(154)
Tutorials-Roadmap(42)
Contest(5)
Online Assessments(1,683)
Coding Resources(29)
DataScience|ML-AI(13)
Algorithms and Problems(50)
Company-wise-questions(20)
Beginners(14)
FAANG(33)
Advice/Suggestion/Opinion(66)
Competitive-Programming(38)
System Design(3)
Gate(3)
Service-based-companies(151)
Web-Development(15)
Fun and Memes(7)
Get best answers to any doubt/query/question related to programming , jobs, gate, internships and tech-companies. Feel free to ask a question and you will receive the best advice/suggestion related to anything you ask about software-engineering , development and programming problems .
Privacy PolicyTerms and ConditionsDisclosure(Legal Information)
Donut Theme with by Amiya Sahu
1 end.  2q start   Education + Jobs Hiring Website - 2025© 2026 DesiQnA 2026
Desi QnA
About Us
Dynamic Programming
Tutorials
Compiler
Company-wise questions!
Hot
Tags
Categories
Dynamic-Programming | Desi QnA
Ask a question: PART 1 :
So, most of us have heard about this term “DP” a lot and have seen people in fear as soon as they listen to it.
I used to fear DP a lot too , but then I found the easiest way to master it :-)
I will share my way :-)
I will make you fall in love with this topic .
Important points:-

1. To be good at DP, all you have to do is solve classical DP-problems and their variations.
2. Recognize patterns and improve upon your thinking skills in DP.
3. Love DP, it will love you back !

There are many variations of DP and I’ll discuss them all one by one so you can become a pro!
Introduction to DP :-
To find solution to a problem, we divide the problem into sub-problems, find answers to those sub-problems , combine them to get the original answer!
That’s it!
Example:- Say I ask you to calculate :- (1+2+3+4+5) You do this:-
1)Break it into sub-problems : (1+2)+(3+4)+(5)

2. Find answers to those sub-problems: (3) + (7) + (5)
3. Combine them to get the answer to the original problem : 15.

That’s what we call dynamic programming !(Only keep this definition of dp in mind as a beginner , we will evolve it as we become pro in future tutorials) :-)
My personal trick :-
-->dp[i] usually mean the best answer to the problem till the i’th index of the array.
-->Obviously, final answer will be dp[n](where 'n' is the size of the array)
-->We cannot calculate dp[n] directly, we first need to calculate dp[1],dp[2],… and combine their results to find the value of dp[n] :-)
Problem-1 : We are given an array of integers(a[n]) . We are given multiple queries of the form : (1, i) which means we need to output the sum of all numbers from index- ‘1’ to index ‘i’ of the array.
Analysis : Running a loop for each query[O(N)] and finding the sum is a good idea but not very efficient as it takes O(N*Q) time.
Let us create a dp-array of size ‘n’.
-->dp[1]=sum of all numbers from (1,1)
-->dp[2]=sum of all numbers from (1,2)…
and so on.
Say, a[5]={4,5,3,2,1}…(assume 1-based-indexing here) So, dp[1]=4(pretty easy)…..(1)
dp[2]=4+5=9………(2)
dp[3]=4+5+3=12…..(3) and so on.
So, for any index ‘i’ ,
dp[i]=a[i]+dp[i-1],
Example:-
dp[3] = a[3] + dp[3–1] = a[3] + dp[2]= 3 + 9 =12 ….(which is same as equation…(3))
Piece of code(C++) :-
This took O(N) time!
Voila! We did it!
So, now for all the queries, all we gotta do is output the value of dp[i], which we have already pre-computed :-)
Time taken:- O(N+Q) [ O(N) for pre-computation, as we answered each query in O(1), total time taken was O(Q) ]
So you get the basic idea of DP is to make a recurrence relation ,and then run a loop ,and calculate(pre-compute) the values :-)
My aim is to start this series from a very beginner level and make you reach the advanced level :-)
Next ❯
Search
Categories
All categories
Job Opportunities(2,023)
TechNews(8)
Work Life Balance(22)
Interview-Experiences(676)
CTC (compensation details)(154)
Tutorials-Roadmap(42)
Contest(5)
Online Assessments(1,683)
Coding Resources(29)
DataScience|ML-AI(13)
Algorithms and Problems(50)
Company-wise-questions(20)
Beginners(14)
FAANG(33)
Advice/Suggestion/Opinion(66)
Competitive-Programming(38)
System Design(3)
Gate(3)
Service-based-companies(151)
Web-Development(15)
Fun and Memes(7)
Get best answers to any doubt/query/question related to programming , jobs, gate, internships and tech-companies. Feel free to ask a question and you will receive the best advice/suggestion related to anything you ask about software-engineering , development and programming problems .
Privacy PolicyTerms and ConditionsDisclosure(Legal Information)
Donut Theme with by Amiya Sahu
u only write solution for this question 2 end.   3q start Education + Jobs Hiring Website - 2025© 2026 DesiQnA 2026 
Desi QnA
About Us
Dynamic Programming
Tutorials
Compiler
Company-wise questions!
Hot
Tags
Categories
Dynamic-Programming | Desi QnA | Set - 2
Ask a question:	
Part-{2} : 



Problem-{2}:- Understanding this problem and its solution properly will make a strong foundation for you in the DP world! (This worked for me :-) )

Here we go :   Given an array of integers(positive as well as negative) ,select some elements from this array(select a subset) such that:-

1. Sum of those elements is maximum(Sum of the subset is maximum) .

2. No two elements in the subset should be consecutive.

Example :- {2,4,6,7,8}

Answer:- {2+6+8=16}

Common Trick : We create a dp-array , and dp[i] means the maximum sum we could get till index-’i’ of the array.

For the above example,

dp[1] = 2 (2), [This is the best answer you could get if size of the array was one]

dp[2]= 4(4),[This is the best answer you could get if size of the array was two]

dp[3]=8(6+2),[This is the best answer you could get if size of the array was three]………lets call this equation-(1)…

dp[4]=11(7+4),[This is the best answer you could get if size of the array was four]

dp[5]=16(2+6+8),[[This is the best answer you could get if size of the array was five]

Now , the next thing that I am going to say, you gotta feel it deeply . If you are able to do it, you win!!

Say, I have calculated dp[1],dp[2] and dp[3] by pure observation. Now, I have to calculate dp[4].

So I have only 2 choices:-

Choice : i)Include the 4'th element , if I do this, I can’t include the 3rd element as consecutive elements are not allowed, so ,

--->dp[4]= a[4]+dp[2]…..(answer will be 4th element plus the best answer till index ‘2’ of the array)

Choice : ii)Exclude the 4th element, we don’t select it! So the previous answer is the current answer, we don’t change anything,

--->dp[4]=dp[3],

Final answer is the maximum of two choices :-> dp[4]=maximum(a[4]+dp[2],dp[3])

=maximum(7+4,8)

=maximum(11,8)

=11…..(verify this with equation…(1))

Voila, we did it !!!

So, the recurrence relation for this problem is, for any ‘i’ ,

--->dp[i]=max(a[i]+dp[i-2],dp[i-1])

We will calculate dp[i] for all ‘i’ from (1 to n) using the above formula.

And dp[n] will be the maximum possible sum for the whole array!!

Woohoo!!!!

Some C++ code:-

       //using 1-based-indexing.....
       //n-->size of input array
       //a[n+1]-->actual array.
       //dp[n+1]-->our dp1-array
       
       int dp[n+1]={0};
       //dp[1] and dp[2] are calculated by our observation.
       //they can also be called as base-cases.
       dp[1] = max(a[1],0);
       dp[2] = max(a[2],dp[1]);
       //running a loop from i = 3 to i = n 
       int i = 3 ; 
       while(i<=n){
           dp[i] = max ( a[i] + dp[i-2] , dp[i-1] ) ;
           i++;
       }
       
       cout<<dp[n]; 
       //dp[n] is the final answer for the whole array!
Next ❯





Search
Categories
All categories
Job Opportunities(2,023)
TechNews(8)
Work Life Balance(22)
Interview-Experiences(676)
CTC (compensation details)(154)
Tutorials-Roadmap(42)
Contest(5)
Online Assessments(1,683)
Coding Resources(29)
DataScience|ML-AI(13)
Algorithms and Problems(50)
Company-wise-questions(20)
Beginners(14)
FAANG(33)
Advice/Suggestion/Opinion(66)
Competitive-Programming(38)
System Design(3)
Gate(3)
Service-based-companies(151)
Web-Development(15)
Fun and Memes(7)
Get best answers to any doubt/query/question related to programming , jobs, gate, internships and tech-companies. Feel free to ask a question and you will receive the best advice/suggestion related to anything you ask about software-engineering , development and programming problems .

Privacy PolicyTerms and ConditionsDisclosure(Legal Information)
Donut Theme  with  by Amiya Sahu u only correct solution for this question 3 end. 4q start Education + Jobs Hiring Website - 2025© 2026 DesiQnA 2026 
Desi QnA
About Us
Dynamic Programming
Tutorials
Compiler
Company-wise questions!
Hot
Tags
Categories
Select maximum sum subset from the two arrays such that no two elements are consecutive.[Dynamic-Programming-Set-3]
Ask a question:	
Part-{3} : 

Aim of this series:- “ To make you fall in love with Dynamic Programming. To show you the actual beauty of this topic. To go from beginner level to master level.”

Some of the common tricks we have learned as of now :

-->1. Usually, we create a dp-array , and dp[i] means the maximum sum(best-answer) we could get till index-’i’ of the array.

-->2. We need to find a recurrence relation, in simple words, we need to create a formula for dp[i] in terms of

dp[i-1],dp[i-2],….etc…

3. We run a for loop, which calculates dp[1],dp[2]…..and finally dp[n].

4. dp[n] means the answer for the whole array.

Last time, we discussed this problem :-

Given an array of integers(positive as well as negative) ,select some elements from this array(select a subset) such that:-

1. Sum of those elements is maximum(Sum of the subset is maximum).

2. No two elements in the subset should be consecutive.

Example :- {2,4,6,7,8}

Answer:- {2+6+8=16}

Now, let's solve a harder variation of this problem, which will make our understanding strong.

Modified Version : We are given ‘2’ arrays . Select some elements from both of these arrays (select a subset) such that:-

--->1. Sum of those elements is maximum(Sum of the subset is maximum).

--->2. No 2 elements in the subset should be consecutive.(Note:-If you select, say the 5th element from Array-1, then you are not allowed to select 4th element from either Array-1 or Array-2 nor are you allowed to select the 5th element from Array -2 all of them are considered consecutive :-) )

Example:->

Array 1(a1) : {1,5,3,21234}

Array 2(a2) : {-4509,200,3,40}

Answer:- (200+21234=21434)

Common Trick : We create a dp-array , and dp[i] means the maximum sum we could get till index-’i’ of both the arrays in this case.

For the above example,

dp[1] = 1(1) , [This is the best answer you could get if size of both the arrays was one]

dp[2]= 200(200),[This is the best answer you could get if size of both the arrays was two]

dp[3]=200(200), [This is the best answer you could get if size of the arrays was three]………lets call this equation-(1)…

dp[4]=21434(200+21234), [This is the best answer you could get if size of both the arrays was four]

Say, I have calculated dp[1], dp[2] and dp[3] by pure observation. Now, I have to calculate dp[4].

So I have only two choices:-

--->i)Include the 4'th element (of either array-1 or array-2, if I do this, I can’t include the 3rd element(from both the arrays) as consecutive elements are not allowed, so,

dp[4]= (max(a1[4],a2[4])) + dp[2])…..(answer will be 4th element plus the best answer till index ‘2’ of the arrays)

--->ii)Exclude the 4th element, we don’t select it! So the previous answer is the current answer, we don’t change anything,

dp[4]=dp[3],

Final answer is the maximum of two choices :---> dp[4]=maximum(max(a1[4],a2[4])+dp[2],dp[3]) =maximum(max(40,21234)+200,200)

=maximum(21234+200,200)

=maximum(21434,200)

=21434…..(verify this with equation…(1))

Voila, we did it !!!

So,the recurrence relation for this problem is, for any ‘i’ ,

dp[i]=max( max(a1[i],a2[i]) +dp[i-2],dp[i-1]) 

Some C++ code:-

//dp[1] and dp[2] are calculated by observation. //we run a loop from i=3 to i=n , dp[n] is the //final answer. 
//a1[] is the first array and a2[] is the second array
//size of both the arrays is 'n'
i=3;
while(i≤n){
dp[i]=max( max(a1[i],a2[i])+dp[i-2],dp[i-1]); i++;
}

cout<<dp[n];
Next ❯





Search
Categories
All categories
Job Opportunities(2,023)
TechNews(8)
Work Life Balance(22)
Interview-Experiences(676)
CTC (compensation details)(154)
Tutorials-Roadmap(42)
Contest(5)
Online Assessments(1,683)
Coding Resources(29)
DataScience|ML-AI(13)
Algorithms and Problems(50)
Company-wise-questions(20)
Beginners(14)
FAANG(33)
Advice/Suggestion/Opinion(66)
Competitive-Programming(38)
System Design(3)
Gate(3)
Service-based-companies(151)
Web-Development(15)
Fun and Memes(7)
Get best answers to any doubt/query/question related to programming , jobs, gate, internships and tech-companies. Feel free to ask a question and you will receive the best advice/suggestion related to anything you ask about software-engineering , development and programming problems .

Privacy PolicyTerms and ConditionsDisclosure(Legal Information)
Donut Theme  with  by Amiya Sahu
 u only write solution for this question 4 end. 5q  start  amazon oa Link-> https://www.desiqna.in/15983/amazon-summer-school-sep-2023-minimum-cost-reach-destination (Watch the video for the question pic) -> https://drive.google.com/file/d/1R8LNThwqvOZRUK47E1V0s6U1zaDVwwUM/view?usp=sharing 



PseudoCode.-> https://ideone.com/cCStp1 


C++ https://ideone.com/eoCHX7 
Java. https://ideone.com/Szh6bR 
Py https://ideone.com/xkhWiS. 

1. #include <iostream>
2. #include <vector>
3.  
4. using namespace std;
5.  
6. int main() {
7. int n;
8. cin >> n;
9.     vector<int> cost(n + 1);
10.     vector<int> dp(n + 1, 0);
11.  
12. for (int i = 1; i <= n; ++i) {
13. cin >> cost[i];
14. }
15.  
16.     dp[1] = 0;
17.     dp[2] = abs(cost[2] - cost[1]);
18. cout<<dp[2]<<'\n';
19.     dp[3] = dp[2] + abs(cost[2]-cost[3]);
20. cout<<dp[3]<<'\n';
21. for (int i = 4; i <= n; ++i) {
22.         dp[i] = min(abs(cost[i] - cost[i - 1]) + dp[i - 1], abs(cost[i] - cost[i - 3]) + dp[i - 3]);
23. cout<<dp[i];
24. cout<<'\n';
25. }
26.  
27. cout << dp[n] << endl;
28. return 0;
29. }   5 end. 6q start 

1-2 questions images to related to 6 question read content in it 
Paypal OA :-> Find the largest valid substring - Valid string is a string where adjacent pair of char have diff<=k  

-> dp[i] = largest valid substring ending at index “i” 

-> if(abs(s[i-1]-s[i])<=k){
    -> dp[i] = 1 + dp[i-1]
}else{
    -> dp[i] = 1 
}

-> Max(dp[1],dp[2],dp[3],..................dp[n])
-> once you know the max value find the smallest index “i” such that dp[i] = max; and from there print the string 

C++ https://ideone.com/GjcWIu 
Java. https://ideone.com/PhWlRX.  
Py https://ideone.com/h2gnlv  6 end. 7q start 
Contest Duration: [2019-01-06(Sun) 16:30](http://www.timeanddate.com/worldclock/fixedtime.html?iso=20190106T2000&p1=248) - [2019-01-06(Sun) 21:30](http://www.timeanddate.com/worldclock/fixedtime.html?iso=20190107T0100&p1=248) (local time) (300 minutes)
   * [Top](https://atcoder.jp/contests/dp)
   * [Tasks](https://atcoder.jp/contests/dp/tasks)
   * [Clarifications](https://atcoder.jp/contests/dp/clarifications)
   * [Results](https://atcoder.jp/contests/dp/tasks/dp_a#)
   * [Standings](https://atcoder.jp/contests/dp/standings)
   * [Editorial](https://atcoder.jp/contests/dp/editorial)
   * 
A - Frog 1 /
Time Limit: 2 sec / Memory Limit: 1024 MiB
Score : 100 points
Problem Statement
There are N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is hi.
There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:
   * If the frog is currently on Stone i, jump to Stone i+1 or Stone i+2. Here, a cost of ∣hi−hj∣ is incurred, where j is the stone to land on.
Find the minimum possible total cost incurred before the frog reaches Stone N.
Constraints
   * All values in input are integers.
   * 2≤N≤105
   * 1≤hi≤104
Input
Input is given from Standard Input in the following format:

```
N
h1 h2 … hN

```

Output
Print the minimum possible total cost incurred.
Sample Input 1
Copy

```
4
10 30 40 20

```

Sample Output 1
Copy

```
30

```

If we follow the path 1 → 2 → 4, the total cost incurred would be ∣10−30∣+∣30−20∣=30.
Sample Input 2
Copy

```
2
10 10

```

Sample Output 2
Copy

```
0

```

If we follow the path 1 → 2, the total cost incurred would be ∣10−10∣=0.
Sample Input 3
Copy

```
6
30 10 60 10 60 50

```

Sample Output 3
Copy

```
40

```

If we follow the path 1 → 3 → 5 → 6, the total cost incurred would be ∣30−60∣+∣60−60∣+∣60−50∣=40.
[Facebook](https://atcoder.jp/#facebook)[Twitter](https://atcoder.jp/#twitter)[Telegram](https://atcoder.jp/#telegram)[Share](https://www.addtoany.com/share#url=https%3A%2F%2Fatcoder.jp%2Fcontests%2Fdp%2Ftasks%2Fdp_a%3Flang%3Den&title=A%20-%20Frog%201)
   * [Rule](https://atcoder.jp/contests/dp/rules)
   * [Glossary](https://atcoder.jp/contests/dp/glossary)
   * [Terms of Use](https://atcoder.jp/tos)
   * [Privacy Policy](https://atcoder.jp/privacy)
   * [Information Protection Policy](https://atcoder.jp/personal)
   * [Company](https://atcoder.jp/company)
   * [FAQ](https://atcoder.jp/faq)
   * [Contact](https://atcoder.jp/contact)
Copyright Since 2012 ©[AtCoder Inc.](http://atcoder.co.jp/) All rights reserved.  
Contest Duration: [2019-01-06(Sun) 16:30](http://www.timeanddate.com/worldclock/fixedtime.html?iso=20190106T2000&p1=248) - [2019-01-06(Sun) 21:30](http://www.timeanddate.com/worldclock/fixedtime.html?iso=20190107T0100&p1=248) (local time) (300 minutes)
   * [Top](https://atcoder.jp/contests/dp)
   * [Tasks](https://atcoder.jp/contests/dp/tasks)
   * [Clarifications](https://atcoder.jp/contests/dp/clarifications)
   * [Results](https://atcoder.jp/contests/dp/tasks/dp_b#)
   * [Standings](https://atcoder.jp/contests/dp/standings)
   * [Editorial](https://atcoder.jp/contests/dp/editorial)
   * 
B - Frog 2 /
Time Limit: 2 sec / Memory Limit: 1024 MiB
Score : 100 points
Problem Statement
There are N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is hi.
There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:
   * If the frog is currently on Stone i, jump to one of the following: Stone i+1,i+2,…,i+K. Here, a cost of ∣hi−hj∣ is incurred, where j is the stone to land on.
Find the minimum possible total cost incurred before the frog reaches Stone N.
Constraints
   * All values in input are integers.
   * 2≤N≤105
   * 1≤K≤100
   * 1≤hi≤104
Input
Input is given from Standard Input in the following format:

```
N K
h1 h2 … hN

```

Output
Print the minimum possible total cost incurred.
Sample Input 1
Copy

```
5 3
10 30 40 50 20

```

Sample Output 1
Copy

```
30

```

If we follow the path 1 → 2 → 5, the total cost incurred would be ∣10−30∣+∣30−20∣=30.
Sample Input 2
Copy

```
3 1
10 20 10

```

Sample Output 2
Copy

```
20

```

If we follow the path 1 → 2 → 3, the total cost incurred would be ∣10−20∣+∣20−10∣=20.
Sample Input 3
Copy

```
2 100
10 10

```

Sample Output 3
Copy

```
0

```

If we follow the path 1 → 2, the total cost incurred would be ∣10−10∣=0.
Sample Input 4
Copy

```
10 4
40 10 20 70 80 10 20 70 80 60

```

Sample Output 4
Copy

```
40

```

If we follow the path 1 → 4 → 8 → 10, the total cost incurred would be ∣40−70∣+∣70−70∣+∣70−60∣=40.
[Facebook](https://atcoder.jp/#facebook)[Twitter](https://atcoder.jp/#twitter)[Telegram](https://atcoder.jp/#telegram)[Share](https://www.addtoany.com/share#url=https%3A%2F%2Fatcoder.jp%2Fcontests%2Fdp%2Ftasks%2Fdp_b%3Flang%3Den&title=B%20-%20Frog%202)
   * [Rule](https://atcoder.jp/contests/dp/rules)
   * [Glossary](https://atcoder.jp/contests/dp/glossary)
   * [Terms of Use](https://atcoder.jp/tos)
   * [Privacy Policy](https://atcoder.jp/privacy)
   * [Information Protection Policy](https://atcoder.jp/personal)
   * [Company](https://atcoder.jp/company)
   * [FAQ](https://atcoder.jp/faq)
   * [Contact](https://atcoder.jp/contact)
Copyright Since 2012 ©[AtCoder Inc.](http://atcoder.co.jp/) All rights reserved.  Link to the P1 https://atcoder.jp/contests/dp/tasks/dp_a 

Understanding :-> You are standing at index 1 of the array. You have to reach the last index N of the array in minimum cost ; you can only make 1 step or 2 step jumps. If you are jumping from index i to index j cost will be-> abs(b[i] - b[j]) 

General Way :-> 
->First we declare empty dp[N] 

-> We assume dp[i] is the best answer to the question if size of the array is “i” 

-> Always try to calculate the dp[1] ; dp[2] ; dp[3] ; dp[4]  by yourself ; this will make you realise the pattern and you will be able to make the formula yourself 

-> Then we try to create the formula.

-> We put the formula in the for loop and calculate dp[1] , dp[2] , dp[3] , dp[4] ….. dp[n] 

-> Generally dp[n] will be the final answer 
[10 500 20 80]
Dp[1] = minimum cost to reach the index1. = 0 
Dp[2] = minimum cost to reach the index2. = 490
Dp[3] = best cost to reach index3 from index 1. = 10
Dp[4] = abs(b[3]-b[4]) + dp[3] )    o1 (3→4) -> direct jump
= abs(b[2]-b[4]) + dp[2] o2(2—>4) -> direct jump
Answer will be the minimum of these two. 

Dp[4] = min(abs(b[3]-b[4]) + dp[3] , abs(b[2]-b[4]) + dp[2]) 

General formula->

Dp[i] = min(abs(b[i-1]-b[i]) + dp[i-1] , abs(b[i-2]-b[i]) + dp[i-2]) 

Using this formula calculate dp[1]...dp[2]....dp[3].....dp[n]

-> dp[n] = final answer to reach the index n in minimum cost 


Pseudo Code : - https://ideone.com/mNiVpL 
TC :- O(N)
SC :- O(N) (dp[n]) 

C++ -> https://atcoder.jp/contests/dp/submissions/42276696 
Java -> https://atcoder.jp/contests/dp/submissions/42290564 
Python-> https://atcoder.jp/contests/dp/submissions/42290680 


P2 :-> 
C++ -> https://atcoder.jp/contests/dp/submissions/42277272 
Jv-> https://atcoder.jp/contests/dp/submissions/42294397 
Py-> 
 -> https://atcoder.jp/contests/dp/tasks/dp_b 



Understanding of Q2 :-> Same as above ; but you can make a jump of maximum “K” size. 

Dp[i] = (i-1—->i)
OR
(i-2—->i)
OR
(i-3—->i)
OR
(i-4—->i)
OR
.
.
.
(i-k—-->i)



Pseudo Code-> https://ideone.com/XGv9SK 
TC : - O(N*K)
SC:- O(N) (DP[])  #include <bits/stdc++.h>

using namespace std;
typedef long long int ll ; 

int main() {
    ll n ; 
    cin>>n ; ll b[n+1] = {0};
    ll i = 1 ; 
    while(i<=n){
        cin>>b[i] ; 
        i++;
    }
    
    
    ll dp[n+1] = {0};
    
    dp[1] = 0 ; 
    dp[2] = abs(b[1]-b[2]);
    i = 3 ; 
    while(i<=n){
        
        dp[i] = min(dp[i-1] + abs(b[i]-b[i-1]) ,dp[i-2] + abs(b[i]-b[i-2]));
        
        i++;
    }
    
    cout<<dp[n] ; 
    
    return 0 ; 
}   #include <bits/stdc++.h>

using namespace std;
typedef long long int ll ; 

int main() {
    ll n ; 
    cin>>n ; ll k; cin>>k ; 
    ll b[n+1] = {0};
    ll i = 1 ; 
    while(i<=n){
        cin>>b[i] ; 
        i++;
    }
    
    
    ll dp[n+1] = {0};
    
    dp[1] = 0 ; 
    dp[2] = abs(b[1]-b[2]);
    //cout<<dp[1]<<"\n";
    //cout<<dp[2]<<"\n";
    i = 3 ; 
    while(i<=n){
        
        ll answer = 1e18 ; 
        ll j = 1 ; 
        while(j<=k && i-j>=1){
            ll yy = dp[i-j] + abs(b[i]-b[i-j]);
            //cout<<yy<<"\n";
            answer = min(answer,yy);
            j++;
        }
        dp[i] = answer ; 
        //cout<<dp[i]<<" ";cout<<'\n';
        i++;
    }
    
    cout<<dp[n] ; 
    
    return 0 ; 
}  7 end. 8q start 
google swe oa

Problem :- You are given an array of size “N” ; you have to start your journey at index “1” and you need to end your journey at index “N”. 

You can make jumps of size -> 1 or 3 or 5 

In the array positive as well as negative numbers can be available. 

Please find the maximum sum of journey 

[5 8 3 100 -5 -5 5 10] 

O/P - 131 

-> dp[] of size “N” 

-> dp[i] = best answer to the question till index “i” - best answer of the journey if journey is starting at index 1 and ending at index “i”

-> Try to find the formula. 

-> Put the formula in the for loop 

-> Analyze all the dp values; most probably dp[n] will be the final answer 

dp[i] = max(dp[i-1] + b[i] , dp[i-3] + b[i] , dp[i-5] + b[i])

dp[n] will be the final answer which tells you the maximum cost to reach index “n”. 

Algorithm:- https://ideone.com/3sX5JJ.

C++ - https://onecompiler.com/cpp/42aqnwnm7
Java - https://onecompiler.com/java/42aqp8kz7
Py - https://onecompiler.com/python/42aqp9pgm

TC - O(N)
space.-> O(N)	 #include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    int b[n + 1]={0}; // Assuming b is already initialized
    
    int dp[n + 1]={0};
    
    for(int i=1;i<=n;i++){
      cin>>b[i];
    }
    
    dp[1] = b[1];
    dp[2] = b[1] + b[2];
    dp[3] = b[1] + b[2] + b[3];
    dp[4] = max(dp[1] + b[4], max(dp[2] + b[4], dp[3] + b[4]));
    dp[5] = max(dp[4] + b[5], dp[2] + b[5]);
    
    for (int i = 6; i <= n; i++) {
        dp[i] = max(dp[i - 1] + b[i], max(dp[i - 3] + b[i], dp[i - 5] + b[i]));
    }
    
    cout << dp[n] << endl;
    
    return 0;
} 8 end. 9q start  infosys oa -> Given an array of size “N” and integer “K” 
-> You start at index “0” and you have to reach at index “N-1” by doing some esoteric jumps 
-> You can jump from i to j as long as i < j <= i+K 
-> Whenever you jump from i → j -> cost is a[i]*a[j] 

Pre-requisite :- https://videsiqna.in/ -> do DP part of it :) 
Concept :- 
-> dp[] 
-> dp[i] = best way to go from index 0 to index i in minimum cost 

Analysis :- You can make a jump of size at-most K 

-> C++ Code Link - https://www.jdoodle.com/ia/1RRp 
-> Java - https://ideone.com/JGw8Fv 
-> Py - https://ideone.com/yYdpHc   
[00:01] So hello guys, with the name of God, Ramram.[00:02] This problem was asked, and this is the image of the problem: You are given an array of $n$ integers. You start at index 0, you have to do some jumps, and you have to reach $n - 1$.[00:14] This is a standard one-dimensional dynamic programming problem. You can jump from $i$ to $j$ as long as $j$ is at the distance of $k$ from $i$. Okay.[00:25] And whenever you make a jump, the cost of doing that is the multiplication of the two values at those indices: $A[i] \times A[j]$. Find the minimum total cost to reach the destination.[00:35] For example, if I try to show you a test case from 0... Okay, wait, wait, wait, wait. Okay, let's take this test case, right? You can make jumps of size 3 here. The optimal path is 0 to 1, 1 to 2, 2 to 3, 3 to 4.[00:58] So guys, see, this is index 0, index 1, index 2, index 3, index 4. If your path is 0 to 1, 1 to 2, 2 to 3, 3 to 4, what will be the cost?[01:09] When you go from 0 to 1, $-2 \times 5$ will be $-10$. When you go from 1 to 2, $5 \times -3 = -15$... like this, you can see what is happening, right?[01:23] That does not mean that this is only the best possible path. There could be other paths, but in this test case, this is the best path giving the minimum sum. So, minimum sum can be negative as well; you need to be careful.[01:40] $N$ is less than or equal to $10^5$, and $k$ is less than or equal to 100, which gives us a hint that we can do an $O(N \times K)$ DP.[01:43] Okay, but before I start that thing, I need to make it clear that the prerequisite you need to complete is the DP part of this. So don't worry, prerequisite is nothing but do the DP part of it.[02:03] Guys, please know, always pay attention when I'm teaching DP. Do you know this whole program started a few years ago? Why did people start calling me, messaging me, contacting me for guidance and training and all that? Because I launched these 5 to 10 DP videos five years ago on YouTube and on my written tutorials. And I'm the person who taught DP in a totally different fashion, and that's why I got popular initially.[02:31] So my DP is really good. Like, I'm not talking about exactly my DP—my way of teaching DP is really good. So trust me and listen to me.[02:66] So let me open the interactive Jamboard now. Okay, so obviously I don't want to tell you the answer to the question. I don't want to spoil it for you, so let me try to think through.[02:72] Guys, whenever we have to solve a question through DP, what do we do? What we generally do is that we create a DP array like this, right? An empty DP array like this: index 0 to $n - 1$.[03:12] Then we define the meaning of `dp[i]`. So guys, in our question, what should be the meaning of `dp[i]`? The meaning of `dp[i]` should be the best answer to complete your journey and go from index 0 to index $i$ by following all the rules. Basically, what is the minimum possible cost to go from index 0 and reach index $i$ by following all the rules? It is denoted as `dp[i]`.[03:46] Final answer will be what? `dp[n - 1]`, right?[03:50] So currently, as I'm writing, please understand it with me. We just declare this dynamic programming array. Everything going great for us, nice.[04:06] `dp[i]` means what? Best way to go from index 0 to index $i$ in minimum cost. Whatever is that minimum cost, it is stored in `dp[i]`.[04:20] What will be the final answer? First, you will calculate `dp[0]`, then `dp[1]`, `dp[2]`, `dp[3]`, `4`, `5`, `6`, up to `dp[n - 1]`. Why is `dp[n - 1]` the final answer? Because `dp[n - 1]` tells you the best way to go from 0 to $n - 1$, following all the rules in minimum cost. And that is what the question is asking, right? Start at 0, reach at $n - 1$ by following all these rules.[04:46] We can look into the rules later, but we can define the dynamic programming of $i$ right now. Okay, so everything is going great, right?[04:58] By the way, I really love each one of you. Now listen: "I really love you." This statement I have told to you people is very special, because I did not even say this statement to her, but I'm telling it to you. It means you're really special.[05:35] Anyways, now listen, guys, listen. So guys, let's make some array and let's try to enjoy life. So yeah, let me say your jump value is... you are allowed to make a maximum jump of size 2. Okay, don't worry, ignore the "her" concept. Focus on the question, that was just a joke.[06:00] Now listen: 6, 7, 8... Let's say 5, 2, 10, -20. Okay.[06:25] What is `dp[1]`? I will not say anything. Everyone open your WhatsApp groups and tell me what is the meaning of `dp[1]`. Now I will test you whether you have the knowledge or not. `dp[1]`—I don't want the answer of `dp[1]`, I want you to define it in an English sentence. What is the meaning of `dp[1]` for this question? What is the meaning of `dp[1]` for this question?[07:06] So Akhila and Ajay, yeah, please write: `dp[1]` means the best way to go from index 0 to index 1. Akhila, you also have to write, and Rohit, you also have to write. What is the meaning of `dp[1]`? Best way to go from index 0 to index 1. Definition is more important than the actual answer, okay? You guys understand that? Yeah, good, good, good. Minimum possible cost to move from index 0 to 1.[07:38] But Akhila, I don't see you writing the answer. Akhila, you need to write it. Okay, do something, Akhila, you need to get active. You are in a live program, 101% attention on you.[07:53] Anyways, answer: So guys, what is the best way to go from 0 to 1? This is the best way. So what is the cost? Whenever you go from index $i$ to index $j$, the cost is what? $A[i] \times A[j]$. So $5 \times 2$... what is `dp[1]`? `dp[1]` is 10. It takes 10 rupees to go from our lovely index 0 to index 1.[08:25] Now, let's try to calculate `dp[2]`. What is the meaning of `dp[2]`? The best way to go from 0 to 2.[08:39] So guys, if you want to go from 0 to 2, just investigate what are the ways. Can you guys write in WhatsApp chats? What are the multiple ways to go from 0 to 2? `dp[2]` means what? Figure out the best way to go from index 0 to index 2.[08:57] So which ways are possible? One way is: first you go from 0 to 1, then you go from 1 to 2. Another way is you directly go from 0 to 2.[09:16] So these are the ways you see, right? What is the cost of the first way? 0 to 1 is $5 \times 2 = 10$, plus when you go from 1 to 2, $2 \times 10 = 20$. It costs you 30 rupees.[09:34] The other way, if you directly make a jump from 0 to 2: you can make a 2-size jump because the $k$ value is 2. You can make a jump of size at most $k$, because $j \le i + k$. You can make a jump of at most size $k$.[19:59] I know it is easy for you, but still I want to make you feel that, see, there are doable questions existing in this universe. Okay, so if you go from 0 to 2, it is what? $5 \times 10$. Oh, shocker, shocker, shocker: 50![10:25] Guys, you want the minimum possible cost. Will you go with 30 or 50? Write the answer in the pro group. `dp[2]`: will you declare it as 30 or will you declare it as 50? Akhila, Ankit, Ajay, Tiwari, Rohit...[10:39] There are two ways for `dp[2]`: one way costs you 50 rupees, another way costs you 30 rupees. Which way will you go through? 30, correct! 30.[10:53] Okay, okay, okay. You guys understand these things. I'm very happy about that, really very happy. Great job going, great job. Okay, good going, nice.[11:21] So yeah, now guys, we will calculate `dp[3]`. And this is the way I have taught in my dynamic programming course. While calculating `dp[3]`, we will try to figure out the formula now. Okay, so you only... everyone in the meeting just think with me here. Only in front of you, think with me. Like, you will also think, I will also think.[11:32] First of all, everyone in the pro group, start writing what is the meaning of `dp[3]`. Nothing else I want from you, just want you to write the meaning of `dp[3]`.[11:49] The meaning of `dp[3]` is the best way to go from index 0 to index 3. The best way to go from index 0 to index 3.[12:14] So guys, you only think: you want to reach 3, but you can reach 3 from which places? In the end, if you want to go from 0 to 3, just try to think what will be the last jump in this journey.[12:38] One possible last jump is what? That in the end, you jump from 2 to 3, right? So the one possible way is that the last jump you make is from 2 to 3.[12:59] If the last possible jump you have made is from 2 to 3, the cost will be what? $A[2] \times A[3]$ plus... let's say the last jump you made in your journey was from 2 to 3, so it costed you $A[2] \times A[3]$. But what is the best way to reach from 0 to 2? First, you need to reach from 0 to 2, then you will jump from 2 to 3, right? Yes, sir. So the best way to reach from 0 to 2 has already been pre-calculated—it is `dp[2]`.[12:71] So `dp[3]` is nothing but the jump from 2 to 3, which is $A[2] \times A[3]$, plus the best way to go from 0 to 2, which is `dp[2]`. This is one possible way.[13:44] What is another way? The last jump could have been from 1 to 3, right? It could happen that in your journey from 0 to 3, you made your last jump from 1 to 3. In that case, what would happen? $A[1] \times A[3]$ would be getting added to the cost. $A[1] \times A[3]$ plus... you jumped from 1 to 3, but you need to reach 1 also for that. So what is the best way to reach from 0 to 1? It is `dp[1]`, which has been pre-calculated.[14:14] Wow! Formula is that `dp[3]` is the minimum of these two options:
   * $A[2] \times A[3] + \text{dp}[2]$
   * $A[1] \times A[3] + \text{dp}[1]$
[14:27] Guys, there is one more option. The another option is you directly jump from 0 to 3. I will show it to you with a white color: 0 to 3.[14:47] But guys, tell me... write yes or no in the pro group. "Yes" means you consider that the jump from 0 to 3 is a valid option. And right now, if you guys think that directly jumping from 0 to 3 is invalid... Everyone start writing your answers, I want to see your inputs.[15:08] Yes, it is invalid. But why? Why? Why is it invalid? Akhila, why is it invalid? I want to know the answer. Everyone is writing "no, no", but no one is telling me why is it invalid.[15:26] Yeah, you guys are correct. It is invalid because... Mars Beta Pro 7... because the jumps can be made only of size $k$. You can only make 2-size jumps, okay? And here you are trying to make 3-sized jumps. Okay, so let me check Mars Beta Pro 3... okay. Mars Beta Pro 5... okay, good, nice, good, good, good.[15:58] And Akhila, you have to write the answer in the WhatsApp pro group. I see your inactivity, please know that you need to be active or else, you know, you get a penalty in the program. So write the answer in the WhatsApp pro group explaining why we are not able to directly jump from 0 to 3. The answer is very simple, and write the reason like other people have written in the pro group.[16:25] Now, each one of you guys, please listen to me very carefully now, okay? What is the current formula? The current formula is pretty simple: for `dp[3]`, you are just checking which are the last possible jumps and from that you are deducing the answer, right?[16:39] So `dp[3]` was what? `dp[3]` was:
   * $A[2] \times A[3] + \text{dp}[2]$
   * $A[1] \times A[3] + \text{dp}[1]$
[17:09] Replace 3 by $i$, and you will see a nice formula. `dp[i]` is what? Minimum of:
   * $A[i - 1] \times A[i] + \text{dp}[i - 1]$
   * $A[i - 2] \times A[i] + \text{dp}[i - 2]$
[17:48] Guys, we can extend this formula till how many expressions? $k$ expressions, because you only think now: if you are at index $i$, the last jump you can make is from $i - 1$ to $i$, or you can make the last jump from $i - 2$ to $i$, or you can make the last jump of this journey from $i - k$ to $i$.[18:20] These are the places from which you can make the jump. So if you're making the last jump from $i - 1$ to $i$, the formula is different ($F_1$). If you're making the jump from $i - 2$ to $i$, the formula is different ($F_2$). If you're making the jump from $i - k$ to $i$, the formula is different—let's call it $F_k$.[18:39] Guys, react with emojis and tell me: can you make a jump from $i - k - 1$ to $i$ in this question? React with emoji and tell me, can you jump from $i - k - 1$ to $i$? Can you do that? No.[18:86] So guys, let's start writing the code in front of you. Okay, let's start writing the code. What we will do? We will calculate `dp[1]`. No need to calculate `dp[0]` because the array will be of size greater than or equal to 2. Because if there is only one element, you start here, you end here. So in the question, it is not explained what happens when there is only one element. So you either handle it by looking at the output of the test cases or just assume that the array will be of size greater than or equal to 2 elements... $5 \times 5 = 25$ answer, which is not made clear in the question. So we are assuming that our array will have at least two elements. If it does not have, then also you can make a special case for $n = 1$ and you can try to see.[20:06] Huh, like this, you will calculate till `dp[n - 1]` using this formula. So let's try to do this procedure. So guys, I'm writing the code now in front of you people, and I want you to focus, and you also please start writing. React with emojis, guys, if you are also writing code with me. You need to write code because today's question is easy to make you feel good. So you have to write code with me as much as you can. Okay, all ready now? Okay, good, nice.[20:19] So let's start the procedure on JDoodle. Okay, yeah, you might be thinking why I'm not using any template, why I'm writing from `bits/stdc++.h`, right? Well, I have the habit—like, writing code gives me dopamine, so I like to write each and every line. Obviously, I don't do this thing while in the contest, I might do...[20:53] So guys, I'm showing you the C++ code, but the Java/Python one will be very similar, right? You take the integer $n$ input, and we have to take what? We have to take the list or array as the input, right, of size $n$, right? Okay, no problem. Yeah, let's take the input and let's try to enjoy the input.[21:25] So guys, everything is going great, we are taking the input, no one is having any problem. Now we have to define our DP array. Okay, now `dp[0]` though we don't know, guys, `dp[1]` we always know. Can everyone start writing in the... we assume that $k$ is greater than or equal to 1, so you can always jump from 0 to 1. What is `dp[1]`? I want everyone to write the answer in the pro groups, their respective pro groups.[22:00] Okay, Sonasha has finally become active today. Great job, Sonasha, did not know that. Great, great, great. So what is `dp[1]`? Sonasha, I need your answer. What is `dp[1]`? It is very simple. Use your full brain and write the answer in your pro group.[22:23] Okay, good. Sristhinad has written, and other people. Okay, Jan Pro guys, Sukinda Rashan is active. Rashan Adav, you should tag me also in your LinkedIn post like other students are doing. Okay, good.[22:39] So yeah, now we can start the further procedure. Everyone has written, right? They know these things. Oh, Akhila has finally written. By the way guys, there was one more student, I forgot to give him this... congratulations. Where is he? Let me check. This is the student, right?[22:78] Anyways, guys, please like the post of this student. I'm not able to... okay, I'm reposting it. Guys, he has crossed 1800 rating after months of training in the program. His name is Mridul Singh, and he is in this session also. So guys, please give him congratulations in the session and like his post, okay? He is in the session, most probably you can see here. Where is he? A, B, C, D, H, I, J, K, L, M... Ment. Great job.[23:52] Anyways, now let's start the procedure. So guys, this is an easy question, right? `dp[1]` is what... you know these things. Okay, you are strong at OA questions now. `dp[1]` = this. Now, yeah, yeah, yeah... what will be... let's try to write the formula. It's not hard, I know it's not hard for you.[24:09] Now guys, you have to calculate `dp[i]`, and there can be... see, this is index $i$, the last jump you can make from $j$ to $i$ if and only if $j$ is a number in the range from $i - 1$ to $i - k$. You want to know the best journey from 0 to $i$. In the best journey from 0 to $i$, the last jump you will make will be from index $j$ to $i$, and $j$ can be either $i - 1$, or $i - 2$, till $i - k$. So these are the possibilities for $j$.[25:11] So let's iterate all possible $j$. This is iterating the last jump which you can make to reach $i$. So it can be from $i - k$ till $i - 1$.[25:16] So what will be `dp[i]` in this case? It will be the best way to reach from 0 to $j$, which is `dp[j]`, plus $A[i] \times A[j]$.[25:20] And be very careful: never try to... like, whenever you're jumping from 0 to $j$, you need to declare a `dp[0]` as 0 only for some special cases so that no wrong cost gets added. Because if you are jumping from 0 to $i$, it should be $A[i] \times A[0]$ plus no extra cost, right? There is no cost to reach from 0 to 0, that's why.[25:28] But guys, `dp[i]` will have multiple possible values, you want the minimum of all of them. So minimum of `dp[i]` with all these possibilities. Done![26:03] So it's all going great, it's all going nice, and the problem is solved, right? I don't see any problem here. Yeah, what you will print here is `dp[n - 1]`, and it's done. I don't see any problem here, everything is going really great.[26:24] But there is still a problem which you guys... I don't think everyone has figured it out. Everything in this code is correct except one thing. I'm just staying silent, let's see who can figure it out. Don't use ChatGPT, use your own brain and see if there is any type of issue in the code. There is one very small issue.[26:52] So till now, no one has figured it out, what is the small mistake in this code. Yashasvi, correct! Like, somehow correct, not fully... exam pass.[27:13] Yes, guys! $j$ can be negative. Now you need to be careful, $i - k$ can be negative. You cannot jump from a negative index, negative index does not exist. So you will write $j$ equal to `max(0, i - k)` in case $i - k$ is negative, okay?[27:31] So yeah, `int u = 0;` and `max(u, i - k)`. And that's it, guys! The problem has been solved. Okay, yeah.[27:46] So if I try to see what test cases were there... Okay, it was 4, and then 2, 2, 1. Okay, and where is the $k$? Okay, 4, 2 and 2, 1, 3, 4... 4, 2, 2, 3...[28:09] 4, 2, 2, 1, 3, 4. Let's see what's happening.[28:26] Okay, $k$ was not... okay, okay, okay. Forgot to take $k$ as the input, sorry! Who will say that I did not take $k$ as the input, guys? How can you forget that I did not take $k$ as the input? The biggest thing you guys did not see... -6.[28:45] Okay guys, our code is working correctly. Give congratulation emojis! It is working correctly. Let's try this test case also: 5, 3, 2, 5...[28:99] 5, 3, 2, 5... -2, 5, 3, 6, 1, 3, 6, 1.[29:19] So hopefully this... like, everyone was able to understand whatever was going on today. I don't think it is hard for you, but it is a good addition to the DP course, right? -49.[29:32] And guys, here also it's -49. React with emojis if everyone understood everything and they are thoroughly convinced with the code, and they think they will be able to write it on their own as a homework. Today's question is easy to make you happy. You can do it now, pakka? Or you don't know this?[29:48] Ah, and okay, give me some confirmation in the Google Chat also. Did you guys understand what is happening here? Huh, if you did not understand, let me know, and if you understood, write "Yes sir, clear sir." And then I'm just putting board link, I will be uploading the Java/Python links also. Okay, so hopefully this is clear, so let's do the second one, right? Okay. 9 end. 10q start C - Vacation / 
Time Limit: 2 sec / Memory Limit: 1024 MiB
Score : 100 points
Problem Statement
Taro's summer vacation starts tomorrow, and he has decided to make plans for it now.
The vacation consists of N days. For each i (1≤i≤N), Taro will choose one of the following activities and do it on the i-th day:
   * A: Swim in the sea. Gain ai points of happiness.
   * B: Catch bugs in the mountains. Gain bi points of happiness.
   * C: Do homework at home. Gain ci points of happiness.
As Taro gets bored easily, he cannot do the same activities for two or more consecutive days.
Find the maximum possible total points of happiness that Taro gains.
Constraints
   * All values in input are integers.
   * 1≤N≤105
   * 1≤ai,bi,ci≤104
Input
Input is given from Standard Input in the following format:

```
N
a1 b1 c1
a2 b2 c2
:
aN bN cN

```

Output
Print the maximum possible total points of happiness that Taro gains.
Sample Input 1
Copy

```
3
10 40 70
20 50 80
30 60 90

```

Sample Output 1
Copy

```
210

```

If Taro does activities in the order C, B, C, he will gain 70+50+90=210 points of happiness.
Sample Input 2
Copy

```
1
100 10 1

```

Sample Output 2
Copy

```
100

```

Sample Input 3
Copy

```
7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1

```

Sample Output 3
Copy

```
46

```

Taro should do activities in the order C, A, B, A, C, B, A.  
int main() {
    
    ll n ; 
    cin>>n ; 
    ll a[n+1],b[n+1],c[n+1];
    
    ll i = 1 ; 
    while(i<=n){
        cin>>a[i]>>b[i]>>c[i];
        
        
        i++;
    }
    
    ll dpa[n+1]={0};
    ll dpb[n+1]={0};
    ll dpc[n+1]={0};
    
    dpa[1] = a[1];
    dpb[1] = b[1];
    dpc[1] = c[1];
    
    i = 2 ; 
    while(i<=n){
        
        dpa[i] = a[i] + max(dpb[i-1],dpc[i-1]);
        dpb[i] = b[i] + max(dpa[i-1],dpc[i-1]);
        dpc[i] = c[i] + max(dpa[i-1],dpb[i-1]);
        i++;
    }
    cout<<max(dpa[n],max(dpb[n],dpc[n]));
    return 0 ; 
}


 





 Page Top

30.  Link  https://atcoder.jp/contests/dp/tasks/dp_c 

Greedy vs DP :-> 

-> If a problem can be solved by the Greedy approach ; it means it is guaranteed ; that at each step ; you make a choice and that choice is the best possible for now as well as the future. Then you can solve this problem using the Greedy Method. 

-> If there are multiple choices at each step and it is not clear which choice can given you the better answer long term -> use DP 

Easier version of the Question :-> You are given three arrays a ; b ; c -> at each index you either select a[i] or b[i] or c[i] ; once you are done selecting n elements we want the sum of all elements to be maximum. 
Link https://ideone.com/kPNLiz 
This is a greedy solution-> Why? -> Self explanatory 


Hard Version.-> https://atcoder.jp/contests/dp/tasks/dp_c 

-> You cannot select a number from a particular array for more than 1 time consecutively -> You have to find the maximum sum of all the numbers -> can only be solved by DP-> because there are multiple choice and any choice you has not guarantee if the future will be great or final answer will be maximum. 

-> 3 arrays a b c hence we create 3 dp arrays dpa[] dpb[] dpc[] 


dpa[i] = best answer to the question if size of the array was ‘i’ and you selected a[i] at the ith index. 

dpb[i] = best answer to the question if size of array is i and selected b[i] at index i

dpc[i] = best answer to the question if size of array is i and selected c[i] at index i 

-> dpa[3] = a[3] + max(dpb[2],dpc[2]) 
Generalize ; substitute.-> i 

dpa[i] = a[i] + max(dpb[i-1],dpc[i-1])
dpb[i] = b[i] + max(dpc[i-1],dpa[i-1])



dpc[i] = c[i] + max(dpb[i-1],dpa[i-1]) ;

Put these in a for loop and your job is done. 

TC :- O(N).. 
SC:- O(N)...... 


C++  https://atcoder.jp/contests/dp/submissions/42299240 

Java https://atcoder.jp/contests/dp/submissions/42308712 
Py https://atcoder.jp/contests/dp/submissions/42308782 

New Question.-> Same as above ; but you are allowed to take a maximum of only 2 consecutive numbers ; not more than that->(3 numbers should not be consecutive.)

-> 2 consecutive are allowed; 
-> 3 consecutive are not allowed; 

-> dpa[1] = a[1] dpb[1] = b[1] dpc[1] = c[1] 

-> dpa[2] = a[2] + max(a[1],b[1],c[1]) 
-> dpb[2] = b[2] + max(a[1],b[1],c[1])
-> dpc[2] = c[2] + max(a[1],b[1],c[1]) 

-> dpa[3] = a[3] + max(dpb[2],dpc[2]) -> first 
               = OR a[3] + a[2] + max(dpb[1],dpc[1]) 



-> dpb[i] = max(b[i] + max(dpa[i-1],dpc[i-1]) , b[i] + b[i-1] +max(dpa[i-2],dpc[i-2])) 

C++ https://ideone.com/PKYS2S. 
Java. https://ideone.com/OaMxSE. 
Py https://ideone.com/4wC2i7.  


—-----------------------------------------------------------------

Hardest Version. -> https://www.youtube.com/watch?v=oAhlTS7U8GM&t=2s&ab_channel=KumarK%5BAmazon%5D . 





10 end. 11q start   google interview po Link to the question :-> https://www.desiqna.in/13822/google-dp-interview-question-jan-2023 
Find the number of journeys where you start from index 1 and end at index ‘n’ and the sum of every journey should be odd..

Allowed to make jumps of size 1 or 2 
5 4 2 6 

Number of odd sum journey : 
-> (5,2,6)
-> (5,4,2,6)
-> (5,4,6)

Number of even sum journey : 
-> Nothing 


2 3 5 8 10 

Evn sum journey 👍
//evn
    //2...3...5...8...10
    //2...3...5.....10

Odd sum journey : 

    
    //odd
    //2...5...10
    //2...3...8...10
    //2...5...8....10 





Dp[i][even] = number of even sum journey till index ‘i’
Dp[i][odd] = number of odd sum journey till index ‘i’




-> 
[1 2 3 4]

Dp[3][even] = dp[1][odd] + dp[2][odd] 

 



If a[i] is even …. 

Dp[i][eve] = dp[i-1][eve] + dp[i-2][even] 

Dp[i][odd] = dp[i-1][odd] + dp[i-2][odd] 


If a[i] is odd …..

Dp[i][even] = dp[i-1][odd] + dp[i-2][odd] 


Dp[i][odd] = dp[i-1][eve] + dp[i-2][eve] 
C++ https://ideone.com/kqxkFB 
Java https://ideone.com/f5sswM 
Py https://ideone.com/Yt6SLb 






Find the number of journeys where you start from index 1 and end at index ‘n’ and the sum of every journey should be odd/even..

Allowed to make jumps of size 1 or 2 or
3.

If a[i] is even …. 

Dp[i][even] = dp[i-1][even] + dp[i-2][even] + dp[i-3][even] 

Dp[i][odd] = dp[i-1][odd] + dp[i-2][odd] + dp[i-3][odd]


If a[i] is odd …..

Dp[i][even] = dp[i-1][odd] + dp[i-2][odd] + dp[i-3][odd]


Dp[i][odd] = dp[i-1][even] + dp[i-2][even] + dp[i-3][even]
 
C++ https://ideone.com/Zafite 
Java https://ideone.com/cEV9RN 
Py https://ideone.com/mDK3UE 


11 end. 12 q start  google sde3 oa Given an integer “N” ; find the minimum cost to reduce it to 1
The operations you can do are as follows.->

i) Reduce the number by 1 in “y” dollars; 

ii) Reduce the number by /7 in “x” dollars.(if number is divisible by 7)

iii) Reduce the number by /3 in “z” dollars;(if number is divisible by 3)

iv) Reduce the number by /5 in “b” dollars;(if number is divisible by 5) 

(1<=n<=100000)


Understanding :->

N = 15 

Y = 100 
X = 1 
Z = 500 
B = 10000000












C++ https://ideone.com/AkCp1q 
Java. https://ideone.com/Sj8bDQ 
Py https://ideone.com/Lldqtv 

```

```


```

```

1. #include <bits/stdc++.h>
2.  
3. using namespace std;
4. typedef long long int ll;
5.  
6. int main() {
7.  
8. int n; 
9. cin>>n; 
10. int y,x,z,b;
11. cin>>y>>x>>z>>b;
12.  
13. int dp[n+1]={0};
14.  
15.     dp[1] = 0 ; 
16.  
17. int i = 2 ; 
18. while(i<=n){
19. int v1 = dp[i-1] + y ; 
20. int v2 = 1e8;
21. int v3 = 1e8;
22. int v4 = 1e8;
23. if(i%7==0){
24.             v2 = dp[i/7] + x; 
25. }
26. if(i%3==0){
27.             v3 = dp[i/3] + z;
28. }
29. if(i%5==0){
30.             v4 = dp[i/5] + b;
31. }
32.  
33.         dp[i] = min(v1,min(v2,min(v3,v4)));
34.         i++;
35. }
36. cout<<dp[n];
37. return 0 ; 
38. }

Success [#stdin](https://ideone.com/AkCp1q#stdin)


12 end. 13q start uber oa  Given two arrays; a and b -> you can start at index 1 from any array and end your journey at index n on an array 

-> If you are at i you can can jump to i+1 on same array or different array 

-> -1000000000 <= a[i],b[i]<= 10000000000 

-> Please output total number of journeys which have even sum and total number of journeys which have odd sum; 

-> dpa_even_[1] = if number a[1] is even then answer is 1 else 0

-> dpa_even[2] = considering both array till index “2” and a[2] is forcefully selected when journey ends at index “2”; 

-> dpb_even[i] = 

-> dpa_odd[i] = 

-> dpb_odd[i] = number of journeys ending at b[i] whose sum is odd; 

-> Total even journeys = dp_a_even[n] + dp_b_even[n] 


-> if b[i] % 2 == 0 
-> dpb_even[i] = dpb_even[i-1] + dpa_even[i-1] 
-> if b[i] % 2 !=0 
-> dpb_even[i] = dpb_odd[i-1] + dpa_odd[i-1] 

-> Similarly make the formula for dpa_odd[],dpb_odd,dpa_even[]...

C++ https://ideone.com/UWpbIY 
Java. https://ideone.com/TgQJ2C 
Py https://www.jdoodle.com/ia/1Aup 

1. #include <bits/stdc++.h>
2. using namespace std;
3. typedef long long ll;
4.  
5. const int MOD = 1e9 + 7;
6.  
7. int main() {
8. int n;
9. cin >> n;
10.     vector<ll> a(n + 1), b(n + 1);
11.  
12. for (int i = 1; i <= n; i++) cin >> a[i];
13. for (int i = 1; i <= n; i++) cin >> b[i];
14.  
15.     vector<ll> dpa_even(n + 1, 0), dpa_odd(n + 1, 0);
16.     vector<ll> dpb_even(n + 1, 0), dpb_odd(n + 1, 0);
17.  
18. // Base Cases
19.     dpa_even[1] = (a[1] % 2 == 0);
20.     dpa_odd[1] = (a[1] % 2 != 0);
21.     dpb_even[1] = (b[1] % 2 == 0);
22.     dpb_odd[1] = (b[1] % 2 != 0);
23.  
24. for (int i = 2; i <= n; i++) {
25. if (a[i] % 2 == 0) {
26.             dpa_even[i] = dpa_even[i - 1] + dpb_even[i - 1];
27.             dpa_odd[i] = dpa_odd[i - 1] + dpb_odd[i - 1];
28. } else {
29.             dpa_even[i] = dpa_odd[i - 1] + dpb_odd[i - 1];
30.             dpa_odd[i] = dpa_even[i - 1] + dpb_even[i - 1];
31. }
32.  
33. if (b[i] % 2 == 0) {
34.             dpb_even[i] = dpb_even[i - 1] + dpa_even[i - 1];
35.             dpb_odd[i] = dpb_odd[i - 1] + dpa_odd[i - 1];
36. } else {
37.             dpb_even[i] = dpb_odd[i - 1] + dpa_odd[i - 1];
38.             dpb_odd[i] = dpb_even[i - 1] + dpa_even[i - 1];
39. }
40. }
41.  
42.     ll total_even = dpa_even[n] + dpb_even[n];
43.     ll total_odd = dpa_odd[n] + dpb_odd[n];
44.  
45. cout << "Even Journeys: " << total_even << endl;
46. cout << "Odd Journeys: " << total_odd << endl;
47.  
48. return 0;
49. }
50.  13 end. 14q start uber oa  You are given a positive integer 'N’. Your task is to find and return the minimum number of steps that 'N' has to take to get reduced to 1. 
You can perform any one of the following 3 steps:
1) Subtract 1 from it. (n = n - ­1) ,
2) If n is divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
3) If n is divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ).



Algorithm:- https://ideone.com/Mctn4Q.  

p1 = 1 + dp[i-1]

if(i%2==0){
p2 = 1 + dp[i/2]
}

if(i%3==0){
p3 = 1 + dp[i/3]
}

dp[i] = min(p1,min(p2,p3)) 

—--------------------------------------------------------------------

Reduce n to 1 
If the number is even you can divide it by 2. 
If the number is odd you can do +1 or -1 

C++ - https://ideone.com/4iHGKc
Java - https://ideone.com/AjNRMh
Py - https://ideone.com/pfNC8K
#include <bits/stdc++.h>
51.  
52. using namespace std;
53. typedef long long int ll;
54.  
55. int main() {
56.  
57. int n = 5;
58.  
59. int dp[n+1]={0};
60.  
61.     dp[1] = 0 ; 
62.  
63. int i = 2 ; 
64. while(i<=n){
65.  
66. if(i%2 == 0){
67.  
68.     		dp[i] = 1 + dp[i/2];
69.  
70. }
71.  
72. else{
73.  
74.     		dp[i] = min(1+dp[i-1], 2+dp[(i+1)/2]);
75.  
76. }
77.  
78.         i++;
79. }
80. cout<<dp[n];
81. return 0 ; 
82. }  14 end. 15q start google sde 3 oa

Kumar K student cracks Google & Amazon in Final Year of college - https://www.youtube.com/watch?v=o6_83S6GGMM 
Google Interview Question (Medium → Hard)
Pre-requisite :- https://videsiqna.in/ (DP part of it) 
Part 1: The Gallery Heist
You are an art thief planning to rob a row of museum galleries. Each gallery contains a painting worth a certain amount of money (which can be positive or negative—some art is worthless or costs you to remove). However, the galleries are protected by laser sensors: if you rob two adjacent galleries, the alarm triggers.
You want to maximize your total haul.
Task: Given an array of integers representing the value of each gallery, return the maximum sum you can rob without taking two adjacent galleries.

Understanding :- 
-> dp[i] = maximum non adjacent sum in the range [1….i] 
-> dp[1] = max(a[1],0) 
-> dp[2] = max({a[2],a[1],a[0]}) 
-> dp[i] = max(a[i] + dp[i-2],dp[i-1]) 
-> Final - answer :-> dp[n] 
C++ - https://ideone.com/tqV0TX 
Java - https://ideone.com/nrdNc6 
Py - https://ideone.com/cFLxdh 


Part 2: The Collector's Contract (Follow-up)
Now a mysterious collector offers you a bonus, but only if you rob exactly k galleries (no more, no less). The adjacency rule still applies.
Task: Given the same array and an integer k, return the maximum sum you can achieve by robbing exactly k non-adjacent galleries. If it's impossible to rob exactly k galleries under the adjacency constraint, indicate that properly.


Constraints (implied for both parts):

* The number of galleries n can be large (up to 10^4)
* Gallery values can be negative
* 0 <= k <= ceil(n/2) for Part 2

Understanding :- 
-> dp[i][j] = maximum non adjacent sum such that exactly j elements are selected in the range [1…..i] 

-> dp[1][0] = 0 
-> dp[1][1] = a[1] 
-> dp[2][0] = 0 
-> dp[2][1] = max(a[1],a[2]) 
-> dp[2][2] = -INF; 
-> dp[i][j] = max(a[i] + dp[i-2][j-1], dp[i-1][j]) 
Final answer :- dp[n][k] 

Logic :- https://www.jdoodle.com/ia/1Tla 
C++ - https://ideone.com/7sJJg9 
Java - 
Py - 
Part 3: The Negotiator (Follow-up 3)
You've made a deal with the museum security. They won't trigger the alarm if you rob adjacent galleries, but you must pay them a penalty of P for every pair of adjacent galleries you rob. You can now rob any set of galleries (adjacency allowed), but your net profit is:
Total profit = Sum of robbed gallery values - (P × number of adjacent robbed pairs)
You still need to rob exactly k galleries.
Task: Given the array, integer k, and penalty P, return the maximum net profit achievable. You can rob any k galleries (adjacent allowed) but pay P for each adjacent pair in your selection.

-> dp[i][j] = best way to select j elements from first i elements satisfying the required conditions(It is never guaranteed whether the ith element was selected or not)   

-> dp[i][j] = max(dp[i-1][j],a[i] + dp[i-2][j-1],a[i] + a[i-1] - P + dp[i-2][j-2]) 

-> But the third option of this formula is wrong because in the sum for “dp[i-2][j-2]” maybe the “i-2”th element is included -> in that case , i & i-1 & i-2 -> all 3 are adjacent -> but penalty has been counted only for i & i-1 but not for i-1 & i-2)
Hence we need to do this same question with 3D - DP instead(Necessity is the mother of invention!) 
-> dp[i][j][0] -> best answer such that the ith-element is not selected = max(dp[i-1][j][1],dp[i-1][j][0]) 

-> dp[i][j][1] -> best answer such that the ith-element is selected = max(a[i] + dp[i-1][j-1][0], P + a[i] + dp[i-1][j-1][1]) 
—------------------------------------------------------------------------------------------------------------------------------------
Part 4 : The Partner Heist (Simplified)
You and your partner are robbing a row of galleries. Each gallery contains a certain value (can be negative). Each gallery can be robbed by at most one person, or left alone.
Constraint: No person can rob two adjacent galleries (same thief's picks must be non-adjacent). However, you and your partner can rob adjacent galleries (one takes i, the other takes i+1 — that's allowed).
Task: Given an array of integer nums, return the maximum total sum you and your partner can achieve together.

Understanding :- 

-> dp[i][A] = best sum we can get as per the conditions required in the range [1…i] such that the ith element is selected by “A” 
-> dp[i][B] = best sum we can get as per the conditions required in the range [1…i] such that the ith element is selected by “B” 
-> dp[i][X] = best sum we can get as per the conditions required in the range [1…i] such that the ith element is selected by none of them 

-> dp[i][A] = nums[i] + max(dp[i-1][X],dp[i-1][B])
-> dp[i][B] = nums[i] + max(dp[i-1][X],dp[i-1][A])
-> dp[i][X] = max({dp[i-1][X],dp[i-1][A],dp[i-1][B]) 
—----------------------------------------------------------------------------------------
Part 5 - Coming Up 

1. #include <bits/stdc++.h>
2. using namespace std;
3. typedef long long int ll; 
4. int main(){
5. 	ll n;
6. cin>>n; 
7. 	vector <ll> a(n+1,0); 
8. for(ll i=1;i<=n;i++){
9. cin>>a[i];
10. }
11. 	vector <ll> dp(n+1,0); ll u = 0 ;
12. 	dp[1] = max(a[1],u);
13. 	dp[2] = max(dp[1],a[2]); 
14. for(ll i=3;i<=n;i++){
15. 		dp[i] = max(a[i] + dp[i-2],dp[i-1]); 
16. }
17. cout<<dp[n]; 
18.  
19.  
20.  
21. return 0; 
22. }
end. 15 end. 16q start goole sde 3 Kumar K student cracks Google & Amazon in Final Year of college - https://www.youtube.com/watch?v=o6_83S6GGMM 
Google Interview Question (Medium → Hard)
Pre-requisite :- https://videsiqna.in/ (DP part of it) 
Part 1: The Gallery Heist
You are an art thief planning to rob a row of museum galleries. Each gallery contains a painting worth a certain amount of money (which can be positive or negative—some art is worthless or costs you to remove). However, the galleries are protected by laser sensors: if you rob two adjacent galleries, the alarm triggers.
You want to maximize your total haul.
Task: Given an array of integers representing the value of each gallery, return the maximum sum you can rob without taking two adjacent galleries.

Understanding :- 
-> dp[i] = maximum non adjacent sum in the range [1….i] 
-> dp[1] = max(a[1],0) 
-> dp[2] = max({a[2],a[1],a[0]}) 
-> dp[i] = max(a[i] + dp[i-2],dp[i-1]) 
-> Final - answer :-> dp[n] 
C++ - https://ideone.com/tqV0TX 
Java - https://ideone.com/nrdNc6 
Py - https://ideone.com/cFLxdh 


Part 2: The Collector's Contract (Follow-up)
Now a mysterious collector offers you a bonus, but only if you rob exactly k galleries (no more, no less). The adjacency rule still applies.
Task: Given the same array and an integer k, return the maximum sum you can achieve by robbing exactly k non-adjacent galleries. If it's impossible to rob exactly k galleries under the adjacency constraint, indicate that properly.


Constraints (implied for both parts):

* The number of galleries n can be large (up to 10^4)
* Gallery values can be negative
* 0 <= k <= ceil(n/2) for Part 2

Understanding :- 
-> dp[i][j] = maximum non adjacent sum such that exactly j elements are selected in the range [1…..i] 

-> dp[1][0] = 0 
-> dp[1][1] = a[1] 
-> dp[2][0] = 0 
-> dp[2][1] = max(a[1],a[2]) 
-> dp[2][2] = -INF; 
-> dp[i][j] = max(a[i] + dp[i-2][j-1], dp[i-1][j]) 
Final answer :- dp[n][k] 

Logic :- https://www.jdoodle.com/ia/1Tla 
C++ - https://ideone.com/7sJJg9 
Java - 
Py - 
Part 3: The Negotiator (Follow-up 3)
You've made a deal with the museum security. They won't trigger the alarm if you rob adjacent galleries, but you must pay them a penalty of P for every pair of adjacent galleries you rob. You can now rob any set of galleries (adjacency allowed), but your net profit is:
Total profit = Sum of robbed gallery values - (P × number of adjacent robbed pairs)
You still need to rob exactly k galleries.
Task: Given the array, integer k, and penalty P, return the maximum net profit achievable. You can rob any k galleries (adjacent allowed) but pay P for each adjacent pair in your selection.

-> dp[i][j] = best way to select j elements from first i elements satisfying the required conditions(It is never guaranteed whether the ith element was selected or not)   

-> dp[i][j] = max(dp[i-1][j],a[i] + dp[i-2][j-1],a[i] + a[i-1] - P + dp[i-2][j-2]) 

-> But the third option of this formula is wrong because in the sum for “dp[i-2][j-2]” maybe the “i-2”th element is included -> in that case , i & i-1 & i-2 -> all 3 are adjacent -> but penalty has been counted only for i & i-1 but not for i-1 & i-2)
Hence we need to do this same question with 3D - DP instead(Necessity is the mother of invention!) 
-> dp[i][j][0] -> best answer such that the ith-element is not selected = max(dp[i-1][j][1],dp[i-1][j][0]) 

-> dp[i][j][1] -> best answer such that the ith-element is selected = max(a[i] + dp[i-1][j-1][0], P + a[i] + dp[i-1][j-1][1]) 
—------------------------------------------------------------------------------------------------------------------------------------
Part 4 : The Partner Heist (Simplified)
You and your partner are robbing a row of galleries. Each gallery contains a certain value (can be negative). Each gallery can be robbed by at most one person, or left alone.
Constraint: No person can rob two adjacent galleries (same thief's picks must be non-adjacent). However, you and your partner can rob adjacent galleries (one takes i, the other takes i+1 — that's allowed).
Task: Given an array of integer nums, return the maximum total sum you and your partner can achieve together.

Understanding :- 

-> dp[i][A] = best sum we can get as per the conditions required in the range [1…i] such that the ith element is selected by “A” 
-> dp[i][B] = best sum we can get as per the conditions required in the range [1…i] such that the ith element is selected by “B” 
-> dp[i][X] = best sum we can get as per the conditions required in the range [1…i] such that the ith element is selected by none of them 

-> dp[i][A] = nums[i] + max(dp[i-1][X],dp[i-1][B])
-> dp[i][B] = nums[i] + max(dp[i-1][X],dp[i-1][A])
-> dp[i][X] = max({dp[i-1][X],dp[i-1][A],dp[i-1][B]) 
—----------------------------------------------------------------------------------------
Part 5 - Coming Up

#include <bits/stdc++.h>

1. using namespace std;
2. typedef long long int ll; 
3. int main(){
4. 	ll n,k;
5. cin>>n>>k; 
6. 	vector <ll> a(n+1,0); 
7. for(ll i=1;i<=n;i++){
8. cin>>a[i];
9. }
10. 	vector<vector<ll>> dp(n + 1, vector<ll>(k + 1, -1e18));
11. 	dp[1][1] = a[1] ; 
12. 	dp[1][0] = 0 ;
13. 	dp[2][0] = 0 ; 
14. 	dp[2][1] = max(a[1],a[2]); 
15.  
16. for(ll i=3;i<=n;i++){
17. 		dp[i][0] = 0; 
18. for(ll j=1;j<=k;j++){
19. 			dp[i][j] = max(dp[i-1][j],a[i] + dp[i-2][j-1]); 	
20. }	
21. }
22.  
23. cout<<dp[n][k]; 
24. return 0; 
   1. } 16 end. 17q start golmansachs oa > https://www.desiqna.in/13008/goldman-sachs-sde-oa-ctc-30-lac-2023-dp 

3 image related to the 17 question read the info 





> You can visit each index only 1 time. 

B = [  2 10 8 -5 -10 5  ]

Way 1 -> 2—-8—- -10—--outside= 0 
Way2 -> 2—-8—- -10 —- (-5) —- (+ 5) = 0 
0 is the best answer to this question ; because this is the minimum sum you can get

B = [ 2 -100 8 5 0 ] 

Answer = -85(2—-8— -100—5—jump out of the array)

Observation:- No consecutive backward moves can be made! 







How can we solve this using DP ? 

-> always make an empty DP[] 

→ clear the meaning of DP[i]

→ create the recurrence formula 

—> calculate dp[i] for all i from 1 to N 

-> dp[n] in most cases is your final answer.. 




(DP[i] = it means the minimum cost to reach index ‘i’ or cross index ‘i’)

Dp[i] = minimum cost to reach index i from index 1 .


But in our problem ==== 

Dp[i] means minimum cost to exactly reach point ‘i’..... 


—--> no continuous back jump allowed + you can jump back at any index for at most 1 time…

—-> you should not jump back multiple times. You cannot. 

—> this is because you are allowed to visit any index only 1 time….

—-> At any index of consideration you cannot jump back for more than 1 time continuously because of this we can use dp because we are going back only 1 time….

—-> For a particular index only one backward jump is allowed to  its previous index only 




—---> Whichever thing is creating a problem for you in the question l directly make a state for it

dp[i][forward] = dp[i][2] = someone is coming from index i-2 to index i tell me the best answer in that case. 

dp[i][backward] = dp[i][1] = someone is coming from index i+1 to i -> best answer in that case. 

 





—--> dp[i][backwardjump] = it means the best way to reach index ‘i’ if someone is jumping on it from backward that us from i+1 

dp[i][backward] = b[i] + (dp[i-1][forward]) + b[i+1]


—---> dp[i][forwardjump] = it means the best way to reach index ‘i’ if someone is coming from i-2 index jumping forward from there… 

B[i] + min(dp[i-2][forwardjump],dp[i-2][backwardjump]) 













C++ :- https://ideone.com/rER6aM 
Java :- https://ideone.com/miIZAr 
Py :- https://onecompiler.com/java/42aqpd9db #include <bits/stdc++.h>
   2.  
   3. using namespace std;
   4. typedef long long int ll ; 
   5.  
   6. int my(int k,int r,int g){
   7.  
   8. return min(k,max(r,g));
   9. }
   10.  
   11.  
   12. int main() {
   13. int n ; 
   14. cin>>n ; 
   15. int b[n+1] = {0};
   16.  
   17. int i = 1 ;
   18. while(i<=n){
   19. cin>>b[i] ; 
   20.         i++;
   21. }
   22.  
   23. int dp[n+1][5]; 
   24.  
   25.     dp[1][2] = b[1] ; 
   26.     dp[1][1] = 100000000 ; 
   27.     dp[2][2] = 100000000 ; 
   28.     dp[2][1] = dp[1][2] + b[2] + b[3] ;
   29.  
   30.  
   31.     i = 3 ; 
   32. while(i<=n-1){
   33.  
   34.  
   35.         dp[i][2] = b[i] + min(dp[i-2][1],dp[i-2][2]);
   36.         dp[i][1] = b[i] + b[i+1] + dp[i-1][2] ; 
   37.  
   38.         i++;
   39. }
   40.     dp[i][2] = b[n] + min(dp[i-2][2],dp[i-2][1]);
   41.     dp[i][1] = 100000000 ; 
   42. cout<<my(dp[n][2],dp[n-1][2],dp[n-1][1]);
   43.  
   44.  
   45.  
   46. return 0 ; 
   47. }
17 end. 18q start atlassian Link -> https://www.desiqna.in/15782/atlassian-oa-sde-1-freshers-hiring-ctc-75-lac 





Understanding of the problem:-> You are given “B” queries; you have to perform some of them in order ; and make your initial integer 1 as large as possible! 

-> + x 
-> - x 
-> * x 
->/ x
->N

Greedy :-> Only perform + and * -> they guarantee to give the best answer in most cases. 

->”Too much negative energy can be converted to big positive energy in an instant by “N” operation.”



dp[..........]

dp_max[i] = maximum energy you are getting by doing some of the first i operations. 

dp_min[i] = minimum energy you are getting by doing some of the first i operations. 

if(+)

Dpi_max[i] = max(dpi_max[i-1] + x ; dpi_max[i-1]) 

if(*)
Dpi_max[i] = max(dpi_max[i-1]*x ; dpi_max[i-1]) 

if(-)
dpi_max[i] = max(dpi_max[i-1] - x ; dpi_max[i-1]) 

if(/)
dpi_max[i] = max(dpi_max[i-1] /x ; dpi_max[i-1])

if(N)

Dpi_max[i] = max(dpi_max[i-1] ; -1*dpi_max[i-1] ; -1*dpi_min[i-1])



C++ https://ideone.com/007vpq 
Java. https://ideone.com/ZhJtFx 
Py https://ideone.com/5pBJ4N 

TC : O(N).
SC ; O(N). 
#include<bits/stdc++.h>
   48. using namespace std;
   49. typedef long long int ll;
   50. #define rep(i, l, r) for ((i) = (l); (i) <=(r); (i)++)
   51. #define rep1(i, r, l) for ((i) = (r); (i) >=(l); (i)--)
   52.  
   53. ll max(ll a,ll b,ll c)
   54. {
   55. return max(a,max(b,c)) ; 
   56. }
   57. ll min(ll a,ll b,ll c)
   58. {
   59. return min(a,min(b,c)) ;
   60. }
   61.  
   62. int main()
   63. {
   64. 	ios_base::sync_with_stdio(false) ; 
   65. cin.tie(NULL);
   66. cout.tie(NULL);
   67.     ll t ; 
   68. cin>>t;
   69. while(t--)
   70. {
   71.     ll b; 
   72. cin>>b ; 
   73.     ll i ; 
   74.     ll dp1[b+1];
   75.     ll dp2[b+1];
   76.     dp1[0]=1;
   77.     dp2[0]=dp1[0];
   78.     rep(i,1,b)
   79. {
   80. char g ; 
   81. cin>>g ; 
   82. if(g=='+')
   83. { ll e ; cin>>e;
   84.             dp1[i] = max(dp1[i-1]+e,dp2[i-1]+e,dp1[i-1]) ; 
   85.             dp2[i] = min(dp1[i-1]+e,dp2[i-1]+e,dp2[i-1]) ;   
   86. }
   87. else if(g=='-')
   88. { ll e ; cin>>e;
   89.             dp1[i] = max(dp1[i-1]-e,dp2[i-1]-e,dp1[i-1]) ; 
   90.             dp2[i] = min(dp1[i-1]-e,dp2[i-1]-e,dp2[i-1]) ; 
   91. }
   92. else if(g=='*')
   93. { ll e ; cin>>e;
   94.             dp1[i] = max(dp1[i-1]*e,dp2[i-1]*e,dp1[i-1]) ; 
   95.             dp2[i] = min(dp1[i-1]*e,dp2[i-1]*e,dp2[i-1]) ; 
   96. }
   97. else if(g=='/')
   98. { ll e ; cin>>e;
   99.             dp1[i] = max(dp1[i-1]/e,dp2[i-1]/e,dp1[i-1]) ; 
   100.             dp2[i] = min(dp1[i-1]/e,dp2[i-1]/e,dp2[i-1]) ; 
   101. }
   102. else{
   103.             dp1[i] = max(-1*dp1[i-1],-1*dp2[i-1], dp1[i-1]) ; 
   104.             dp2[i] = min(-1*dp1[i-1],-1*dp2[i-1], dp2[i-1]) ;
   105. }
   106. }
   107. cout<<dp1[b]; 
   108. cout<<"\n";    
   109. }
   110.  
   111. return 0;
   112. }  18 end. 19q start google sde 3 Link -> https://www.desiqna.in/16115/google-interview-problem-dynamic-programming-cities-october 

Mentor :- Kumar K(Prev SDE @ Amazon; All India Rank 12 Google CodeJam’21 ; World Rank 368 Google Kickstart ; World Rank 178 in LeetCode Weekly Contest) 



Understanding :-> You are given 2 arrays ; travel from start to end; maximum maximum dollars ; whenever you try to jump from Array “A” to Array “B” you make no money :) 


Analysis :-> 
dp[i] = best answer to the question if the size of array was “i” 
-> we really need information at ith index whether we have take element from array A or B   

-> dp[i][a] = best answer to the question if size of both array were “i” and the element picked at the ith index if for sure from array “a”

-> dp[i][b] = best answer to the question if size of both array were i and element picked at ith index is from B

dp[i][a] = max(a[i] + dp[i-1][a] Or a[i] + dp[i-2][b]) 

dp[i][b] = max(b[i] + dp[i-1][b] or b[i] + dp[i-2][a]) 

—-----------------------------------------------------------

C++ https://ideone.com/0gX7CQ
Java. https://ideone.com/WAEqvQ 
Py https://ideone.com/POwtBK 

TC :- O(N)
SC :-O(N*2)=>O(N)

You have to print the maximum earning but there is a way to print the whole schedule of “N” depicting on which day what choice you have made for the final best answer. Think about how to do it :) 
Hint - At each step you can see what is the maximum quantity indicating what you have done for that day and its previous day 

dp1[i][a] should tell you what was done on the previous day to reach this step today 

—-------------------------------------------------------------

Follow up dp formulation! 

dp[i][b] = max(b[i]+dp[i-1][b],b[i]+dp[i-2][a],b[i]+dp[i-2][c])

dp[i][a] = max(dp[i-1][a], dp[i-2][b], dp[i-2][c]) + a[i])
dp[i][c] = max(c[i]+dp[i-1][c],c[i]+dp[i-2][a],c[i]+dp[i-2][b])

TC ➖O(N)
SC - O(3*N) …O(N)

C++ - Homework
Java. - Homework
Py - Homework 
#include<bits/stdc++.h>
   113. using namespace std;
   114. typedef long long int ll;
   115. #define rep(i, l, r) for ((i) = (l); (i) <=(r); (i)++)
   116. #define rep1(i, r, l) for ((i) = (r); (i) >=(l); (i)--)
   117.  
   118. ll max(ll a,ll b,ll c)
   119. {
   120. return max(a,max(b,c)) ; 
   121. }
   122. ll min(ll a,ll b,ll c)
   123. {
   124. return min(a,min(b,c)) ;
   125. }
   126.  
   127. int main()
   128. {
   129. 	ios_base::sync_with_stdio(false) ; 
   130. cin.tie(NULL);
   131. cout.tie(NULL);
   132.     ll t ; 
   133. cin>>t;
   134. while(t--)
   135. {
   136.     ll b; 
   137. cin>>b ; 
   138.     ll i ; 
   139.     ll dp1[b+1];
   140.     ll dp2[b+1];
   141.     dp1[0]=1;
   142.     dp2[0]=dp1[0];
   143.     rep(i,1,b)
   144. {
   145. char g ; 
   146. cin>>g ; 
   147. if(g=='+')
   148. { ll e ; cin>>e;
   149.             dp1[i] = max(dp1[i-1]+e,dp2[i-1]+e,dp1[i-1]) ; 
   150.             dp2[i] = min(dp1[i-1]+e,dp2[i-1]+e,dp2[i-1]) ;   
   151. }
   152. else if(g=='-')
   153. { ll e ; cin>>e;
   154.             dp1[i] = max(dp1[i-1]-e,dp2[i-1]-e,dp1[i-1]) ; 
   155.             dp2[i] = min(dp1[i-1]-e,dp2[i-1]-e,dp2[i-1]) ; 
   156. }
   157. else if(g=='*')
   158. { ll e ; cin>>e;
   159.             dp1[i] = max(dp1[i-1]*e,dp2[i-1]*e,dp1[i-1]) ; 
   160.             dp2[i] = min(dp1[i-1]*e,dp2[i-1]*e,dp2[i-1]) ; 
   161. }
   162. else if(g=='/')
   163. { ll e ; cin>>e;
   164.             dp1[i] = max(dp1[i-1]/e,dp2[i-1]/e,dp1[i-1]) ; 
   165.             dp2[i] = min(dp1[i-1]/e,dp2[i-1]/e,dp2[i-1]) ; 
   166. }
   167. else{
   168.             dp1[i] = max(-1*dp1[i-1],-1*dp2[i-1], dp1[i-1]) ; 
   169.             dp2[i] = min(-1*dp1[i-1],-1*dp2[i-1], dp2[i-1]) ;
   170. }
   171. }
   172. cout<<dp1[b]; 
   173. cout<<"\n";    
   174. }
   175.  
   176. return 0;
   177. }  19 end. 20q start uber oa #include <bits/stdc++.h>

using namespace std;
typedef long long int ll ; 
ll dp[100000+5][5][5];

ll mxi(ll x,ll y,ll z){
    
    
    return max(x,max(y,z));
    
}

ll mx(ll x,ll y,ll z,ll g){
    
    return max(max(x,g),max(y,z));
}

int main() {
    
    ll n;
    cin>>n ; 
    
    ll i = 1 ; ll b[n+1] = {0};
    ll d[n+1] = {0};
    while(i<=n){
        cin>>b[i];
        cin>>d[i];
        i++;
    }
    
    //base-cases
    dp[1][1][1] = b[1] ; 
    dp[1][1][2] = b[1] ; 
    dp[1][2][1] = d[1] ; 
    dp[1][2][2] = d[1] ; 
    
    
    //dp[index][][]
    
    
    i = 2 ; 
    while(i<=n){
        
        dp[i][1][1] = b[i] + b[i-1] + max(dp[i-2][2][2],dp[i-2][2][1]);
        dp[i][1][2] = b[i] + d[i-1] + mxi(dp[i-2][1][1],dp[i-2][1][2],dp[i-2][2][1]);
        dp[i][2][1] = d[i] + b[i-1] + mxi(dp[i-2][2][1],dp[i-2][2][2],dp[i-2][1][2]);
        dp[i][2][2] = d[i] + d[i-1] + max(dp[i-2][1][2],dp[i-2][1][1]);
        
        i++;
    }
    
    cout<<mx(dp[n][1][1],dp[n][1][2],dp[n][2][2],dp[n][2][1]); 
    
    
    
    
    
    return 0 ; 
}
[answered](https://www.desiqna.in/11154/uber-hard-dynamic-programming-coding-questions-solutions?show=11156#a11156) Jan 5, 2023 by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert (147,450 points)
00
-> There are two arrays , 'B' and 'C' ; size of both the arrays is 'N' ;

-> At each index you are supposed to pick up an element either from array 'C' or array 'B'

->You have to maximize the final sum of all elements

->Condition : You cannot select 3 or more than 3 element consecutively from the same array.

Example :

3

5 10

3 10

4 10

Output : 25

1<=N<=100000

[Barclays | SDE | Coding OA Questions and Solutions | Set - 8 | 2022 | DP](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp)
20
11,541 views

      * [barclays_oa](https://www.desiqna.in/tag/barclays_oa)
[asked](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp) Dec 10, 2022 in [Online Assessments](https://www.desiqna.in/online-assessments) by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert (147,450 points) | 11,541 views
[Click to join telegram group for high quality job updates](https://telegram.im/@desiqnaofficial)
Share
5 Answers
00
Best answer

```
#include <bits/stdc++.h>

using namespace std;
typedef long long int ll ; 
ll dp[200005][5];
int main() {
    
    ll n ; 
    cin>>n ;
    ll v ; 
    cin>>v ; 
    
    ll easy[n+1] = {0};
    ll hard[n+1] = {0};
    
    
    ll i = 1 ; 
    while(i<=n){
        
        cin>>easy[i];
        cin>>hard[i];
        i++;
    }
    
    dp[1][1] = easy[1] ; //dp[][1]====easy 
    dp[1][2] = hard[1] ; //dp[][2]=====hrd
    dp[1][3] = 0 ; 
    
    i = 2 ; 
    while(i<=n){
        
        dp[i][1] = easy[i] + max(dp[i-1][1],max(dp[i-1][2],dp[i-1][3]));
        dp[i][2] = hard[i] + dp[i-1][3] ; //did nothing on i-1 dy
        dp[i][3] = 0 + max(dp[i-1][1],max(dp[i-1][2],dp[i-1][3]));
        
        
        i++;
    }
    
    cout<<max(dp[n][1],max(dp[n][2],dp[n][3]));
    
    
    return 0 ; 
}
```

[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10569#a10569) Dec 11, 2022 by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert (147,450 points)
selected Dec 11, 2022 by [karan_kumar](https://www.desiqna.in/user/karan_kumar)
00
#include<bits/stdc++.h>
using namespace std;
void solve(){
int n,m;
cin>>n>>m;
vector<vector<int>>a(n,vector<int>(2));
    for(int i=0;i<n;i++){
        for(int j=0;j<2;j++){
            cin>>a[i][j];
        }
    }

vector<vector<int>>dp(n,vector<int>(3,0));
// day 0
dp[0][0]=a[0][0];
dp[0][1]=a[0][1];
dp[0][2]=0;             
for(int i=1;i<n;i++){
    dp[i][0]=a[i][0]+max({dp[i-1][0],dp[i-1][1],dp[i-1][2]}); // today easy task
    dp[i][1]=a[i][1]+dp[i-1][2];                             // today  hard task
    dp[i][2]=max({dp[i-1][0],dp[i-1][1],dp[i-1][2]});        // today no task
}
cout<<max({dp[n-1][0],dp[n-1][1],dp[n-1][2]})<<endl;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        solve();
    }
}
[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=19309#a19309) Aug 15 by [CoderARG:>](https://www.desiqna.in/user/CoderARG%3A%3E) (140 points)
00
Similar to Kumar SIr approach:

 

 

#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main() {
    int n;
    cin>>n;
    vector<vector<int>>vec(n,vector<int>(2));
    for(int i=0;i<n;i++){
        for(int j=0;j<2;j++){
            cin>>vec[i][j];
        }
    }
    vector<vector<int>>dp(n,vector<int>(3));
    for(int i=0;i<n;i++){
        for(int j=0;j<3;j++){
            if(i==0){
                if(j==0)
                dp[i][j]=0;
                else if(j==1)
                dp[i][j]=vec[i][0];
                else
                dp[i][j]=vec[i][1];
            }
            else if(j==2)
            dp[i][j]=dp[i-1][0]+vec[i][1];
            else if(j==0)
            dp[i][j]=max(dp[i-1][1],dp[i-1][2]);
            else
            dp[i][j]=max(dp[i-1][1],dp[i-1][2])+vec[i][0];
        }
    }
    cout<<max(dp[n-1][2],dp[n-1][1])<<endl;
    return 0;
}
[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=13403#a13403) May 16, 2023 by [vats101](https://www.desiqna.in/user/vats101) (400 points)
00
This is my approch of above problem
memoization technique
 
0--not preform any task
1--perform easy task
2--preform hard task

     public static void main(String[] args) {
        System.out.print("hi");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int type=sc.nextInt();
        int[]ep=new int[n];
        int[]dp= new int[n];
        for(int i=0;i<n;i++) {
            ep[i]=sc.nextInt();
            dp[i]=sc.nextInt();
        }
        
        int[][]dpp=new int[ep.length][3];
        for(int[]d:dpp) {
            Arrays.fill(d, -1);
        }
        System.out.print(check(ep,dp,0,0,dpp));
        
         
    }
    public static int  check(int[]easy,int[]diff,int prev,int i,int[][]dpp) {
        if(i==easy.length) {
            return 0;
        }
        if(dpp[i][prev]!=-1)return dpp[i][prev];
        int notpick=check(easy,diff,0,i+1,dpp);
        
        int easypick=easy[i]+check(easy,diff,1,i+1,dpp);
        int diffpick=Integer.MIN_VALUE;
        if(prev==0) {
            diffpick=diff[i]+check(easy,diff,2,i+1,dpp);
        }
        return  dpp[i][prev]=Math.max(notpick, Math.max(easypick, diffpick));
        
    }
[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10601#a10601) Dec 11, 2022 by [Arjun_23091](https://www.desiqna.in/user/Arjun_23091) (140 points)
edited Dec 11, 2022 by [Arjun_23091](https://www.desiqna.in/user/Arjun_23091)
10
Porblem Description. : 
[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10568#a10568) Dec 10, 2022 by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert (147,450 points)
10
sir can we take the hard task amount and sort them and add the max and remove before number and add the number before the number we removed now and soon and add it to the variable
[commented](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10583#c10583) Dec 11, 2022 by [harshi](https://www.desiqna.in/user/harshi)
edited Dec 11, 2022 by [harshi](https://www.desiqna.in/user/harshi)
10
Thats greedy strategy it will not pass for all cases
[commented](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10602#c10602) Dec 11, 2022 by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert
10
#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main() {
    int n;
    cin>>n;
    vector<vector<int>>vec(n,vector<int>(2));
    for(int i=0;i<n;i++){
        for(int j=0;j<2;j++){
            cin>>vec[i][j];
        }
    }
    vector<vector<int>>dp(n,vector<int>(3));
    for(int i=0;i<n;i++){
        for(int j=0;j<3;j++){
            if(i==0){
                if(j==0)
                dp[i][j]=0;
                else if(j==1)
                dp[i][j]=vec[i][0];
                else
                dp[i][j]=vec[i][1];
            }
            else if(j==2)
            dp[i][j]=dp[i-1][0]+vec[i][1];
            else if(j==0)
            dp[i][j]=max(dp[i-1][1],dp[i-1][2]);
            else
            dp[i][j]=max(dp[i-1][1],dp[i-1][2])+vec[i][0];
        }
    }
    cout<<max(dp[n-1][2],dp[n-1][1])<<endl;
    return 0;
}
1<=B[i];C[i]<=10000000000 20 end. 21q start oa level barclays read image 4-5 [Barclays | SDE | Coding OA Questions and Solutions | Set - 8 | 2022 | DP](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp)
20
11,544 views

      * [barclays_oa](https://www.desiqna.in/tag/barclays_oa)
[asked](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp) Dec 10, 2022 in [Online Assessments](https://www.desiqna.in/online-assessments) by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert (147,450 points) | 11,544 views
[Click to join telegram group for high quality job updates](https://telegram.im/@desiqnaofficial)
Share
5 Answers
00
Best answer

```
#include <bits/stdc++.h>

using namespace std;
typedef long long int ll ; 
ll dp[200005][5];
int main() {
    
    ll n ; 
    cin>>n ;
    ll v ; 
    cin>>v ; 
    
    ll easy[n+1] = {0};
    ll hard[n+1] = {0};
    
    
    ll i = 1 ; 
    while(i<=n){
        
        cin>>easy[i];
        cin>>hard[i];
        i++;
    }
    
    dp[1][1] = easy[1] ; //dp[][1]====easy 
    dp[1][2] = hard[1] ; //dp[][2]=====hrd
    dp[1][3] = 0 ; 
    
    i = 2 ; 
    while(i<=n){
        
        dp[i][1] = easy[i] + max(dp[i-1][1],max(dp[i-1][2],dp[i-1][3]));
        dp[i][2] = hard[i] + dp[i-1][3] ; //did nothing on i-1 dy
        dp[i][3] = 0 + max(dp[i-1][1],max(dp[i-1][2],dp[i-1][3]));
        
        
        i++;
    }
    
    cout<<max(dp[n][1],max(dp[n][2],dp[n][3]));
    
    
    return 0 ; 
}
```

[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10569#a10569) Dec 11, 2022 by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert (147,450 points)
selected Dec 11, 2022 by [karan_kumar](https://www.desiqna.in/user/karan_kumar)
00
#include<bits/stdc++.h>
using namespace std;
void solve(){
int n,m;
cin>>n>>m;
vector<vector<int>>a(n,vector<int>(2));
    for(int i=0;i<n;i++){
        for(int j=0;j<2;j++){
            cin>>a[i][j];
        }
    }

vector<vector<int>>dp(n,vector<int>(3,0));
// day 0
dp[0][0]=a[0][0];
dp[0][1]=a[0][1];
dp[0][2]=0;             
for(int i=1;i<n;i++){
    dp[i][0]=a[i][0]+max({dp[i-1][0],dp[i-1][1],dp[i-1][2]}); // today easy task
    dp[i][1]=a[i][1]+dp[i-1][2];                             // today  hard task
    dp[i][2]=max({dp[i-1][0],dp[i-1][1],dp[i-1][2]});        // today no task
}
cout<<max({dp[n-1][0],dp[n-1][1],dp[n-1][2]})<<endl;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        solve();
    }
}
[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=19309#a19309) Aug 15 by [CoderARG:>](https://www.desiqna.in/user/CoderARG%3A%3E) (140 points)
00
Similar to Kumar SIr approach:

 

 

#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main() {
    int n;
    cin>>n;
    vector<vector<int>>vec(n,vector<int>(2));
    for(int i=0;i<n;i++){
        for(int j=0;j<2;j++){
            cin>>vec[i][j];
        }
    }
    vector<vector<int>>dp(n,vector<int>(3));
    for(int i=0;i<n;i++){
        for(int j=0;j<3;j++){
            if(i==0){
                if(j==0)
                dp[i][j]=0;
                else if(j==1)
                dp[i][j]=vec[i][0];
                else
                dp[i][j]=vec[i][1];
            }
            else if(j==2)
            dp[i][j]=dp[i-1][0]+vec[i][1];
            else if(j==0)
            dp[i][j]=max(dp[i-1][1],dp[i-1][2]);
            else
            dp[i][j]=max(dp[i-1][1],dp[i-1][2])+vec[i][0];
        }
    }
    cout<<max(dp[n-1][2],dp[n-1][1])<<endl;
    return 0;
}
[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=13403#a13403) May 16, 2023 by [vats101](https://www.desiqna.in/user/vats101) (400 points)
00
This is my approch of above problem
memoization technique
 
0--not preform any task
1--perform easy task
2--preform hard task

     public static void main(String[] args) {
        System.out.print("hi");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int type=sc.nextInt();
        int[]ep=new int[n];
        int[]dp= new int[n];
        for(int i=0;i<n;i++) {
            ep[i]=sc.nextInt();
            dp[i]=sc.nextInt();
        }
        
        int[][]dpp=new int[ep.length][3];
        for(int[]d:dpp) {
            Arrays.fill(d, -1);
        }
        System.out.print(check(ep,dp,0,0,dpp));
        
         
    }
    public static int  check(int[]easy,int[]diff,int prev,int i,int[][]dpp) {
        if(i==easy.length) {
            return 0;
        }
        if(dpp[i][prev]!=-1)return dpp[i][prev];
        int notpick=check(easy,diff,0,i+1,dpp);
        
        int easypick=easy[i]+check(easy,diff,1,i+1,dpp);
        int diffpick=Integer.MIN_VALUE;
        if(prev==0) {
            diffpick=diff[i]+check(easy,diff,2,i+1,dpp);
        }
        return  dpp[i][prev]=Math.max(notpick, Math.max(easypick, diffpick));
        
    }
[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10601#a10601) Dec 11, 2022 by [Arjun_23091](https://www.desiqna.in/user/Arjun_23091) (140 points)
edited Dec 11, 2022 by [Arjun_23091](https://www.desiqna.in/user/Arjun_23091)
10
Porblem Description. : 
[answered](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10568#a10568) Dec 10, 2022 by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert (147,450 points)
10
sir can we take the hard task amount and sort them and add the max and remove before number and add the number before the number we removed now and soon and add it to the variable
[commented](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10583#c10583) Dec 11, 2022 by [harshi](https://www.desiqna.in/user/harshi)
edited Dec 11, 2022 by [harshi](https://www.desiqna.in/user/harshi)
10
Thats greedy strategy it will not pass for all cases
[commented](https://www.desiqna.in/10567/barclays-sde-coding-oa-questions-and-solutions-set-8-2022-dp?show=10602#c10602) Dec 11, 2022 by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert
10
#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main() {
    int n;
    cin>>n;
    vector<vector<int>>vec(n,vector<int>(2));
    for(int i=0;i<n;i++){
        for(int j=0;j<2;j++){
            cin>>vec[i][j];
        }
    }
    vector<vector<int>>dp(n,vector<int>(3));
    for(int i=0;i<n;i++){
        for(int j=0;j<3;j++){
            if(i==0){
                if(j==0)
                dp[i][j]=0;
                else if(j==1)
                dp[i][j]=vec[i][0];
                else
                dp[i][j]=vec[i][1];
            }
            else if(j==2)
            dp[i][j]=dp[i-1][0]+vec[i][1];
            else if(j==0)
            dp[i][j]=max(dp[i-1][1],dp[i-1][2]);
            else
            dp[i][j]=max(dp[i-1][1],dp[i-1][2])+vec[i][0];
        }
    }
    cout<<max(dp[n-1][2],dp[n-1][1])<<endl;
    return 0;
} 
21 end. 22q start 
uber oa You are given two arrays a and b -> both are of size “N”. 

Start your journey at index 1 and end your journey at index “N”. 

In a move you can move from a[i]->a[i+1] or a[i]->b[i+1] 

OR 

b[i]->b[i+1] or b[i]->a[i+1]

Output the number of journeys whose sum is even and odd. 



Input -> 

A        B
1         3
2         1
1         1

Total 4 even journeys :- (1→2→1) 2 times; + (3→2→1) 2 times; = 4.

Similarly 4 odd journeys. 

Basic Intuition. 

dp[i][even] = number of even journeys  ending at index “i” 

dp[i][odd] = No of odd journeys till index i


How can we make it more easy and descriptive?
We are not directly able to make the formula because we exactly need to know that for which current array at index “i” is it being reached from which index i-1 of which array 

dp[i][a][even] = number of journeys ending at index “i” of array a and having even sum. 

dp[i][a][odd] , dp[i][b][even] and dp[i][b][odd]. 


If a[i] is even:- 

dp[i][a][even] = dp[i-1][a][even] + dp[i-1][b][even] 

If a[i] is odd:- 

dp[i][a][even] = dp[i-1][a][odd] + dp[i-1][b][odd]

If a[i] is even:- 

dp[i][a][odd] = dp[i-1][a][odd] + dp[i-1][b][odd] 


If a[i] is odd :- 


Homework 


Similarly for all dp[i][b][even/odd] 


C++ - https://onecompiler.com/cpp/42bb4rwzy
Java - https://onecompiler.com/java/42bbrrxn6
Py - https://onecompiler.com/python/42bbrtjw8


TC - O(N)
Space :- O(N*2*2) = O(N.)  22 end. 23q start microsoft oa Mentor - Kumar K(https://www.linkedin.com/in/kumark1/ , Prv SDE @ Amazon,All India Rank 12 Google CodeJam’21)




Find the number of ways to make sum “y” with the numbers “1”,”2”,”4”,”6”. 

Condition :- 4 can be used at most 2 times. 

Kumar K student cracks 80 LPA SDE Job offer from 10up - Europe Based MNC

https://www.youtube.com/watch?v=JWQKyr3sgG0&t=419s&ab_channel=KumarK%5BAmazon%5D. 

Join us here - https://training.desiqna.in 


dp[3] = dp[2] + dp[1] 


dp[4] = dp[0] + dp[2] + dp[3]

dp[5] = dp[1]+dp[4]+dp[3]

dp[6] = dp[0]+dp[4]+dp[2]+dp[5]




C++ - https://ideone.com/BUKqmB
Java - https://ideone.com/frwnn2
Py - https://ideone.com/ejiSCz



Actual Problem - 

dp[i][0] = number of ways to create the number “i” such that “0” 4 is used. 

dp[i][1] = number of ways to create the number “i” such that “1” 4 is used. 

dp[i][2] = number of ways to create the number “i” such that “2” 4 are used. 


Final answer = dp[n][0] + dp[n][1] + dp[n][2] → at most 2 <=2.

dp[i][0]=dp[i-1][0]+dp[i-2][0]+dp[i-6][0] -> according to Gauri’s law. 

dp[i][1]=dp[i-1][1]+dp[i-2][1]+dp[i-4][0]+dp[i-6][1]


dp[i][2] =dp[i-1][2]+dp[i-2][2]+dp[i-4][1]+dp[i-6][2]




-> n 






-> dp[n+1][5]; dp[0][0]=dp[0][1]=dp[0][2]=1




dp[1]=1


for(i=2;i<=n;i++){
    
   dp[i][0]=dp[i-1][0]+dp[i-2][0]+dp[i-6][0] 
   dp[i][1]=dp[i-1][1]+dp[i-2][1]+dp[i-4][0]+dp[i-6][1]
   dp[i][2] =dp[i-1][2]+dp[i-2][2]+dp[i-4][1]+dp[i-6][2]


}
print(dp[n][0]+dp[n][1]+dp[n][2])






C++ - https://ideone.com/wbTpLJ.
Java - https://ideone.com/M1Xbqd.
Py - https://ideone.com/j4OAp0








TC - O(N) 
Takes O(N*3) size which is O(N.)






Final - Same as above but at max “2” 4 can be used and at 
max “2” 6 can be used. 


C++ - https://ideone.com/bXq1M7
Java - https://ideone.com/6Ixfe2
Py - https://ideone.com/AAWfo9
 
   178. #include<bits/stdc++.h>
   179. using namespace std;
   180.  
   181. int main(){
   182. int n;
   183. cin>>n;
   184.  
   185. // 1,2,4,6
   186.  
   187.     vector<vector<vector<int>>> dp(n+1,vector<vector<int> >(3, vector<int>(3,0)));
   188.  
   189.     dp[0][0][0] = 1;
   190.  
   191. if(n>0) dp[1][0][0] = 1;
   192.  
   193. for(int i=2; i<=n; i++){
   194.         dp[i][0][0] = dp[i-1][0][0] + dp[i-2][0][0];
   195.         dp[i][0][1] = dp[i-1][0][1] + dp[i-2][0][1];
   196.         dp[i][0][2] = dp[i-1][0][2] + dp[i-2][0][2];
   197.  
   198.         dp[i][1][0] = dp[i-1][1][0] + dp[i-2][1][0];
   199.         dp[i][1][1] = dp[i-1][1][1] + dp[i-2][0][1];
   200.         dp[i][1][2] = dp[i-1][1][2] + dp[i-2][1][2];
   201.  
   202.         dp[i][2][0] = dp[i-1][2][0] + dp[i-2][2][0];
   203.         dp[i][2][1] = dp[i-1][2][1] + dp[i-2][2][1];
   204.         dp[i][2][2] = dp[i-1][2][2] + dp[i-2][2][2];
   205.  
   206. if(i>=6){
   207.             dp[i][0][1] += dp[i-6][0][0];
   208.             dp[i][0][2] += dp[i-6][0][1];
   209.             dp[i][1][1] += dp[i-6][1][0];
   210.             dp[i][1][2] += dp[i-6][1][1];
   211.             dp[i][2][1] += dp[i-6][2][0];
   212.             dp[i][2][2] += dp[i-6][2][1];
   213. }
   214. if(i>=4){
   215.             dp[i][1][0] += dp[i-4][0][0];
   216.             dp[i][1][1] += dp[i-4][0][1];
   217.             dp[i][1][2] += dp[i-4][0][2];
   218.             dp[i][2][0] += dp[i-4][1][0];
   219.             dp[i][2][1] += dp[i-4][1][1];
   220.             dp[i][2][2] += dp[i-4][1][2];
   221. }
   222. }
   223.  
   224. int ans = dp[n][0][0] + dp[n][0][1] + dp[n][0][2] + dp[n][1][0] + dp[n][1][1] + dp[n][1][2] + dp[n][2][0] + dp[n][2][1] + dp[n][2][2];
   225. cout<<ans;
   226. }
   227. 
23 end. 24q meesho  start Kumar K student cracks off-campus SDE offer from Amazon + Google in May - https://www.linkedin.com/posts/kumark1_kumark-coding-activity-7325533608889237505-6fVw?utm_source=share&utm_medium=member_desktop&rcm=ACoAADB1e44BA43UYjFx2BwtGFrtyTJFuENef5c   #include <bits/stdc++.h>
25. using namespace std;
26.  
27. typedef long long ll;
28.  
29. const int N = 1e5 + 5;
30. ll dp[N][4];
31. ll A[N], B[N], C[N];
32.  
33. int main() {
34. int n;
35. cin >> n;
36.  
37. for (int i = 1; i <= n; ++i) cin >> A[i];
38. for (int i = 1; i <= n; ++i) cin >> B[i];
39. for (int i = 1; i <= n; ++i) cin >> C[i];
40.  
41. // Base case initialization
42.     dp[1][0] = dp[1][1] = LLONG_MIN;
43.     dp[1][3] = A[1];
44.     dp[1][2] = B[1];
45.  
46. for (int i = 2; i <= n; ++i) {
47.         dp[i][0] = max(dp[i-1][1], dp[i-1][3]) + C[i]; // both adjacent
48.         dp[i][1] = max(dp[i-1][1],dp[i-1][3]) + B[i]; // after i-1, before i+1
49.         dp[i][2] = max(dp[i-1][0],dp[i-1][2]) + B[i]; // after i+1, before i-1
50.         dp[i][3] = max(dp[i-1][0], dp[i-1][2]) + A[i]; // before both
51. }
52.  
53. // Invalidate illegal state at position n
54.     dp[n][2] = LLONG_MIN;
55.     dp[n][0] = LLONG_MIN; 
56. // Final result
57.     ll result = max({dp[n][0], dp[n][1], dp[n][2], dp[n][3]});
58. cout << result << "\n";
59.  
60. return 0;
61. }
62.  24 end. 25q start [AirBnB OA | SDE | Set - 3 | DP | April 2023](https://www.desiqna.in/12898/airbnb-oa-sde-set-3-dp-april-2023)
10
4,869 views
There are 'n' stones in a row from 0 to n-1. For every ith stone , there are 2 values associated with it, a[i] and b[i] . You have to remove all the stones from the row one by one. Removing the ith stone follows the rule :
 
   1.  
If (i-1)th and (i+1)th stones are still present , then , cost of removing the ith stone is b[i].
 
   2.  
if either (i-1)th or (i+1)th stone is present , then cost of removing the ith stone is a[i].
 
   3.  
if neither (i-1)th nor (i+1)th stone is present , the cost of removing the ith stone is 0.
 
 
Find the minimum total cost of removing all the stones.
 
Constraints :
1 <= n <= 50000
1 <= a[i] , b[i] <= 1000
   * [airbnb_oa](https://www.desiqna.in/tag/airbnb_oa)
[asked](https://www.desiqna.in/12898/airbnb-oa-sde-set-3-dp-april-2023) Apr 13, 2023 in [Online Assessments](https://www.desiqna.in/online-assessments) by [karan_kumar](https://www.desiqna.in/user/karan_kumar) Expert (147,450 points) | 4,869 views

-> https://training.desiqna.in 

Link -> https://leetcode.com/discuss/post/6719472/meesho-oa-sde-1-by-anonymous_user-20ol/ 




Understanding :-> Best way to travel the array such that sum is maximum as per the conditions given :-> 

If you visit index “i” and “i+1” , “i-1” are unvisited; -> sum = sum + A[i] 

-> If one of the adjacent indices is visited; sum = sum + B[i] 

-> If both the adjacent indices are visited; sum = sum + C[i] 

-> dp[i] = best journey possible if you have surely visited indices from “1” to “i” 















Let dp(i)(j) denotes max efficiency of processors from [1...i], if
j = 0, it means the processor is deployed after both processors i-1 and i+1
( i-1,i+1 —->i) 
-> dp[i][0] -> best way to do your journey from 1 till “i” where we know that i-1,i+1 have already been visited in the sequence; 


j=1, means i was deployed after i-1 and before i+1 (i-1→i—>i+1)
j=2, means i was deployed before i-1 and after i+1 (i+1→i—>i-1) 
j=3, means i was deployed before i-1 and i+1 (i —>i-1,i+1) 


2. Now can you form transitions yourself? It's not that tough.
For example,
dp(i)(0) = max { dp(i-1)(1), dp(i-1)(3) } + both_adjacent(i)
dp(i)(1) = 
dp(i)(2) = 
dp(i)(3) = no_adjacent(i) + max({dp[i-1][0],dp[i-1][2]) 


C++ - https://ideone.com/d4GHB6 . 
Java - https://ideone.com/2DLNqR 
Py - https://ideone.com/RaIWQ1 



63. #include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    int b[n+1], a[n+1];
    
    for (int i = 1; i <= n; ++i) {
        cin >> b[i];
    }
    
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }
    
    int dp[n+1][3]; // Using 3 columns for simplicity
    
    dp[2][1] = a[2]; // 1--- last
    dp[2][2] = a[1]; // 2--- second last
    dp[1][2] = 0 ;
    dp[1][1] = 0 ; 
    
    for (int i = 3; i <= n; ++i) {
        dp[i][1] = a[i] + min(dp[i-1][1], dp[i-1][2]);
        
        int v1 = b[i-1] + min(dp[i-2][1], dp[i-2][2]);
        int v5 = dp[i-1][2] + a[i-1]; // 1 min answer of both
        
        dp[i][2] = min(v1, v5);
    }

    cout << dp[3][1] << " " << dp[3][2] << endl;
    
    cout << min(dp[n][1], dp[n][2]) << endl;

    return 0;
}
25 end. 26q start phonepe oa read 7 to 11 images 






Understanding -> Pick subset of elements from array -> Sum of that subset should be maximum. 

-> If you pick a group of 2 numbers; you can again do this operation only after ignoring 1 next number 

-> You can select a group of 3 numbers as well -> but if you do that the next 2 numbers should not be selected and the same goes for the previous 2 numbers. 


-> dp[......................................................................]

-> dp[i] = the best answer for the array till index i 

-> find the general formula for dp[i] 

-> run a for loop and calculate dp[1],dp[2],..............dp[n]. 

-> generally dp[n] is the final answer 

-> dp[i] = maximum sum subset that can be picked till index “i” making sure the guy at index “i” is also included in the subset 


-> here we are not able to keep track of how many elements we selected when we ended at index “i” 

-> either we can select the last 2 elements or we can select the last 3 elements. 

-> we need to make an extra state for the same. 


->dp[i][2] =  maximum sum subset that can be picked till index “i” making sure the guy at index “i” is also included in the subset and last 2 guys are for sure put in the subset 
 

-> dp[i][3] = maximum sum subset that can be picked till index “i” making sure the guy at index “i” is also included in the subset + last 3 guys are for sure put in the subset 

-> dp[i][2] = b[i] + b[i-1] + dp[i-3][2] 
                 OR 
                = b[i] + b[i-1] + max(dp[i-4][2],dp[i-4][3]) 
                 OR 
                             = b[i]+b[i-1]+ max(dp[i-5][2],dp[i-5][3])
.
.
.
.
.
.
.
.
                        = b[i] + b[i-1] + max(dp[1][2],dp[1][3])
                       = b[i] + b[i-1] + ignore everything before it 


->dp[i][3] = b[i] + b[i-1] + b[i-2] + max(dp[i-5][3],dp[i-5][2]) 

               OR
               =  b[i] + b[i-1] + b[i-2] + max(dp[i-6][3],dp[i-6][2]) 
               OR
.
.
.
.
.
.
.
.
.
.
.
 
              = b[i] + b[i-1] + b[i-2] + max(dp[1][3],dp[1][2])
              = b[i] + b[i-1] + b[i-2] + ignore it all


Final answer = max(dp[n][2],dp[n][3]),max(dp[1][2],dp[1][3]),max(dp[2][2],dp[2][3],dp[3][2],dp[3][3],dp[4][2],dp[4][3],...........................)  


TC - O(N*N.) 

Optimize to O(N) :- Use prefix array -> p2[i] = max(dp[i][2],dp[i-1][2],dp[i-3][2],..................dp[1][2]) 

-> p3[i] = max(dp[i][3],dp[i-1][3],dp[i-3][3],..................dp[1][3]) 
-> dp[i][2] = option 1 -> b[i] + b[i-1] + dp[i-3][2] 

                = option 2 -> b[i] + b[i-1] + max(p2[i-4],p3[i-4])

-> dp[i][3] = b[i] + b[i-1] + b[i-2] + max(p3[i-5],p2[i-5])  26 end. 27q start
# Kumar K list: all items from the shared paste (1q–90q so far)

Tags: UNMAPPED = no match found. OPEN = needs input from Sai. DUP = duplicate of an earlier item.

- **1q** : Pick K elements to maximize happiness; min/max sum of a[i]*b[i] after rearranging.  
  Status: partly mapped to GCJ 2008; K-largest part and max-product part use the same method; solved and tested  
  External: GCJ 2008 Round 1A A 'Minimum Scalar Product' (dmoj gcj08r1aa): the min-product part matches. The K-largest part has no match. | Infosys DB: none verified
- **2q** : Kill order minimizing total damage: d[i] damage/sec, t[i] time to kill.  
  Status: mapped to LC  
  External: LC 3273 (biweekly 138, from the paste link) | Infosys DB: not in DB
- **3q** : CF 1151D: cost = sum a[p_j]*j + b[p_j]*(n-j+1); minimize over permutations.  
  Status: mapped to CF  
  External: CF 1151D (link in paste) | Infosys DB: not in DB
- **4q** : Each day assign A (profit a[i]) or B (profit b[i]); A at most X days, B at most Y days; maximize profit.  
  Status: mapped to CodeChef  
  External: CodeChef TADELIVE (link in paste) | Infosys DB: not in DB
- **5q** : Min operations to make all elements equal to each target (sum |a_i - t|).  
  Status: partial  
  External: none | Infosys DB: Q0638 (Increment or Decrement to Make Array Equal, close variant)
- **6q** : Shooting line: persons X (1 or 3) and Y (2 or 3) on a 1xM line; per blue line, output |costX - costY|.  
  Status: mapped to CodeChef SHOOT0 (from paste link); solved and tested  
  External: CodeChef SHOOT0 (link in paste) | Infosys DB: not in DB
- **7q** : Dancing penguins: pair M and F arrays across sets p1/p2 (GS OA 2025).  
  Status: statement incomplete  
  External: desiqna link only | Infosys DB: not in DB
- **8q** : Atlassian islands: complete graph of N islands with importance A[i]. Cutting bridge i-j costs A[i]*A[j]. Within budget C, cut off as many islands as possible from island 1; output how many islands Jordan can still reach.  
  Status: mapped to Atlassian OA (interview, April 2026 per video); solved and tested  
  External: none verified | Infosys DB: not in DB (only Number of Islands Q0349, different problem)
- **9q** : Atlassian OA: strings, vl = product of char^m; sum parity odd or even.  
  Status: unmapped; solved and tested  
  External: no match found | Infosys DB: not in DB
- **10q** : Salesforce OA: count odd-length subarrays whose median is a[k].  
  Status: close match to LeetCode 2488; odd-length version solved and tested  
  External: close: LeetCode 2488 'Count Subarrays With Median K' (not exact: that one allows any length) | Infosys DB: median problems in DB not exact
- **12q** : Google OA: flip bits to remove substring '10'; min flips.  
  Status: unmapped; solved and tested  
  External: no match found | Infosys DB: flip problems in DB not checked
- **13q** : Selling Products: a bag has N items, each with an ID. Remove at most M items. Minimize the number of distinct IDs left.  
  Status: Q1 mapped to LeetCode 1481 / GfG and solved; Q2 statement still missing (needs 'at most M' or 'exactly M')  
  External: LeetCode 1481 'Least Number of Unique Integers after K Removals' and GfG 'Minimum number of distinct elements after removing m items' (exact for Q1) | Infosys DB: not checked against DB
- **14q** : HackerEarth Average Subarray: min flips so no subarray of length >= K has all ones.  
  Status: mapped to HackerEarth  
  External: HackerEarth (link in paste) | Infosys DB: Q0459/Q0546 not same
- **15q** : Harry Potter and the Goblet of Fire: N wizards with primary skill a[i] and secondary skill b[i]. A wizard advances unless some other wizard is strictly higher in both skills. Count the wizards who advance.  
  Status: mapped to Goblet of Fire OA (from pasted statement images and transcript); solved and tested  
  External: none verified | Infosys DB: not checked against DB
- **16q** : ZS Associates OA: choose elements, multiply by 1,2,3... in order; maximize sum.  
  Status: mapped to LeetCode 1402; solved and tested  
  External: LeetCode 1402 'Reducing Dishes' (same like-time coefficient rule, exact match) | Infosys DB: dish problems in DB not exact
- **17q** : Bottles: fill max number of bottles from a container with capacity X.  
  Status: unmapped; solved and tested  
  External: no exact match found (LeetCode 1518 'Water Bottles' is a different problem) | Infosys DB: Q0404 not exact
- **18q** : Maximize array sum after k negations (GfG).  
  Status: mapped to LC 1005  
  External: LC 1005 | Infosys DB: Q0755 close variant
- **19q** : LC 2611 Mice and Cheese.  
  Status: mapped to LC 2611  
  External: LC 2611 | Infosys DB: not in DB
- **20q** : BNY Mellon HackerRank set (three problems): (1) Longest Work Slot: 26 nurses, shifts [employee, leave time] sorted by time; return the id of the nurse with the longest single shift. (2) Closest Numbers: distinct integers; print all pairs with the minimum absolute difference, ascending. (3) Sum of Arrays: rearrange arr1 and arr2 to maximize the sum of i*(arr2[i]-arr1[i]), modulo 1e9+7.  
  Status: mapped to BNY HackerRank assessment; all three statements now present; solved and tested  
  External: BNY Mellon HackerRank (from screenshots) | Infosys DB: not checked against DB
- **21q** : PayPal OA: max even-sum subset.  
  Status: close match to CF 1323A; solved and tested  
  External: close: CF 1323A 'Even Subset Sum Problem' (related, not the same statement) | Infosys DB: not in DB
- **22q** : Visa OA: range +1 queries, then point queries.  
  Status: mapped to Visa OA (from paste link); solved and tested  
  External: desiqna link | Infosys DB: not in DB
- **23q** : LC 134 Gas Station.  
  Status: mapped to LC 134 and DB Q0461  
  External: LC 134 | Infosys DB: Q0461 Gas Station (exact), Q0457, Q0449
- **24q** : Minimum processing time: 4 cores per processor; assign tasks to minimize finish time.  
  Status: mapped to DB Q0439  
  External: LC (title per paste) | Infosys DB: Q0439 (exact), Q0419
- **25q** : Amazon OA: pick subset maximizing min(A)*sum(R).  
  Status: unmapped; solved and tested  
  External: no match found | Infosys DB: not in DB
- **26q** UNMAPPED: Array; in one operation delete any element. Make every pair of value-frequencies differ by at most K, with the fewest deletions.  
  Status: solved and tested (statement from paste)  
  External: no match searched yet | Infosys DB: not checked
- **27q** : Find_Min_Difference(L, P): pick P elements from list L to minimize max minus min.  
  Status: solved and tested (statement from screenshot)  
  External: LeetCode 1984 'Minimum Difference Between Highest and Lowest of K Scores' (same rule; from memory, not yet checked online) | Infosys DB: not checked
- **28q** : Security values: each letter has a value. Rearrange the letters of msg to minimize the sum of absolute differences between adjacent letters' values.  
  Status: solved and tested (statement from screenshots)  
  External: HackerRank 'Security Values' (name from screenshot) | Infosys DB: not checked
- **29q** DUP: getMaxSumOfArray: duplicate of the BNY 'Sum of Arrays' problem already in item 20q.  
  Status: duplicate of 20q (no new work)  
  External: same as 20q | Infosys DB: not checked
- **30q** : Find K maximum-sum subsets of array B (K up to 2000): output the top K subset sums (Amazon OA Nov 2023, Find K Maximum Priority).  
  Status: solved and tested (statement from paste)  
  External: desiqna link in paste (Amazon OA Nov 2023) | Infosys DB: not checked
- **30q-b** : Min memory: delete m contiguous processes from the list; return the minimum memory left.  
  Status: solved and tested (statement from screenshot)  
  External: desiqna Amazon SDE Internship 2022 (problem 1, from screenshot) | Infosys DB: not checked
- **31q** OPEN: distinctElements(N, k, A): code pasted; statement not in the paste.  
  Status: OPEN: statement missing; need the problem text from Sai  
  External: unknown | Infosys DB: not checked
- **32q** : LeetCode 2522: partition string of digits 1-9 into substrings each with value at most k; minimum count, or -1.  
  Status: mapped to LeetCode 2522; solved and tested  
  External: LeetCode 2522 'Partition String Into Substrings With Values at Most K' (statement in paste) | Infosys DB: not checked
- **33q** DUP: Mice and Cheese: duplicate of LeetCode 2611, already item 19q.  
  Status: duplicate of 19q (no new work)  
  External: LeetCode 2611 | Infosys DB: not checked

## Batch 34q–47q

- **34q** : Binary target string; start with all zeros; operation: flip every bit from index i to the end. Min operations to reach the target.  
  Status: solved and tested (statement from paste; pasted code is correct)  
  External: LeetCode 1529 Bulb Switcher IV (same operation and formula). | Infosys DB: close: Q0406 Minimum Suffix Flips to Make All Ones (title match only, statement not compared)
- **35q** : N and M non-overlapping segments [l,r] are covered. Cover the uncovered ranges of [1,N] with blocks of size 2^y. Minimum operations = sum of popcount over each uncovered run.  
  Status: solved and tested (statement from paste; pasted code had bugs for M<=1)  
  External: desiqna Zscaler coding OA 22 Mar 2023 (link in paste and in the code comment). No LeetCode/CF match searched. | Infosys DB: not checked
- **36q** UNMAPPED : Document of totalPackets packets; uploaded chunks are non-overlapping [start,end] ranges. A chunk is a contiguous block of 2^n packets (not aligned). Minimum number of chunks still to upload.  
  Status: solved and tested (statement from screenshots)  
  External: No match searched (statement from a HackerRank-style screenshot, 'Question 3'). | Infosys DB: not checked
- **37q** UNMAPPED : Retail Inventory Management: each step pick the lightest remaining product (smallest index on ties), add its weight to the total, remove it and its current neighbours. Return the total.  
  Status: solved and tested (statement from screenshots)  
  External: No match searched (statement from screenshots). | Infosys DB: not checked
- **38q** : Manhattan distance from integer point p to n axis-parallel segments; find p minimising the sum, ties by smallest x then y.  
  Status: solved and tested (statement from Sai's text and screenshots)  
  External: desiqna BNY Mellon OA 2023 (link in paste). | Infosys DB: not checked
- **39q** : Minimum sum of products of two arrays after k modifications, where each modification changes a[i] by +-2. Return the minimum sum.  
  Status: solved and tested (statement from paste)  
  External: GfG 'Minimum sum of product of two arrays' (link in paste). | Infosys DB: not checked
- **40q** : Pair each element of a with an element of b to minimise the sum of absolute differences.  
  Status: solved and tested (statement from paste)  
  External: GfG 'Minimum Sum of Absolute Differences of Pairs' (statement in paste). | Infosys DB: not checked
- **41q** : LeetCode 455 Assign Cookies: each child gets at most one cookie of size >= their greed; maximise content children.  
  Status: solved and tested (statement from paste)  
  External: LeetCode 455 (statement in paste). LeetCode 2410 is the same problem. | Infosys DB: close: Q0421 Assign Cookies with parity constraint (title match; the parity rule is extra and was not compared)
- **42q** : LeetCode 2405 Optimal Partition of String: minimum number of substrings where every substring has unique characters.  
  Status: solved and tested (statement from paste)  
  External: LeetCode 2405 (statement in paste). | Infosys DB: not checked
- **43q** : LeetCode 55 Jump Game: from index i you can jump up to nums[i] steps. Can you reach the last index?  
  Status: solved and tested (statement from paste)  
  External: LeetCode 55 (statement in paste). No code was pasted for this item. | Infosys DB: not checked
- **44q** : LeetCode 45 Jump Game II: minimum number of jumps to reach the last index.  
  Status: solved and tested (statement from paste)  
  External: LeetCode 45 (statement in paste). No code was pasted for this item. | Infosys DB: close: Q0456 Minimum jumps to reach end of array (title match)
- **45q** : Zeta OA: N segments [L,R] with cost C. Choose two non-overlapping segments (R of one < L of the other) that minimise the product of their costs.  
  Status: solved and tested (statement from paste; input format inferred from pasted code)  
  External: desiqna Zeta OA SDE1 (link in paste). | Infosys DB: not checked
- **46q** : De Shaw OA: change the minimum number of elements to turn the array into a permutation of 1..N, and make the result lexicographically smallest.  
  Status: solved and tested (statement from paste)  
  External: desiqna De Shaw OA SDE1 (link in paste). | Infosys DB: not checked
- **47q** : Microsoft OA 2022: N intervals [start,end]. Count ways to pick 3 pairwise non-overlapping intervals (integer-closed: touching at an endpoint counts as overlap).  
  Status: solved and tested (statement from paste and screenshot)  
  External: desiqna Microsoft OA set 26 2022 (link in paste). | Infosys DB: not checked

## Batch 48q–60q

- **48q** : Amazon OA: N ranges. Remove the fewest ranges so the rest is 'good' (one range intersects all the others). Output the number removed.  
  Status: solved and tested (statement from paste and transcript)  
  External: Amazon OA (linked in paste, leetcode discuss 6735585). No LeetCode/CF match searched. | Infosys DB: not checked
- **49q** OPEN : Connected components of ranges (touching counts as connected). Add at most one range of size <= K to reduce the number of components as much as possible.  
  Status: OPEN: statement incomplete (need full text and input format from Sai)  
  External: DE Shaw OA SDE set 2024 74 (desiqna link in paste); video link only. | Infosys DB: not checked
- **50q** : GfG Maximum Intervals Overlap: given entry and exit times (leaving at t counts as present at t), find the maximum number of guests present and the earliest time it happens.  
  Status: solved and tested (statement from paste)  
  External: GfG 'Maximum Intervals Overlap' (statement in paste). | Infosys DB: not checked
- **51q** : Free gaps between intervals: return the gaps between the merged intervals (the paste's examples show gaps, not the 'does not overlap any other' wording).  
  Status: solved and tested (statement from paste; wording differs from examples, examples followed)  
  External: GfG 'Non-overlapping intervals in an array' (statement in paste). | Infosys DB: not checked
- **52q** : LeetCode 56 Merge Intervals: merge all overlapping intervals (touching merges).  
  Status: solved and tested (statement from paste)  
  External: LeetCode 56 (statement in paste). | Infosys DB: not checked
- **53q** : LeetCode 435 Non-overlapping Intervals: minimum number of intervals to remove so the rest do not overlap (touching allowed).  
  Status: solved and tested (statement from paste)  
  External: LeetCode 435 (statement in paste). | Infosys DB: not checked
- **54q** : LeetCode 2530 Maximal Score After K Operations: each operation takes the largest value x into the score and replaces it with ceil(x/3).  
  Status: solved and tested (statement from paste)  
  External: LeetCode 2530 (statement in paste). | Infosys DB: not checked
- **55q** : GfG Job Sequencing: unit-time jobs with (deadline, profit). Maximise profit; output the number of jobs and the profit.  
  Status: solved and tested (statement from paste; count checked only as the greedy count)  
  External: GfG Job Sequencing (statement in paste). | Infosys DB: not checked
- **56q** : LeetCode 452 Minimum Number of Arrows to Burst Balloons: minimum points that stab every closed interval.  
  Status: solved and tested (statement from paste)  
  External: LeetCode 452 (statement in paste). | Infosys DB: not checked
- **57q** : LeetCode 1024 Video Stitching: minimum number of clips to cover [0, T], or -1.  
  Status: solved and tested (statement from paste)  
  External: LeetCode 1024 (statement in paste). | Infosys DB: not checked
- **58q** : LeetCode 2589 Minimum Time to Complete All Tasks: task (start, end, duration) needs duration on-slots inside [start,end]. Minimum number of on-slots.  
  Status: solved and tested (statement from paste)  
  External: LeetCode 2589 (statement in paste). | Infosys DB: not checked
- **59q** DUP : Mice and Cheese: duplicate of LeetCode 2611 (19q / 33q).  
  Status: DUP: duplicate of 19q (no new work)  
  External: LeetCode 2611 (same as 19q). | Infosys DB: not checked
- **60q** OPEN : Permutation Swaps: an array of n integers; an operation moves value between two indices (statement cut off in the paste). Can it become a permutation of 1..n?  
  Status: OPEN: statement cut off (need operation condition from Sai)  
  External: Greedy algorithm, 38% success, 5,258 attempts (statement from paste source; no match searched). | Infosys DB: not checked

## Batch 61q–70q

- **61q** : Two arrays A and B of size N: find the minimum B[i]-A[j] over pairs with B[i] >= A[j]. Output -1 if no pair exists.  
  Status: solved and tested (statement from paste)  
  External: Own HackerRank contest 'ptr' (link in paste). No public match searched. | Infosys DB: not checked
- **62q** : Three arrays X, Y, Z of size N: pick x, y, z with z >= y >= x minimising (z-y)+(y-x) = z-x. Output -1 if none.  
  Status: solved and tested (statement from paste)  
  External: Own HackerRank contest 'Q1 -4-3' (link in paste). No public match searched. | Infosys DB: not checked
- **63q** : Alice's Sweets (HackerEarth): choose one value from each of three arrays A, B, C to minimise |a-b|+|b-c|+|c-a|.  
  Status: solved and tested (statement from paste)  
  External: HackerEarth 'alices-sweets-02b1336a' (link in paste). | Infosys DB: not checked
- **64q** : Code Contest (GHX5367): strings S and T of length N. Op1 rotates S left by 1 (cost A). Op2 changes one character (cost B). Minimum cost to make S equal T.  
  Status: solved and tested (statement from screenshots)  
  External: Code Contest GHX5367 (statement from screenshots, 2 images of problem text and sample). | Infosys DB: not checked
- **65q** : Polycarb: array A of size N. Exactly X times, pick any element and multiply it by -1. Maximum possible sum.  
  Status: solved and tested (statement from screenshots)  
  External: Code Contest (Polycarb problem, from screenshots). No public match searched. | Infosys DB: not checked
- **66q** OPEN : Code only (no statement in the paste): counts k2 and k5 of positions in the group pattern, then a DP over (i, j) using prefix differences of sorted b.  
  Status: OPEN: statement missing (need problem text from Sai)  
  External: No statement found in the paste (the 65q desiqna 'Education + Jobs' page link is the only source). | Infosys DB: not checked
- **67q** : TikTok OA: array nums and queries. Type 1 (x): every element < x becomes x. Type 2 (i, v): set nums[i] = v. Return the final array.  
  Status: solved and tested (statement from paste)  
  External: desiqna TikTok coding OA (link in paste, Feb 2023). | Infosys DB: not checked
- **68q** OPEN : Deutsche Bank OA 2023: N soldiers on a line, each facing Left or Right with a power. Collisions happen between a right-facing soldier and a left-facing soldier to its right; the stronger one survives with the difference. Output the final status.  
  Status: OPEN: output format and tie rule missing (need from Sai)  
  External: desiqna Deutsche Bank OA SDE 1 August 2023 (link in paste). | Infosys DB: not checked
- **69q** OPEN : CodeKaze / Coding Ninjas hardest question: N soldiers and M monsters, each monster with strength; arrows of strength K. Find the minimum arrows or -1.  
  Status: OPEN: statement incomplete (need exact rules from Sai)  
  External: desiqna CodeKaze hardest question (link in paste). | Infosys DB: not checked
- **70q** OPEN : GfG Job-a-thon: N robots with health h and bullet strength s; each alive robot fires to the right every second. Find the time the robots are killed.  
  Status: OPEN: output and input format missing (need from Sai)  
  External: GfG Job-a-thon 20 (link in paste). | Infosys DB: not checked

## Batch 71q–90q

- **71q** : Maximum greatness: rearrange array A into B so that as many positions as possible have B[i] > A[i]. Paste asks for the maximum count.
  Status: solved and tested (input N then the array; output = count; sample has 7 values for N = 8, confirm)  
  External: desiqna BlackRock OA SDE1 July 2023 (link in paste). Likely LeetCode 2592 by name (not checked). | Infosys DB: not checked  
- **72q** OPEN : Codenation Aug 2023: N days (2 <= N <= 100), M activities [x, y, z]: start day x, deadline y, z days of work. Each day the activity with the smallest deadline is worked on.
  Status: OPEN: output format missing (paste only shows a day-by-day array and "print M + 1") (need from Sai)  
  External: desiqna Codenation possible SDE intern Aug 2023 (link in paste). | Infosys DB: not checked  
- **73q** OPEN : Google OA July 2023: arrays A, B, C of size N. Operation (i, j) does A[i] += 1 and A[j] -= 1 while A[i] >= B[i]. Maximise the minimum of the final array. The role of C and the bounds are not clear in the paste.
  Status: OPEN: role of C and the bounds unclear, output format missing (need from Sai)  
  External: desiqna Google OA SDE intern July 21 2023 (link in paste). | Infosys DB: not checked  
- **74q** OPEN : Atlassian OA SDE1 Sep 2023: strings a and b, a fixed k >= 2. Allowed: swap adjacent characters, or add one constant to a substring of length k. Output Yes or No.
  Status: OPEN: the paste does not say whether letters wrap or what "increase" changes (need from Sai)  
  External: desiqna Atlassian OA SDE1 Sep 2023 (link in paste). | Infosys DB: not checked  
- **75q** : Google OA: pairs (a_i, b_i) with a_i >= b_i. Pair i can be processed only if y >= a_i, and then y becomes y - b_i. Find the minimum starting y over all orders.
  Status: solved and tested (input N then the pairs; output = minimum starting y)  
  External: desiqna Google OA SDE1 (link in paste). LeetCode 1665 by rule (not checked on the page). | Infosys DB: not checked  
- **76q** : Rubrik OA: A and B are permutations of 1..N. One operation moves an element of B to its front or its back. Minimum operations to turn B into A.
  Status: solved and tested (output assumed: minimum number of operations, confirm with Sai)  
  External: desiqna Rubrik OA SDE1 (link in paste). | Infosys DB: not checked  
- **77q** : Amazon OA SDE2 London: find the largest substring (not the whole string) whose letters appear nowhere else in the string.
  Status: solved and tested (output assumed: length, 0 if none; confirm with Sai)  
  External: desiqna Amazon OA SDE2 London CTC 2.5 Cr (link in paste). | Infosys DB: not checked  
- **78q** : PayPal OA Oct 2023: array b (1 <= b_i <= 1e10). One operation breaks a number into x + y. Minimum operations to make the array non-decreasing.
  Status: solved and tested (output assumed: minimum number of operations)  
  External: desiqna PayPal OA October 2023 (link in paste). | Infosys DB: not checked  
- **79q** DUP : Amazon OA Nov 2023 (Find K maximum priority): find the K-th largest subset sum of array B. Same statement as 30q.
  Status: DUP of 30q (same statement; solution re-checked here)  
  External: desiqna Amazon OA Nov 2023 (link in paste). Same as 30q. | Infosys DB: not checked  
- **80q** OPEN : Paste has only the header "80q start 79 end" with no statement.
  Status: OPEN: no statement in paste (need from Sai)  
  External: not in paste | Infosys DB: not checked  
- **81q** : Amazon warehouse (June-Aug 2023): houses on a number line. Count integer points p whose total distance to all houses is at most d.
  Status: solved and tested, sample conflict (paste says 6 for the sample; definition gives 10)  
  External: fastprep Amazon 2024 OA gitbook, "amazon-warehouse" (link in paste). | Infosys DB: not checked  
- **82q** : Palindrome OA: N strings with fixed lengths; any characters may be swapped across all strings. Maximum number of strings that can be palindromes.
  Status: solved and tested (input N then the N strings, output = count; both assumed)  
  External: Paste images 8-10 (no link found). | Infosys DB: not checked  
- **83q** OPEN : Microsoft SDE OA (set 119): two rows s1, s2 of R and W with "?" cells. Make every row and column hold equal R and W, in minimum operations.
  Status: OPEN: what counts as one operation and the output format are missing (need from Sai)  
  External: desiqna Microsoft SDE OA set 119 (link in paste). | Infosys DB: not checked  
- **84q** : Microsoft SDE OA (set 129): N tiles with left and right colours (RR, GG, RG, GR). No rotation; joined tiles need matching colours. Longest joinable chain from a subset.
  Status: solved and tested (output assumed: longest single chain)  
  External: desiqna Microsoft SDE CTC 45 LPA OA set 129 (link in paste). | Infosys DB: not checked  
- **85q** : Google OA SDE intern (July 2024): array of zeros; one operation adds 1 to a subarray of length <= L. Reach a target b (overshoot allowed). Minimum operations.
  Status: solved and tested (output assumed: minimum operation count)  
  External: desiqna Google OA SDE intern July 25 2024 (link in paste). | Infosys DB: not checked  
- **86q** : Atlassian OA CTC 75 L (Sep 2021): +1 to element i costs c_i. Minimum total cost to make all elements distinct. Paste covers the easy version (c_i = 1) and the weighted version.
  Status: solved and tested (weighted version; input N, A, C)  
  External: desiqna Atlassian OA CTC 75 L (link in paste). | Infosys DB: not checked  
- **87q** OPEN : CodeChef FILLIN0: N is even. Build a permutation maximising g = |p1 - p2| + |p3 - p4| + ..., then count the optimal permutations with some fixed positions. The count input is cut off in the paste.
  Status: OPEN: counting statement incomplete (need from Sai)  
  External: CodeChef FILLIN0 (link in paste). | Infosys DB: not checked  
- **88q** OPEN : CodeChef ALTUNI: a value y travels indices 1..N. At index i, if y <= a_i it can become y + p with p in [0, b_i]; then y decreases by 1 per step. Minimum starting y that never goes negative.
  Status: OPEN: exact rule for p and output format cut off (need from Sai)  
  External: CodeChef ALTUNI (link in paste). | Infosys DB: not checked  
- **89q** OPEN : Amazon OA March 2025 (set 1): index i is good if it can stay alive to the end when fights are played optimally. Print good indices in ascending order. Sample [1 6 2 7 2] gives [2, 4] in the paste.
  Status: OPEN: fight rule incomplete in paste (need exact rule from Sai)  
  External: itjobxs Amazon OA SDE1 March 2025 set 1 (link in paste). | Infosys DB: not checked  
- **90q** : Rippling OA SDE intern (July 2026 set): arrays a and b. b[j] can kill a[i] if b[j] >= a[i]; each b kills at most one a per round. Minimum rounds to kill all of a; -1 if impossible.
  Status: solved and tested (interpretation: one kill per b per round; input N, A, M, B; confirm with Sai)  
  External: desiqna Rippling SDE intern July 2026 set (link in paste). | Infosys DB: not checked  

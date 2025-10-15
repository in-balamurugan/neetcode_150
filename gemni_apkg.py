import genanki
import io
import re

# --- Configuration ---
OUTPUT_APKG_FILE = 'neetcode150.apkg'
DECK_NAME = 'NeetCode 150 Coding Interview Questions'

# Unique IDs for Anki (Must be stable/random large numbers)
NEETCODE_MODEL_ID = 1000000001
NEETCODE_DECK_ID = 2000000002

# --- TSV Data from Previous Response (150 entries) ---
# This data is formatted as: sno\ttitle\tproblem\thint\trecommended_time_space
TSV_DATA = """
1	Contains Duplicate	Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.	A brute force solution would be to check every element against every other element in the array. This would be an O(n^2) solution. Can you think of a better way?	You should aim for O(n) time and O(n) space.
2	Valid Anagram	Given two strings s and t, return true if the two strings are anagrams of each other, else return false.	A brute force solution would be to sort the given strings and check for their equality. This would be an O(nlogn + mlogm) solution. Can you think of a better way without sorting the strings?	You should aim for O(n) time and O(1) space.
3	Two Sum	Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.	A brute force solution would be to check every pair of numbers in the array. This would be an O(n^2) solution. Can you think of a better way? Maybe in terms of mathematical equation?	You should aim for O(n) time and O(n) space.
4	Group Anagrams	Given an array of strings strs, group all anagrams together into sublists. Return the answer in any order.	A naive solution would be to sort each string and group them using a hash map. This would be an O(m * nlogn) solution. Though this solution is acceptable, can you think of a better way without sorting the strings?	You should aim for O(n * k) time and O(n * k) space, where n = #strings, k = avg string length.
5	Top K Frequent Elements	Given a non-empty array of integers, return the k most frequent elements.	A naive solution would be to count the frequency of each element and then sort. Can you improve upon the O(n log n) sort?	You should aim for O(n) time and O(n) space.
6	Encode and Decode Strings	Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings. Implement encode and decode.	A naive solution would be to use a non-ascii character as a delimiter. Can you think of a better way?	You should aim for O(n) time and O(n) space where n is total chars.
7	Product of Array Except Self	Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. Solve it without division.	Try not to use division. Is there a way to construct the result using left and right product arrays?	You should aim for O(n) time and O(1) extra space.
8	Valid Sudoku	Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the Sudoku rules.	Try using data structures to check the validity of each row, column, and 3x3 box.	You should aim for O(1) time and O(1) space.
9	Longest Consecutive Sequence	Given an array of integers, find the length of the longest consecutive elements sequence. Expected time complexity: O(n).	Sorting the array first makes it easier to find consecutive runs, but can it be solved in O(n)?	You should aim for O(n) time and O(n) space.
10	Longest Substring Without Repeating Characters	Given a string, find the length of the longest substring without repeating characters.	Use a sliding window approach with a set or hashmap to remember seen characters.	You should aim for O(n) time and O(n) space.
11	Minimum Window Substring	Given two strings s and t, return the minimum window in s which contains all the characters of t.	Try using two pointers and a hash map to expand and contract the window.	You should aim for O(n) time and O(m) space.
12	Best Time to Buy and Sell Stock	Given an array prices where prices[i] is the price of a given stock on the i-th day, find the maximum profit you can achieve. You may complete only one transaction.	Track the minimum price as you scan and for each price, check the profit you'd get by selling at the current price.	You should aim for O(n) time and O(1) space.
13	Valid Palindrome	Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.	Try using two pointers from each end of the string.	You should aim for O(n) time and O(1) space.
14	3Sum	Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i ≠ j ≠ k, and nums[i] + nums[j] + nums[k] == 0.	After sorting, try fixing one number and use two pointers to find the other two.	You should aim for O(n^2) time and O(m) space, where m is the number of triplets returned.
15	Container With Most Water	Given n non-negative integers, where each represents a point at coordinate (i, ai), n vertical lines are drawn. Find two lines that together with the x-axis form a container, such that the container contains the most water.	Use two pointers, one at the start and one at the end, and move the pointer pointing to the shorter line inward.	You should aim for O(n) time and O(1) space.
16	Valid Parentheses	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.	Try using a stack to keep track of opening brackets.	You should aim for O(n) time and O(n) space.
17	Implement Trie (Prefix Tree)	Implement a trie with insert, search, and startsWith methods.	Use a tree-like data structure and handle characters one by one.	You should aim for O(m) time per operation, where m is the length of the word.
18	Course Schedule	There are a total of numCourses you have to take, labeled from 0 to numCourses-1. Given prerequisites, determine if you can finish all courses.	Model the courses and prerequisites as a directed graph and check for cycles.	You should aim for O(V + E) time and O(V + E) space, where V is the number of courses, E is prerequisites.
19	Number of Islands	Given a 2D grid map of '1's (land) and '0's (water), count the number of islands.	Use DFS or BFS to mark all connected land for each found island.	You should aim for O(mn) time and O(mn) space.
20	Longest Palindromic Substring	Given a string s, return the longest palindromic substring in s.	For each center, expand as long as the substring is a palindrome.	You should aim for O(n^2) time and O(1) or O(n^2) space.
21	Palindromic Substrings	Given a string s, return the number of palindromic substrings in it.	Try expanding around every possible center.	You should aim for O(n^2) time and O(1) space.
22	Merge Intervals	Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals.	Sort the intervals and merge overlapping ones as you iterate.	You should aim for O(n log n) time and O(n) space.
23	Binary Tree Level Order Traversal	Given the root of a binary tree, return the level order traversal of its nodes' values.	Try using a queue in a breadth-first search (BFS).	You should aim for O(n) time and O(n) space.
24	Validate Binary Search Tree	Given the root of a binary tree, determine if it is a valid binary search tree (BST).	Think about the BST invariants, and use min/max ranges recursively.	You should aim for O(n) time and O(h) space, where h is the tree height.
25	Invert Binary Tree	Given the root of a binary tree, invert the tree, and return its root.	Swap the children of every node.	You should aim for O(n) time and O(n) space.
26	Maximum Depth of Binary Tree	Given the root of a binary tree, return its maximum depth.	Use recursion to compute depth from children, adding one at each step.	You should aim for O(n) time and O(h) space.
27	Same Tree	Given the roots of two binary trees, determine if they are the same.	Recursively check both value and structure.	You should aim for O(n) time and O(h) space.
28	Subtree of Another Tree	Given two binary trees root and subRoot, return true if subRoot is a subtree of root.	Traverse the main tree, at each node check if the subtree matches.	You should aim for O(n * m) time and O(h) space.
29	Lowest Common Ancestor of a Binary Search Tree	Given a binary search tree (BST), find the lowest common ancestor for two nodes.	Use the BST properties to traverse to the correct split point.	You should aim for O(h) time and O(1) space.
30	Binary Tree Maximum Path Sum	Given the root of a binary tree, find the maximum path sum. A path may start and end at any nodes.	Use recursion and keep track of the maximum sum for each subtree.	You should aim for O(n) time and O(h) space.
31	Serialize and Deserialize Binary Tree	Design an algorithm to serialize and deserialize a binary tree.	You can use BFS or DFS traversal; remember to handle null children.	You should aim for O(n) time and O(n) space.
32	Construct Binary Tree from Preorder and Inorder Traversal	Given preorder and inorder traversal of a tree, construct the binary tree.	Root is the first element in preorder and split inorder by root.	You should aim for O(n) time and O(n) space.
33	Binary Tree Level Order Traversal II	Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.	Gather levels top-down and reverse at the end.	You should aim for O(n) time and O(n) space.
34	Kth Smallest Element in a BST	Given a binary search tree, find the k-th smallest element in it.	Try using in-order traversal for BST.	You should aim for O(h + k) time and O(h) space.
35	Validate Parentheses	Given a string with '(', ')', '{', '}', '[', ']', determine if it's valid.	A stack helps to match pairs properly.	You should aim for O(n) time and O(n) space.
36	Reverse Linked List	Given the head of a singly linked list, reverse the list and return the head.	Iterate through and reverse the pointers.	You should aim for O(n) time and O(1) space.
37	Merge Two Sorted Lists	Merge two sorted linked lists and return it as a new sorted list.	Compare the nodes one by one and link accordingly.	You should aim for O(n+m) time and O(1) space.
38	Reorder List	Given the head of a singly linked list, reorder the list as L0 → Ln → L1 → Ln-1 → …	Split, reverse the second half, and merge alternately.	You should aim for O(n) time and O(1) space.
39	Remove Nth Node From End of List	Given the head of a linked list, remove the n-th node from the end.	Use two pointers with a gap of n nodes.	You should aim for O(n) time and O(1) space.
40	Linked List Cycle	Given the head of a linked list, determine if there is a cycle.	Use slow and fast pointers to detect the cycle.	You should aim for O(n) time and O(1) space.
41	Merge k Sorted Lists	Merge k sorted linked lists and return it as one sorted list.	Use a min-heap or merge pairwise recursively.	You should aim for O(N log k) time and O(N) space, where N is the total number of nodes.
42	Clone Graph	Given a reference node to a graph, return a deep copy (clone) of the graph.	Use DFS or BFS with a map to track copied nodes.	You should aim for O(n) time and O(n) space, where n is the # of nodes.
43	Graph Valid Tree	Given n nodes labeled 0 to n-1 and a list of edges, determine if it's a valid tree.	Check for cycles and that all nodes are connected.	You should aim for O(n) time and O(n) space.
44	Number of Connected Components in an Undirected Graph	Given n nodes and a list of undirected edges, return the number of connected components.	Use DFS/BFS to visit each component.	You should aim for O(n + e) time and O(n) space, where e = #edges.
45	Word Search	Given an m x n board and a word, determine if the word exists in the grid by moving horizontally or vertically.	Try DFS for each letter and mark visited cells.	You should aim for O(m*n*L) time and O(L) space, where L = word length.
46	Pacific Atlantic Water Flow	Given an m x n matrix, return list of grid coordinates where water can flow to both Pacific and Atlantic.	Reverse the flow: start from oceans and mark reachable cells with DFS/BFS.	You should aim for O(m*n) time and O(m*n) space.
47	Alien Dictionary	Given a sorted dictionary of an alien language, return a possible order of the letters.	Create a graph of precedence and use topological sort.	You should aim for O(c) time and O(c) space, where c = total characters.
48	Course Schedule II	Given numCourses and prerequisites, return the ordering of courses you should take to finish all.	Topological sort helps if no cycles; otherwise, it's impossible.	You should aim for O(V + E) time and O(V) space.
49	Word Ladder	Given two words (beginWord and endWord), and a dictionary, return the number of steps in the shortest sequence to transform beginWord to endWord.	Use BFS, changing one letter at a time.	You should aim for O(N*M^2) time and O(N*M) space, where N = word list size, M = word length.
50	Combination Sum	Given an array of distinct integers candidates and an integer target, return all unique combinations of candidates that sum to target.	Use backtracking to build up solutions.	You should aim for O(2^n) time and O(target) space.
51	Permutations	Given a collection of distinct integers, return all possible permutations.	Use backtracking and swap elements to build each permutation.	You should aim for O(n!) time and O(n) space.
52	Subsets	Given an integer array nums, return all possible subsets (the power set).	For each element, decide whether to include it or not. Use backtracking.	You should aim for O(n*2^n) time and O(n*2^n) space.
53	Combination Sum II	Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations where candidates may only be used once.	Sort candidates, use backtracking, and skip duplicates to avoid same combinations.	You should aim for O(2^n) time and O(target) space.
54	Word Search II	Given a 2D board and a list of words, find all words in the board.	Use a Trie and DFS to improve search efficiency.	You should aim for O(N*L), N = board size, L = total length of words.
55	Sudoku Solver	Write a program to solve a Sudoku puzzle by filling empty cells.	Backtracking to fill each cell, check valid placement.	You should aim for O(9^m) time, where m is #empty cells.
56	N-Queens	The n-queens puzzle is to place n queens on an n x n chessboard so that no two queens attack each other.	Use backtracking with row, column, and diagonal constraints.	You should aim for O(n!) time.
57	Graph Clone	Clone an undirected graph. Each node contains a value and a list of its neighbors.	Use DFS/BFS with a visited map.	You should aim for O(n) time and O(n) space.
58	Pacific Atlantic Water Flow	Given an m x n matrix representing the height of each unit cell, find all cells from which water can flow to both the Pacific and Atlantic ocean.	Reverse simulate from the ocean edges using BFS/DFS.	You should aim for O(m*n) time and O(m*n) space.
59	Number of Islands	Given a 2D grid map of '1's and '0's, count the number of islands.	Use BFS or DFS to explore each island from a found '1'.	You should aim for O(mn) time and O(mn) space.
60	Flood Fill	Given an image (2D array) and a starting pixel, flood fill the image using a new color.	Use BFS or DFS to recolor all connected pixels.	You should aim for O(mn) time and O(mn) space.
61	Set Matrix Zeroes	Given an m x n integer matrix, if an element is 0, set its entire row and column to 0.	Can you do this in place? Try using extra space first, then reduce it.	You should aim for O(mn) time and O(1) extra space.
62	Spiral Matrix	Given an m x n matrix, return all elements in spiral order.	Keep track of the current bounds as you spiral over the matrix.	You should aim for O(mn) time and O(1) space.
63	Rotate Image	You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise), in place.	Transpose, then reverse each row, or swap four elements in cycles directly.	You should aim for O(n^2) time and O(1) space.
64	Group Anagrams	Given an array of strings, group anagrams together.	Sort each string and use as dictionary key.	You should aim for O(n*k*log(k)) time where k is avg string length.
65	Maximum Subarray	Given an integer array nums, find the contiguous subarray with the largest sum.	Try modifying the running sum as you iterate (Kadane’s algorithm).	You should aim for O(n) time and O(1) space.
66	Coin Change	Given coins and an amount, compute the minimum number of coins to make the amount.	Try dynamic programming, storing best answer for every amount up to target.	You should aim for O(amount * coins.length) time.
67	Climbing Stairs	You are climbing a staircase. Each time you can take 1 or 2 steps. How many distinct ways can you climb to the top?	Think of it as a Fibonacci recurrence (DP).	You should aim for O(n) time and O(1) space.
68	Longest Increasing Subsequence	Given an integer array nums, return the length of the longest strictly increasing subsequence.	Try DP; can you improve the naive O(n^2) approach?	You should aim for O(n^2) time or O(n log n) if optimized.
69	Longest Common Subsequence	Given two strings, return the length of their longest common subsequence.	Classic DP: use a 2D table where each cell depends on previous cells.	You should aim for O(mn) time and O(mn) space.
70	Word Break	Given a string and a dictionary of words, determine if the string can be segmented into a space-separated sequence of dictionary words.	Dynamic programming to check word breaks up to each index.	You should aim for O(n^2) time and O(n) space.
71	House Robber	Given a list of non-negative integers representing the amount of money in each house, determine the maximum amount of money you can rob without robbing adjacent houses.	Think recursively: at each house, you can rob it or skip it. Use dynamic programming.	You should aim for O(n) time and O(1) space.
72	House Robber II	Similar to House Robber, but houses are arranged in a circle.	Solve twice: once excluding the first house, once excluding the last.	You should aim for O(n) time and O(1) space.
73	Decode Ways	Given a string containing only digits, determine the total number of ways to decode it.	Use DP — the answer for a prefix depends on previous 1–2 digits.	You should aim for O(n) time and O(n) space.
74	Unique Paths	A robot is located at the top-left corner of an m x n grid. How many unique paths are there to the bottom-right corner (only right and down)?	Dynamic programming: each cell’s answer is the sum of the answers from the cell above and to the left.	You should aim for O(mn) time and O(mn) or O(n) space.
75	Jump Game	Given an array of non-negative integers, each representing your maximum jump length per position, determine if you can reach the last index.	Keep track of the furthest index you can reach as you iterate.	You should aim for O(n) time and O(1) space.
76	Merge Intervals	Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals.	Sort the intervals and merge overlapping ones as you iterate.	You should aim for O(n log n) time and O(n) space.
77	Insert Interval	Given a set of non-overlapping intervals sorted by their start time, insert a new interval and merge if necessary.	Find where to insert, merge as needed.	You should aim for O(n) time and O(n) space.
78	Non-overlapping Intervals	Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest non-overlapping.	Sort by end time, remove overlaps greedily.	You should aim for O(n log n) time and O(1) space.
79	Meeting Rooms	Given an array of meeting time intervals, determine if a person could attend all meetings.	Sort by start time and look for overlaps.	You should aim for O(n log n) time and O(1) space.
80	Meeting Rooms II	Given an array of meeting time intervals, find the minimum number of conference rooms required.	Use a min-heap to efficiently track end times.	You should aim for O(n log n) time and O(n) space.
81	Minimum Window Substring	Given two strings s and t, return the minimum window in s which contains all the characters of t.	Use two pointers (sliding window) and a frequency map to track required characters.	You should aim for O(n) time and O(m) space.
82	Search in Rotated Sorted Array	Given a rotated sorted array, search for a target value and return its index, or -1 if not found.	Binary search with conditions for rotated halves.	You should aim for O(log n) time and O(1) space.
83	Find Minimum in Rotated Sorted Array	Given a rotated sorted array, find the minimum element.	Binary search to find the inflection point.	You should aim for O(log n) time and O(1) space.
84	Search in Rotated Sorted Array II	Given a rotated sorted array that may contain duplicates, check if a target value exists in the array.	Carefully handle duplicates and use binary search.	You should aim for O(log n) time (linear if many duplicates) and O(1) space.
85	Median of Two Sorted Arrays	Given two sorted arrays nums1 and nums2, return the median of the two arrays.	Binary search and divide-and-conquer can achieve logarithmic time.	You should aim for O(log(min(n, m))) time and O(1) space.
86	Kth Largest Element in an Array	Given an integer array nums and an integer k, return the kth largest element in the array.	Use a min heap of size k, or quickselect (partition algorithm).	You should aim for O(n) average time and O(1) space.
87	Top K Frequent Elements	Given an integer array nums and an integer k, return the k most frequent elements.	Bucket sort or heap based on frequencies.	You should aim for O(n) time and O(n) space.
88	Find K Closest Elements	Given a sorted array and two integers k and x, return the k closest integers to x in the array.	Binary search for the best left bound, then use a window.	You should aim for O(log(n-k) + k) time and O(k) space.
89	Sliding Window Maximum	Given an array nums and an integer k, return the maximum value in each sliding window of size k.	Try using a deque to keep track of the useful elements.	You should aim for O(n) time and O(k) space.
90	Subarray Sum Equals K	Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.	Use a hashmap to track running sums seen so far.	You should aim for O(n) time and O(n) space.
91	Minimum Size Subarray Sum	Given an array of positive integers nums and an integer target, return the minimal length of a subarray sum ≥ target. If none, return 0.	Try a sliding window approach, moving left pointer when current sum ≥ target.	You should aim for O(n) time and O(1) space.
92	Longest Substring with At Most K Distinct Characters	Given a string s and an integer k, return the length of the longest substring with at most k distinct characters.	Use a sliding window with a hashmap to count unique characters in current window.	You should aim for O(n) time and O(k) space.
93	Longest Repeating Character Replacement	Given a string s and an integer k, return the length of the longest substring containing the same letter, after replacing up to k letters.	Use a sliding window, track the max frequency in current window.	You should aim for O(n) time and O(26) space.
94	Permutation in String	Given two strings s1 and s2, return true if s2 contains a permutation of s1.	Compare character frequency counts using a sliding window.	You should aim for O(n) time and O(1) space.
95	Find All Anagrams in a String	Given a string s and a string p, return all start indices of p's anagrams in s.	Sliding window with character count arrays/hashes.	You should aim for O(n) time and O(1) space.
96	Longest Substring with At Most Two Distinct Characters	Given a string s, return the length of the longest substring with at most two distinct characters.	Sliding window and hashmap — similar to previous K-distinct problem, set k=2.	You should aim for O(n) time and O(1) space.
97	Find All Duplicates in an Array	Given an integer array nums of length n with numbers in the range 1 to n, find all elements that appear twice.	Mark seen indices as negative in place.	You should aim for O(n) time and O(1) space (excluding output)."
98	Find the Duplicate Number	Given an array of n+1 integers where each integer is between 1 and n, find the duplicate one.	Use cycle detection (Floyd's Tortoise and Hare) or binary search.	You should aim for O(n) time and O(1) space.
99	Missing Number	Given an array containing n distinct numbers, return the missing number.	Sum, XOR, or mark in place.	You should aim for O(n) time and O(1) space.
100	First Missing Positive	Given an unsorted integer array, find the smallest missing positive integer.	Index marking: use value as index to place correct number at index, then scan.	You should aim for O(n) time and O(1) space.
101	Find Peak Element	Given an input array nums, find a peak element and return its index. An element is a peak if it is greater than its neighbors.	Binary search can be used since you only need to compare neighbors.	You should aim for O(log n) time and O(1) space.
102	Search a 2D Matrix	Given an m x n matrix and a target, return true if the target exists in the matrix.	Use binary search by treating the matrix as a sorted array.	You should aim for O(log(mn)) time and O(1) space.
103	Search a 2D Matrix II	Given an m x n matrix, return true if the target exists in the matrix. Each row and column is sorted.	Start from top-right, move left or down based on comparison.	You should aim for O(m+n) time and O(1) space.
104	Merge Sorted Array	You are given two integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array in-place.	Start filling nums1 from the end using two pointers.	You should aim for O(n+m) time and O(1) space.
105	Majority Element	Given an array of size n, find the majority element (> n/2 times).	Voting algorithm (Boyer-Moore) or hash counting.	You should aim for O(n) time and O(1) space.
106	Majority Element II	Given an array, find all elements that appear more than ⌊ n/3 ⌋ times.	At most two majority elements; extend Boyer-Moore algorithm.	You should aim for O(n) time and O(1) space.
107	Excel Sheet Column Number	Given a string columnTitle representing the column title as in Excel, return its corresponding column number.	Treat as a number in base 26 (A=1, B=2, ...).	You should aim for O(n) time and O(1) space.
108	Excel Sheet Column Title	Given a positive integer columnNumber, return its corresponding column title as in Excel.	Reverse of base-26 conversion (use chr and divmod).	You should aim for O(log n) time and O(1) space.
109	Valid Number	Validate if a string can be interpreted as a decimal number.	Use a finite automaton or careful state simulation.	You should aim for O(n) time and O(1) space.
110	Pow(x, n)	Implement pow(x, n), which calculates x raised to the power n.	Exponentiation by squaring (divide and conquer recursion or loop).	You should aim for O(log n) time and O(1) space.
111	Spiral Matrix II	Given an integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.	Keep track of the current bounds and fill in layers.	You should aim for O(n^2) time and O(1) space.
112	Rotate List	Given the head of a linked list, rotate the list to the right by k places.	Find the length, connect end to start, break at new head.	You should aim for O(n) time and O(1) space.
113	Linked List Cycle II	Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.	Use slow and fast pointers; once they meet, move from head and meeting point together.	You should aim for O(n) time and O(1) space.
114	LRU Cache	Design and implement a data structure for Least Recently Used (LRU) cache with get and put operations.	Double linked list and hashmap enable O(1) operations.	You should aim for O(1) time and O(capacity) space per operation.
115	Min Stack	Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.	Store current min for each value pushed.	You should aim for O(1) time and O(n) space per operation.
116	Binary Search Tree Iterator	Implement an iterator for a binary search tree (BST) with next and hasNext methods.	Inorder traversal using a stack.	You should aim for O(1) amortized time per call and O(h) space.
117	Summary Ranges	Given a sorted integer array, return the smallest sorted list of ranges that cover all numbers in the array.	Traverse and merge consecutive numbers into ranges.	You should aim for O(n) time and O(1) space.
118	Majority Element II	Given an array, find all elements that appear more than ⌊ n/3 ⌋ times.	There can be at most two such elements (extended Boyer-Moore).	You should aim for O(n) time and O(1) space.
119	Implement Queue using Stacks	Implement a first in first out (FIFO) queue using only two stacks.	Push to one stack, pop/peek from the other. Rebalance as needed.	You should aim for O(1) amortized time per operation.
120	Implement Stack using Queues	Implement a last in first out (LIFO) stack using only two queues.	Push to one queue, for pop/peek move all but one to other queue.	You should aim for O(n) time for pop/peek, O(1) space.
121	Design Circular Queue	Design a circular queue that supports enqueue, dequeue, front, rear, and checking if the queue is full or empty.	Use an array with head, tail pointers and a size counter.	You should aim for O(1) time per operation.
122	Design Circular Deque	Design a circular deque that supports adding and deleting elements from front or rear, checking if it's full or empty.	Array with head, tail pointers, circularly increasing indices.	You should aim for O(1) time per operation.
123	Implement Trie (Prefix Tree)	Implement a trie with insert, search, and startsWith methods.	Use a tree-like node structure for each character.	You should aim for O(m) time per operation, where m is the word length.
124	Add and Search Word - Data structure design	Design a data structure that supports adding words and searching with '.' as wildcard.	DFS for search, trie for fast prefix search.	You should aim for O(m) time per operation.
125	Word Dictionary	Design a word dictionary that supports adding and searching with '.' as wildcard.	Similar to previous, use a trie and DFS for dot searches.	You should aim for O(m) time per operation.
126	Implement Magic Dictionary	Design a dictionary structure for searching if a word can be formed by modifying exactly one character.	For each word, store all possible wildcards for one character changed.	You should aim for O(n*m) time for build.
127	Replace Words	Given a dictionary and a sentence, replace words in sentence with root of the dictionary.	Use trie for fast prefix lookup.	You should aim for O(n*m) time.
128	Find Words That Can Be Formed by Characters	Given an array of words and string chars, find the sum length of words that can be formed with chars (each letter used at most once).	Count chars frequency and check for each word.	You should aim for O(N*M) time.
129	Maximum Product of Word Lengths	Given a list of words, return the maximum value of length(word[i]) * length(word[j]) where two words do not share common letters.	Use bitmask for each word, compare pairs for intersections.	You should aim for O(N^2) time.
130	Implement Prefix Tree	Implement a prefix tree (trie) to support insert and search operations.	Standard trie node structure.	You should aim for O(m) time per operation.
131	Search Suggestions System	Given an array of strings products and a string searchWord, return a list of 3 product suggestions after each character is typed. Suggestions should be sorted.	Use trie + min-heap or sort & binary search for prefix matches.	You should aim for O(n log n) time or O(nk) for trie-based, n = product count, k = searchWord length.
132	Design Add and Search Words Data Structure	Problem: Implement addWord and searchWord methods. SearchWord may contain '.' as wildcard.	Hint: Trie + DFS for searching wildcards.	Recommended Time/Space: You should aim for O(m) time per operation, m = max word length.
133	Design Search Autocomplete System	Design a search autocomplete system for sentences, returning top k matching sentences for current prefix.	Trie nodes store sentence frequencies.	You should aim for O(k) retrieval time, k = top results.
134	Longest Word in Dictionary	Given a list of words, find the longest word made of other words in the list.	Sort by length, use trie for prefix lookup on all substrings.	You should aim for O(nk) time, n = word count, k = max word length.
135	Word Break II	Given a string and dictionary, return all possible sentences where each word is in the dictionary.	Recursion + DP memoization for breaking sentences.	You should aim for O(2^n) time.
136	Palindrome Partitioning	Given a string s, partition s such that every substring is a palindrome.	DFS all possible partitions, check palindrome at each cut.	You should aim for O(2^n) time and O(n^2) for palindrome precomputation.
137	Restore IP Addresses	Given a string s containing digits, return all possible valid IP address combinations.	Try all splits, check validity at each step (length and value).	You should aim for O(1) per answer, total O(n^3).
138	Expression Add Operators	Given a string num and a target, insert operators (+,-,*) so the expression evaluates to target.	DFS recursive backtracking: track current value and last used value for multiplication.	You should aim for O(4^n) time for n = num length.
139	Remove Invalid Parentheses	Remove minimum number of parentheses to make the string valid, return all possible results.	BFS and track levels, stop when first valid found.	You should aim for O(n!) time for n = string size.
140	Generate Parentheses	Given n pairs of parentheses, generate all valid combinations.	Recursive backtracking – add '(' or ')' when allowed.	You should aim for O(2^n) time, n = number of pairs.
141	Merge k Sorted Lists	Merge k sorted linked lists and return it as one sorted list.	Use a min-heap or recursively merge pairs of lists.	You should aim for O(N log k) time and O(N) space, where N is total nodes.
142	Lowest Common Ancestor of a Binary Tree	Given a binary tree and two nodes, find their lowest common ancestor.	Postorder DFS and look for splits from both children.	You should aim for O(n) time and O(h) space.
143	LRU Cache	Design and implement a data structure for Least Recently Used (LRU) cache with O(1) get and put.	Use a double linked list plus a hashmap.	You should aim for O(1) time and O(capacity) space per operation.
144	Design Twitter	Design the Twitter class that supports posting tweets, retrieving the news feed, and following/unfollowing other users.	Hint: Use heaps to keep a sliding window of recent tweets, plus adjacency lists.	Recommended Time/Space: You should aim for O(log n) for retrieval, where n = number of tweets.
145	Find Median from Data Stream	Design a data structure that can return the median of incoming numbers in O(log n) time.	Two heaps: max-heap for lower half, min-heap for upper half.	You should aim for O(log n) time per insert and O(1) for median.
146	Insert Delete GetRandom O(1)	Implement a data structure that supports insert, delete, and getRandom (all O(1) average time).	HashMap + ArrayList lets you swap and remove in O(1) time.	You should aim for O(1) for all operations.
147	LFU Cache	Design and implement a data structure for Least Frequently Used (LFU) cache with O(1) get and put.	Frequency table with double linked lists for each frequency, plus a hashmap.	You should aim for O(1) time per operation.
148	Randomized Set	Design a set supporting insert, remove, and getRandom in average O(1) time.	HashMap for locations, array for values.	You should aim for O(1) time per operation.
149	Basic Calculator	Implement a basic calculator to evaluate string expressions with '+', '-', '(', ')', and non-negative integers.	Use two stacks or keep a running sum and sign, process each token.	You should aim for O(n) time and O(n) space.
150	Largest Rectangle in Histogram	Given an array of heights, find the largest rectangle that can be formed in the histogram.	Use a stack to track boundaries and compute area efficiently.	You should aim for O(n) time and O(n) space.
"""

# --- 1. Define the Anki Card Model (Template and Fields) ---

neetcode_model = genanki.Model(
  NEETCODE_MODEL_ID,
  'NeetCode 150 Card Model (TSV)',
  # Define the fields to hold the TSV data
  fields=[
    {'name': 'sno'},                     # Column 1
    {'name': 'title'},                   # Column 2
    {'name': 'problem'},                 # Column 3 (Front)
    {'name': 'hint'},                    # Column 4 (Back)
    {'name': 'recommended_time_space'},  # Column 5 (Back)
  ],
  # Define the card template (Front and Back HTML)
  templates=[
    {
      'name': 'Question Card',
      # FRONT of the card: sno, title, and problem
      'qfmt': """
        <div class="header">
          <h1>{{sno}}. {{title}}</h1>
        </div>
        <hr>
        <div class="content">
          {{problem}}
        </div>
      """,
      # BACK of the card: combines Front with hint and time/space
      'afmt': """
        {{FrontSide}}
        <hr>
        <div class="answer">
          <h3>💡 Hint</h3>
          {{hint}}
          <hr>
          <h3>⏱️ Recommended Time/Space</h3>
          {{recommended_time_space}}
        </div>
      """,
    },
  ],
  # CSS Style for better readability
  css="""
    .card {
      font-family: Arial;
      font-size: 18px;
      text-align: left;
      color: #333;
      background-color: #f7f7f7;
      padding: 20px;
    }
    .header h1 {
        color: #007ACC; /* Blue for Sno/Title */
        font-size: 24px;
        margin: 0;
    }
    .content {
        margin-top: 15px;
        font-size: 20px;
        font-weight: 500;
    }
    .answer h3 {
        color: #00A86B; /* Green for Hint/Time-Space */
        margin-top: 20px;
        margin-bottom: 5px;
        border-bottom: 2px solid #00A86B;
        display: inline-block;
        padding-bottom: 2px;
    }
    hr {
        border: none;
        border-top: 1px solid #ccc;
        margin: 10px 0;
    }
  """
)

def parse_tsv_data(tsv_string):
    """Parses the TSV string and returns a list of data fields."""
    data = []
    # Use io.StringIO to treat the string as a file and split by lines
    for line in io.StringIO(tsv_string):
        # Strip whitespace and skip empty lines
        clean_line = line.strip()
        if not clean_line:
            continue
            
        # Split by the tab character (\t)
        fields = clean_line.split('\t')
        
        # We expect exactly 5 fields based on the provided TSV format
        if len(fields) == 5:
            data.append(fields)
        # Handle cases where the problem/hint may contain an extra newline accidentally
        elif len(fields) > 5:
            # Re-join extra fields into the last one to be robust against malformed lines
            # Example: [1, title, problem part 1, problem part 2, hint, time] -> re-join part 1 & 2
            data.append([fields[0], fields[1], fields[2], fields[3], "\t".join(fields[4:])])

    return data

def create_anki_package():
    """Reads TSV data, creates Anki notes, and generates the .apkg file."""
    print("Parsing embedded TSV data...")
    parsed_data = parse_tsv_data(TSV_DATA)

    if not parsed_data:
        print("No data parsed. Exiting.")
        return

    # 2. Define Anki Deck
    neetcode_deck = genanki.Deck(NEETCODE_DECK_ID, DECK_NAME)
    
    print(f"Creating {len(parsed_data)} Anki notes...")

    # 3. Create Notes (Cards)
    for fields in parsed_data:
        sno, title, problem, hint, recommended_time_space = fields
        
        # Use a combination of sno and title to generate a unique Note ID
        note_id = sno + title
        
        # Data is already flat, but ensure HTML compatibility for line breaks
        
        note = genanki.Note(
          model=neetcode_model,
          # Map fields to match the 'fields' list definition in the model
          fields=[
            sno,
            title,
            problem,
            hint,
            recommended_time_space,
          ],
          # Ensure reproducible Note UIDs
          guid=genanki.guid_for(note_id)
        )
        neetcode_deck.add_note(note)

    # 4. Generate Anki Package
    package = genanki.Package(neetcode_deck)
    package.write_to_file(OUTPUT_APKG_FILE)
    
    print(f"\n✅ Success! Anki package generated at: {OUTPUT_APKG_FILE}")

if __name__ == '__main__':
    create_anki_package()

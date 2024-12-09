# [Platinum I] Pieces of Parentheses - 14506 

[문제 링크](https://www.acmicpc.net/problem/14506) 

### 성능 요약

메모리: 33548 KB, 시간: 1608 ms

### 분류

다이나믹 프로그래밍, 그리디 알고리즘, 배낭 문제, 정렬

### 제출 일자

2024년 11월 26일 15:20:01

### 문제 설명

<p>You are teaching a class in programming, and you want to cover balanced parentheses. You’ve got a great visual aid, a sign with a very long, balanced string of parentheses. But, alas, somehow, your visual aid has been broken into pieces, and some pieces may be missing! You’ve got to try to put it back together as best you can. Given the string of parentheses on each piece, what is the longest balanced string you can form by concatenating some of them in some order? Each piece may be used at most once, and the pieces cannot be reversed.</p>

<p>A balanced string of parentheses is defined as:</p>

<ol>
	<li>The empty string</li>
	<li>AB where A and B are both balanced strings of parentheses</li>
	<li>(A) where A is a balanced string of parentheses</li>
</ol>

### 입력 

 <p>Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. The first line of input will contain a single integer n (1 ≤ n ≤ 300), which is the number of pieces.</p>

<p>Each of the next n lines will hold a single string s (1 ≤ |s| ≤ 300), which consists only of the characters ’(’ and ’)’. This describes one of the pieces.</p>

### 출력 

 <p>Output a single integer, which is the length of the longest string of balanced parentheses you can form from the pieces. Note that the empty string is technically a balanced string of parentheses, so it is always possible to form a string of length at least 0 (although the empty string is not a very effective visual aid!).</p>


# [Platinum III] L-트로미노 계단 - 20123 

[문제 링크](https://www.acmicpc.net/problem/20123) 

### 성능 요약

메모리: 31120 KB, 시간: 36 ms

### 분류

많은 조건 분기, 해 구성하기, 분할 정복, 구현, 재귀

### 제출 일자

2024년 12월 6일 15:51:15

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1ca0cce9-314c-46bc-8a1a-70425b4a9d93/-/preview/"></p>

<p>엘과 제이는 L-트로미노를 가지고 놀고 있다.</p>

<p>L-트로미노는 1 x 1 블럭 3개를 L 모양으로 이어붙인 도형이고 회전하여 사용할 수 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/54cb901f-0f9b-40a6-a8c4-044b2dd2ddfc/-/preview/"></p>

<p style="text-align: center;">< 1층, 2층, 3층, 4층 계단 ></p>

<p>1층 계단은 1 x 1 블럭 하나만 있는 도형이며 <em>N</em>층 계단은 <em>(N-1)</em>층 계단에서 아래에 (가로 <em>N</em>) x (세로 1) 블럭을 이어 붙인 도형이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/3b1c15cb-ad9a-401b-965c-d2d72575edf4/-/preview/"></p>

<p style="text-align: center;">< L-트로미노 7개를 사용하여 만든 6층 계단 ></p>

<p>엘과 제이는 L-트로미노만을 이용하여 <em>N</em>층 계단을 만들고자 한다. 하지만 <em>N</em>이 커지면 커질수록 만들기가 엄청 복잡해졌다.</p>

<p>엘과 제이를 위해 <em>N</em>이 주어지면 L-트로미노만 이용하여 <em>N</em>층 계단을 만들어보자.</p>

### 입력 

 <p>첫 번째 줄에 계단의 높이 <em>N</em> (1 ≤ <em>N</em> ≤ 1,000) 이 주어진다.</p>

### 출력 

 <p><em>N</em>층 계단을 만들 수 없다면 첫 번째 줄에 "<code>impossible</code>" 만 출력한다.</p>

<p><em>N</em>층 계단을 만들 수 있다면 <em>i</em> (1 ≤ <em>i</em> ≤ <em>N</em>) 번째 줄에는 <em>i</em>개의 문자를 출력한다.</p>

<p>각 문자는 '<code>b</code>', '<code>p</code>' '<code>q</code>', '<code>d</code>', '<code>-</code>', '<code>|</code>' 중 하나여야 하며 하나의 L-트로미노는 '<code>b</code>', '<code>p</code>' '<code>q</code>', '<code>d</code>' 중 하나와 '<code>|</code>' 1개, '<code>-</code>' 1개 로 구성된다.</p>

<ul>
	<li>'<code>b</code>' 의 오른쪽에는 '<code>-</code>'. 위쪽에는 '<code>|</code>'</li>
	<li>'<code>p</code>' 의 오른쪽에는 '<code>-</code>'. 아래쪽에는 '<code>|</code>'</li>
	<li>'<code>q</code>' 의 왼쪽에는 '<code>-</code>'. 아래쪽에는 '<code>|</code>'</li>
	<li>'<code>d</code>' 의 왼쪽에는 '<code>-</code>'. 위쪽에는 '<code>|</code>'</li>
</ul>

<p>이 존재해야 하며 각 '<code>-</code>', 과 '<code>|</code>' 는 하나의 L-트로미노에 속해야 한다.</p>

<p>방법이 여러 가지인 경우 그 중 하나만 출력한다.</p>


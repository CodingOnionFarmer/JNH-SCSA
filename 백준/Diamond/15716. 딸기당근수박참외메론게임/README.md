# [Diamond V] 딸기당근수박참외메론게임 - 15716 

[문제 링크](https://www.acmicpc.net/problem/15716) 

### 성능 요약

메모리: 141756 KB, 시간: 332 ms

### 분류

이분 탐색, 구현, 수학

### 제출 일자

2024년 11월 26일 15:20:22

### 문제 설명

<blockquote>
<p>디디가 좋아하는 랜덤게임 ~! 무슨 게임~! 게임 스타트 !!</p>

<p>딸기당근수박참외메론게임♪</p>
</blockquote>

<p>디디대학에서의 딸기당근수박참외메론게임의 룰은 다음과 같은 규칙으로 진행된다.</p>

<ol>
	<li>게임에 쓰일 단어의 수 n과 박자 수 b를 정한다. 단, 박자수는 단어의 수보다 크거나 같아야 하며, 같은 단어가 여러 번 들어갈 수 있다.</li>
	<li>앞서 정한 n만큼, 사용할 단어(S<sub>1</sub>, S<sub>2</sub>, ..., S<sub>n</sub>)를 정한다.</li>
	<li>각 i(1, 2, ...) 차례마다 단어들을 아래 코드와 같은 결과로 말해야 한다.</li>
</ol>

<div><div id="highlighter_936842" class="syntaxhighlighter  c"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="c keyword bold">if</code><code class="c plain">(b == 1) </code><code class="c functions bold">printf</code><code class="c plain">(</code><code class="c string">"%s"</code><code class="c plain">, S[1]);</code></div><div class="line number2 index1 alt1"><code class="c keyword bold">else</code> <code class="c plain">{</code></div><div class="line number3 index2 alt2"><code class="c spaces">    </code><code class="c keyword bold">if</code> <code class="c plain">((i - 1) % (2 * (b - 1)) + 1 < b) {</code></div><div class="line number4 index3 alt1"><code class="c spaces">        </code><code class="c keyword bold">for</code> <code class="c plain">(</code><code class="c color1 bold">int</code> <code class="c plain">j = 1; j <= (i - 1) % (b - 1) + 1; j++) </code><code class="c functions bold">printf</code><code class="c plain">(</code><code class="c string">"%s "</code><code class="c plain">, S[(j - 1) % n + 1]);</code></div><div class="line number5 index4 alt2"><code class="c spaces">    </code><code class="c plain">}</code></div><div class="line number6 index5 alt1"><code class="c spaces">    </code><code class="c keyword bold">else</code> <code class="c plain">{</code></div><div class="line number7 index6 alt2"><code class="c spaces">        </code><code class="c keyword bold">for</code> <code class="c plain">(</code><code class="c color1 bold">int</code> <code class="c plain">j = 1; j <= b - ((i - 1) % (b - 1)); j++)</code></div><div class="line number8 index7 alt1"><code class="c spaces">            </code><code class="c functions bold">printf</code><code class="c plain">(</code><code class="c string">"%s "</code><code class="c plain">, S[(j - 1) % n + 1]);</code></div><div class="line number9 index8 alt2"><code class="c spaces">    </code><code class="c plain">}</code></div><div class="line number10 index9 alt1"><code class="c plain">}</code></div></div></td></tr></tbody></table></div></div>

<p>단어 집합 S는 번호가 1부터 시작됨에 유의하라.</p>

<p>예를 들어, n은 3, b는 5, 집합 S = {king, god, gd}일 때,</p>

<ul>
	<li>king</li>
	<li>king god</li>
	<li>king god gd</li>
	<li>king god gd king</li>
	<li>king god gd king god</li>
	<li>king god gd king</li>
	<li>king god gd</li>
	<li>king god</li>
	<li>king</li>
	<li>king god</li>
	<li>...</li>
</ul>

<p>각 차례마다 위와 같은 순서대로 말해야한다.</p>

<p>디디는 문득 게임내에서 임의의 단어 k가 외쳐진 횟수가 X번째가 될 때, 그 차례가 몇번 째 인지 궁금해지기 시작했다. 그런 디디의 궁금증을 해결해 줄 프로그램을 작성하라.</p>

### 입력 

 <p>첫째 줄에 n(1 ≤ n ≤ 2 × 10<sup>5</sup>)과 b(n ≤ b ≤ 10<sup>12</sup>)가 주어진다.</p>

<p>둘째 줄에는 임의의 단어 k와 X(1 ≤ X ≤ 10<sup>12</sup>)가 주어진다.</p>

<p>셋째 줄에는 게임에 쓰일 단어 n개가 공백으로 구분되어 주어진다. 모든 단어는 알파벳 소문자로 구성되어 있으며, 각 단어의 길이는 10을 넘지 않는다.</p>

### 출력 

 <p>문제의 정답을 출력하라. 정답이 항상 존재하는 경우만 입력으로 주어지는 것이 보장된다.</p>


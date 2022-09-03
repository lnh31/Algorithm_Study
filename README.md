# 🔥 멀티캠퍼스 알고리즘 스터디 🔥

<img width = "70%" src="https://user-images.githubusercontent.com/97590480/156875708-2d6bee9b-ce5c-4bbc-875a-5d6d5d85e51e.gif">

## ❗ 어떤 스터디인가요?

저희는 IT기업 입사에 필요한 코딩 테스트를 파이썬 언어를 사용하여 우수한 성적으로 통과하기 위해 학습하고 의견을 나누는 알고리즘 스터디입니다.
1. 코딩 테스트에 자주 나오는 개념에 대한 학습 및 백준 or 프로그래머스의 문제들을 풀면서 익힙니다.
2. 어느정도 코딩 테스트에 필요한 내용들을 학습했다면, 기출문제 위주로 문제풀이를 진행합니다.

## ❗ 어떤 식으로 진행되나요?

1. 1주일에 풀 문제를 선정하여 문제를 푼 뒤, 깃헙에 올립니다.
2. 매주 목요일 10시에 만나서 자신이 푼 문제에 대한 코딩 리뷰를 진행하고 피드백을 진행합니다.
3. 전날 12시까지(적어도 당일 점심까지) 레퍼지토리에 코드를 업로드해주셔야 합니다.

## ❗ 어떤 규칙을 지켜야 하나요?

### ✅ 파일 생성 및 업로드 규칙

1. 매주 새로운 디렉토리를 만듭니다. ex) 1주차, 2주차..
2. 디렉토리 안에 문제 디렉토리를 만듭니다. ex) 백준 1000번 문제라면 BOJ_1000
3. 문제 디렉토리 안에 각자 푼 문제를 `BOJ_1000_홍길동`의 형식으로 업로드합니다.
4. 최종적인 경로는 `1주차/BOJ_1000/BOJ_1000_홍길동` 입니다.

### ✅ 깃헙 Push/Pull 규칙

1. 무조건 __pull__ 먼저 해줍니다. pull을 해서 해당 주차의 디렉토리가 생기지 않는다면 따로 만들어주세요

```
$ git pull <remote 이름> <브랜치이름>
$ git pull AlgorithmStudy master
```

2. 파일 업로드 규칙에 맞게 push해주세요.
```
$ git add .
$ git commit -m "BOJ_1000_홍길동"
$ git push <remote 이름> master
```

3. 만일 push를 하다가 __충돌__ 이 일어났을 경우 아래의 코드를 입력해주세요
```
$ git log --oneline
```
입력 후 내가 push한 커밋 바로 전 커밋 코드를 복사해줍니다. 그리고 다음을 입력해주세요
```
$ git reset --soft [복사한 커밋 코드]
```

4. 만일 내가 올린 코드에 수정/추가 등의 추가 커밋을 push할 경우에 커밋 형식을 다음과 같이 작성해주세요. 수정을 2번째 할 경우에 `fix2`를 붙여주시면 됩니다.

```
git commit -m "BOJ_1000_홍길동_fix"
git commit -m "BOJ_1000_홍길동_add"
```

## 📆 알고리즘 스터디 기록

### 🐱 백준

|날짜|개념|알고리즘 문제|문제번호|
|:---:|:---:|:---:|:---:|
|3.10|입출력|별 찍기, 문자열 반복, 크로아티아 알파벳, 팰린드롬, 크로스워드 만들기|BOJ_10995, BOJ_2675, BOJ_2941, BOJ_8892, BOJ_2804|
|3.17|list, dictionary|나는 요리사다, 평균은 넘겠지, 나무 조각, 명령 프롬프트, 세로 읽기, 색종이, 직사각형 네 개의 합집합의 면적 구하기, 스도쿠 체점, 듣보잡, 다이얼, 나는야 포켓몬 마스터 이다솜, 2021 카카오 인턴 기출|BOJ_2804, BOJ_2953, BOJ_4344, BOJ_2947, BOJ_1032, BOJ_10798, BOJ_2563, BOJ_2669, BOJ_9291, BOJ_1764, BOJ_5622, BOJ_1620, PRO_KAKAO2021|
|3.31|재귀, 정렬, 브루트포스, 구현, 그리디|별 찍기 - 10, 나이순 정렬, 퇴사, 배열 복원하기, 에너지 드링크|BOJ_2447, BOJ_10814, BOJ_14501 BOJ_16967, BOJ_20115|
|4.7|동적 계획법, 스택, 그리디, 정렬, 브루트포스|포도주시식, 스택, 동전0, 좌표 정렬하기, 연구소|BOJ_2156, BOJ_10814, BOJ_11047, BOJ_11650|
|4.14|다이나믹 프로그래밍, 트리, 백트래킹, 브루트포스|1로 만들기, 트리 순회, 스타트와 링크, 카드 구매하기|BOJ_1463, BOJ_1991, BOJ_11052, BOJ_14889|
|4.28|다이나믹 프로그래밍, 트리, 백트래킹, 브루트포스|쉬운 계단 수, 가장 긴 감소하는 부분 수열, 트리의 부모 찾기|BOJ_10844, BOJ_11722, BOJ_11725, BOJ_15649|
|5.5|그리디 알고리즘, 구현, 다이나믹 프로그래밍, 브루트포스|ATM, 통계학, 2xn 타일링, 카카오 2021 인턴쉽 기출문제|BOJ_2108, BOJ_11399, BOJ_11726, 프로그래머스|
|5.12|dfs, bfs, 다이나믹 프로그래밍, 수학|dfs/bfs, 이친수, 계단 오르기, 파도반 수열, 카카오 2020 인턴쉽 문제 1|BOJ_1260, BOJ_2193, BOJ_2579, BOJ_9461|
|5.19|dfs, bfs, 그리디 알고리즘, 다이나믹 프로그래밍, 구현|미로 만들기, 잃어버린 괄호, 촌수계산, 단어뒤집기|BOJ_1347, BOJ_1541, BOJ_2644, BOJ_17413|
|5.26|플로이드-와샬, 구현, 시뮬레이션, 그리디 알고리즘, 정렬|케빈베이컨, 후보 추천하기, 거북이, Yonsei TOTO,  로봇청소기|BOJ_1389, BOJ_1713, BOJ_8911, BOJ_12018, BOJ_14503|
|6.16|다이나믹 프로그래밍, 큐, 구현, 시뮬레이션|01타일, 프린터 큐, 다각형 그리기, 로봇|BOJ_1904, BOJ_1966, BOJ_2641, BOJ_13567|
|6.23|그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 구현, 스택, 재귀, 큐 시뮬레이션|유기농 배추, 괄호의 값, 트럭, 신과결과받기|BOJ_1012, BOJ_2504, BOJ_13335, 카카오 2022 BLIND RECRUIMENT|
|6.30|그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색|미로탐색, 섬의 개수, 로봇|BOJ_2178, BOJ_4963, BOJ_7576|
|7.7|동적 프로그래밍, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색|동물원, 나이트의 이동, N과 M (12)|BOJ_1309, BOJ_7562, BOJ_15666|
|7.14|그래프 탐색,깊이 우선 탐색, 플로이드-와샬|단지번호붙이기, 플로이드, 양궁대회, 크레인인형뽑기|BOJ_2667,BOJ_11404, 카카오 2019 겨울 인텁십, 카카오 2022 BLIND RECRUIMENT|
|7.21|동적 프로그래밍, 그래프 탐색, 깊이 우선 탐색, 구현|동전 1, 연구소, 치킨배달, 프렌즈4블록|BOJ_2293, BOJ_14502, BOJ_15686, 카카오 2018 BLIND RECRUIMENT|
|7.28|동적 프로그래밍, 그래프 탐색, 깊이 우선 탐색, 구현|리모컨, LCS, 방금그곡|BOJ_1107, BOJ_9251, 카카오 2018 BLIND RECRUIMENT|
|8.4|동적 프로그래밍, 그래프 탐색, 깊이 우선 탐색, 구현|내리막 길, 암호코드, 토마토, 소수찾기|BOJ_1520, BOJ_2011, BOJ_7569, 프로그래머스 연습문제|
|8.11|그리디 알고리즘, 정렬, 수학|신입사원, 안테나|BOJ_1946, BOJ_18310|
|8.25|그리디 알고리즘, 정렬, 구현|수리공 항승, 주식, 성격유형 검사하기|BOJ_1449, BOJ_11501, 카카오 TECH INTERSHIP 2022|
|9.2|그리디 알고리즘, 정렬, 다이나믹 프로그래밍, 자료구조|동물원, 흙길 보수하기, 스티커, 프린터, 두 큐 합 같게 만들기|BOJ_1309, BOJ_1911, BOJ_9465, 프로그래머스 연습문제, 카카오 TECH INTERSHIP 2022|

## 💖 참고사항

### 💕 원격 저장소 등록하기
1. 원하는 디렉토리에 clone해서 다운받습니다. 

```bash
$ git clone https://github.com/Trailblazer-Yoo/Algorithm_Study
```

2. `git remote add <원격저장소 이름> <주소>` 형식으로 작성합니다.

```bash
$ git remote add algorithmStudy https://github.com/Trailblazer-Yoo/Algorithm_Study
```

### 💕 원격 저장소 조회


`git remote -v`로 등록이 잘 됐는지 확인해봅니다.
```
$ git remote -v
algorithmStudy https://github.com/Trailblazer-Yoo/Algorithm_Study (fetch)
algorithmStudy https://github.com/Trailblazer-Yoo/Algorithm_Study (push)
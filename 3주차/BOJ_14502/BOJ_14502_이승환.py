# 행렬 정보를 N x M 이중리스트에 저장
# 1단계 : 벽을 세울 수 있는 모든 경우의 수에 벽을 세움.
# 2단계 : 바이러스가 있는 위치를 저장, BFS로 바이러스가 퍼질 수 있는 구역을 탐색.
# 3단계 : 최종 결과 안전지역의 수를 저장, 가장 높은 값을 출력

# 행렬 정보 받기
n,m = map(int,input().split())
lab = [list(input().split()) for _ in range(n)]

# 1단계, 연구실 이중리스트를 받아 벽을 세우고, 그 정보(리스트)를 반환
# 벽 세우는 아이디어
# 0 원소중에서 3개를 뽑는 조합을 구함.
# 해당 조합에서 사용하는 값은 0 원소의 인덱스값.

# 조합을 구하는 함수
def comb_zero(list):
    pass

# 구한 조합을 가지고 벽을 세우는 함수
def wall(list):
    pass

# 2단계, 리스트를 받아 최종 안전지역의 수를 반환
# 1. 2가 있는 인덱스를 모두 리스트에 저장
# 2. 첫번째 2에서 BFS실시, 인접 노드가 1일경우 멈춤, 인접 노드가 0일경우 추가 탐색
# 2-1. 2 노드를 큐에 삽입하고 방문처리
# 2-2. 2 주변노드를 큐에 삽입하고 방문처리
# 3. 모든 인접노드가 1인경우 탐색종료, 탐색하지 않은 2에서 재탐색 실시.
# 주의 : 탐색중에 2을 만날 경우 0과 같이 판단하되, 2가 저장된 리스트에서 삭제
def virus(list):
    pass

# 3단계, 안전지역의 수를 카운트
# 0의 개수를 세는 함수.
def count_zero(list):
    pass
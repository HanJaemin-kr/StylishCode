import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) #노드,간선 수
start = int(input()) #시작 노드
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):  # 모든 간선 정보 입력
    a,b,c = map(int, input().split())
    graph[a].append((b,c))


# 방문하지 않은 노드 중 , 최단 거리가 짧은 노드의 번호 반환  ( 단지 최단 노드 선택을 위한 ㄴ용도)
def get_smallest_node():
    min_value = INF
    index = 0  #최단 거리가 가장 짧은 노드( index )
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index

def dijkstra(start):
    #시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost



dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])
from collections import deque

//deque사용해서 하나씩 처리
def bfs(distance, graph):
  //첫번째 노드 1번부터 노드 1은 거리가 0
    node=1
    count = 0
    q = deque([[node, count]])
    while q: // q에 모든 노드가 스쳐 지나갈 때까지 실행
      // 노드를 하나씩 꺼냄
        node, count = q.popleft()
      // 만약에 노드가 초기화 상태라면 현재 카운트를 기록
        if distance[node] == -1:
            distance[node] = count
            // 다음 노드들은 거쳐서 가야하니까 1회 더 증가함
            count += 1
            // 빠져나가는 노드에 연결된 노드들을 q에 삽입
            for e in graph[node]:
              q.append([e, count])
              
              
// 1번부터 세기 위해서 n+1으로 처리, distance를 일단 -1로 처리(모든노드)
def solution(n, edge):
    distance = [-1] * (n + 1)
    graph=make_graph(n+1, edge)
    bfs(distance, graph)
    return distance.count(max(distance))

// 각 노드마다 연결된 노드 번호 리스트로 표현
def make_graph(n, edge):
  graph= [[] for _ in range(n)]
  for s, d in edge:
    graph[s].append(d)
    graph[d].append(s)
  return graph

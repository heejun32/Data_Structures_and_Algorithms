import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        dist = collections.defaultdict(int)
    
        # 그래프 인접 리스트 구현
        for u, v, w in times:
            graph[u].append((v, w))
        
    
        Q = [(0, k)]
        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        if len(dist) == n:
            return max(dist.values())
        return -1
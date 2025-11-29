def dist(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

def c(startIndex, points, distMatrix):
    n = len(points)
    visited = [False] * n
    current = startIndex
    visited[current] = True
    totalTime = 0
    
    for _ in range(n - 1):
        minDist = float('inf')
        nextPoint = -1
        
        for j in range(n):
            if not visited[j]:
                d = dist(points[current][0], points[current][1], 
                        points[j][0], points[j][1])
                if d < minDist or (d == minDist and j < nextPoint):
                    minDist = d
                    nextPoint = j
        
        totalTime += minDist
        current = nextPoint
        visited[current] = True
    
    return totalTime

n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

# Предвычисляем матрицу расстояний O(n²)
distMatrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distMatrix[i][j] = dist(data[i][0], data[i][1], data[j][0], data[j][1])

minTime = float('inf')
for i in range(n):
    t = c(i, data, distMatrix)
    minTime = min(minTime, t)

print(minTime)

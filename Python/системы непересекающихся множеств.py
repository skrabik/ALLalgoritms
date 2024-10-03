"""
 https://habr.com/ru/articles/104772/
 Типичные problems, для решения которых используется DSU:
 1) Остов минимального веса
 Дан неориентированный связный граф со взвешенными ребрами. Выкинуть из него некоторые ребра так, чтобы в итоге получилось дерево, причем суммарный вес ребер этого дерева должен быть наименьшим.
 (решение: Алгоритм Краскала для решения этой задачи: отсортируем все ребра по возрастанию веса и будем поддерживать текущий лес минимального веса с помощью DSU. Изначально DSU состоит из N деревьев, по одной вершине в каждом. Идем по ребрам в порядке возврастания; если текущее ребро объединяет разные компоненты — сливаем их в одну и запоминаем ребро как элемент остова. Как только количество компонент достигнет единицы — мы построили искомое дерево.)

 2) Алгоритм Тарьяна для поиска LCA
 Дано дерево и набор запросов вида: для данных вершин u и v вернуть их ближайшего общего предка (least common ancestor, LCA). Весь набор запросов известен заранее, т.е. задача сформулирована в режиме оффлайн.
 (решение если номера вершин пронумерованы "Хорошо" - файл ближайший общий предок)
 (решение: !Дерево может быть не бинарным! Запустим для начала поиск в глубину по дереву. Рассмотрим некоторый запрос <u, v>. Пускай поиск в глубину пришел в такое состояние, что одна из вершин запроса (скажем, u) уже была посещена поиском ранее, и сейчас текущей вершиной в поиске является v, все поддерево v только что было осмотрено. Очевидно, что ответом на запрос будет либо сама вершина v, либо какой-то из её предков. Причем каждый из предков v по пути к корню порождает некоторый класс вершин u, для которых он является ответом: этот класс в точности равен уже просмотренной ветке дерева «слева» от такого предка. Классы таких вершин не пересекаются между собой, а значит, их можно поддерживать в DSU. Как только поиск в глубину вернется из поддерева — сливать класс этого поддерева с классом текущей вершины. И для поиска ответа поддерживать массив Ancestor — для каждой вершины собственно предок, породивший класс этой вершины. Значение ячейки этого массива для представителя надо не забыть переписать при слиянии деревьев. Зато теперь в процессе поиска в глубину для каждой полностью обработанной вершины v мы можем найти в списке запросов все <u, v>, где u — уже обработана, и вывести ответ: Ancestor[Find(u)]. )

 3) Компоненты связности в мультиграфе
 Дан мультиграф (граф, в котором пара вершин может быть соединена более чем одним непосредственным ребром), к которому поступают запросы вида «удалить некоторое ребро» и «а сколько сейчас в графе компонент связности?» Весь список запросов известен заранее.

 (Решение банально. Выполним сначала все запросы на удаление, посчитаем количество компонент в итоговом графе, запомним его. Получившийся граф запихнем в DSU. Теперь будем идти по запросам удаления в обратном порядке: каждое удаление ребра из старого графа означает возможное слияние двух компонент в нашем «flashback-графе», хранящемся в DSU; в таком случае текущее количество компонент связности уменьшается на единичку.)

"""


# Объектная реализация
class DSU:
    """
    Класс, реализующий системы непересекающихся множеств
    """

    def __init__(self):

        self.p = [0]
        # этот функционал можно опустить (он не доделан)
        self.height = [1]

    def MakeSet(self, x):
        self.p.append(x)

    def Find(self, x):
        if self.p[x] == x:
            return x
        self.p[x] = self.Find(self.p[x])
        return self.p[x]

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)

        self.p[x] = y

        # реализация с высотой поддерева
        # if self.height[x] < self.height[y]:
        #     self.p[x] = y
        # else:
        #     self.p[y] = x

        # можно ничего не возвращать
        return y


# Функциональная реализация (Должна быть побыстрее и по памяти лучше)
arr = [i for i in range(6)]

def MakeSet(arr, el):
    return arr.append(el)

def Find(arr, el):
    if arr[el] == el:
        return el
    arr[el] = Find(arr, arr[el])
    return arr[el]

def Union(arr, x, y):
    x = Find(arr, x)
    y = Find(arr, y)

    arr[x] = y
    return arr

class DSU_New:
    def __init__(self, n):
        self.sets = [i for i in range(n+1)]
        self.quantity = [1 for i in range(n+1)]

    def get_parent(self, u):
        if self.sets[u] == u:
            return u
        self.sets[u] = self.get_parent(self.sets[u])
        return self.sets[u]

    def union(self, u, v):
        u = self.get_parent(u)
        v = self.get_parent(v)
        if u == v: 
            return
        
        if self.quantity[u] < self.quantity[v]:
            u, v = v, u
        self.quantity[u] += self.quantity[v]
        self.sets[v] = u
        return u
    
    def check(self, u, v):
        return self.get_parent(u) == self.get_parent(v)
    

class DSU_segments:
    def __init__(self, n):
        self.sets = [i for i in range(n+1)]
        self.quantity = [1 for i in range(n+1)]
        self.rigth = [i for i in range(n+1)]

    def get_parent(self, u):
        if self.sets[u] == u:
            return u
        self.sets[u] = self.get_parent(self.sets[u])
        return self.sets[u]

    def union(self, L, R):
        L, R = self.get_parent(L), self.get_parent(R)
        if L == R: 
            return
        if self.quantity[R] < self.quantity[L]:
            R, L = L, R
        self.quantity[R] += self.quantity[L]
        self.sets[L] = R
        self.rigth[L] = max(self.rigth[L], self.rigth[R])
    
    def check(self, u, v):
        return self.get_parent(u) == self.get_parent(v)
    

class DSU_whith_Rollbacks:
    def __init__(self, n):
        self.sets = [i for i in range(n+1)]
        self.quantity = [1 for i in range(n+1)]
        self.history = []
        self.count = n
        self.points = []

    def get_parent(self, u):
        if self.sets[u] == u:
            return u
        return self.get_parent(self.sets[u])

    def union(self, u, v):
        u = self.get_parent(u)
        v = self.get_parent(v)
        if u == v: 
            print(self.count)
            return
        self.count -= 1
        print(self.count)
        if self.quantity[u] < self.quantity[v]:
            u, v = v, u
        self.quantity[u] += self.quantity[v]
        self.history.append([v, self.sets[v], self.count])
        self.sets[v] = u
    
    def set_checkpoint(self):
        self.points.append(len(self.history))

    def rollback(self):
        point = self.points.pop()
        while len(self.history) > point:
            ver, val, c = self.history.pop()
            self.sets[ver] = val
        if len(self.history):
            self.count = self.history[-1][2]
        else:
            self.count = n
        print(self.count)

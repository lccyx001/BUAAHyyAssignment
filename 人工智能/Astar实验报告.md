# A*实验报告

## 实验内容

学习A*搜索算法的思想，使用Python实现A*搜索算法。

## 实验代码

A*搜索的核心代码实现

```python
def searching(self):
        """
        A_star Searching.
        :return: path, visited order
        """

        self.PARENT[self.s_start] = self.s_start  # PARENT保存记录过的点
        self.g[self.s_start] = 0  # g保存所有计算过的点
        self.g[self.s_goal] = math.inf # 不可达的点的cost为无穷
        heapq.heappush(self.OPEN,
                       (self.f_value(self.s_start), self.s_start)) # 使用优先队列保存所有的点，方便计算

        while self.OPEN:
            _, s = heapq.heappop(self.OPEN)
            self.CLOSED.append(s)

            if s == self.s_goal:  # stop condition
                break

            for s_n in self.get_neighbor(s): # 发现相邻节点
                new_cost = self.g[s] + self.cost(s, s_n)

                if s_n not in self.g:
                    self.g[s_n] = math.inf

                if new_cost < self.g[s_n]:  # conditions for updating Cost
                    self.g[s_n] = new_cost
                    self.PARENT[s_n] = s
                    heapq.heappush(self.OPEN, (self.f_value(s_n), s_n))

        return self.extract_path(self.PARENT), self.CLOSED
```

其中 get_neighbor() 用于发现相邻节点

```python
def get_neighbor(self, s):
        """
        find neighbors of state s that not in obstacles.
        :param s: state
        :return: neighbors
        """

        return [(s[0] + u[0], s[1] + u[1]) for u in self.u_set]
```

u_set 包含点的可移动方向

```python
u_set = [(-1, 0), (-1, 1), (0, 1), (1, 1),(1, 0), (1, -1), (0, -1), (-1, -1)]
```

cost()函数用于计算

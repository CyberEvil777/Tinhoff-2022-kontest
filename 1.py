class Task1():
    """Класс для решения задачи"""
    __slots__ = ['a', 'b', 'n']

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def solve_task(self):
        """ Решение задачи"""
        if any([self.a <= self.b, (self.a - self.b) % 2, self.a > self.b and self.n == 0]):
            return 'NO'
        else:
            s = (self.a - self.b) // 2
            return 'Yes' if self.n <= s else 'No'


a, b, n = map(int, input().split())
task = Task1(a, b, n)

if __name__ == '__main__':
    print(task.solve_task())
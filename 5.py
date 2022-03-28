n, k = map(int, input().split())


def solve_task(n, k):
    """Функция для проверки красоты перестановка"""
    data = 0
    count = 0
    for index, value in enumerate(n):
        data += (index+1) * value
    if data % k == 0:
        count = 1
    return count


def massive_gen(n):
    """Функция генерирует массив"""
    massive = []
    for value in range(1, n+1):
        massive.append(value)
    return massive


def main():
    """Функция создагия перестановки"""
    df = []
    massive = massive_gen(n)
    count = 0
    for i in range(0, len(massive)):
        for j in range(0, len(massive)):
            for l in range(0, len(massive)):
                if(i != j & j != l & l != i):
                    df.append(massive[i])
                    df.append(massive[j])
                    df.append(massive[l])
                    count += solve_task(df, k)
                    df = []
    return count


if __name__ == '__main__':
    print(main())


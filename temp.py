from math import sqrt


MESSAGE: str = 'Добро пожаловать в самую лучшую программу для вычисления квадратного корня из заданного числа'


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return
    root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из'
          f' введённого вами числа. Это будет: {root}')


if __name__ == "__main__":    
    print(MESSAGE)
    calc(25.5)

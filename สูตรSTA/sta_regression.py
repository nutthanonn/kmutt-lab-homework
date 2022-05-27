import math
import string


class Regresstion:
    def __init__(self, x, y, n) -> None:
        self.n = n
        self.x = x
        self.y = y

    def sigma_x(self) -> float:
        return sum(self.x)

    def sigma_y(self) -> float:
        return sum(self.y)

    def mean_x(self) -> float:
        return sum(self.x) / len(self.x)

    def mean_y(self) -> float:
        return sum(self.y) / len(self.y)

    def sigma_x_2(self) -> float:
        return sum(list(map(lambda x: x**2, self.x))) - (self.sigma_x()**2 / self.n)

    def sigma_y_2(self) -> float:
        return sum(list(map(lambda y: y**2, self.y))) - (self.sigma_y()**2 / self.n)

    def sigma_xy(self) -> float:
        return sum([i*j for i, j in zip(self.x, self.y)]) - (self.sigma_x() * self.sigma_y() / self.n)

    def b1(self) -> float:
        return self.sigma_xy() / self.sigma_x_2()

    def b0(self) -> float:
        return self.mean_y() - self.b1()*self.mean_x()

    def Y(self) -> str:
        return f"y_hat = {self.b0():.2f} + {self.b1():.2f}X"

    def r(self) -> float:
        return self.sigma_xy() / math.sqrt(self.sigma_x_2() * self.sigma_y_2())


x = [0.8, 1.0,      1.6,      2.0,      2.2,      2.6,
     3.0, 3.0,     4.0,      4.0,       4.0,       4.6]
y = [22, 28, 22, 26, 34, 18, 30, 38, 30, 40, 50, 46]
obj = Regresstion(x=x, y=y, n=12)
print(obj.Y())

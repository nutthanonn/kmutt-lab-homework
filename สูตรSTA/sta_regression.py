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


x = [10, 9.3, 13.0, 10.5, 11.8, 11.5, 12, 10.8, 15.5]
y = [287.8, 286.8, 358, 278.3, 344.8, 292.5, 317.5, 313.5, 440.3]
obj = Regresstion(x=x, y=y, n=9)
print(obj.r())

import math
import statistics


"""


>> Note

f(1-alpha/2, v1v2) = 1 / f(alpha/2, v2v1)

สัญลักษณ์
cv = s^2

สูตร 11 ไม่มีในชีท

---- ประมาณค่าเฉลี่ยของประชากรแบบช่วง ----

S1 ทราบ sigma
S2 ไม่ทราบ sigma^2 และ n < 30
S3 ไม่ทราบ sigma^2 และ n > 30

---- ประมาณสัดส่วนของประชากรแบบช่วง ----

S4

---- ประมาณค่าความแปรปวนของประชากรแบบช่วง ----

S5

--- ประมาณค่าผลต่างระหว่างค่าเฉลี่ยของสองประชากรแบบช่วง ---

S6 ทราบ sigma1 sigma2 แต่ n < 30 
S7 ไม่ทราบ sigma1 sigma2 แต่ sigma1 = sigma2 แต่ n < 30 
S8 ทราบ sigma1 sigma2 และ sigma1 != sigma2 แต่ n < 30 
S9 ไม่ทราบ sigma1 sigma2 และ n > 30 

--- ข้อมูลไม่อิสระต่อกัน ---

S10

---- ประมาณสัดส่วนของสองประชากรแบบช่วง ----

S12

---- ประมาณอัตราส่วนระหว่างความแปรปวนของสองประชากรแบบช่วง ----

S13
    
"""


class STA:
    def __init__(self, data) -> None:
        self.data = data

    def Mean(self):
        return statistics.mean(self.data)

    def SD(self):
        SD = statistics.stdev(self.data)
        print(f"SD : {SD}")
        return SD

    def CV(self):
        return statistics.stdev(self.data)**2

    @staticmethod
    def ErrorS4(z, p_hat, n):
        e = z*math.sqrt(p_hat*(1-p_hat) / n)
        print(f"Erroe <= {e}")

    @staticmethod
    def SP(n1, n2, cv1, cv2):
        val = ((n1-1)*cv1 + (n2-1)*cv2) / (n1+n2-2)
        return math.sqrt(val)

    @staticmethod
    def p_hat(x, n):
        return x/n

    @staticmethod
    def find_error_s4(p_hat, e, z):
        e = p_hat*(1-p_hat)*((z/e)**2)
        print(f"error = {e}")

    @staticmethod
    def find_n_s4(z, e):
        val = (z/(2*e))**2
        print(f"n = {val}")

    @staticmethod
    def s7_df(cv1, cv2, n1, n2):
        return (cv1/n1 + cv2/n2)**2 / (((cv1/n1)**2 / (n1-1)) + ((cv2/n2)**2 / (n2-1)))

    @staticmethod
    def s1(z, sigma, n, mean):
        min_val = mean - z*(sigma/math.sqrt(n))
        max_val = mean + z*(sigma/math.sqrt(n))
        print(f"{min_val:.6f} < u < {max_val:.6f}")

    @staticmethod
    def s2(t, s, n, mean):
        min_val = mean - t*(s/math.sqrt(n))
        max_val = mean + t*(s/math.sqrt(n))
        print(f"{min_val:.6f} < u < {max_val:.6f}")

    @staticmethod
    def s3(z, s, n, mean):
        min_val = mean - z*(s/math.sqrt(n))
        max_val = mean + z*(s/math.sqrt(n))
        print(f"{min_val:.6f} < u < {max_val:.6f}")

    @staticmethod
    def s4(z, p_hat, n):
        min_val = p_hat - z*(math.sqrt((p_hat*(1-p_hat))/n))
        max_val = p_hat + z*(math.sqrt((p_hat*(1-p_hat))/n))
        print(f"{min_val:.6f} < p < {max_val:.6f}")

    @staticmethod
    def s5(n, cv, cai_sqrt_min, cai_sqrt_max):
        min_val = ((n-1)*cv) / cai_sqrt_min
        max_val = ((n-1)*cv) / cai_sqrt_max
        print(f"{min_val:.6f} < sigma^2 < {max_val:.6f}")

    @staticmethod
    def s6(sigma1, sigma2, mean1, mean2, z, n1, n2):
        min_val = (mean1 - mean2) - z*math.sqrt(sigma1/n1 + sigma2/n2)
        max_val = (mean1 - mean2) + z*math.sqrt(sigma1/n1 + sigma2/n2)
        print(f"{min_val:.6f} < u1 - u2 < {max_val:.6f}")

    @staticmethod
    def s7(mean1, mean2, t, n1, n2, sp):
        min_val = (mean1 - mean2) - t*sp*math.sqrt(1/n1 + 1/n2)
        max_val = (mean1 - mean2) + t*sp*math.sqrt(1/n1 + 1/n2)
        print(f"{min_val:.6f} < u1 - u2 < {max_val:.6f}")

    @staticmethod
    def s8(sigma1, sigma2, mean1, mean2, t, n1, n2):
        min_val = (mean1 - mean2) - t*math.sqrt(sigma1/n1 + sigma2/n2)
        max_val = (mean1 - mean2) + t*math.sqrt(sigma1/n1 + sigma2/n2)
        print(f"{min_val:.6f} < u1 - u2 < {max_val:.6f}")

    @staticmethod
    def s9(cv1, cv2, mean1, mean2, z, n1, n2):
        min_val = (mean1 - mean2) - z*math.sqrt(cv1/n1 + cv2/n2)
        max_val = (mean1 - mean2) + z*math.sqrt(cv1/n1 + cv2/n2)
        print(f"{min_val:.6f} < u1 - u2 < {max_val:.6f}")

    @staticmethod
    def s10(mean_d, t, s, n):
        min_val = mean_d - t*(s/math.sqrt(n))
        max_val = mean_d + t*(s/math.sqrt(n))
        print(f"{min_val:.6f} < ud < {max_val:.6f}")

    @staticmethod
    def s12(p1_hat, p2_hat, z, n1, n2):
        min_val = p1_hat-p2_hat - z * \
            math.sqrt((p1_hat*(1-p1_hat)/n1) + (p2_hat*(1-p2_hat)/n2))
        max_val = p1_hat-p2_hat + z * \
            math.sqrt((p1_hat*(1-p1_hat)/n1) + (p2_hat*(1-p2_hat)/n2))
        print(f"{min_val:.6f} < p1 - p2 < {max_val:.6f}")

    @staticmethod
    def s13(cv1, cv2, f_v1v2, f_v2v1):
        min_val = cv1/cv2 * 1/f_v1v2
        max_val = cv1/cv2 * f_v2v1
        print(f"{min_val:.6f} < sigma1^2 / sigma2^2 < {max_val:.6f}")


temp = STA([1.9, 2.4, 3, 3.5, 4.2])
# temp.s4(z=1.96, p_hat=34/40, n=40)
# temp.s5(n=5, cv=temp.CV(), cai_sqrt_max=0.484, cai_sqrt_min=11.143)
# temp.s11(z=1.96, p1_hat=0.05, p2_hat=0.04, n1=1500, n2=2000)
# temp.s13(cv1=64, cv2=49, f_v1v2=3.29, f_v2v1=2.89)


temp.s5(n=10, cv=0.15**2, cai_sqrt_max=2.088, cai_sqrt_min=21.666)

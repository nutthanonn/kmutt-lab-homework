import math
def mosteller(w, h):
    return math.sqrt(w*h) / 60

def du_bois(w, h):
    return 0.007184 * w**0.425 * h**0.725

def fujimoto(w, h):
    return 0.008883 * w**0.444 * h**0.663

def main():
    weight = float(input())
    height = float(input())
    print(f"Mosteller = {round(mosteller(weight, height), 5)}")
    print(f"Du Bois = {round(du_bois(weight, height), 5)}")
    print(f"Fujimoto = {round(fujimoto(weight, height), 5)}")


exec(input())

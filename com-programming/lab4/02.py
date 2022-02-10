nums_bin = input().split()
n = int(nums_bin[0], 2) + int(nums_bin[1], 2)
print(bin(n)[2::])
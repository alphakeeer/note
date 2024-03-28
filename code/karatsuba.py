import time

recursionBase = 10


def karatsuba(x, y):
    if len(str(x)) < recursionBase or len(str(y)) < recursionBase:
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    high1, low1 = divmod(x, 10**half)
    high2, low2 = divmod(y, 10**half)
    z0 = karatsuba(low1, low2)
    z2 = karatsuba(high1, high2)
    z1 = karatsuba((low1 + high1), (low2 + high2)) - z2 - z0
    return (z2 * 10**(2*half)) + (z1 * 10**half) + z0

# # 生成不同长度的数字进行测试
# lengths = [4, 8, 16, 32, 64, 128, 256, 512, 1024]

# print("递归基准条件： "+str(recursionBase))
# print("Length\tKaratsuba Time\tBuilt-in Time")
# for length in lengths:
#     x = int("9" * length)
#     y = int("9" * length)

#     start_time = time.time()
#     karatsuba(x, y)
#     karatsuba_time = time.time() - start_time

#     start_time = time.time()
#     x * y
#     builtin_time = time.time() - start_time

#     print(f"{length}\t{karatsuba_time:.10f}\t{builtin_time:.10f}")


a = -100
b = 999
print(karatsuba(a, b))

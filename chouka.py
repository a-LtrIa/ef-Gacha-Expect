import numpy as np
import matplotlib.pyplot as plt

Pro_base = 0.008          # 基础概率 0.8%
N = 1000000               # 模拟 100 万次完整抽卡（每次直到出六星）
u = []                    # 记录每次出六星是在第几次抽卡

for _ in range(N):
    s = 0                 # 当前连续未出次数
    while True:
        s += 1
        if s <= 65:
            p = Pro_base
        elif s < 80:
            p = Pro_base + (s - 65) * 0.05   # 第66次: +0.05, 第67次: +0.10, ...
        else:  # s == 80
            p = 1.0                          # 保底必出

        x = np.random.uniform(0, 1)
        if x < p:
            u.append(s)
            break

# 统计前80次的出现频率（百分比）
number = []
total = len(u)
for i in range(1, 81):
    count = u.count(i)
    percentage = 100 * count / total
    number.append(percentage)

# 画图
plt.figure(figsize=(12, 6))
plt.bar(range(1, 81), number, color='skyblue', width=0.8)
plt.title('Distribution of 6★ Operator Appearance Position (Arknights-like System)')
plt.xlabel('Pull Number')
plt.ylabel('Probability (%)')
plt.xlim(0, 81)
plt.xticks(np.arange(0, 81, 5))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 打印期望值
expectation = sum((i+1) * freq for i, freq in enumerate(number)) / 100
print(f"Simulated expected pulls for 6★: {expectation:.2f}")

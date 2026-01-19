import numpy as np
import matplotlib.pyplot as plt

# 参数设置
N = 1000000          # 模拟 N 次“120抽之后”的独立实验
results = []        # 记录每次首次再出莱万汀是在第几次（从1开始计，即第121抽记为1）

for _ in range(N):
    s = 0           # 当前连续未出六星次数（120抽后重置）
    pulls = 0       # 本次实验抽了多少次（从121开始算，这里记为1,2,3...）
    while True:
        pulls += 1
        s += 1

        # 计算当前六星出率
        if s <= 65:
            p_6star = 0.008
        elif s < 80:
            p_6star = 0.008 + (s - 65) * 0.05
        else:  # s == 80
            p_6star = 1.0

        # 抽一次
        if np.random.random() < p_6star:
            # 出了六星，有50%概率是莱万汀
            if np.random.random() < 0.5:
                results.append(pulls)
                break
            else:
                # 出了其他六星，保底和概率计数重置！
                s = 0  # 六星出了，无论是不是莱万汀，小保底计数都重置
                # 继续抽
        # else: 未出六星，继续循环

# 统计前100次内的分布（超过100次的归入"100+"，但通常极少）
max_plot = 100
dist = [0] * max_plot
total = len(results)

for r in results:
    if r <= max_plot:
        dist[r - 1] += 1

# 转换为百分比
percentage = [100 * x / total for x in dist]

# 画图
plt.figure(figsize=(12, 6))
plt.bar(range(1, max_plot + 1), percentage, color='lightcoral', width=0.8)
plt.title('Probability Distribution of Getting Lævateinn Again After 120 Pulls')
plt.xlabel('Number of Additional Pulls (starting from pull #121)')
plt.ylabel('Probability (%)')
plt.xlim(0, max_plot + 1)
plt.xticks(np.arange(0, max_plot + 1, 5))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 计算期望
expectation = np.mean(results)
print(f"Average additional pulls to get Lævateinn again: {expectation:.2f}")
print(f"Median: {np.median(results):.0f}")
print(f"95% of players get her again within {np.percentile(results, 95):.0f} pulls")

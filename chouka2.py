def calculate_6star_expectation():
    # E[k] 表示已经连续失败 k 次，从现在开始到出6星的期望抽卡次数
    E = [0.0] * 81  # k 从 0 到 80
    
    # 从后往前递推
    for k in range(79, -1, -1):
        if k == 79:
            p = 1.0  # 第80次必出
        elif k >= 65:
            p = 0.008 + (k - 64) * 0.05  # 每次+5%
        else:
            p = 0.008
        
        E[k] = 1 + (1 - p) * E[k + 1]
    
    return E[0]

# 计算期望
exp = calculate_6star_expectation()
print(f"期望抽卡次数：{exp:.2f} 次")

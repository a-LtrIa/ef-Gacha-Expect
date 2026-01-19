def calculate_lev_expectation():
    # 使用迭代法求解 E[0]：再次抽到莱万汀的期望抽卡次数
    # 状态：E[k] = 当前已连续k次未出六星，到抽到莱万汀的期望次数
    E = [0.0] * 81  # E[0] ~ E[80], E[80] 实际不会用到（因为第80抽必出六星）
    
    # 初始猜测
    for _ in range(1000):  # 迭代直到收敛
        E_new = [0.0] * 81
        # 从 k=79 到 0 反向更新（虽然依赖 E[0]，但迭代可收敛）
        for k in range(79, -1, -1):
            if k == 79:
                p = 1.0
            elif k >= 65:
                p = 0.008 + (k - 64) * 0.05
            else:
                p = 0.008
            
            # 出六星后：50% 结束，50% 重置到 E[0]
            E_new[k] = 1 + (1 - p) * E[k + 1] + 0.5 * p * E[0]
        
        E = E_new
        
        # 可选：检查收敛
        # if abs(E[0] - old_E0) < 1e-6: break
    
    return E[0]

# 计算并输出
exp_lev = calculate_lev_expectation()
print(f"120抽后，再次抽到莱万汀的期望抽卡次数：{exp_lev:.2f} 次")

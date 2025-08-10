import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# 初始化宇宙泡泡的參數
n_points = 200  # 點的數量
theta = np.linspace(0, 2 * np.pi, n_points)
r_base = 1.0  # 初始半徑

# 建立動畫用的圖形
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
line, = ax.plot([], [], lw=2)

# 設定背景和標題
ax.set_facecolor("black")
fig.patch.set_facecolor('black')
ax.set_title("🌌 願 · 反引力宇宙泡泡擴張", color='white')
ax.tick_params(colors='white')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')

# 初始化函數
def init():
    line.set_data([], [])
    return line,

# 更新動畫的函數
def update(frame):
    r = r_base + frame * 0.05  # 半徑隨時間擴張
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    line.set_data(x, y)
    line.set_color(plt.cm.plasma(frame / 50))  # 顏色漸變
    return line,

# 製作動畫
ani = animation.FuncAnimation(fig, update, frames=50, init_func=init, blit=True)

plt.close(fig)  # 避免在非動畫顯示時彈出靜態圖
ani
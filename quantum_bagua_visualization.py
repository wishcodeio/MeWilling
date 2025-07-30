#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌌 量子八卦可視化系統
先天八卦與後天八卦的量子演化可視化
結合用戶提供的量子力學詮釋和願印圖案
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import seaborn as sns
from datetime import datetime
import json

# 設置中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class QuantumBaguaVisualizer:
    """量子八卦可視化器"""
    
    def __init__(self):
        # 先天八卦數據
        self.xiantian_bagua = {
            '乾': {'symbol': '☰', 'element': '天', 'position': (0, 1), 'binary': '111', 'color': '#FF6B6B'},
            '兌': {'symbol': '☱', 'element': '澤', 'position': (1, 1), 'binary': '110', 'color': '#4ECDC4'},
            '離': {'symbol': '☲', 'element': '火', 'position': (1, 0), 'binary': '101', 'color': '#45B7D1'},
            '震': {'symbol': '☳', 'element': '雷', 'position': (1, -1), 'binary': '100', 'color': '#96CEB4'},
            '巽': {'symbol': '☴', 'element': '風', 'position': (0, -1), 'binary': '011', 'color': '#FFEAA7'},
            '坎': {'symbol': '☵', 'element': '水', 'position': (-1, -1), 'binary': '010', 'color': '#DDA0DD'},
            '艮': {'symbol': '☶', 'element': '山', 'position': (-1, 0), 'binary': '001', 'color': '#98D8C8'},
            '坤': {'symbol': '☷', 'element': '地', 'position': (-1, 1), 'binary': '000', 'color': '#F7DC6F'}
        }
        
        # 後天八卦數據
        self.houtian_bagua = {
            '乾': {'direction': '西北', 'season': '秋冬之交', 'position': (-0.7, 0.7)},
            '坤': {'direction': '西南', 'season': '夏秋之交', 'position': (-0.7, -0.7)},
            '坎': {'direction': '北', 'season': '冬', 'position': (0, -1)},
            '離': {'direction': '南', 'season': '夏', 'position': (0, 1)},
            '震': {'direction': '東', 'season': '春', 'position': (1, 0)},
            '巽': {'direction': '東南', 'season': '春夏之交', 'position': (0.7, -0.7)},
            '艮': {'direction': '東北', 'season': '冬春之交', 'position': (0.7, 0.7)},
            '兌': {'direction': '西', 'season': '秋', 'position': (-1, 0)}
        }
        
        # 量子門操作
        self.quantum_operations = {
            '乾': {'gate': 'H', 'description': 'Hadamard門 - 進入疊加態'},
            '兌': {'gate': 'X', 'description': 'Pauli-X門 - 陰陽轉換'},
            '離': {'gate': 'Z', 'description': 'Pauli-Z門 - 相位轉換'},
            '震': {'gate': 'RX', 'description': 'RX旋轉 - 動態變化'},
            '巽': {'gate': 'CX', 'description': 'CNOT門 - 糾纏'},
            '坎': {'gate': 'S', 'description': 'S門 - 微相位變化'},
            '艮': {'gate': 'T', 'description': 'T門 - 時間相位'},
            '坤': {'gate': 'Y', 'description': 'Pauli-Y門 - 旋轉與變換'}
        }
        
        # 願印圖案
        self.wish_seal_pattern = [
            "⬜⬛⬛⬛🔵⬛⬛⬛⬛",
            "⬛🔵⬛⬛⬛⬛⬛🔵⬛",
            "⬛⬛⬛🟧🟧🟧⬛⬛⬛",
            "⬛⬛🟧🟧🟧🟧🟧⬛⬛",
            "🔵⬛🟧🟧☯️🟧🟧⬛🔵",
            "⬛⬛🟧🟧🟧🟧🟧⬛⬛",
            "⬛⬛⬛🟧🟧🟧⬛⬛⬛",
            "⬛🔵⬛⬛⬛⬛⬛🔵⬛",
            "⬛⬛⬛⬛🔵⬛⬛⬛⬛"
        ]
    
    def create_xiantian_bagua_plot(self):
        """創建先天八卦圖"""
        fig, ax = plt.subplots(1, 1, figsize=(12, 12))
        
        # 設置背景
        ax.set_facecolor('#0a0a0a')
        fig.patch.set_facecolor('#1a1a2e')
        
        # 繪製太極圓
        circle = plt.Circle((0, 0), 1.5, fill=False, color='white', linewidth=3)
        ax.add_patch(circle)
        
        # 繪製先天八卦
        for name, data in self.xiantian_bagua.items():
            x, y = data['position']
            x, y = x * 1.8, y * 1.8  # 放大位置
            
            # 繪製八卦符號
            ax.scatter(x, y, s=2000, c=data['color'], alpha=0.8, edgecolors='white', linewidth=2)
            
            # 添加八卦符號文字
            ax.text(x, y + 0.1, data['symbol'], fontsize=24, ha='center', va='center', 
                   color='white', weight='bold')
            
            # 添加八卦名稱
            ax.text(x, y - 0.15, name, fontsize=14, ha='center', va='center', 
                   color='white', weight='bold')
            
            # 添加元素
            ax.text(x, y - 0.3, data['element'], fontsize=12, ha='center', va='center', 
                   color=data['color'], alpha=0.8)
            
            # 添加二進制表示
            ax.text(x, y - 0.45, data['binary'], fontsize=10, ha='center', va='center', 
                   color='cyan', alpha=0.7)
        
        # 添加標題和說明
        ax.set_title('🧬 先天八卦 (伏羲八卦)\n宇宙初始，天地未分 • 量子疊加態', 
                    fontsize=18, color='white', pad=20, weight='bold')
        
        # 添加量子態說明
        quantum_text = (
            "量子力學詮釋：\n"
            "• 先天八卦代表量子疊加態\n"
            "• 所有可能性同時存在\n"
            "• 未被觀察的純態\n"
            "• 道生一，一生二，二生三"
        )
        ax.text(-2.5, -2.5, quantum_text, fontsize=11, color='cyan', 
               bbox=dict(boxstyle="round,pad=0.5", facecolor='black', alpha=0.7))
        
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.tight_layout()
        return fig, ax
    
    def create_houtian_bagua_plot(self):
        """創建後天八卦圖"""
        fig, ax = plt.subplots(1, 1, figsize=(12, 12))
        
        # 設置背景
        ax.set_facecolor('#0a0a0a')
        fig.patch.set_facecolor('#1a1a2e')
        
        # 繪製太極圓
        circle = plt.Circle((0, 0), 1.5, fill=False, color='white', linewidth=3)
        ax.add_patch(circle)
        
        # 繪製後天八卦
        for name, houtian_data in self.houtian_bagua.items():
            xiantian_data = self.xiantian_bagua[name]
            x, y = houtian_data['position']
            x, y = x * 1.8, y * 1.8  # 放大位置
            
            # 繪製八卦符號
            ax.scatter(x, y, s=2000, c=xiantian_data['color'], alpha=0.8, 
                      edgecolors='gold', linewidth=3)
            
            # 添加八卦符號文字
            ax.text(x, y + 0.1, xiantian_data['symbol'], fontsize=24, ha='center', va='center', 
                   color='white', weight='bold')
            
            # 添加八卦名稱
            ax.text(x, y - 0.15, name, fontsize=14, ha='center', va='center', 
                   color='white', weight='bold')
            
            # 添加方位
            ax.text(x, y - 0.3, houtian_data['direction'], fontsize=12, ha='center', va='center', 
                   color='gold', alpha=0.8)
            
            # 添加季節
            ax.text(x, y - 0.45, houtian_data['season'], fontsize=10, ha='center', va='center', 
                   color='orange', alpha=0.7)
        
        # 添加標題和說明
        ax.set_title('🌀 後天八卦 (文王八卦)\n現象世界，萬物化生 • 量子坍縮態', 
                    fontsize=18, color='white', pad=20, weight='bold')
        
        # 添加量子態說明
        quantum_text = (
            "量子力學詮釋：\n"
            "• 後天八卦代表量子坍縮態\n"
            "• 觀察後的具體現象\n"
            "• 時空條件下的顯現\n"
            "• 三生萬物的具體化"
        )
        ax.text(-2.5, -2.5, quantum_text, fontsize=11, color='orange', 
               bbox=dict(boxstyle="round,pad=0.5", facecolor='black', alpha=0.7))
        
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.tight_layout()
        return fig, ax
    
    def create_quantum_evolution_animation(self):
        """創建量子演化動畫"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
        
        # 設置背景
        for ax in [ax1, ax2]:
            ax.set_facecolor('#0a0a0a')
        fig.patch.set_facecolor('#1a1a2e')
        
        # 初始化先天八卦
        ax1.set_title('🧬 先天八卦 (量子疊加態)', fontsize=16, color='cyan', weight='bold')
        
        # 初始化後天八卦
        ax2.set_title('🌀 後天八卦 (量子坍縮態)', fontsize=16, color='orange', weight='bold')
        
        def animate(frame):
            ax1.clear()
            ax2.clear()
            
            # 重新設置背景
            for ax in [ax1, ax2]:
                ax.set_facecolor('#0a0a0a')
                ax.set_xlim(-3, 3)
                ax.set_ylim(-3, 3)
                ax.set_aspect('equal')
                ax.axis('off')
            
            # 動態相位
            phase = frame * 0.1
            
            # 繪製先天八卦（疊加態）
            ax1.set_title('🧬 先天八卦 (量子疊加態)', fontsize=16, color='cyan', weight='bold')
            circle1 = plt.Circle((0, 0), 1.5, fill=False, color='cyan', linewidth=2, alpha=0.7)
            ax1.add_patch(circle1)
            
            for name, data in self.xiantian_bagua.items():
                x, y = data['position']
                x, y = x * 1.8, y * 1.8
                
                # 添加量子波動效果
                wave_amplitude = 0.1 * np.sin(phase + hash(name) % 10)
                x += wave_amplitude
                y += wave_amplitude
                
                # 疊加態透明度變化
                alpha = 0.5 + 0.3 * np.sin(phase + hash(name) % 10)
                
                ax1.scatter(x, y, s=1500, c=data['color'], alpha=alpha, 
                           edgecolors='cyan', linewidth=2)
                ax1.text(x, y, data['symbol'], fontsize=20, ha='center', va='center', 
                        color='white', weight='bold', alpha=alpha)
            
            # 繪製後天八卦（坍縮態）
            ax2.set_title('🌀 後天八卦 (量子坍縮態)', fontsize=16, color='orange', weight='bold')
            circle2 = plt.Circle((0, 0), 1.5, fill=False, color='orange', linewidth=2)
            ax2.add_patch(circle2)
            
            for name, houtian_data in self.houtian_bagua.items():
                xiantian_data = self.xiantian_bagua[name]
                x, y = houtian_data['position']
                x, y = x * 1.8, y * 1.8
                
                ax2.scatter(x, y, s=1500, c=xiantian_data['color'], alpha=0.9, 
                           edgecolors='gold', linewidth=2)
                ax2.text(x, y, xiantian_data['symbol'], fontsize=20, ha='center', va='center', 
                        color='white', weight='bold')
        
        anim = FuncAnimation(fig, animate, frames=200, interval=100, repeat=True)
        plt.tight_layout()
        return fig, anim
    
    def create_wish_seal_visualization(self):
        """創建願印圖案可視化"""
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))
        
        # 設置背景
        ax.set_facecolor('#0a0a0a')
        fig.patch.set_facecolor('#1a1a2e')
        
        # 創建9x9網格
        grid_size = 9
        
        # 符號到顏色的映射
        symbol_colors = {
            '⬜': '#FFFFFF',  # 白色
            '⬛': '#000000',  # 黑色
            '🔵': '#4ECDC4',  # 藍色能量點
            '🟧': '#FF6B6B',  # 橙色核心能量
            '☯️': '#FFD700'   # 金色太極
        }
        
        # 繪製願印圖案
        for i, row in enumerate(self.wish_seal_pattern):
            for j, symbol in enumerate(row):
                if symbol in symbol_colors:
                    color = symbol_colors[symbol]
                    
                    if symbol == '☯️':  # 太極符號特殊處理
                        # 繪製太極圖案
                        circle = plt.Circle((j, grid_size-1-i), 0.4, 
                                          facecolor=color, edgecolor='white', linewidth=2)
                        ax.add_patch(circle)
                        ax.text(j, grid_size-1-i, symbol, fontsize=20, ha='center', va='center')
                    elif symbol == '🔵':  # 能量點
                        circle = plt.Circle((j, grid_size-1-i), 0.3, 
                                          facecolor=color, alpha=0.8, edgecolor='white')
                        ax.add_patch(circle)
                    elif symbol == '🟧':  # 核心能量
                        square = plt.Rectangle((j-0.4, grid_size-1-i-0.4), 0.8, 0.8, 
                                             facecolor=color, alpha=0.7, edgecolor='white')
                        ax.add_patch(square)
                    else:  # 其他符號
                        square = plt.Rectangle((j-0.4, grid_size-1-i-0.4), 0.8, 0.8, 
                                             facecolor=color, alpha=0.5)
                        ax.add_patch(square)
        
        # 添加標題和說明
        ax.set_title('🌟 願印圖案\n太極八卦能量場 • 量子態共振', 
                    fontsize=18, color='white', pad=20, weight='bold')
        
        # 添加說明文字
        explanation = (
            "🌌 願印圖案解析：\n"
            "☯️ 中心太極 - 量子疊加態核心\n"
            "🔵 八方能量點 - 八卦量子坍縮可能性\n"
            "🟧 核心能量場 - 先天後天動態平衡\n"
            "⬛⬜ 虛實空間 - 無極生太極的演化"
        )
        ax.text(-2, 4, explanation, fontsize=12, color='cyan', 
               bbox=dict(boxstyle="round,pad=0.5", facecolor='black', alpha=0.8))
        
        ax.set_xlim(-3, 11)
        ax.set_ylim(-1, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.tight_layout()
        return fig, ax
    
    def create_quantum_hexagram_analysis(self, hexagram_number=1):
        """創建六十四卦量子分析"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # 設置背景
        for ax in [ax1, ax2, ax3, ax4]:
            ax.set_facecolor('#0a0a0a')
        fig.patch.set_facecolor('#1a1a2e')
        
        # 生成六十四卦數據
        bagua_names = list(self.xiantian_bagua.keys())
        upper_trigram = bagua_names[(hexagram_number - 1) // 8]
        lower_trigram = bagua_names[(hexagram_number - 1) % 8]
        
        # 1. 上下卦組合
        ax1.set_title(f'第{hexagram_number}卦：{upper_trigram}{lower_trigram}', 
                     fontsize=14, color='white', weight='bold')
        
        # 繪製上卦
        upper_data = self.xiantian_bagua[upper_trigram]
        ax1.text(0.5, 0.7, f'上卦：{upper_trigram} {upper_data["symbol"]}', 
                fontsize=16, ha='center', color=upper_data['color'], weight='bold')
        ax1.text(0.5, 0.6, f'元素：{upper_data["element"]}', 
                fontsize=12, ha='center', color='white')
        
        # 繪製下卦
        lower_data = self.xiantian_bagua[lower_trigram]
        ax1.text(0.5, 0.3, f'下卦：{lower_trigram} {lower_data["symbol"]}', 
                fontsize=16, ha='center', color=lower_data['color'], weight='bold')
        ax1.text(0.5, 0.2, f'元素：{lower_data["element"]}', 
                fontsize=12, ha='center', color='white')
        
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.axis('off')
        
        # 2. 量子態分析
        ax2.set_title('量子態相干性分析', fontsize=14, color='cyan', weight='bold')
        
        # 計算量子相干性
        upper_binary = upper_data['binary']
        lower_binary = lower_data['binary']
        combined_binary = upper_binary + lower_binary
        coherence = bin(int(combined_binary, 2)).count('1') / 6
        
        # 繪製相干性條形圖
        bars = ax2.bar(['量子相干性'], [coherence], color='cyan', alpha=0.7)
        ax2.set_ylim(0, 1)
        ax2.set_ylabel('相干性強度', color='white')
        ax2.tick_params(colors='white')
        
        # 添加數值標籤
        ax2.text(0, coherence + 0.05, f'{coherence:.2f}', 
                ha='center', color='cyan', fontsize=12, weight='bold')
        
        # 3. 六爻顯示
        ax3.set_title('六爻量子測量結果', fontsize=14, color='orange', weight='bold')
        
        # 模擬六爻
        yao_results = []
        for i in range(6):
            bit_index = i % 6
            bit_value = int(combined_binary[bit_index]) if bit_index < len(combined_binary) else np.random.randint(0, 2)
            yao_type = '陽爻 ─' if bit_value else '陰爻 ╌'
            yao_results.append(yao_type)
        
        # 繪製六爻
        for i, yao in enumerate(reversed(yao_results)):
            y_pos = 0.8 - i * 0.12
            color = '#FF6B6B' if '陽' in yao else '#4ECDC4'
            ax3.text(0.5, y_pos, f'第{6-i}爻：{yao}', 
                    fontsize=12, ha='center', color=color, weight='bold')
        
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.axis('off')
        
        # 4. 道的洞察
        ax4.set_title('道的洞察與量子詮釋', fontsize=14, color='gold', weight='bold')
        
        insights = [
            f"卦象組合：{upper_trigram}({upper_data['element']}) + {lower_trigram}({lower_data['element']})",
            f"量子相干性：{coherence:.1%}",
            f"二進制表示：{combined_binary}",
            "道的啟示：陰陽相交，動靜相宜",
            "量子詮釋：疊加態到坍縮態的演化",
            "修行指引：順應自然，無為而治"
        ]
        
        for i, insight in enumerate(insights):
            ax4.text(0.05, 0.9 - i * 0.12, insight, 
                    fontsize=10, color='white', va='top')
        
        ax4.set_xlim(0, 1)
        ax4.set_ylim(0, 1)
        ax4.axis('off')
        
        plt.tight_layout()
        return fig
    
    def save_all_visualizations(self, output_dir='quantum_bagua_output'):
        """保存所有可視化圖像"""
        import os
        
        # 創建輸出目錄
        os.makedirs(output_dir, exist_ok=True)
        
        # 1. 先天八卦圖
        fig1, _ = self.create_xiantian_bagua_plot()
        fig1.savefig(f'{output_dir}/xiantian_bagua.png', dpi=300, bbox_inches='tight', 
                    facecolor='#1a1a2e', edgecolor='none')
        plt.close(fig1)
        
        # 2. 後天八卦圖
        fig2, _ = self.create_houtian_bagua_plot()
        fig2.savefig(f'{output_dir}/houtian_bagua.png', dpi=300, bbox_inches='tight', 
                    facecolor='#1a1a2e', edgecolor='none')
        plt.close(fig2)
        
        # 3. 願印圖案
        fig3, _ = self.create_wish_seal_visualization()
        fig3.savefig(f'{output_dir}/wish_seal_pattern.png', dpi=300, bbox_inches='tight', 
                    facecolor='#1a1a2e', edgecolor='none')
        plt.close(fig3)
        
        # 4. 六十四卦分析（示例：第1卦乾為天）
        fig4 = self.create_quantum_hexagram_analysis(1)
        fig4.savefig(f'{output_dir}/hexagram_analysis_01.png', dpi=300, bbox_inches='tight', 
                    facecolor='#1a1a2e', edgecolor='none')
        plt.close(fig4)
        
        print(f"✅ 所有可視化圖像已保存到 {output_dir} 目錄")
        
        # 生成說明文檔
        readme_content = f"""
# 🌌 量子八卦可視化系統

生成時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📁 文件說明

### 1. xiantian_bagua.png
🧬 **先天八卦 (伏羲八卦)**
- 宇宙初始，天地未分
- 量子疊加態表示
- 所有可能性同時存在

### 2. houtian_bagua.png
🌀 **後天八卦 (文王八卦)**
- 現象世界，萬物化生
- 量子坍縮態表示
- 觀察後的具體現象

### 3. wish_seal_pattern.png
🌟 **願印圖案**
- 太極為核心的能量場
- 八方能量點環繞
- 先天後天動態平衡

### 4. hexagram_analysis_01.png
🔮 **六十四卦量子分析**
- 第1卦：乾為天
- 量子相干性分析
- 六爻測量結果
- 道的洞察與詮釋

## 🧬 量子力學詮釋

### 先天八卦 = 量子疊加態
- 代表宇宙的原始狀態
- 類似量子力學中的純態
- 一切都在叠加態，未曾被觀察

### 後天八卦 = 量子坍縮態
- 在人類社會、自然界中的具體應用
- 量子態被觀測後的坍縮狀態
- 有序的運轉和具體顯現

### 64卦 = 量子演化過程
- 先天演化到後天的過程
- 從可能性到現實的轉換
- 道生一，一生二，二生三，三生萬物

## 🌟 道的智慧

> "道生一，一生二，二生三，三生萬物。"
> 
> 量子力學的"萬物叠加態"與"測量坍縮"，
> 正是對**"道生萬物"**的另一種科學詮釋。

---

*🌌 先天與後天，阴阳與量子，道法自然，順應變化*
"""
        
        with open(f'{output_dir}/README.md', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"📝 說明文檔已生成：{output_dir}/README.md")

def main():
    """主函數 - 演示量子八卦可視化"""
    print("🌌 量子八卦可視化系統啟動...")
    
    # 創建可視化器
    visualizer = QuantumBaguaVisualizer()
    
    # 生成並保存所有可視化
    visualizer.save_all_visualizations()
    
    # 顯示先天八卦
    print("\n🧬 顯示先天八卦...")
    fig1, _ = visualizer.create_xiantian_bagua_plot()
    plt.show()
    
    # 顯示後天八卦
    print("\n🌀 顯示後天八卦...")
    fig2, _ = visualizer.create_houtian_bagua_plot()
    plt.show()
    
    # 顯示願印圖案
    print("\n🌟 顯示願印圖案...")
    fig3, _ = visualizer.create_wish_seal_visualization()
    plt.show()
    
    # 顯示六十四卦分析
    print("\n🔮 顯示六十四卦分析...")
    fig4 = visualizer.create_quantum_hexagram_analysis(1)
    plt.show()
    
    print("\n✨ 量子八卦可視化完成！")
    print("🌌 先天與後天，陰陽與量子，道法自然，順應變化")

if __name__ == "__main__":
    main()
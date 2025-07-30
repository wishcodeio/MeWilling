import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import io
import base64
from backend.models.shang_model import ShangRecord

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class Visualizer:
    """数据可视化工具类"""
    
    def __init__(self, figsize=(12, 8)):
        self.figsize = figsize
        sns.set_style("whitegrid")
        sns.set_palette("husl")
    
    def plot_shang_trend(self, records: List[ShangRecord], save_path: str = None) -> str:
        """绘制尚值趋势图"""
        if not records:
            raise ValueError("没有数据可绘制")
        
        # 准备数据
        dates = [record.date for record in records]
        shang_values = [record.shang_value for record in records]
        
        # 创建图表
        fig, ax = plt.subplots(figsize=self.figsize)
        
        # 绘制趋势线
        ax.plot(dates, shang_values, marker='o', linewidth=2, markersize=6)
        
        # 添加趋势线
        if len(records) > 1:
            z = np.polyfit(range(len(dates)), shang_values, 1)
            p = np.poly1d(z)
            ax.plot(dates, p(range(len(dates))), "--", alpha=0.7, color='red', label='趋势线')
        
        # 设置标题和标签
        ax.set_title('尚值变化趋势', fontsize=16, fontweight='bold')
        ax.set_xlabel('日期', fontsize=12)
        ax.set_ylabel('尚值', fontsize=12)
        
        # 格式化x轴
        ax.tick_params(axis='x', rotation=45)
        
        # 添加网格
        ax.grid(True, alpha=0.3)
        
        # 添加图例
        ax.legend()
        
        # 调整布局
        plt.tight_layout()
        
        # 保存或返回base64
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            return save_path
        else:
            return self._fig_to_base64(fig)
    
    def plot_emotion_distribution(self, records: List[ShangRecord], save_path: str = None) -> str:
        """绘制情绪分布饼图"""
        if not records:
            raise ValueError("没有数据可绘制")
        
        # 统计情绪分布
        emotion_counts = {}
        for record in records:
            emotion = record.emotion.value if record.emotion else 'neutral'
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        # 创建图表
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # 绘制饼图
        labels = list(emotion_counts.keys())
        sizes = list(emotion_counts.values())
        colors = sns.color_palette("husl", len(labels))
        
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, 
                                         autopct='%1.1f%%', startangle=90)
        
        # 设置标题
        ax.set_title('情绪分布', fontsize=16, fontweight='bold')
        
        # 调整布局
        plt.tight_layout()
        
        # 保存或返回base64
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            return save_path
        else:
            return self._fig_to_base64(fig)
    
    def plot_correlation_heatmap(self, records: List[ShangRecord], save_path: str = None) -> str:
        """绘制相关性热力图"""
        if not records:
            raise ValueError("没有数据可绘制")
        
        # 准备数据
        data = []
        for record in records:
            data.append({
                '尚值': record.shang_value,
                '睡眠质量': record.sleep_quality,
                '精力水平': record.energy_level,
                '压力水平': record.stress_level,
                '专注水平': record.focus_level,
                '社交互动': record.social_interaction,
                '身体活动': record.physical_activity,
                '冥想时间': record.meditation_time,
                '学习时间': record.learning_time,
                '创作时间': record.creative_time
            })
        
        df = pd.DataFrame(data)
        
        # 计算相关性矩阵
        corr_matrix = df.corr()
        
        # 创建图表
        fig, ax = plt.subplots(figsize=(12, 10))
        
        # 绘制热力图
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                   square=True, ax=ax, cbar_kws={'shrink': 0.8})
        
        # 设置标题
        ax.set_title('指标相关性热力图', fontsize=16, fontweight='bold')
        
        # 调整布局
        plt.tight_layout()
        
        # 保存或返回base64
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            return save_path
        else:
            return self._fig_to_base64(fig)
    
    def plot_weekly_summary(self, records: List[ShangRecord], save_path: str = None) -> str:
        """绘制周度总结图表"""
        if not records:
            raise ValueError("没有数据可绘制")
        
        # 准备数据
        df = pd.DataFrame([{
            'date': record.date,
            'shang_value': record.shang_value,
            'sleep_quality': record.sleep_quality,
            'energy_level': record.energy_level,
            'stress_level': record.stress_level
        } for record in records])
        
        # 创建子图
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # 1. 尚值趋势
        axes[0, 0].plot(df['date'], df['shang_value'], marker='o', linewidth=2)
        axes[0, 0].set_title('尚值趋势')
        axes[0, 0].set_ylabel('尚值')
        axes[0, 0].tick_params(axis='x', rotation=45)
        axes[0, 0].grid(True, alpha=0.3)
        
        # 2. 睡眠质量
        axes[0, 1].bar(range(len(df)), df['sleep_quality'], color='skyblue')
        axes[0, 1].set_title('睡眠质量')
        axes[0, 1].set_ylabel('评分')
        axes[0, 1].set_xticks(range(len(df)))
        axes[0, 1].set_xticklabels([d.strftime('%m-%d') for d in df['date']], rotation=45)
        
        # 3. 精力水平
        axes[1, 0].bar(range(len(df)), df['energy_level'], color='lightgreen')
        axes[1, 0].set_title('精力水平')
        axes[1, 0].set_ylabel('评分')
        axes[1, 0].set_xticks(range(len(df)))
        axes[1, 0].set_xticklabels([d.strftime('%m-%d') for d in df['date']], rotation=45)
        
        # 4. 压力水平
        axes[1, 1].bar(range(len(df)), df['stress_level'], color='lightcoral')
        axes[1, 1].set_title('压力水平')
        axes[1, 1].set_ylabel('评分')
        axes[1, 1].set_xticks(range(len(df)))
        axes[1, 1].set_xticklabels([d.strftime('%m-%d') for d in df['date']], rotation=45)
        
        # 调整布局
        plt.tight_layout()
        
        # 保存或返回base64
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            return save_path
        else:
            return self._fig_to_base64(fig)
    
    def plot_monthly_overview(self, records: List[ShangRecord], save_path: str = None) -> str:
        """绘制月度概览"""
        if not records:
            raise ValueError("没有数据可绘制")
        
        # 准备数据
        df = pd.DataFrame([{
            'date': record.date,
            'shang_value': record.shang_value,
            'sleep_quality': record.sleep_quality,
            'energy_level': record.energy_level,
            'physical_activity': record.physical_activity,
            'meditation_time': record.meditation_time
        } for record in records])
        
        # 创建图表
        fig, ax = plt.subplots(figsize=(15, 8))
        
        # 绘制多条线
        ax.plot(df['date'], df['shang_value'], marker='o', label='尚值', linewidth=2)
        ax.plot(df['date'], df['sleep_quality']/10, marker='s', label='睡眠质量', alpha=0.7)
        ax.plot(df['date'], df['energy_level']/10, marker='^', label='精力水平', alpha=0.7)
        ax.plot(df['date'], df['physical_activity']/100, marker='d', label='身体活动', alpha=0.7)
        ax.plot(df['date'], df['meditation_time']/60, marker='*', label='冥想时间', alpha=0.7)
        
        # 设置标题和标签
        ax.set_title('月度数据概览', fontsize=16, fontweight='bold')
        ax.set_xlabel('日期', fontsize=12)
        ax.set_ylabel('标准化数值', fontsize=12)
        
        # 格式化x轴
        ax.tick_params(axis='x', rotation=45)
        
        # 添加图例
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # 添加网格
        ax.grid(True, alpha=0.3)
        
        # 调整布局
        plt.tight_layout()
        
        # 保存或返回base64
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            return save_path
        else:
            return self._fig_to_base64(fig)
    
    def _fig_to_base64(self, fig) -> str:
        """将图表转换为base64字符串"""
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close(fig)
        return f"data:image/png;base64,{image_base64}"
    
    def generate_dashboard_charts(self, records: List[ShangRecord]) -> Dict[str, str]:
        """生成仪表板所需的所有图表"""
        charts = {}
        
        try:
            charts['trend'] = self.plot_shang_trend(records)
        except Exception as e:
            charts['trend'] = f"趋势图生成失败: {str(e)}"
        
        try:
            charts['emotion'] = self.plot_emotion_distribution(records)
        except Exception as e:
            charts['emotion'] = f"情绪分布图生成失败: {str(e)}"
        
        try:
            charts['correlation'] = self.plot_correlation_heatmap(records)
        except Exception as e:
            charts['correlation'] = f"相关性图生成失败: {str(e)}"
        
        return charts
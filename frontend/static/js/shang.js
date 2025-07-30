// 商增管理系统前端逻辑

class ShangManager {
    constructor() {
        this.currentAudio = null;
        this.chart = null;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.updateCurrentDate();
        this.loadTodayData();
        this.setupRangeSliders();
        this.initChart();
    }

    setupEventListeners() {
        // 表单提交
        const form = document.getElementById('shang-form');
        if (form) {
            form.addEventListener('submit', (e) => this.handleFormSubmit(e));
        }

        // 实时计算按钮
        const calculateBtn = document.getElementById('calculate-btn');
        if (calculateBtn) {
            calculateBtn.addEventListener('click', () => this.calculateShang());
        }

        // 音频控制
        document.querySelectorAll('.audio-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.handleAudioSelect(e));
        });

        const playPauseBtn = document.getElementById('play-pause-btn');
        if (playPauseBtn) {
            playPauseBtn.addEventListener('click', () => this.toggleAudio());
        }

        const volumeSlider = document.getElementById('volume-slider');
        if (volumeSlider) {
            volumeSlider.addEventListener('input', (e) => this.updateVolume(e.target.value));
        }

        // 图表周期选择
        const chartPeriod = document.getElementById('chart-period');
        if (chartPeriod) {
            chartPeriod.addEventListener('change', (e) => this.updateChart(e.target.value));
        }
    }

    setupRangeSliders() {
        // 睡眠质量滑块
        const sleepSlider = document.getElementById('sleep-quality');
        const sleepValue = document.getElementById('sleep-value');
        if (sleepSlider && sleepValue) {
            sleepSlider.addEventListener('input', (e) => {
                sleepValue.textContent = e.target.value;
            });
        }

        // 压力水平滑块
        const stressSlider = document.getElementById('stress-level');
        const stressValue = document.getElementById('stress-value');
        if (stressSlider && stressValue) {
            stressSlider.addEventListener('input', (e) => {
                stressValue.textContent = e.target.value;
            });
        }
    }

    updateCurrentDate() {
        const dateDisplay = document.getElementById('current-date');
        if (dateDisplay) {
            const today = new Date();
            dateDisplay.textContent = today.toLocaleDateString('zh-CN');
        }
    }

    async loadTodayData() {
        try {
            const today = new Date().toISOString().split('T')[0];
            const response = await fetch(`/api/shang/record/${today}`);
            const data = await response.json();
            
            if (data.success && data.data) {
                this.populateForm(data.data);
                this.updateDisplay(data.data);
            }
        } catch (error) {
            console.log('今日暂无数据，使用默认值');
        }
    }

    populateForm(data) {
        const fields = {
            'heart-rate': data.heart_rate,
            'steps': data.steps,
            'sleep-quality': data.sleep_quality,
            'emotion': data.emotion_log,
            'stress-level': data.stress_level,
            'meditation': data.meditation_notes,
            'gratitude': data.gratitude_items
        };

        Object.entries(fields).forEach(([id, value]) => {
            const element = document.getElementById(id);
            if (element && value !== undefined) {
                element.value = value;
                // 触发change事件更新显示
                element.dispatchEvent(new Event('input'));
            }
        });
    }

    async calculateShang() {
        const formData = this.getFormData();
        
        try {
            const response = await fetch('/api/shang/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.updateDisplay(result.data);
            } else {
                this.showError(result.message || '计算失败');
            }
        } catch (error) {
            this.showError('网络错误，请稍后重试');
        }
    }

    async handleFormSubmit(e) {
        e.preventDefault();
        
        const formData = this.getFormData();
        formData.date = new Date().toISOString().split('T')[0];
        
        try {
            const response = await fetch('/api/shang/record', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.updateDisplay(result.data);
                this.showSuccess('数据保存成功！');
                this.updateChart(); // 刷新图表
            } else {
                this.showError(result.message || '保存失败');
            }
        } catch (error) {
            this.showError('网络错误，请稍后重试');
        }
    }

    getFormData() {
        return {
            heart_rate: parseInt(document.getElementById('heart-rate').value),
            steps: parseInt(document.getElementById('steps').value),
            sleep_quality: parseInt(document.getElementById('sleep-quality').value),
            emotion_log: document.getElementById('emotion').value,
            stress_level: parseInt(document.getElementById('stress-level').value),
            meditation_notes: document.getElementById('meditation').value,
            gratitude_items: document.getElementById('gratitude').value
        };
    }

    updateDisplay(data) {
        // 更新商值显示
        const elements = {
            'numerator-value': data.numerator?.toFixed(2) || '--',
            'denominator-value': data.denominator?.toFixed(2) || '--',
            'shang-result': data.shang_value?.toFixed(4) || '--',
            'suggestion-text': data.suggestion || '请输入数据以获得建议'
        };

        Object.entries(elements).forEach(([id, value]) => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
            }
        });

        // 更新仪表盘
        if (data.shang_value) {
            this.updateGauge(data.shang_value);
            this.updateStats(data);
        }
    }

    updateGauge(value) {
        const canvas = document.getElementById('shang-gauge-canvas');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        const centerX = canvas.width / 2;
        const centerY = canvas.height - 20;
        const radius = 80;
        
        // 清除画布
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // 绘制背景弧
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, Math.PI, 0);
        ctx.strokeStyle = '#e9ecef';
        ctx.lineWidth = 10;
        ctx.stroke();
        
        // 计算角度 (0.5-2.0 映射到 π-0)
        const minValue = 0.5;
        const maxValue = 2.0;
        const normalizedValue = Math.max(minValue, Math.min(maxValue, value));
        const angle = Math.PI - (normalizedValue - minValue) / (maxValue - minValue) * Math.PI;
        
        // 绘制数值弧
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, Math.PI, angle);
        ctx.strokeStyle = this.getGaugeColor(value);
        ctx.lineWidth = 10;
        ctx.stroke();
        
        // 绘制指针
        const pointerX = centerX + Math.cos(angle) * (radius - 5);
        const pointerY = centerY + Math.sin(angle) * (radius - 5);
        
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(pointerX, pointerY);
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 3;
        ctx.stroke();
        
        // 绘制中心点
        ctx.beginPath();
        ctx.arc(centerX, centerY, 5, 0, 2 * Math.PI);
        ctx.fillStyle = '#333';
        ctx.fill();
    }

    getGaugeColor(value) {
        if (value < 0.8) return '#28a745'; // 绿色 - 良好
        if (value > 1.5) return '#dc3545'; // 红色 - 过高
        return '#ffc107'; // 黄色 - 正常
    }

    updateStats(data) {
        // 更新统计卡片
        const currentShang = document.getElementById('current-shang');
        if (currentShang) {
            currentShang.textContent = data.shang_value?.toFixed(4) || '--';
        }
    }

    // 音频控制方法
    handleAudioSelect(e) {
        const audioName = e.target.dataset.audio;
        if (!audioName) return;
        
        // 移除其他按钮的active状态
        document.querySelectorAll('.audio-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // 添加当前按钮的active状态
        e.target.classList.add('active');
        
        // 更新当前音轨显示
        const currentTrack = document.getElementById('current-track');
        if (currentTrack) {
            currentTrack.textContent = e.target.textContent;
        }
        
        // 加载音频
        this.loadAudio(audioName);
    }

    loadAudio(audioName) {
        if (this.currentAudio) {
            this.currentAudio.pause();
        }
        
        this.currentAudio = new Audio(`/static/audio/${audioName}.m4a`);
        this.currentAudio.loop = true;
        
        // 设置音量
        const volumeSlider = document.getElementById('volume-slider');
        if (volumeSlider) {
            this.currentAudio.volume = volumeSlider.value / 100;
        }
    }

    toggleAudio() {
        if (!this.currentAudio) {
            this.showError('请先选择音频');
            return;
        }
        
        const playPauseBtn = document.getElementById('play-pause-btn');
        const icon = playPauseBtn.querySelector('i');
        
        if (this.currentAudio.paused) {
            this.currentAudio.play();
            icon.className = 'fas fa-pause';
        } else {
            this.currentAudio.pause();
            icon.className = 'fas fa-play';
        }
    }

    updateVolume(value) {
        if (this.currentAudio) {
            this.currentAudio.volume = value / 100;
        }
    }

    // 图表相关方法
    async initChart() {
        const canvas = document.getElementById('trend-chart');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        
        // 获取数据
        const data = await this.getChartData(7);
        
        this.chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: '商值趋势',
                    data: data.values,
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: false,
                        min: 0.5,
                        max: 2.0
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }

    async updateChart(days = 7) {
        if (!this.chart) return;
        
        const data = await this.getChartData(days);
        this.chart.data.labels = data.labels;
        this.chart.data.datasets[0].data = data.values;
        this.chart.update();
    }

    async getChartData(days) {
        try {
            const response = await fetch(`/api/shang/records?limit=${days}`);
            const result = await response.json();
            
            if (result.success) {
                const records = result.data.reverse(); // 按时间正序
                return {
                    labels: records.map(r => new Date(r.date).toLocaleDateString('zh-CN', { month: 'short', day: 'numeric' })),
                    values: records.map(r => r.shang_value || 0)
                };
            }
        } catch (error) {
            console.error('获取图表数据失败:', error);
        }
        
        return { labels: [], values: [] };
    }

    // 工具方法
    showSuccess(message) {
        this.showMessage(message, 'success');
    }

    showError(message) {
        this.showMessage(message, 'error');
    }

    showMessage(message, type) {
        // 简单的消息提示
        const alertClass = type === 'success' ? 'alert-success' : 'alert-danger';
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert ${alertClass}`;
        alertDiv.textContent = message;
        alertDiv.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 1rem;
            border-radius: 5px;
            background: ${type === 'success' ? '#d4edda' : '#f8d7da'};
            color: ${type === 'success' ? '#155724' : '#721c24'};
            border: 1px solid ${type === 'success' ? '#c3e6cb' : '#f5c6cb'};
            z-index: 1000;
        `;
        
        document.body.appendChild(alertDiv);
        
        setTimeout(() => {
            alertDiv.remove();
        }, 3000);
    }
}

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    new ShangManager();
});
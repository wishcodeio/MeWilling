// 专用音频播放器类
class AudioPlayer {
    constructor() {
        this.currentAudio = null;
        this.currentTrack = null;
        this.isPlaying = false;
        this.volume = 0.7;
        this.catalog = null;
        this.recommendations = null;
        this.init();
    }

    async init() {
        await this.loadAudioCatalog();
        this.setupEventListeners();
        this.renderAudioControls();
    }

    async loadAudioCatalog() {
        try {
            const response = await fetch('/api/audio/catalog');
            const result = await response.json();
            if (result.success) {
                this.catalog = result.data;
            }
        } catch (error) {
            console.error('加載音頻目錄失敗:', error);
        }
    }

    setupEventListeners() {
        // 播放/暂停按钮
        const playPauseBtn = document.getElementById('play-pause-btn');
        if (playPauseBtn) {
            playPauseBtn.addEventListener('click', () => this.togglePlayPause());
        }

        // 音量控制
        const volumeSlider = document.getElementById('volume-slider');
        if (volumeSlider) {
            volumeSlider.addEventListener('input', (e) => this.setVolume(e.target.value / 100));
        }

        // 停止按钮
        const stopBtn = document.getElementById('stop-btn');
        if (stopBtn) {
            stopBtn.addEventListener('click', () => this.stop());
        }
    }

    renderAudioControls() {
        if (!this.catalog) return;

        // 渲染神咒类别
        this.renderCategory('divine_mantras', 'divine-mantras-container');
        
        // 渲染木鱼类别
        this.renderCategory('wooden_fish', 'wooden-fish-container');
    }

    renderCategory(categoryKey, containerId) {
        const container = document.getElementById(containerId);
        if (!container || !this.catalog[categoryKey]) return;

        const category = this.catalog[categoryKey];
        const files = category.files;

        let html = `<h4>${category.name}</h4><div class="audio-grid">`;
        
        Object.entries(files).forEach(([audioId, audioInfo]) => {
            html += `
                <div class="audio-item" data-audio-id="${audioId}">
                    <button class="audio-btn" onclick="audioPlayer.selectAudio('${audioId}')">
                        <i class="fas fa-music"></i>
                        <span class="audio-name">${audioInfo.name}</span>
                        ${audioInfo.bpm ? `<span class="audio-bpm">${audioInfo.bpm} BPM</span>` : ''}
                    </button>
                    <div class="audio-info">
                        <p class="audio-description">${audioInfo.description}</p>
                        <p class="audio-usage"><strong>用途:</strong> ${audioInfo.usage}</p>
                        ${audioInfo.stage ? `<p class="audio-stage"><strong>階段:</strong> ${audioInfo.stage}</p>` : ''}
                    </div>
                </div>
            `;
        });
        
        html += '</div>';
        container.innerHTML = html;
    }

    async selectAudio(audioId) {
        try {
            // 获取音频信息
            const response = await fetch(`/api/audio/info/${audioId}`);
            const result = await response.json();
            
            if (!result.success) {
                throw new Error(result.message);
            }

            const audioInfo = result.data;
            
            // 停止当前播放
            this.stop();
            
            // 创建新的音频对象
            this.currentAudio = new Audio(`/static/audio/${audioInfo.file}`);
            this.currentAudio.loop = true;
            this.currentAudio.volume = this.volume;
            
            // 设置事件监听
            this.currentAudio.addEventListener('loadeddata', () => {
                console.log('音频加载完成');
            });
            
            this.currentAudio.addEventListener('error', (e) => {
                console.error('音频加载错误:', e);
                this.showMessage('音频加载失败', 'error');
            });

            this.currentTrack = audioInfo;
            this.updateCurrentTrackDisplay();
            this.updateAudioSelection(audioId);
            
            // 显示呼吸节奏信息（如果是木鱼）
            if (audioInfo.bpm) {
                await this.showBreathingRhythm(audioInfo.bpm);
            }
            
        } catch (error) {
            console.error('选择音频失败:', error);
            this.showMessage('选择音频失败', 'error');
        }
    }

    togglePlayPause() {
        if (!this.currentAudio) {
            this.showMessage('请先选择音频', 'warning');
            return;
        }

        if (this.isPlaying) {
            this.pause();
        } else {
            this.play();
        }
    }

    play() {
        if (!this.currentAudio) return;
        
        this.currentAudio.play().then(() => {
            this.isPlaying = true;
            this.updatePlayButton();
            this.showMessage('开始播放', 'success');
        }).catch(error => {
            console.error('播放失败:', error);
            this.showMessage('播放失败', 'error');
        });
    }

    pause() {
        if (!this.currentAudio) return;
        
        this.currentAudio.pause();
        this.isPlaying = false;
        this.updatePlayButton();
        this.showMessage('暂停播放', 'info');
    }

    stop() {
        if (this.currentAudio) {
            this.currentAudio.pause();
            this.currentAudio.currentTime = 0;
        }
        this.isPlaying = false;
        this.updatePlayButton();
    }

    setVolume(volume) {
        this.volume = volume;
        if (this.currentAudio) {
            this.currentAudio.volume = volume;
        }
    }

    updatePlayButton() {
        const playPauseBtn = document.getElementById('play-pause-btn');
        const icon = playPauseBtn?.querySelector('i');
        
        if (icon) {
            icon.className = this.isPlaying ? 'fas fa-pause' : 'fas fa-play';
        }
    }

    updateCurrentTrackDisplay() {
        const currentTrackElement = document.getElementById('current-track');
        if (currentTrackElement && this.currentTrack) {
            currentTrackElement.innerHTML = `
                <div class="current-track-info">
                    <span class="track-name">${this.currentTrack.name}</span>
                    <span class="track-category">${this.currentTrack.category}</span>
                    <span class="track-description">${this.currentTrack.description}</span>
                </div>
            `;
        }
    }

    updateAudioSelection(selectedId) {
        // 移除所有选中状态
        document.querySelectorAll('.audio-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // 添加当前选中状态
        const selectedItem = document.querySelector(`[data-audio-id="${selectedId}"] .audio-btn`);
        if (selectedItem) {
            selectedItem.classList.add('active');
        }
    }

    async showBreathingRhythm(bpm) {
        try {
            const response = await fetch(`/api/audio/breathing/${bpm}`);
            const result = await response.json();
            
            if (result.success) {
                const rhythm = result.data;
                this.displayBreathingGuide(rhythm);
            }
        } catch (error) {
            console.error('获取呼吸节奏失败:', error);
        }
    }

    displayBreathingGuide(rhythm) {
        const guideContainer = document.getElementById('breathing-guide');
        if (!guideContainer) return;
        
        guideContainer.innerHTML = `
            <div class="breathing-rhythm">
                <h5><i class="fas fa-lungs"></i> 呼吸節奏指導</h5>
                <div class="rhythm-info">
                    <div class="rhythm-item">
                        <span class="label">節拍:</span>
                        <span class="value">${rhythm.bpm} BPM</span>
                    </div>
                    <div class="rhythm-item">
                        <span class="label">每分鐘呼吸:</span>
                        <span class="value">${rhythm.breaths_per_minute} 次</span>
                    </div>
                    <div class="rhythm-item">
                        <span class="label">每次呼吸:</span>
                        <span class="value">${rhythm.seconds_per_breath} 秒</span>
                    </div>
                </div>
                <div class="breathing-pattern">
                    <div class="pattern-step">
                        <span class="step-name">吸氣</span>
                        <span class="step-duration">${rhythm.inhale_seconds}秒</span>
                    </div>
                    <div class="pattern-step">
                        <span class="step-name">屏息</span>
                        <span class="step-duration">${rhythm.hold_seconds}秒</span>
                    </div>
                    <div class="pattern-step">
                        <span class="step-name">呼氣</span>
                        <span class="step-duration">${rhythm.exhale_seconds}秒</span>
                    </div>
                </div>
            </div>
        `;
    }

    async getRecommendations(shangValue, emotion) {
        try {
            const response = await fetch('/api/audio/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    shang_value: shangValue,
                    emotion: emotion
                })
            });
            
            const result = await response.json();
            if (result.success) {
                this.recommendations = result.data;
                this.displayRecommendations();
            }
        } catch (error) {
            console.error('获取推荐失败:', error);
        }
    }

    displayRecommendations() {
        const container = document.getElementById('audio-recommendations');
        if (!container || !this.recommendations) return;
        
        let html = '<div class="recommendations"><h5><i class="fas fa-lightbulb"></i> 音頻推薦</h5>';
        
        if (this.recommendations.by_shang) {
            const rec = this.recommendations.by_shang;
            html += `
                <div class="recommendation-item">
                    <h6>基於商值推薦</h6>
                    <p class="rec-reason">${rec.reason}</p>
                    <div class="rec-buttons">
                        <button class="btn btn-sm btn-primary" onclick="audioPlayer.selectAudio('${rec.primary}')">
                            推薦: ${this.getAudioName(rec.primary)}
                        </button>
                        <button class="btn btn-sm btn-secondary" onclick="audioPlayer.selectAudio('${rec.secondary}')">
                            備選: ${this.getAudioName(rec.secondary)}
                        </button>
                    </div>
                </div>
            `;
        }
        
        if (this.recommendations.by_mood) {
            const rec = this.recommendations.by_mood;
            html += `
                <div class="recommendation-item">
                    <h6>基於情緒推薦</h6>
                    <div class="rec-buttons">
                        <button class="btn btn-sm btn-primary" onclick="audioPlayer.selectAudio('${rec.primary}')">
                            主要: ${this.getAudioName(rec.primary)}
                        </button>
                        <button class="btn btn-sm btn-secondary" onclick="audioPlayer.selectAudio('${rec.secondary}')">
                            輔助: ${this.getAudioName(rec.secondary)}
                        </button>
                    </div>
                </div>
            `;
        }
        
        html += '</div>';
        container.innerHTML = html;
    }

    getAudioName(audioId) {
        if (!this.catalog) return audioId;
        
        for (const category of Object.values(this.catalog)) {
            if (category.files[audioId]) {
                return category.files[audioId].name;
            }
        }
        return audioId;
    }

    showMessage(message, type = 'info') {
        // 简单的消息提示
        console.log(`[${type.toUpperCase()}] ${message}`);
        
        // 可以在这里添加更复杂的消息显示逻辑
        const messageContainer = document.getElementById('audio-messages');
        if (messageContainer) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message message-${type}`;
            messageDiv.textContent = message;
            messageContainer.appendChild(messageDiv);
            
            setTimeout(() => {
                messageDiv.remove();
            }, 3000);
        }
    }
}

// 全局音频播放器实例
let audioPlayer;

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    audioPlayer = new AudioPlayer();
});
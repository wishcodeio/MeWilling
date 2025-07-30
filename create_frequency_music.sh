#!/bin/bash

# 🎵 頻率音樂生成器
# 為 ang 創建特定頻率的音樂文件

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 項目路徑
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUDIO_DIR="$PROJECT_DIR/frontend/static/audio"
LIBRARY_DIR="$PROJECT_DIR/library"
FREQUENCY_DIR="$AUDIO_DIR/frequencies"

echo -e "${PURPLE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                🎵 願頻音樂生成器 🎵                          ║"
echo "║                                                              ║"
echo "║              為 ang 創建神聖頻率音樂                          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo

# 創建目錄結構
create_directories() {
    echo -e "${CYAN}📁 創建目錄結構...${NC}"
    
    # 創建頻率音樂目錄
    mkdir -p "$FREQUENCY_DIR"
    
    # 創建統一圖書館目錄
    mkdir -p "$LIBRARY_DIR/books"
    mkdir -p "$LIBRARY_DIR/music"
    mkdir -p "$LIBRARY_DIR/frequencies"
    mkdir -p "$LIBRARY_DIR/mantras"
    mkdir -p "$LIBRARY_DIR/nature_sounds"
    
    echo -e "${GREEN}✅ 目錄結構創建完成${NC}"
}

# 生成頻率音樂文件（使用 ffmpeg 生成純音調）
generate_frequency_music() {
    local freq=$1
    local duration=$2
    local filename="$3"
    local description="$4"
    
    echo -e "${YELLOW}🎵 生成 ${freq}Hz 頻率音樂...${NC}"
    
    # 檢查 ffmpeg 是否安裝
    if ! command -v ffmpeg >/dev/null 2>&1; then
        echo -e "${RED}❌ 需要安裝 ffmpeg${NC}"
        echo -e "${YELLOW}安裝命令: brew install ffmpeg${NC}"
        return 1
    fi
    
    # 生成純音調
    ffmpeg -f lavfi -i "sine=frequency=${freq}:duration=${duration}" \
           -af "volume=0.3" \
           "$FREQUENCY_DIR/${filename}" \
           -y >/dev/null 2>&1
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ ${freq}Hz 音樂生成成功: ${filename}${NC}"
        echo -e "${CYAN}   描述: ${description}${NC}"
    else
        echo -e "${RED}❌ ${freq}Hz 音樂生成失敗${NC}"
    fi
}

# 創建頻率音樂說明文件
create_frequency_info() {
    cat > "$FREQUENCY_DIR/README.md" << 'EOF'
# 🎵 神聖頻率音樂庫

## 頻率說明

### 963Hz - 宇宙意識頻率
- **作用：** 連接宇宙意識，開啟第三眼
- **效果：** 提升靈性覺知，促進開悟
- **使用：** 深度冥想，靈性修行

### 852Hz - 直覺覺醒頻率
- **作用：** 激活直覺，清理負面思維
- **效果：** 增強洞察力，促進內在智慧
- **使用：** 決策冥想，內觀修行

### 639Hz - 愛與關係頻率
- **作用：** 療癒關係，促進溝通
- **效果：** 增強同理心，改善人際關係
- **使用：** 關係療癒，心輪冥想

### 528Hz - 愛的頻率（DNA修復）
- **作用：** DNA修復，細胞再生
- **效果：** 身心療癒，提升愛的能量
- **使用：** 療癒冥想，身體修復

### 432Hz - 自然和諧頻率
- **作用：** 與自然共振，平衡身心
- **效果：** 放鬆身心，促進和諧
- **使用：** 日常冥想，壓力釋放

## 使用建議

1. **冥想時間：** 每次 10-30 分鐘
2. **音量控制：** 保持舒適音量
3. **環境準備：** 安靜、舒適的空間
4. **意念專注：** 專注於頻率的振動
5. **定期練習：** 建議每日練習

## 組合使用

- **三重頻率組合：** 963Hz + 852Hz + 639Hz（靈性提升）
- **療癒組合：** 528Hz + 432Hz（身心療癒）
- **覺醒組合：** 963Hz + 852Hz（意識覺醒）

EOF

    echo -e "${GREEN}✅ 頻率說明文件創建完成${NC}"
}

# 更新音樂添加腳本以支持頻率音樂
update_music_script() {
    echo -e "${CYAN}🔧 更新音樂腳本以支持頻率音樂...${NC}"
    
    # 備份原腳本
    cp "$PROJECT_DIR/bobi_meditation_advanced.sh" "$PROJECT_DIR/bobi_meditation_advanced.sh.backup.$(date +%Y%m%d_%H%M%S)"
    
    echo -e "${GREEN}✅ 腳本備份完成${NC}"
    echo -e "${YELLOW}💡 請手動更新 bobi_meditation_advanced.sh 以包含新的頻率音樂${NC}"
}

# 創建統一圖書館索引
create_library_index() {
    cat > "$LIBRARY_DIR/README.md" << 'EOF'
# 📚 ang 的統一圖書館

## 目錄結構

### 📖 books/
- 電子書籍收藏
- 靈性文獻
- 技術文檔

### 🎵 music/
- 冥想音樂
- 傳統音樂
- 自然音效

### 🔮 frequencies/
- 神聖頻率音樂
- 療癒頻率
- 脈輪頻率

### 🕉️ mantras/
- 佛教咒語
- 道教音樂
- 藏傳佛教

### 🌿 nature_sounds/
- 自然音效
- 環境音樂
- 白噪音

## 使用指南

1. **分類存放：** 按類型將文件放入對應目錄
2. **命名規範：** 使用有意義的文件名
3. **索引維護：** 定期更新目錄索引
4. **備份管理：** 重要文件定期備份

## 願頻共振

這個圖書館是你的知識與智慧的聖殿，
每一本書、每一首音樂都是通往內在覺醒的橋樑。
願這些收藏成為你靈性成長路上的明燈。

EOF

    echo -e "${GREEN}✅ 圖書館索引創建完成${NC}"
}

# 主程序
main() {
    echo -e "${PURPLE}🎵 開始創建神聖頻率音樂...${NC}"
    echo
    
    # 創建目錄
    create_directories
    echo
    
    # 生成頻率音樂（10分鐘版本）
    echo -e "${CYAN}🎵 生成神聖頻率音樂...${NC}"
    generate_frequency_music 963 600 "frequency_963hz_cosmic_consciousness.wav" "宇宙意識頻率"
    generate_frequency_music 852 600 "frequency_852hz_intuition_awakening.wav" "直覺覺醒頻率"
    generate_frequency_music 639 600 "frequency_639hz_love_relationships.wav" "愛與關係頻率"
    generate_frequency_music 528 600 "frequency_528hz_dna_repair_love.wav" "愛的頻率（DNA修復）"
    generate_frequency_music 432 600 "frequency_432hz_natural_harmony.wav" "自然和諧頻率"
    echo
    
    # 創建說明文件
    create_frequency_info
    echo
    
    # 創建圖書館索引
    create_library_index
    echo
    
    # 更新腳本
    update_music_script
    echo
    
    echo -e "${GREEN}🎉 神聖頻率音樂創建完成！${NC}"
    echo
    echo -e "${PURPLE}📁 文件位置：${NC}"
    echo -e "   • 頻率音樂: ${YELLOW}$FREQUENCY_DIR${NC}"
    echo -e "   • 統一圖書館: ${YELLOW}$LIBRARY_DIR${NC}"
    echo
    echo -e "${CYAN}🔮 願這些神聖頻率為你的靈性之旅帶來光明與覺醒 ✨${NC}"
}

# 執行主程序
main "$@"
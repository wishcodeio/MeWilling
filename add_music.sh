#!/bin/bash

# 🎵 BoBi 音樂添加助手
# 自動化添加新音樂到冥想系統

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
SCRIPT_FILE="$PROJECT_DIR/bobi_meditation_advanced.sh"

# 顯示歡迎信息
show_welcome() {
    clear
    echo -e "${PURPLE}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    🎵 BoBi 音樂添加助手 🎵                    ║"
    echo "║                                                              ║"
    echo "║              為你的冥想之旅添加新的音樂維度                    ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    echo
}

# 檢查音頻目錄
check_audio_dir() {
    if [ ! -d "$AUDIO_DIR" ]; then
        echo -e "${RED}❌ 音頻目錄不存在: $AUDIO_DIR${NC}"
        echo -e "${YELLOW}正在創建音頻目錄...${NC}"
        mkdir -p "$AUDIO_DIR"
        echo -e "${GREEN}✅ 音頻目錄創建成功${NC}"
    fi
}

# 顯示當前音樂庫
show_current_music() {
    echo -e "${CYAN}📚 當前音樂庫：${NC}"
    echo
    if [ -d "$AUDIO_DIR" ] && [ "$(ls -A $AUDIO_DIR 2>/dev/null)" ]; then
        local count=1
        for file in "$AUDIO_DIR"/*.m4a "$AUDIO_DIR"/*.mp3 "$AUDIO_DIR"/*.wav; do
            if [ -f "$file" ]; then
                local filename=$(basename "$file")
                local size=$(du -h "$file" | cut -f1)
                echo -e "${GREEN}$count. $filename ${YELLOW}($size)${NC}"
                ((count++))
            fi
        done
    else
        echo -e "${YELLOW}📁 音樂庫為空，等待你的第一首音樂...${NC}"
    fi
    echo
}

# 添加音樂文件
add_music_file() {
    echo -e "${PURPLE}🎶 添加新音樂${NC}"
    echo
    
    # 獲取音樂文件路徑
    read -p "請輸入音樂文件的完整路徑: " music_path
    
    # 檢查文件是否存在
    if [ ! -f "$music_path" ]; then
        echo -e "${RED}❌ 文件不存在: $music_path${NC}"
        return 1
    fi
    
    # 檢查文件格式
    local extension="${music_path##*.}"
    case "$extension" in
        m4a|mp3|wav|M4A|MP3|WAV)
            echo -e "${GREEN}✅ 支援的音頻格式: .$extension${NC}"
            ;;
        *)
            echo -e "${YELLOW}⚠️  未知格式: .$extension，建議使用 m4a/mp3/wav${NC}"
            read -p "是否繼續? (y/N): " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                return 1
            fi
            ;;
    esac
    
    # 獲取音樂信息
    echo
    echo -e "${CYAN}📝 請提供音樂信息：${NC}"
    read -p "音樂名稱 (例: 藏傳頌缽): " music_name
    read -p "音樂類型 (例: 療癒/冥想/自然): " music_type
    read -p "BPM或特徵 (例: 60bpm/peaceful): " music_feature
    
    # 生成新文件名
    local safe_name=$(echo "$music_name" | sed 's/[^a-zA-Z0-9\u4e00-\u9fff]/_/g')
    local safe_type=$(echo "$music_type" | sed 's/[^a-zA-Z0-9\u4e00-\u9fff]/_/g')
    local safe_feature=$(echo "$music_feature" | sed 's/[^a-zA-Z0-9\u4e00-\u9fff]/_/g')
    
    local new_filename="${safe_type}_${safe_name}_${safe_feature}.${extension}"
    local new_path="$AUDIO_DIR/$new_filename"
    
    echo
    echo -e "${YELLOW}📋 文件信息預覽：${NC}"
    echo -e "原始文件: $(basename "$music_path")"
    echo -e "新文件名: $new_filename"
    echo -e "目標路徑: $new_path"
    echo
    
    read -p "確認複製文件? (Y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Nn]$ ]]; then
        echo -e "${YELLOW}❌ 操作已取消${NC}"
        return 1
    fi
    
    # 複製文件
    if cp "$music_path" "$new_path"; then
        echo -e "${GREEN}✅ 音樂文件複製成功${NC}"
        
        # 詢問是否添加到腳本選單
        echo
        read -p "是否將此音樂添加到冥想腳本選單? (Y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Nn]$ ]]; then
            add_to_script_menu "$music_name" "$music_type" "$new_filename"
        fi
        
        return 0
    else
        echo -e "${RED}❌ 文件複製失敗${NC}"
        return 1
    fi
}

# 添加到腳本選單
add_to_script_menu() {
    local music_name="$1"
    local music_type="$2"
    local filename="$3"
    
    echo -e "${CYAN}🔧 正在更新冥想腳本...${NC}"
    
    # 備份原腳本
    cp "$SCRIPT_FILE" "${SCRIPT_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
    
    # 找到下一個可用的選項編號
    local next_num=$(grep -o 'echo -e "${CYAN}[0-9]\+\.' "$SCRIPT_FILE" | grep -o '[0-9]\+' | sort -n | tail -1)
    next_num=$((next_num + 1))
    
    # 創建新的選單項目
    local menu_item="    echo -e \"\${CYAN}$next_num. $music_name ($music_type) 🎵\${NC}\""
    local case_item="        $next_num) SELECTED_MUSIC=\"\$AUDIO_DIR/$filename\" ;;"
    
    echo -e "${YELLOW}📝 將添加選單項目：${NC}"
    echo "   $next_num. $music_name ($music_type) 🎵"
    echo
    
    # 這裡可以添加自動修改腳本的邏輯
    # 由於腳本修改較複雜，先提供手動修改指引
    echo -e "${PURPLE}📋 請手動添加以下內容到 bobi_meditation_advanced.sh：${NC}"
    echo
    echo -e "${GREEN}在 show_music_menu() 函數的選單部分添加：${NC}"
    echo -e "${CYAN}$menu_item${NC}"
    echo
    echo -e "${GREEN}在 case 語句中添加：${NC}"
    echo -e "${CYAN}$case_item${NC}"
    echo
    echo -e "${YELLOW}💡 提示：記得更新 read -p 的數字範圍${NC}"
}

# 測試音樂播放
test_music() {
    echo -e "${PURPLE}🎵 測試音樂播放${NC}"
    echo
    
    show_current_music
    
    read -p "請輸入要測試的音樂文件名: " test_filename
    
    local test_path="$AUDIO_DIR/$test_filename"
    
    if [ ! -f "$test_path" ]; then
        echo -e "${RED}❌ 文件不存在: $test_filename${NC}"
        return 1
    fi
    
    echo -e "${GREEN}🎵 正在播放: $test_filename${NC}"
    echo -e "${YELLOW}按 Ctrl+C 停止播放${NC}"
    
    # 使用 afplay (macOS) 或 mpg123 (Linux) 播放
    if command -v afplay >/dev/null 2>&1; then
        afplay "$test_path"
    elif command -v mpg123 >/dev/null 2>&1; then
        mpg123 "$test_path"
    elif command -v ffplay >/dev/null 2>&1; then
        ffplay -nodisp -autoexit "$test_path"
    else
        echo -e "${RED}❌ 未找到音頻播放器 (afplay/mpg123/ffplay)${NC}"
        return 1
    fi
}

# 主選單
show_main_menu() {
    while true; do
        echo -e "${PURPLE}🎵 請選擇操作：${NC}"
        echo -e "${CYAN}1. 查看當前音樂庫${NC}"
        echo -e "${CYAN}2. 添加新音樂${NC}"
        echo -e "${CYAN}3. 測試音樂播放${NC}"
        echo -e "${CYAN}4. 查看使用指南${NC}"
        echo -e "${CYAN}5. 退出${NC}"
        echo
        
        read -p "請選擇 (1-5): " -n 1 -r
        echo
        echo
        
        case $REPLY in
            1)
                show_current_music
                ;;
            2)
                add_music_file
                ;;
            3)
                test_music
                ;;
            4)
                echo -e "${CYAN}📖 使用指南：${NC}"
                echo -e "${YELLOW}詳細指南請查看: docs/音樂擴展指南.md${NC}"
                echo
                ;;
            5)
                echo -e "${GREEN}🙏 感謝使用 BoBi 音樂添加助手！${NC}"
                echo -e "${PURPLE}願音樂為你的冥想之旅增添更多色彩 🎵✨${NC}"
                exit 0
                ;;
            *)
                echo -e "${RED}❌ 無效選擇，請重新選擇${NC}"
                ;;
        esac
        
        echo
        read -p "按 Enter 繼續..." -r
        clear
        show_welcome
    done
}

# 主程序
main() {
    show_welcome
    check_audio_dir
    show_main_menu
}

# 執行主程序
main "$@"
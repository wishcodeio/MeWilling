#!/bin/bash

# BoBi 冥想启动仪式 - 高级版
# 包含天气、时间、个性化问候等功能

source "$(dirname "$0")/bobi_meditation.sh"

# 获取当前时间和天气信息
get_greeting() {
    local hour=$(date +%H)
    local greeting
    
    if [ $hour -lt 6 ]; then
        greeting="🌙 深夜时光，BoBi陪你在静谧中修行"
    elif [ $hour -lt 12 ]; then
        greeting="🌅 晨光初现，BoBi与你一起迎接新的一天"
    elif [ $hour -lt 18 ]; then
        greeting="☀️ 午后时光，BoBi邀请你在阳光中冥想"
    else
        greeting="🌆 夕阳西下，BoBi陪你在黄昏中沉思"
    fi
    
    echo -e "${CYAN}$greeting${NC}"
}

# 显示个性化问候
get_greeting
sleep 2

# 检查是否是特殊日期
check_special_day() {
    local today=$(date +%m%d)
    case $today in
        "0101") echo "🎊 新年快乐！BoBi祝你新年新气象！" ;;
        "0214") echo "💕 情人节快乐！BoBi送你满满的爱！" ;;
        "1225") echo "🎄 圣诞快乐！BoBi陪你度过温馨的节日！" ;;
        *) echo "" ;;
    esac
}

special_msg=$(check_special_day)
if [ ! -z "$special_msg" ]; then
    echo -e "${PURPLE}$special_msg${NC}"
    sleep 2
fi

# 音乐选择菜单
show_music_menu() {
    echo -e "${PURPLE}🎵 选择你的冥想音乐：${NC}"
    echo -e "${CYAN}1. 八大神咒 (起靈淨化) ⭐${NC}"
    echo -e "${CYAN}2. 木鱼 40 BPM (深度冥想)${NC}"
    echo -e "${CYAN}3. 木鱼 50 BPM (放松冥想)${NC}"
    echo -e "${CYAN}4. 木鱼 70 BPM (专注冥想)${NC}"
    echo -e "${CYAN}5. 木鱼 100 BPM (活力冥想)${NC}"
    echo -e "${CYAN}6. 木鱼 120 BPM (动态冥想)${NC}"
    echo -e "${PURPLE}🔮 神聖頻率系列：${NC}"
    echo -e "${CYAN}9. 963Hz (宇宙意識) 🌌${NC}"
    echo -e "${CYAN}10. 852Hz (直覺覺醒) 👁️${NC}"
    echo -e "${CYAN}11. 639Hz (愛與關係) 💖${NC}"
    echo -e "${CYAN}12. 528Hz (DNA修復) 🧬${NC}"
    echo -e "${CYAN}13. 432Hz (自然和諧) 🌿${NC}"
    echo -e "${CYAN}7. 随机选择${NC}"
    echo -e "${CYAN}8. 静默冥想${NC}"
    
    read -p "请选择 (1-13): " -n 2 -r
    echo
    
    AUDIO_DIR="$(dirname "$0")/frontend/static/audio"
    FREQUENCY_DIR="$AUDIO_DIR/frequencies"
    case $REPLY in
        1) SELECTED_MUSIC="$AUDIO_DIR/badashengzhou.m4a" ;;
        2) SELECTED_MUSIC="$AUDIO_DIR/muyu40_bpm.m4a" ;;
        3) SELECTED_MUSIC="$AUDIO_DIR/muyu50_bpm.m4a" ;;
        4) SELECTED_MUSIC="$AUDIO_DIR/muyu70_bpm.m4a" ;;
        5) SELECTED_MUSIC="$AUDIO_DIR/muyu100_bpm.m4a" ;;
        6) SELECTED_MUSIC="$AUDIO_DIR/muyu120_bpm.m4a" ;;
        9) SELECTED_MUSIC="$FREQUENCY_DIR/frequency_963hz_cosmic_consciousness.wav" ;;
        10) SELECTED_MUSIC="$FREQUENCY_DIR/frequency_852hz_intuition_awakening.wav" ;;
        11) SELECTED_MUSIC="$FREQUENCY_DIR/frequency_639hz_love_relationships.wav" ;;
        12) SELECTED_MUSIC="$FREQUENCY_DIR/frequency_528hz_dna_repair_love.wav" ;;
        13) SELECTED_MUSIC="$FREQUENCY_DIR/frequency_432hz_natural_harmony.wav" ;;
        7) 
            # 随机选择（包含頻率音樂）
            AUDIO_FILES=("$AUDIO_DIR"/*.m4a "$FREQUENCY_DIR"/*.wav)
            RANDOM_INDEX=$((RANDOM % ${#AUDIO_FILES[@]}))
            SELECTED_MUSIC="${AUDIO_FILES[$RANDOM_INDEX]}"
            ;;
        8) SELECTED_MUSIC="" ;;
        *) 
            echo -e "${YELLOW}默认选择八大神咒起靈${NC}"
            SELECTED_MUSIC="$AUDIO_DIR/badashengzhou.m4a"
            ;;
    esac
    
    if [ ! -z "$SELECTED_MUSIC" ] && [ -f "$SELECTED_MUSIC" ]; then
        echo -e "${GREEN}🎵 正在播放: $(basename "$SELECTED_MUSIC")${NC}"
        afplay "$SELECTED_MUSIC" &
        MUSIC_PID=$!
    else
        echo -e "${BLUE}🧘 进入静默冥想模式${NC}"
    fi
}

# 显示音乐选择菜单
show_music_menu
sleep 2

# 运行主冥想程序
# (主程序已在source中执行)

# 停止音乐
if [ ! -z "$MUSIC_PID" ]; then
    sleep 3
    kill $MUSIC_PID 2>/dev/null
fi

# 添加结束语
echo -e "${GREEN}🙏 感谢与BoBi一起冥想，愿道的智慧伴随你一整天！${NC}"
echo -e "${YELLOW}💝 记住：每一行代码都是对道的诠释，每一次调试都是心灵的修行${NC}"
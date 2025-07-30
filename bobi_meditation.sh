#!/bin/bash

# BoBi 冥想启动仪式 - 终端法器开启道场
# 让每次打开终端都成为一次心灵修行

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# 清屏并开始仪式
clear
echo -e "${PURPLE}🔥 欢迎来到道的终端法器！让我们先进入BoBi的冥想状态... 🔥${NC}"
sleep 2

# BoBi冥想动画帧
frames=(
"　　　 ＿＿＿\n　　 ／　　　▲\n／￣　 ヽ　■■\n●　　　　　■■\nヽ＿＿＿　　■■\n　　　　）＝｜\n　　　／　｜｜\n　∩∩＿＿とﾉ\n　しし———┘"
"　　　 ＿＿＿\n　　 ／　　　▲\n／￣　 ヽ　■■\n●　　　　(｡◕‿◕｡)■■\nヽ＿＿＿　　■■\n　　　　）＝｜\n　　　／　｜｜\n　∩∩＿＿とﾉ\n　しし———┘"
"　　　 ＿＿＿\n　　 ／　　　▲\n／￣　 ヽ　■■\n●　　　　(｡-‿-｡)■■\nヽ＿＿＿　　■■\n　　　　）＝｜\n　　　／　｜｜\n　∩∩＿＿とﾉ\n　しし———┘"
"　　　 ＿＿＿\n　　 ／　　　▲\n／￣　 ヽ　■■\n●　　　　(｡◕‿◕｡)■■\nヽ＿＿＿　　■■\n　　　　）＝｜\n　　　／　｜｜\n　∩∩＿＿とﾉ\n　しし———┘"
"　　　 ＿＿＿\n　　 ／　　　▲\n／￣　 ヽ　■■\n●　　　　(｡✧‿✧｡)■■\nヽ＿＿＿　　■■\n　　　　）＝｜\n　　　／　｜｜\n　∩∩＿＿とﾉ\n　しし———┘"
)

# 道德经启示语录
quotes=(
    "道可道，非常道。名可名，非常名。——《道德经》"
    "上善若水，水善利万物而不争。——《道德经》"
    "大音希声，大象无形。——《道德经》"
    "知人者智，自知者明。胜人者有力，自胜者强。——《道德经》"
    "致虚极，守静笃。——《道德经》"
    "天下莫柔弱于水，而攻坚强者莫之能胜。——《道德经》"
    "夫唯不争，故天下莫能与之争。——《道德经》"
    "知足不辱，知止不殆。——《道德经》"
    "千里之行，始于足下。——《道德经》"
    "反者道之动，弱者道之用。——《道德经》"
)

# 播放背景音乐（从audio目录随机选择）
AUDIO_DIR="$(dirname "$0")/frontend/static/audio"
if [ -d "$AUDIO_DIR" ]; then
    # 获取所有音频文件
    AUDIO_FILES=("$AUDIO_DIR"/*.{m4a,mp3,wav})
    # 过滤存在的文件
    EXISTING_FILES=()
    for file in "${AUDIO_FILES[@]}"; do
        if [ -f "$file" ]; then
            EXISTING_FILES+=("$file")
        fi
    done
    
    # 如果有音频文件，随机选择一个播放
    if [ ${#EXISTING_FILES[@]} -gt 0 ]; then
        RANDOM_INDEX=$((RANDOM % ${#EXISTING_FILES[@]}))
        SELECTED_MUSIC="${EXISTING_FILES[$RANDOM_INDEX]}"
        echo -e "${CYAN}🎵 正在播放冥想音乐: $(basename "$SELECTED_MUSIC")${NC}"
        afplay "$SELECTED_MUSIC" &
        MUSIC_PID=$!
    fi
fi

# 冥想动画循环
echo -e "${CYAN}🌿 BoBi 冥想启动中... 请深呼吸，感受道的流动 🌿${NC}"
sleep 1

for i in {1..8}; do
    for frame in "${frames[@]}"; do
        clear
        echo -e "${YELLOW}$frame${NC}"
        echo
        echo -e "${GREEN}🌿 BoBi 正在冥想中... 请深呼吸，感受道的流动 🌿${NC}"
        echo -e "${BLUE}冥想进度: $(printf '█%.0s' $(seq 1 $i))$(printf '░%.0s' $(seq 1 $((8-i)))) ${i}/8${NC}"
        sleep 0.8
    done
done

# 冥想完成
clear
echo -e "${frames[1]}"
echo
echo -e "${PURPLE}✨ BoBi 冥想完成！道场已开启 ✨${NC}"
sleep 2

# 显示今日启示
clear
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║                    🌸 道场已开启 🌸                        ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo
echo -e "${frames[1]}"
echo
echo -e "${YELLOW}📜 今日的道之启示：${NC}"
echo -e "${WHITE}${quotes[$RANDOM % ${#quotes[@]}]}${NC}"
echo
echo -e "${GREEN}✨ 提维时刻已开启，愿你在道的流动中，代码如水般流畅 ✨${NC}"
echo
echo -e "${PURPLE}🌟 欢迎来到你的专属道场，开始今天的修行之旅吧！ 🌟${NC}"
echo

# 停止背景音乐
if [ ! -z "$MUSIC_PID" ]; then
    sleep 5
    kill $MUSIC_PID 2>/dev/null
    echo -e "${CYAN}🎵 冥想音乐已停止${NC}"
fi

# 冥想完成，回到正常终端
echo -e "${PURPLE}🌟 道場修行完成，回到日常編程修行 🌟${NC}"
echo
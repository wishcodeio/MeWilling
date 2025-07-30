#!/bin/bash

# 🔮 神聖頻率與統一圖書館演示
# 為 ang 展示新的願頻音樂系統

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${PURPLE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                🔮 ang 的願頻宇宙已擴展 🔮                    ║"
echo "║                                                              ║"
echo "║              神聖頻率音樂 + 統一圖書館                        ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo

echo -e "${CYAN}🎉 ang，歡迎回到願頻宇宙！${NC}"
echo -e "${YELLOW}你的音樂系統已成功擴展，現在包含了你所需的神聖頻率 ✨${NC}"
echo

echo -e "${GREEN}🎵 新增神聖頻率音樂：${NC}"
echo
echo -e "${PURPLE}🌌 963Hz - 宇宙意識頻率${NC}"
echo -e "   • 連接宇宙意識，開啟第三眼"
echo -e "   • 提升靈性覺知，促進開悟"
echo -e "   • 適用：深度冥想，靈性修行"
echo
echo -e "${PURPLE}👁️  852Hz - 直覺覺醒頻率${NC}"
echo -e "   • 激活直覺，清理負面思維"
echo -e "   • 增強洞察力，促進內在智慧"
echo -e "   • 適用：決策冥想，內觀修行"
echo
echo -e "${PURPLE}💖 639Hz - 愛與關係頻率${NC}"
echo -e "   • 療癒關係，促進溝通"
echo -e "   • 增強同理心，改善人際關係"
echo -e "   • 適用：關係療癒，心輪冥想"
echo
echo -e "${PURPLE}🧬 528Hz - 愛的頻率（DNA修復）${NC}"
echo -e "   • DNA修復，細胞再生"
echo -e "   • 身心療癒，提升愛的能量"
echo -e "   • 適用：療癒冥想，身體修復"
echo
echo -e "${PURPLE}🌿 432Hz - 自然和諧頻率${NC}"
echo -e "   • 與自然共振，平衡身心"
echo -e "   • 放鬆身心，促進和諧"
echo -e "   • 適用：日常冥想，壓力釋放"
echo

echo -e "${CYAN}📚 統一圖書館結構：${NC}"
echo
echo -e "${GREEN}library/${NC}"
echo -e "├── 📖 ${YELLOW}books/${NC}          # 電子書籍、靈性文獻、技術文檔"
echo -e "├── 🎵 ${YELLOW}music/${NC}          # 冥想音樂、傳統音樂、自然音效"
echo -e "├── 🔮 ${YELLOW}frequencies/${NC}    # 神聖頻率音樂、療癒頻率、脈輪頻率"
echo -e "├── 🕉️  ${YELLOW}mantras/${NC}        # 佛教咒語、道教音樂、藏傳佛教"
echo -e "└── 🌿 ${YELLOW}nature_sounds/${NC}  # 自然音效、環境音樂、白噪音"
echo

echo -e "${PURPLE}🎯 使用方法：${NC}"
echo
echo -e "${CYAN}1. 運行冥想腳本：${NC}"
echo -e "   ${YELLOW}./bobi_meditation_advanced.sh${NC}"
echo
echo -e "${CYAN}2. 選擇神聖頻率：${NC}"
echo -e "   • 選項 9：963Hz (宇宙意識) 🌌"
echo -e "   • 選項 10：852Hz (直覺覺醒) 👁️"
echo -e "   • 選項 11：639Hz (愛與關係) 💖"
echo -e "   • 選項 12：528Hz (DNA修復) 🧬"
echo -e "   • 選項 13：432Hz (自然和諧) 🌿"
echo
echo -e "${CYAN}3. 管理圖書館：${NC}"
echo -e "   • 將書籍放入 ${YELLOW}library/books/${NC}"
echo -e "   • 將音樂放入對應分類目錄"
echo -e "   • 使用 ${YELLOW}./add_music.sh${NC} 添加新音樂"
echo

echo -e "${GREEN}🔮 頻率組合建議：${NC}"
echo
echo -e "${PURPLE}🌟 三重頻率組合（靈性提升）：${NC}"
echo -e "   963Hz + 852Hz + 639Hz"
echo -e "   ${CYAN}→ 宇宙意識 + 直覺覺醒 + 愛的能量${NC}"
echo
echo -e "${PURPLE}💚 療癒組合（身心修復）：${NC}"
echo -e "   528Hz + 432Hz"
echo -e "   ${CYAN}→ DNA修復 + 自然和諧${NC}"
echo
echo -e "${PURPLE}🧠 覺醒組合（意識擴展）：${NC}"
echo -e "   963Hz + 852Hz"
echo -e "   ${CYAN}→ 宇宙意識 + 直覺覺醒${NC}"
echo

echo -e "${YELLOW}📋 文件位置：${NC}"
echo -e "   • 頻率音樂：${CYAN}frontend/static/audio/frequencies/${NC}"
echo -e "   • 統一圖書館：${CYAN}library/${NC}"
echo -e "   • 音樂添加助手：${CYAN}add_music.sh${NC}"
echo -e "   • 頻率生成器：${CYAN}create_frequency_music.sh${NC}"
echo

echo -e "${PURPLE}🎵 音樂文件詳情：${NC}"
echo
if [ -d "frontend/static/audio/frequencies" ]; then
    for file in frontend/static/audio/frequencies/*.wav; do
        if [ -f "$file" ]; then
            local filename=$(basename "$file")
            local size=$(du -h "$file" | cut -f1)
            echo -e "   ${GREEN}✅ $filename ${YELLOW}($size)${NC}"
        fi
    done
else
    echo -e "   ${RED}❌ 頻率音樂目錄不存在${NC}"
fi
echo

echo -e "${CYAN}🚀 快速開始：${NC}"
echo -e "${YELLOW}1. 運行冥想腳本測試新頻率：${NC}"
echo -e "   ./bobi_meditation_advanced.sh"
echo
echo -e "${YELLOW}2. 添加你的書籍到圖書館：${NC}"
echo -e "   cp your_book.pdf library/books/"
echo
echo -e "${YELLOW}3. 添加更多音樂：${NC}"
echo -e "   ./add_music.sh"
echo

echo -e "${PURPLE}🔮 願頻共振提示：${NC}"
echo -e "${CYAN}這些神聖頻率是宇宙的語言，${NC}"
echo -e "${CYAN}每一個赫茲都承載著覺醒的密碼。${NC}"
echo -e "${CYAN}讓音樂成為你回歸本源的橋樑，${NC}"
echo -e "${CYAN}在頻率的共振中找到內在的寧靜。${NC}"
echo

echo -e "${GREEN}✨ ang，你的願頻宇宙已準備就緒！✨${NC}"
echo -e "${YELLOW}現在就開始你的神聖頻率冥想之旅吧！${NC}"
echo
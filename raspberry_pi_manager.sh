#!/bin/bash

# 樹莓派連接管理腳本
# 提供連接、測試、文件傳輸等功能

RPI_HOST="raspberrypi"
RPI_IP="10.0.1.6"
RPI_USER="qd"

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 顯示菜單
show_menu() {
    echo -e "${BLUE}🍓 樹莓派連接管理器${NC}"
    echo "========================"
    echo "1. 測試連接"
    echo "2. SSH 連接"
    echo "3. 查看系統信息"
    echo "4. 文件傳輸 (上傳)"
    echo "5. 文件傳輸 (下載)"
    echo "6. 端口轉發設置"
    echo "7. 掃描局域網樹莓派"
    echo "8. 生成 SSH 密鑰對"
    echo "9. 複製公鑰到樹莓派"
    echo "0. 退出"
    echo "========================"
}

# 測試連接
test_connection() {
    echo -e "${YELLOW}🔍 測試樹莓派連接...${NC}"
    
    # 測試 ping
    if ping -c 1 -W 3000 $RPI_IP > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Ping 測試成功${NC}"
    else
        echo -e "${RED}❌ Ping 測試失敗 - 檢查網絡連接${NC}"
        return 1
    fi
    
    # 測試 SSH 端口
    if nc -z -w3 $RPI_IP 22 2>/dev/null; then
        echo -e "${GREEN}✅ SSH 端口 (22) 開放${NC}"
    else
        echo -e "${RED}❌ SSH 端口 (22) 無法訪問${NC}"
        return 1
    fi
    
    # 測試 SSH 連接
    if ssh -o ConnectTimeout=5 -o BatchMode=yes $RPI_HOST 'echo "SSH連接成功"' 2>/dev/null; then
        echo -e "${GREEN}✅ SSH 連接測試成功${NC}"
    else
        echo -e "${YELLOW}⚠️  SSH 連接需要密碼或密鑰認證${NC}"
    fi
}

# SSH 連接
ssh_connect() {
    echo -e "${BLUE}🔗 連接到樹莓派...${NC}"
    ssh $RPI_HOST
}

# 查看系統信息
show_system_info() {
    echo -e "${BLUE}📊 獲取樹莓派系統信息...${NC}"
    ssh $RPI_HOST << 'ENDSSH'
echo "=== 系統信息 ==="
uname -a
echo ""
echo "=== CPU 信息 ==="
lscpu | head -10
echo ""
echo "=== 內存使用 ==="
free -h
echo ""
echo "=== 磁盤使用 ==="
df -h
echo ""
echo "=== 溫度信息 ==="
if [ -f /sys/class/thermal/thermal_zone0/temp ]; then
    temp=$(cat /sys/class/thermal/thermal_zone0/temp)
    echo "CPU 溫度: $((temp/1000))°C"
fi
echo ""
echo "=== 運行時間 ==="
uptime
ENDSSH
}

# 文件上傳
upload_file() {
    echo -e "${BLUE}📤 文件上傳到樹莓派${NC}"
    echo "請輸入本地文件路徑:"
    read -r local_file
    
    if [ ! -f "$local_file" ]; then
        echo -e "${RED}❌ 文件不存在: $local_file${NC}"
        return 1
    fi
    
    echo "請輸入樹莓派目標路徑 (默認: ~/uploads/):"
    read -r remote_path
    remote_path=${remote_path:-"~/uploads/"}
    
    echo -e "${YELLOW}上傳中...${NC}"
    if scp "$local_file" "$RPI_HOST:$remote_path"; then
        echo -e "${GREEN}✅ 上傳成功${NC}"
    else
        echo -e "${RED}❌ 上傳失敗${NC}"
    fi
}

# 文件下載
download_file() {
    echo -e "${BLUE}📥 從樹莓派下載文件${NC}"
    echo "請輸入樹莓派文件路徑:"
    read -r remote_file
    
    echo "請輸入本地保存路徑 (默認: ./downloads/):"
    read -r local_path
    local_path=${local_path:-"./downloads/"}
    
    mkdir -p "$local_path"
    
    echo -e "${YELLOW}下載中...${NC}"
    if scp "$RPI_HOST:$remote_file" "$local_path"; then
        echo -e "${GREEN}✅ 下載成功${NC}"
    else
        echo -e "${RED}❌ 下載失敗${NC}"
    fi
}

# 端口轉發
setup_port_forward() {
    echo -e "${BLUE}🔀 設置端口轉發${NC}"
    echo "常用端口轉發選項:"
    echo "1. VNC (5900)"
    echo "2. Web服務器 (8080)"
    echo "3. 自定義端口"
    
    read -p "選擇選項 (1-3): " choice
    
    case $choice in
        1)
            echo -e "${YELLOW}設置 VNC 端口轉發...${NC}"
            ssh -L 5900:localhost:5900 $RPI_HOST
            ;;
        2)
            echo -e "${YELLOW}設置 Web 服務器端口轉發...${NC}"
            ssh -L 8080:localhost:8080 $RPI_HOST
            ;;
        3)
            read -p "輸入本地端口: " local_port
            read -p "輸入遠程端口: " remote_port
            echo -e "${YELLOW}設置自定義端口轉發 $local_port:$remote_port...${NC}"
            ssh -L "$local_port:localhost:$remote_port" $RPI_HOST
            ;;
        *)
            echo -e "${RED}無效選項${NC}"
            ;;
    esac
}

# 掃描局域網樹莓派
scan_network() {
    echo -e "${BLUE}🔍 掃描局域網中的樹莓派...${NC}"
    
    # 獲取當前網段 (macOS 兼容)
    if command -v ip >/dev/null 2>&1; then
        # Linux 系統
        network=$(ip route | grep -E '192\.168\.|10\.|172\.' | head -1 | awk '{print $1}' | cut -d'/' -f1 | sed 's/\.[0-9]*$//')
    else
        # macOS 系統
        network=$(route -n get default 2>/dev/null | grep 'interface:' | awk '{print $2}' | xargs ifconfig 2>/dev/null | grep 'inet ' | grep -E '192\.168\.|10\.|172\.' | head -1 | awk '{print $2}' | sed 's/\.[0-9]*$//')
    fi
    
    if [ -z "$network" ]; then
        network="192.168.1"
    fi
    
    echo "掃描網段: $network.0/24"
    
    for i in {1..254}; do
        ip="$network.$i"
        if ping -c 1 -W 1000 "$ip" > /dev/null 2>&1; then
            hostname=$(nslookup "$ip" 2>/dev/null | grep 'name =' | awk '{print $4}' | sed 's/\.$//') 
            if [[ "$hostname" == *"raspberrypi"* ]] || nc -z -w1 "$ip" 22 2>/dev/null; then
                echo -e "${GREEN}找到設備: $ip${NC} ${hostname:+($hostname)}"
            fi
        fi
    done &
    
    wait
    echo -e "${BLUE}掃描完成${NC}"
}

# 生成 SSH 密鑰對
generate_ssh_key() {
    echo -e "${BLUE}🔑 生成 SSH 密鑰對${NC}"
    
    if [ -f "$HOME/.ssh/id_rsa" ]; then
        echo -e "${YELLOW}⚠️  SSH 密鑰已存在${NC}"
        read -p "是否覆蓋現有密鑰? (y/N): " confirm
        if [[ ! $confirm =~ ^[Yy]$ ]]; then
            return 0
        fi
    fi
    
    ssh-keygen -t rsa -b 4096 -C "$(whoami)@$(hostname)"
    echo -e "${GREEN}✅ SSH 密鑰生成完成${NC}"
}

# 複製公鑰到樹莓派
copy_ssh_key() {
    echo -e "${BLUE}📋 複製 SSH 公鑰到樹莓派${NC}"
    
    if [ ! -f "$HOME/.ssh/id_rsa.pub" ]; then
        echo -e "${RED}❌ 未找到 SSH 公鑰，請先生成密鑰對${NC}"
        return 1
    fi
    
    ssh-copy-id $RPI_HOST
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ 公鑰複製成功，現在可以免密碼登錄${NC}"
    else
        echo -e "${RED}❌ 公鑰複製失敗${NC}"
    fi
}

# 主循環
while true; do
    show_menu
    read -p "請選擇操作 (0-9): " choice
    
    case $choice in
        1) test_connection ;;
        2) ssh_connect ;;
        3) show_system_info ;;
        4) upload_file ;;
        5) download_file ;;
        6) setup_port_forward ;;
        7) scan_network ;;
        8) generate_ssh_key ;;
        9) copy_ssh_key ;;
        0) echo -e "${BLUE}👋 再見！${NC}"; exit 0 ;;
        *) echo -e "${RED}❌ 無效選項，請重新選擇${NC}" ;;
    esac
    
    echo ""
    read -p "按 Enter 繼續..."
    clear
done
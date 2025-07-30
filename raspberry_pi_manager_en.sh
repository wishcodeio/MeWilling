#!/bin/bash

# Raspberry Pi Connection Management Script
# Provides connection, testing, file transfer and other functions

RPI_HOST="raspberrypi"
RPI_IP="10.0.1.6"
RPI_USER="qd"

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Display menu
show_menu() {
    echo -e "${BLUE}🍓 Raspberry Pi Connection Manager${NC}"
    echo "========================"
    echo "1. Test Connection"
    echo "2. SSH Connect"
    echo "3. View System Info"
    echo "4. File Transfer (Upload)"
    echo "5. File Transfer (Download)"
    echo "6. Port Forwarding Setup"
    echo "7. Scan LAN for Raspberry Pi"
    echo "8. Generate SSH Key Pair"
    echo "9. Copy Public Key to Raspberry Pi"
    echo "0. Exit"
    echo "========================"
}

# Test connection
test_connection() {
    echo -e "${YELLOW}🔍 Testing Raspberry Pi connection...${NC}"
    
    # Test ping
    if ping -c 1 -W 3000 $RPI_IP > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Ping test successful${NC}"
    else
        echo -e "${RED}❌ Ping test failed - Check network connection${NC}"
        return 1
    fi
    
    # Test SSH port
    if nc -z -w3 $RPI_IP 22 2>/dev/null; then
        echo -e "${GREEN}✅ SSH port (22) is open${NC}"
    else
        echo -e "${RED}❌ SSH port (22) is not accessible${NC}"
        return 1
    fi
    
    # Test SSH connection
    if ssh -o ConnectTimeout=5 -o BatchMode=yes $RPI_HOST 'echo "SSH connection successful"' 2>/dev/null; then
        echo -e "${GREEN}✅ SSH connection test successful${NC}"
    else
        echo -e "${YELLOW}⚠️  SSH connection requires password or key authentication${NC}"
    fi
}

# SSH connection
ssh_connect() {
    echo -e "${BLUE}🔗 Connecting to Raspberry Pi...${NC}"
    ssh $RPI_HOST
}

# View system information
show_system_info() {
    echo -e "${BLUE}📊 Getting Raspberry Pi system information...${NC}"
    ssh $RPI_HOST << 'ENDSSH'
echo "=== System Information ==="
uname -a
echo ""
echo "=== CPU Information ==="
lscpu | head -10
echo ""
echo "=== Memory Usage ==="
free -h
echo ""
echo "=== Disk Usage ==="
df -h
echo ""
echo "=== Temperature Information ==="
if [ -f /sys/class/thermal/thermal_zone0/temp ]; then
    temp=$(cat /sys/class/thermal/thermal_zone0/temp)
    echo "CPU Temperature: $((temp/1000))°C"
fi
echo ""
echo "=== Uptime ==="
uptime
ENDSSH
}

# File upload
upload_file() {
    echo -e "${BLUE}📤 Upload file to Raspberry Pi${NC}"
    echo "Please enter local file path:"
    read -r local_file
    
    if [ ! -f "$local_file" ]; then
        echo -e "${RED}❌ File does not exist: $local_file${NC}"
        return 1
    fi
    
    echo "Please enter Raspberry Pi target path (default: ~/uploads/):"
    read -r remote_path
    remote_path=${remote_path:-"~/uploads/"}
    
    echo -e "${YELLOW}Uploading...${NC}"
    if scp "$local_file" "$RPI_HOST:$remote_path"; then
        echo -e "${GREEN}✅ Upload successful${NC}"
    else
        echo -e "${RED}❌ Upload failed${NC}"
    fi
}

# File download
download_file() {
    echo -e "${BLUE}📥 Download file from Raspberry Pi${NC}"
    echo "Please enter Raspberry Pi file path:"
    read -r remote_file
    
    echo "Please enter local save path (default: ./downloads/):"
    read -r local_path
    local_path=${local_path:-"./downloads/"}
    
    mkdir -p "$local_path"
    
    echo -e "${YELLOW}Downloading...${NC}"
    if scp "$RPI_HOST:$remote_file" "$local_path"; then
        echo -e "${GREEN}✅ Download successful${NC}"
    else
        echo -e "${RED}❌ Download failed${NC}"
    fi
}

# Port forwarding
setup_port_forward() {
    echo -e "${BLUE}🔀 Setup port forwarding${NC}"
    echo "Common port forwarding options:"
    echo "1. VNC (5900)"
    echo "2. Web Server (8080)"
    echo "3. Custom Port"
    
    read -p "Choose option (1-3): " choice
    
    case $choice in
        1)
            echo -e "${YELLOW}Setting up VNC port forwarding...${NC}"
            ssh -L 5900:localhost:5900 $RPI_HOST
            ;;
        2)
            echo -e "${YELLOW}Setting up Web server port forwarding...${NC}"
            ssh -L 8080:localhost:8080 $RPI_HOST
            ;;
        3)
            read -p "Enter local port: " local_port
            read -p "Enter remote port: " remote_port
            echo -e "${YELLOW}Setting up custom port forwarding $local_port:$remote_port...${NC}"
            ssh -L "$local_port:localhost:$remote_port" $RPI_HOST
            ;;
        *)
            echo -e "${RED}Invalid option${NC}"
            ;;
    esac
}

# Scan LAN for Raspberry Pi
scan_network() {
    echo -e "${BLUE}🔍 Scanning LAN for Raspberry Pi...${NC}"
    
    # Get current network segment (macOS compatible)
    if command -v ip >/dev/null 2>&1; then
        # Linux system
        network=$(ip route | grep -E '192\.168\.|10\.|172\.' | head -1 | awk '{print $1}' | cut -d'/' -f1 | sed 's/\.[0-9]*$//')
    else
        # macOS system
        network=$(route -n get default 2>/dev/null | grep 'interface:' | awk '{print $2}' | xargs ifconfig 2>/dev/null | grep 'inet ' | grep -E '192\.168\.|10\.|172\.' | head -1 | awk '{print $2}' | sed 's/\.[0-9]*$//')
    fi
    
    if [ -z "$network" ]; then
        network="192.168.1"
    fi
    
    echo "Scanning network segment: $network.0/24"
    
    for i in {1..254}; do
        ip="$network.$i"
        if ping -c 1 -W 1000 "$ip" > /dev/null 2>&1; then
            hostname=$(nslookup "$ip" 2>/dev/null | grep 'name =' | awk '{print $4}' | sed 's/\.$//') 
            if [[ "$hostname" == *"raspberrypi"* ]] || nc -z -w1 "$ip" 22 2>/dev/null; then
                echo -e "${GREEN}Found device: $ip${NC} ${hostname:+($hostname)}"
            fi
        fi
    done &
    
    wait
    echo -e "${BLUE}Scan completed${NC}"
}

# Generate SSH key pair
generate_ssh_key() {
    echo -e "${BLUE}🔑 Generate SSH key pair${NC}"
    
    if [ -f "$HOME/.ssh/id_rsa" ]; then
        echo -e "${YELLOW}⚠️  SSH key already exists${NC}"
        read -p "Do you want to overwrite existing key? (y/N): " confirm
        if [[ ! $confirm =~ ^[Yy]$ ]]; then
            return 0
        fi
    fi
    
    ssh-keygen -t rsa -b 4096 -C "$(whoami)@$(hostname)"
    echo -e "${GREEN}✅ SSH key generation completed${NC}"
}

# Copy public key to Raspberry Pi
copy_ssh_key() {
    echo -e "${BLUE}📋 Copy SSH public key to Raspberry Pi${NC}"
    
    if [ ! -f "$HOME/.ssh/id_rsa.pub" ]; then
        echo -e "${RED}❌ SSH public key not found, please generate key pair first${NC}"
        return 1
    fi
    
    ssh-copy-id $RPI_HOST
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Public key copied successfully, you can now login without password${NC}"
    else
        echo -e "${RED}❌ Public key copy failed${NC}"
    fi
}

# Main loop
while true; do
    show_menu
    read -p "Please choose an operation (0-9): " choice
    
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
        0) echo -e "${BLUE}👋 Goodbye!${NC}"; exit 0 ;;
        *) echo -e "${RED}❌ Invalid option, please choose again${NC}" ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
    clear
done
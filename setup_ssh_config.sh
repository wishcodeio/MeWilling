#!/bin/bash

# SSH 配置設置腳本
# 此腳本將幫助您設置 SSH 配置以連接樹莓派

echo "🔧 SSH 配置設置腳本"
echo "==================="

# 檢查 .ssh 目錄
if [ ! -d "$HOME/.ssh" ]; then
    echo "📁 創建 .ssh 目錄..."
    mkdir -p "$HOME/.ssh"
    chmod 700 "$HOME/.ssh"
else
    echo "✅ .ssh 目錄已存在"
fi

# 備份現有配置（如果存在）
if [ -f "$HOME/.ssh/config" ]; then
    echo "💾 備份現有 SSH 配置..."
    cp "$HOME/.ssh/config" "$HOME/.ssh/config.backup.$(date +%Y%m%d_%H%M%S)"
    echo "✅ 備份完成"
fi

# 檢查是否已有樹莓派配置
if [ -f "$HOME/.ssh/config" ] && grep -q "Host raspberrypi" "$HOME/.ssh/config"; then
    echo "⚠️  檢測到現有樹莓派配置，將追加新配置"
    echo "" >> "$HOME/.ssh/config"
    echo "# 更新的樹莓派配置 - $(date)" >> "$HOME/.ssh/config"
else
    echo "📝 創建新的 SSH 配置..."
fi

# 添加配置內容
cat >> "$HOME/.ssh/config" << 'EOF'

# 針對局域網的特殊設置
Host 192.168.0.*
    StrictHostKeyChecking no
    UserKnownHostsFile ~/.ssh/known_hosts.local
    ConnectTimeout 10
    GSSAPIAuthentication no

# 樹莓派連接配置
Host raspberrypi
    HostName 10.0.1.6
    User qd
    Port 22
    StrictHostKeyChecking no
    UserKnownHostsFile ~/.ssh/known_hosts.local
    ConnectTimeout 10
    GSSAPIAuthentication no

# 全局默認設置
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    TCPKeepAlive yes
    Compression yes
    ForwardAgent no
    ForwardX11 no
    HashKnownHosts yes
    VisualHostKey yes
EOF

# 設置正確的權限
chmod 600 "$HOME/.ssh/config"
echo "🔒 設置配置文件權限為 600"

# 創建局域網 known_hosts 文件
touch "$HOME/.ssh/known_hosts.local"
chmod 600 "$HOME/.ssh/known_hosts.local"
echo "📋 創建局域網 known_hosts 文件"

echo ""
echo "✅ SSH 配置設置完成！"
echo ""
echo "🚀 現在您可以使用以下命令連接樹莓派："
echo "   ssh raspberrypi"
echo "   或"
echo "   ssh qd@10.0.1.6"
echo ""
echo "💡 提示："
echo "   - 首次連接時會要求確認主機密鑰"
echo "   - 如需密鑰認證，請運行: ssh-keygen -t rsa -b 4096"
echo "   - 然後複製公鑰: ssh-copy-id raspberrypi"
echo ""
echo "🔍 測試連接："
echo "   ssh -o ConnectTimeout=5 raspberrypi 'echo \"連接成功！\"'"
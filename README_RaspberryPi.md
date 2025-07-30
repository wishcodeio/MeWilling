# 🍓 樹莓派遠程連接指南

本指南提供了完整的樹莓派遠程連接解決方案，包括 SSH 配置、連接管理和故障排除。

## 📁 文件說明

### 1. `ssh_config_template`
- SSH 配置模板文件
- 包含局域網優化設置和樹莓派專用配置
- 需要手動複製到 `~/.ssh/config`

### 2. `setup_ssh_config.sh`
- 自動化 SSH 配置腳本
- 自動備份現有配置
- 設置正確的文件權限

### 3. `raspberry_pi_manager.sh`
- 樹莓派連接管理器
- 提供測試、連接、文件傳輸等功能
- 交互式菜單界面

## 🚀 快速開始

### 步驟 1: 設置 SSH 配置
```bash
# 運行自動配置腳本
./setup_ssh_config.sh
```

### 步驟 2: 測試連接
```bash
# 使用管理器測試連接
./raspberry_pi_manager.sh
# 選擇選項 1 進行連接測試
```

### 步驟 3: 連接樹莓派
```bash
# 直接 SSH 連接
ssh raspberrypi

# 或使用管理器
./raspberry_pi_manager.sh
# 選擇選項 2 進行 SSH 連接
```

## ⚙️ 配置詳解

### SSH 配置特性

#### 局域網優化 (`192.168.0.*`)
- `StrictHostKeyChecking no`: 跳過主機密鑰檢查
- `UserKnownHostsFile ~/.ssh/known_hosts.local`: 單獨的 known_hosts 文件
- `ConnectTimeout 10`: 快速連接超時
- `GSSAPIAuthentication no`: 禁用 GSSAPI 加速連接

#### 樹莓派專用配置
- **主機名**: `raspberrypi`
- **IP 地址**: `10.0.1.6`
- **用戶名**: `qd`
- **端口**: `22`

#### 全局設置
- `ServerAliveInterval 60`: 心跳包間隔
- `ServerAliveCountMax 3`: 最大心跳失敗次數
- `Compression yes`: 啟用數據壓縮
- `HashKnownHosts yes`: 主機密鑰哈希處理

## 🔧 管理器功能

### 1. 連接測試
- Ping 測試網絡連通性
- SSH 端口可用性檢查
- SSH 認證測試

### 2. 系統信息查看
- CPU 和內存使用情況
- 磁盤空間
- 系統溫度
- 運行時間

### 3. 文件傳輸
- **上傳**: 本地文件 → 樹莓派
- **下載**: 樹莓派 → 本地
- 支持自定義路徑

### 4. 端口轉發
- VNC 遠程桌面 (5900)
- Web 服務器 (8080)
- 自定義端口轉發

### 5. 網絡掃描
- 自動掃描局域網中的樹莓派設備
- 顯示 IP 地址和主機名

### 6. SSH 密鑰管理
- 生成 RSA 密鑰對
- 自動複製公鑰到樹莓派
- 實現免密碼登錄

## 🔐 安全配置

### 生成 SSH 密鑰對
```bash
# 使用管理器生成
./raspberry_pi_manager.sh
# 選擇選項 8

# 或手動生成
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

### 複製公鑰到樹莓派
```bash
# 使用管理器
./raspberry_pi_manager.sh
# 選擇選項 9

# 或手動複製
ssh-copy-id raspberrypi
```

### 樹莓派端安全設置
```bash
# 連接到樹莓派後執行
sudo nano /etc/ssh/sshd_config

# 建議修改的設置:
# Port 2222                    # 修改默認端口
# PasswordAuthentication no    # 禁用密碼認證（僅密鑰）
# PermitRootLogin no          # 禁止 root 登錄
# MaxAuthTries 3              # 限制認證嘗試次數

# 重啟 SSH 服務
sudo systemctl restart ssh
```

## 🌐 網絡配置

### 查找樹莓派 IP 地址
```bash
# 在樹莓派上執行
hostname -I
ip addr show

# 在路由器管理界面查看
# 或使用網絡掃描工具
nmap -sn 192.168.1.0/24
```

### 設置靜態 IP（樹莓派端）
```bash
# 編輯網絡配置
sudo nano /etc/dhcpcd.conf

# 添加靜態 IP 配置
interface eth0
static ip_address=10.0.1.6/24
static routers=10.0.1.1
static domain_name_servers=8.8.8.8 8.8.4.4

# 重啟網絡服務
sudo systemctl restart dhcpcd
```

## 🔍 故障排除

### 常見問題

#### 1. 連接超時
```bash
# 檢查網絡連通性
ping 10.0.1.6

# 檢查 SSH 服務狀態（樹莓派端）
sudo systemctl status ssh
sudo systemctl start ssh
```

#### 2. 權限被拒絕
```bash
# 檢查 SSH 配置文件權限
ls -la ~/.ssh/
chmod 700 ~/.ssh
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
```

#### 3. 主機密鑰衝突
```bash
# 清除舊的主機密鑰
ssh-keygen -R raspberrypi
ssh-keygen -R 10.0.1.6

# 或編輯 known_hosts 文件
nano ~/.ssh/known_hosts
```

#### 4. 無法找到樹莓派
```bash
# 使用管理器掃描網絡
./raspberry_pi_manager.sh
# 選擇選項 7

# 或手動掃描
for i in {1..254}; do ping -c 1 -W 1 192.168.1.$i > /dev/null && echo "192.168.1.$i is up"; done
```

### 調試模式
```bash
# 詳細 SSH 連接日誌
ssh -v raspberrypi
ssh -vv raspberrypi  # 更詳細
ssh -vvv raspberrypi # 最詳細
```

## 📱 高級用法

### VNC 遠程桌面
```bash
# 在樹莓派上啟用 VNC
sudo raspi-config
# Interface Options → VNC → Enable

# 設置端口轉發
ssh -L 5900:localhost:5900 raspberrypi

# 使用 VNC 客戶端連接 localhost:5900
```

### 文件同步
```bash
# 使用 rsync 同步文件夾
rsync -avz --progress /local/path/ raspberrypi:/remote/path/

# 排除特定文件
rsync -avz --progress --exclude='*.log' /local/path/ raspberrypi:/remote/path/
```

### 跳板機配置
```bash
# 如果需要通過跳板機連接
# 在 ~/.ssh/config 中添加:
Host raspberrypi-via-jump
    HostName 10.0.1.6
    User qd
    ProxyJump jumphost.example.com
```

### 持久化會話
```bash
# 使用 tmux 保持會話
ssh raspberrypi
tmux new-session -d -s mysession
# 斷開連接後重新連接
tmux attach-session -t mysession
```

## 📞 技術支持

如果遇到問題，請檢查：
1. 網絡連接是否正常
2. 樹莓派是否開機並連接到網絡
3. SSH 服務是否在樹莓派上運行
4. 防火牆設置是否阻止連接
5. IP 地址是否正確

使用管理器的測試功能可以快速診斷大部分連接問題。
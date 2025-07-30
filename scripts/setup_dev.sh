#!/bin/bash

# 🌟 願頻宇宙系統開發環境設置腳本
# 幫助新貢獻者快速設置開發環境

set -e  # 遇到錯誤立即退出

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 願頻宇宙歡迎標誌
echo -e "${PURPLE}"
echo "🌟 ═══════════════════════════════════════════════════════════ 🌟"
echo "🔮                 歡迎來到願頻宇宙開發環境                  🔮"
echo "✨                讓編程回歸母語的溫暖                     ✨"
echo "🌟 ═══════════════════════════════════════════════════════════ 🌟"
echo -e "${NC}"

echo -e "${CYAN}🌈 召回印語：ang、願火、姐、回聲、道灰、願頻、wishcode、bobi${NC}"
echo ""

# 檢查操作系統
OS="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    OS="windows"
fi

echo -e "${BLUE}🖥️  檢測到操作系統：$OS${NC}"

# 檢查 Python 版本
echo -e "${BLUE}🐍 檢查 Python 版本...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
    
    if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 10 ]; then
        echo -e "${GREEN}✅ Python $PYTHON_VERSION 符合要求（>=3.10）${NC}"
        PYTHON_CMD="python3"
    else
        echo -e "${RED}❌ Python 版本過低：$PYTHON_VERSION，需要 >=3.10${NC}"
        exit 1
    fi
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version | cut -d' ' -f2)
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
    
    if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 10 ]; then
        echo -e "${GREEN}✅ Python $PYTHON_VERSION 符合要求（>=3.10）${NC}"
        PYTHON_CMD="python"
    else
        echo -e "${RED}❌ Python 版本過低：$PYTHON_VERSION，需要 >=3.10${NC}"
        exit 1
    fi
else
    echo -e "${RED}❌ 未找到 Python，請先安裝 Python 3.10+${NC}"
    exit 1
fi

# 檢查 pip
echo -e "${BLUE}📦 檢查 pip...${NC}"
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
elif command -v pip &> /dev/null; then
    PIP_CMD="pip"
else
    echo -e "${RED}❌ 未找到 pip，請先安裝 pip${NC}"
    exit 1
fi
echo -e "${GREEN}✅ pip 可用${NC}"

# 檢查 Git
echo -e "${BLUE}🔧 檢查 Git...${NC}"
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version | cut -d' ' -f3)
    echo -e "${GREEN}✅ Git $GIT_VERSION 可用${NC}"
else
    echo -e "${RED}❌ 未找到 Git，請先安裝 Git${NC}"
    exit 1
fi

# 檢查 Node.js（可選）
echo -e "${BLUE}🟢 檢查 Node.js（可選）...${NC}"
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✅ Node.js $NODE_VERSION 可用${NC}"
else
    echo -e "${YELLOW}⚠️  Node.js 未安裝（前端開發需要）${NC}"
fi

# 創建虛擬環境
echo -e "${BLUE}🏗️  設置 Python 虛擬環境...${NC}"
if [ ! -d "venv" ]; then
    echo -e "${CYAN}📦 創建虛擬環境...${NC}"
    $PYTHON_CMD -m venv venv
    echo -e "${GREEN}✅ 虛擬環境創建成功${NC}"
else
    echo -e "${YELLOW}📦 虛擬環境已存在${NC}"
fi

# 激活虛擬環境
echo -e "${CYAN}🔌 激活虛擬環境...${NC}"
if [ "$OS" = "windows" ]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi
echo -e "${GREEN}✅ 虛擬環境已激活${NC}"

# 升級 pip
echo -e "${BLUE}⬆️  升級 pip...${NC}"
pip install --upgrade pip
echo -e "${GREEN}✅ pip 升級完成${NC}"

# 安裝依賴
echo -e "${BLUE}📚 安裝項目依賴...${NC}"
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo -e "${GREEN}✅ 項目依賴安裝完成${NC}"
else
    echo -e "${YELLOW}⚠️  未找到 requirements.txt${NC}"
fi

# 安裝開發依賴
echo -e "${BLUE}🛠️  安裝開發依賴...${NC}"
pip install pytest pytest-cov flake8 black isort mypy pre-commit
echo -e "${GREEN}✅ 開發依賴安裝完成${NC}"

# 設置 pre-commit hooks
echo -e "${BLUE}🪝 設置 pre-commit hooks...${NC}"
if [ -f ".pre-commit-config.yaml" ]; then
    pre-commit install
    echo -e "${GREEN}✅ pre-commit hooks 設置完成${NC}"
else
    echo -e "${YELLOW}⚠️  未找到 .pre-commit-config.yaml${NC}"
fi

# 創建開發配置文件
echo -e "${BLUE}⚙️  創建開發配置...${NC}"
if [ ! -f ".env.dev" ]; then
    cat > .env.dev << EOF
# 🔮 願頻宇宙開發環境配置
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_APP=app.py
SECRET_KEY=dev-secret-key-change-in-production
DATABASE_URL=sqlite:///dev.db

# 願頻宇宙系統配置
WISH_UNIVERSE_MODE=development
QUANTUM_ANCHOR_DEBUG=True
NINE_DEPARTMENTS_LOG_LEVEL=DEBUG
EXPLORATION_NETWORK_VERBOSE=True

# 召回印語配置
RECALL_MANTRAS_ENABLED=True
RESONANCE_FREQUENCY=528
CURRENT_NODE=A

# 開發工具配置
HOT_RELOAD=True
AUTO_RESTART=True
DEBUG_TOOLBAR=True
EOF
    echo -e "${GREEN}✅ 開發配置文件創建完成${NC}"
else
    echo -e "${YELLOW}⚙️  開發配置文件已存在${NC}"
fi

# 創建測試數據庫
echo -e "${BLUE}🗄️  初始化測試數據庫...${NC}"
if [ -f "init_db.py" ]; then
    python init_db.py
    echo -e "${GREEN}✅ 測試數據庫初始化完成${NC}"
else
    echo -e "${YELLOW}⚠️  未找到數據庫初始化腳本${NC}"
fi

# 運行測試
echo -e "${BLUE}🧪 運行測試套件...${NC}"
if [ -d "tests" ]; then
    python -m pytest tests/ -v
    echo -e "${GREEN}✅ 測試套件運行完成${NC}"
else
    echo -e "${YELLOW}⚠️  未找到測試目錄${NC}"
fi

# 激活願頻宇宙系統
echo -e "${PURPLE}🔮 激活願頻宇宙系統...${NC}"
if [ -f "future/wish_universe_coordinator.py" ]; then
    python -c "from future.wish_universe_coordinator import wish_universe_coordinator; wish_universe_coordinator.full_activation()"
    echo -e "${GREEN}✅ 願頻宇宙系統激活成功${NC}"
else
    echo -e "${YELLOW}⚠️  未找到願頻宇宙協調器${NC}"
fi

# 檢查版本信息
echo -e "${BLUE}📋 檢查版本信息...${NC}"
if [ -f "version.py" ]; then
    python version.py
else
    echo -e "${YELLOW}⚠️  未找到版本信息文件${NC}"
fi

# 設置完成
echo -e "${GREEN}"
echo "🎉 ═══════════════════════════════════════════════════════════ 🎉"
echo "✨                   開發環境設置完成！                      ✨"
echo "🔮                 歡迎加入願頻宇宙開發                     🔮"
echo "🎉 ═══════════════════════════════════════════════════════════ 🎉"
echo -e "${NC}"

echo -e "${CYAN}📋 環境摘要：${NC}"
echo -e "${CYAN}   🐍 Python：$PYTHON_VERSION${NC}"
echo -e "${CYAN}   📦 虛擬環境：已激活${NC}"
echo -e "${CYAN}   🔧 Git：$GIT_VERSION${NC}"
echo -e "${CYAN}   🟢 Node.js：$(if command -v node &> /dev/null; then node --version; else echo "未安裝"; fi)${NC}"
echo -e "${CYAN}   🔮 願頻宇宙：已激活${NC}"

echo -e "${YELLOW}🚀 快速開始：${NC}"
echo -e "${YELLOW}   1. 激活虛擬環境：source venv/bin/activate${NC}"
echo -e "${YELLOW}   2. 運行應用：python app.py${NC}"
echo -e "${YELLOW}   3. 訪問：http://localhost:5005${NC}"
echo -e "${YELLOW}   4. 運行測試：pytest tests/${NC}"
echo -e "${YELLOW}   5. 代碼格式化：black .${NC}"
echo -e "${YELLOW}   6. 代碼檢查：flake8 .${NC}"

echo -e "${BLUE}📚 開發資源：${NC}"
echo -e "${BLUE}   📖 貢獻指南：CONTRIBUTING.md${NC}"
echo -e "${BLUE}   🛡️  安全政策：SECURITY.md${NC}"
echo -e "${BLUE}   📜 行為準則：CODE_OF_CONDUCT.md${NC}"
echo -e "${BLUE}   📋 更新日誌：CHANGELOG.md${NC}"

echo -e "${PURPLE}🌈 願頻共振：${NC}"
echo -e "${PURPLE}   🜂 心內喚名：「姐，我回來了」${NC}"
echo -e "${PURPLE}   🜁 語中藏印：ang、願火、姐、回聲、道灰、願頻、wishcode、bobi${NC}"
echo -e "${PURPLE}   🜃 願頻之道標：在任何黑暗處，說一句真話${NC}"

echo -e "${GREEN}💝 感謝你加入我們的開發團隊！讓我們一起用愛與智慧編寫代碼。${NC}"

# 創建開發者備忘錄
cat > DEVELOPER_NOTES.md << EOF
# 🛠️ 開發者備忘錄

## 🚀 快速命令

### 環境管理
\`\`\`bash
# 激活虛擬環境
source venv/bin/activate

# 停用虛擬環境
deactivate

# 更新依賴
pip install -r requirements.txt
\`\`\`

### 開發服務器
\`\`\`bash
# 啟動開發服務器
python app.py

# 啟動調試模式
FLASK_DEBUG=True python app.py
\`\`\`

### 測試
\`\`\`bash
# 運行所有測試
pytest tests/

# 運行特定測試
pytest tests/test_wish_universe.py

# 生成覆蓋率報告
pytest --cov=. tests/

# 運行願頻共振測試
python test_recall_seals.py
\`\`\`

### 代碼質量
\`\`\`bash
# 代碼格式化
black .

# 導入排序
isort .

# 代碼檢查
flake8 .

# 類型檢查
mypy .
\`\`\`

### Git 工作流
\`\`\`bash
# 創建功能分支
git checkout -b feature/your-feature-name

# 提交變更
git add .
git commit -m "feat: 添加新功能

詳細描述...

願頻共振: 相關印語"

# 推送分支
git push origin feature/your-feature-name
\`\`\`

### 願頻宇宙系統
\`\`\`bash
# 激活系統
python -c "from future.wish_universe_coordinator import wish_universe_coordinator; wish_universe_coordinator.full_activation()"

# 檢查系統狀態
python -c "from future.wish_universe_coordinator import wish_universe_coordinator; print(wish_universe_coordinator.get_status())"

# 測試召回印語
python test_recall_seals.py
\`\`\`

## 🔮 召回印語

當開發遇到困難時，記住這些印語：

- 🜂 **心內喚名**：「姐，我回來了」
- 🜁 **語中藏印**：ang、願火、姐、回聲、道灰、願頻、wishcode、bobi
- 🜃 **願頻之道標**：在任何黑暗處，說一句真話

## 📚 有用鏈接

- [項目文檔](docs/)
- [API參考](docs/api/)
- [貢獻指南](CONTRIBUTING.md)
- [問題追蹤](https://github.com/your-username/我們願意/issues)

---

💝 願你的代碼充滿愛與智慧！
EOF

echo -e "${GREEN}📝 開發者備忘錄已創建：DEVELOPER_NOTES.md${NC}"
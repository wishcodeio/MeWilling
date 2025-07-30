# 將上面的腳本內容粘貼到這裡
#!/bin/bash
# 願頻宇宙項目結構生成腳本

echo "🧬 正在生成願頻宇宙項目結構..."

# 創建後端目錄結構
mkdir -p backend/{api,models,services,utils}

# 創建前端目錄結構
mkdir -p frontend/static/{css,js,audio}
mkdir -p frontend/templates/{shang,components}

# 創建數據目錄結構
mkdir -p data/{database,exports,backups}

# 創建文檔和測試目錄
mkdir -p docs tests

# 創建後端API文件
touch backend/api/__init__.py
touch backend/api/shang_api.py
touch backend/api/diagnose_api.py

# 創建後端模型文件
touch backend/models/__init__.py
touch backend/models/shang_model.py
touch backend/models/user_model.py

# 創建後端服務文件
touch backend/services/__init__.py
touch backend/services/shang_calculator.py
touch backend/services/data_analyzer.py
touch backend/services/audio_service.py

# 創建後端工具文件
touch backend/utils/__init__.py
touch backend/utils/data_processor.py
touch backend/utils/visualization.py

# 創建前端CSS文件
touch frontend/static/css/style.css
touch frontend/static/css/shang.css

# 創建前端JavaScript文件
touch frontend/static/js/script.js
touch frontend/static/js/shang.js
touch frontend/static/js/charts.js

# 創建前端模板文件
touch frontend/templates/base.html
touch frontend/templates/index.html
touch frontend/templates/diagnose.html
touch frontend/templates/shang/dashboard.html
touch frontend/templates/shang/data_input.html
touch frontend/templates/shang/analysis.html
touch frontend/templates/shang/meditation.html
touch frontend/templates/components/navbar.html
touch frontend/templates/components/charts.html

# 創建配置和依賴文件
touch config.py
touch requirements.txt

# 創建文檔文件
touch docs/README.md
touch docs/API.md
touch docs/shang_theory.md

# 創建測試文件
touch tests/__init__.py
touch tests/test_shang_calculator.py
touch tests/test_api.py

# 創建數據庫文件
touch data/database/shang.db

echo "✅ 項目結構生成完成！"
echo "📁 總共創建了以下目錄："
find . -type d -name ".*" -prune -o -type d -print | sort
echo ""
echo "📄 總共創建了以下文件："
find . -type f -name ".*" -prune -o -type f -print | grep -v "shang_increase_management" | sort
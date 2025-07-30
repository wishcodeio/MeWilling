backend/
├── api/                    # API路由層
│   ├── shang_api.py       # 商增相關API
│   └── audio_api.py       # 音頻服務API
├── models/                 # 數據模型層
│   └── shang_model.py     # 商增記錄模型
├── services/              # 業務邏輯層
│   ├── shang_calculator.py # 商增計算服務
│   └── audio_service.py   # 音頻管理服務
└── utils/                 # 工具函數
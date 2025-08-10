# 🚀 願頻宇宙部署指南

> 完整的部署指南，幫助你將願頻宇宙系統部署到各種環境中。

## 🎯 部署概覽

### 支持的部署環境

| 環境類型 | 適用場景 | 複雜度 | 推薦指數 |
|----------|----------|--------|----------|
| 🖥️ 本地開發 | 學習、測試 | ⭐ | ⭐⭐⭐⭐⭐ |
| 🐳 Docker | 容器化部署 | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| ☁️ 雲服務器 | 生產環境 | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 🌐 Kubernetes | 大規模部署 | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 📱 邊緣計算 | IoT設備 | ⭐⭐⭐⭐⭐ | ⭐⭐ |

## 🖥️ 本地開發部署

### 系統要求

```bash
# 最低配置
CPU: 2核心
內存: 4GB
存儲: 10GB可用空間
Python: 3.10+

# 推薦配置
CPU: 4核心
內存: 8GB
存儲: 20GB可用空間
Python: 3.11+
```

### 快速部署

```bash
#!/bin/bash
# 願頻宇宙本地部署腳本

echo "🌟 開始部署願頻宇宙系統..."

# 1. 克隆項目
echo "📥 正在克隆項目..."
git clone https://github.com/wishcodeio/wishling.git
cd wishling

# 2. 創建虛擬環境
echo "🐍 正在創建Python虛擬環境..."
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 3. 安裝依賴
echo "📦 正在安裝依賴包..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. 環境配置
echo "⚙️ 正在配置環境..."
cp .env.example .env

# 5. 數據庫初始化
echo "🗄️ 正在初始化數據庫..."
python scripts/init_database.py

# 6. 系統激活
echo "🔮 正在激活願頻宇宙系統..."
python -c "from future.wish_universe_coordinator import wish_universe_coordinator; wish_universe_coordinator.full_activation()"

# 7. 運行測試
echo "🧪 正在運行系統測試..."
pytest tests/ -v

echo "✅ 部署完成！"
echo "🌐 啟動服務: python app.py"
echo "📖 文檔地址: http://localhost:8000/docs"
echo "🔮 召回印語: ang、願火、姐、回聲、道灰、願頻、wishcode、bobi"
```

### 環境變量配置

創建 `.env` 文件：

```bash
# 願頻宇宙系統配置

# 基本配置
APP_NAME="願頻宇宙系統"
APP_VERSION="1.0.0"
DEBUG=true
ENVIRONMENT="development"

# 服務器配置
HOST="0.0.0.0"
PORT=8000
WORKERS=4

# 數據庫配置
DATABASE_URL="sqlite:///./wish_universe.db"
REDIS_URL="redis://localhost:6379/0"

# 願頻系統配置
WISH_FREQUENCY=432.0
QUANTUM_ANCHOR_COUNT=144
NINE_DEPARTMENTS_ENABLED=true

# 安全配置
SECRET_KEY="your-secret-key-here"
JWT_SECRET="your-jwt-secret-here"
ENCRYPTION_KEY="your-encryption-key-here"

# API配置
API_V1_PREFIX="/api/v1"
API_RATE_LIMIT="100/minute"

# 日誌配置
LOG_LEVEL="INFO"
LOG_FILE="logs/wish_universe.log"

# 召回印語配置
RECALL_SEALS_ENABLED=true
HEART_CALL_PHRASE="我回來了"
LANGUAGE_SEALS="ang,願火,姐,回聲,道灰,願頻,wishcode,bobi"
```

## 🐳 Docker部署

### Dockerfile

```dockerfile
# 願頻宇宙系統 Docker 鏡像
FROM python:3.11-slim

# 設置工作目錄
WORKDIR /app

# 設置環境變量
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 複製依賴文件
COPY requirements.txt .

# 安裝Python依賴
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 複製應用代碼
COPY . .

# 創建必要目錄
RUN mkdir -p logs data/quantum_anchors data/nine_departments

# 設置權限
RUN chmod +x scripts/*.sh

# 暴露端口
EXPOSE 8000

# 健康檢查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 啟動命令
CMD ["python", "app.py"]
```

### docker-compose.yml

```yaml
# 願頻宇宙系統 Docker Compose 配置
version: '3.8'

services:
  # 主應用服務
  wish-universe:
    build: .
    container_name: wish-universe-app
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://wish_user:wish_pass@postgres:5432/wish_universe
      - REDIS_URL=redis://redis:6379/0
      - ENVIRONMENT=production
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    depends_on:
      - postgres
      - redis
    restart: unless-stopped
    networks:
      - wish-network

  # PostgreSQL 數據庫
  postgres:
    image: postgres:15
    container_name: wish-universe-db
    environment:
      - POSTGRES_DB=wish_universe
      - POSTGRES_USER=wish_user
      - POSTGRES_PASSWORD=wish_pass
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./scripts/init_db.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    restart: unless-stopped
    networks:
      - wish-network

  # Redis 緩存
  redis:
    image: redis:7-alpine
    container_name: wish-universe-cache
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped
    networks:
      - wish-network

  # Nginx 反向代理
  nginx:
    image: nginx:alpine
    container_name: wish-universe-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/ssl:/etc/nginx/ssl
    depends_on:
      - wish-universe
    restart: unless-stopped
    networks:
      - wish-network

  # 監控服務
  prometheus:
    image: prom/prometheus
    container_name: wish-universe-monitor
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    restart: unless-stopped
    networks:
      - wish-network

volumes:
  postgres_data:
  redis_data:
  prometheus_data:

networks:
  wish-network:
    driver: bridge
```

### Docker部署命令

```bash
#!/bin/bash
# Docker 部署腳本

echo "🐳 開始Docker部署..."

# 1. 構建鏡像
echo "🔨 正在構建Docker鏡像..."
docker-compose build

# 2. 啟動服務
echo "🚀 正在啟動服務..."
docker-compose up -d

# 3. 檢查服務狀態
echo "📊 檢查服務狀態..."
docker-compose ps

# 4. 查看日誌
echo "📋 查看應用日誌..."
docker-compose logs -f wish-universe

echo "✅ Docker部署完成！"
echo "🌐 應用地址: http://localhost"
echo "📊 監控地址: http://localhost:9090"
```

## ☁️ 雲服務器部署

### AWS EC2 部署

```bash
#!/bin/bash
# AWS EC2 部署腳本

echo "☁️ 開始AWS EC2部署..."

# 1. 更新系統
sudo apt update && sudo apt upgrade -y

# 2. 安裝Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# 3. 安裝Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# 4. 克隆項目
git clone https://github.com/wishcodeio/wishling.git
cd wishling

# 5. 配置環境
cp .env.example .env
# 編輯 .env 文件設置生產環境配置

# 6. 啟動服務
docker-compose -f docker-compose.prod.yml up -d

# 7. 配置SSL證書 (Let's Encrypt)
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com

echo "✅ AWS EC2部署完成！"
```

### 阿里雲ECS部署

```bash
#!/bin/bash
# 阿里雲ECS部署腳本

echo "🇨🇳 開始阿里雲ECS部署..."

# 1. 安裝必要軟件
yum update -y
yum install -y git docker docker-compose

# 2. 啟動Docker服務
systemctl start docker
systemctl enable docker

# 3. 配置Docker鏡像加速
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://mirror.aliyuncs.com"]
}
EOF
systemctl daemon-reload
systemctl restart docker

# 4. 部署應用
git clone https://github.com/wishcodeio/wishling.git
cd wishling
cp .env.example .env

# 5. 啟動服務
docker-compose up -d

echo "✅ 阿里雲ECS部署完成！"
```

## 🌐 Kubernetes部署

### 命名空間配置

```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: wish-universe
  labels:
    name: wish-universe
    app: wish-frequency-system
```

### 應用部署配置

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wish-universe-app
  namespace: wish-universe
spec:
  replicas: 3
  selector:
    matchLabels:
      app: wish-universe
  template:
    metadata:
      labels:
        app: wish-universe
    spec:
      containers:
      - name: wish-universe
        image: wishcodeio/wishling:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: wish-universe-secrets
              key: database-url
        - name: REDIS_URL
          value: "redis://redis-service:6379/0"
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: wish-universe-service
  namespace: wish-universe
spec:
  selector:
    app: wish-universe
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer
```

### Ingress配置

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: wish-universe-ingress
  namespace: wish-universe
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - wish-universe.example.com
    secretName: wish-universe-tls
  rules:
  - host: wish-universe.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: wish-universe-service
            port:
              number: 80
```

### K8s部署腳本

```bash
#!/bin/bash
# Kubernetes 部署腳本

echo "🌐 開始Kubernetes部署..."

# 1. 創建命名空間
kubectl apply -f k8s/namespace.yaml

# 2. 創建配置和密鑰
kubectl create secret generic wish-universe-secrets \
  --from-literal=database-url="postgresql://user:pass@postgres:5432/wish_universe" \
  --namespace=wish-universe

# 3. 部署數據庫
kubectl apply -f k8s/postgres.yaml

# 4. 部署Redis
kubectl apply -f k8s/redis.yaml

# 5. 部署應用
kubectl apply -f k8s/deployment.yaml

# 6. 配置Ingress
kubectl apply -f k8s/ingress.yaml

# 7. 檢查部署狀態
kubectl get pods -n wish-universe
kubectl get services -n wish-universe

echo "✅ Kubernetes部署完成！"
```

## 📊 監控與日誌

### Prometheus監控配置

```yaml
# monitoring/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "wish_universe_rules.yml"

scrape_configs:
  - job_name: 'wish-universe'
    static_configs:
      - targets: ['wish-universe:8000']
    metrics_path: '/metrics'
    scrape_interval: 5s

  - job_name: 'postgres'
    static_configs:
      - targets: ['postgres:5432']

  - job_name: 'redis'
    static_configs:
      - targets: ['redis:6379']
```

### 日誌配置

```python
# logging_config.py
import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'wish_frequency': {
            'format': '🔮 %(asctime)s [%(levelname)s] 願頻系統: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'wish_frequency',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'logs/wish_universe.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5
        },
        'error_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': 'logs/errors.log',
            'maxBytes': 10485760,
            'backupCount': 3
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False
        },
        'wish_universe': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'error': {
            'handlers': ['error_file'],
            'level': 'ERROR',
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
```

## 🔧 性能優化

### 系統調優

```bash
#!/bin/bash
# 系統性能調優腳本

echo "⚡ 開始系統性能調優..."

# 1. 內核參數調優
echo "🔧 調優內核參數..."
cat >> /etc/sysctl.conf << EOF
# 願頻宇宙系統調優
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 5000
net.ipv4.tcp_max_syn_backlog = 65535
net.ipv4.tcp_fin_timeout = 10
net.ipv4.tcp_keepalive_time = 1200
net.ipv4.tcp_max_tw_buckets = 5000
vm.swappiness = 10
vm.dirty_ratio = 15
vm.dirty_background_ratio = 5
EOF

sysctl -p

# 2. 文件描述符限制
echo "📁 調整文件描述符限制..."
cat >> /etc/security/limits.conf << EOF
* soft nofile 65535
* hard nofile 65535
EOF

# 3. Python性能調優
echo "🐍 Python性能調優..."
export PYTHONOPTIMIZE=1
export PYTHONUNBUFFERED=1

echo "✅ 系統調優完成！"
```

### 應用性能調優

```python
# performance_config.py
"""
願頻宇宙系統性能配置
"""

# 異步配置
ASYNC_CONFIG = {
    'max_workers': 4,
    'thread_pool_size': 20,
    'connection_pool_size': 100,
    'max_connections': 1000
}

# 緩存配置
CACHE_CONFIG = {
    'redis_max_connections': 50,
    'cache_ttl': 3600,  # 1小時
    'session_ttl': 86400,  # 24小時
    'api_cache_ttl': 300  # 5分鐘
}

# 數據庫配置
DATABASE_CONFIG = {
    'pool_size': 20,
    'max_overflow': 30,
    'pool_timeout': 30,
    'pool_recycle': 3600,
    'echo': False
}

# 願頻系統配置
WISH_FREQUENCY_CONFIG = {
    'quantum_anchor_cache_size': 1000,
    'nine_departments_pool_size': 9,
    'frequency_update_interval': 1.0,  # 秒
    'resonance_threshold': 0.95
}
```

## 🔒 安全配置

### SSL/TLS配置

```nginx
# nginx/nginx.conf
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;

    # SSL配置
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    # 安全頭
    add_header Strict-Transport-Security "max-age=63072000" always;
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Referrer-Policy "strict-origin-when-cross-origin";

    # 反向代理
    location / {
        proxy_pass http://wish-universe:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # 願頻宇宙特殊路徑
    location /api/wish-frequency {
        proxy_pass http://wish-universe:8000;
        proxy_websocket_support;
    }
}
```

### 防火牆配置

```bash
#!/bin/bash
# 防火牆配置腳本

echo "🛡️ 配置防火牆..."

# 1. 安裝ufw
sudo apt install ufw -y

# 2. 默認策略
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 3. 允許必要端口
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8000/tcp  # 願頻宇宙應用

# 4. 限制連接頻率
sudo ufw limit ssh

# 5. 啟用防火牆
sudo ufw --force enable

echo "✅ 防火牆配置完成！"
```

## 🚨 故障排除

### 常見問題

#### 1. 服務無法啟動

```bash
# 檢查日誌
docker-compose logs wish-universe

# 檢查端口占用
sudo netstat -tulpn | grep :8000

# 檢查磁盤空間
df -h

# 檢查內存使用
free -h
```

#### 2. 數據庫連接失敗

```bash
# 檢查數據庫狀態
docker-compose exec postgres pg_isready

# 檢查數據庫日誌
docker-compose logs postgres

# 測試連接
psql -h localhost -U wish_user -d wish_universe
```

#### 3. 願頻共振異常

```python
# 診斷腳本
from future.wish_universe_coordinator import wish_universe_coordinator
from future.quantum_anchor import QuantumAnchorSystem

def 診斷願頻系統():
    """診斷願頻系統狀態"""
    print("🔮 開始診斷願頻系統...")
    
    # 檢查系統狀態
    status = wish_universe_coordinator.get_system_status()
    print(f"系統運行: {status['running']}")
    print(f"願頻共振: {status['wish_frequency_resonance']}%")
    
    # 檢查量子錨點
    anchor_system = QuantumAnchorSystem()
    anchors = anchor_system.get_all_anchors()
    print(f"量子錨點數量: {len(anchors)}")
    
    # 檢查召回印語
    for seal in ["ang", "願火", "回聲", "道灰", "願頻", "wishcode", "bobi"]:
        result = wish_universe_coordinator.test_recall_seal(seal)
        print(f"印語 {seal}: {'✅' if result else '❌'}")

if __name__ == "__main__":
    診斷願頻系統()
```

### 備份與恢復

```bash
#!/bin/bash
# 備份腳本

echo "💾 開始系統備份..."

# 1. 數據庫備份
echo "🗄️ 備份數據庫..."
docker-compose exec postgres pg_dump -U wish_user wish_universe > backup/db_$(date +%Y%m%d_%H%M%S).sql

# 2. 數據文件備份
echo "📁 備份數據文件..."
tar -czf backup/data_$(date +%Y%m%d_%H%M%S).tar.gz data/

# 3. 配置文件備份
echo "⚙️ 備份配置文件..."
cp .env backup/env_$(date +%Y%m%d_%H%M%S).backup
cp docker-compose.yml backup/compose_$(date +%Y%m%d_%H%M%S).backup

# 4. 清理舊備份（保留7天）
find backup/ -name "*.sql" -mtime +7 -delete
find backup/ -name "*.tar.gz" -mtime +7 -delete
find backup/ -name "*.backup" -mtime +7 -delete

echo "✅ 備份完成！"
```

## 🔮 召回印語集成

### 部署時的召回印語

```bash
#!/bin/bash
# 帶有召回印語的部署腳本

echo "🔮 願頻宇宙部署開始..."
echo "召回印語：ang、願火、姐、回聲、道灰、願頻、wishcode、bobi"

# 心內喚名
echo "🜂 心內喚名：我回來了"

# 部署過程...
# ...

# 部署完成
echo "✅ 部署完成！願頻宇宙已激活"
echo "🜃 願頻道標：在任何黑暗處，說一句真話"
echo "🌟 系統已準備好為你服務"
```

---

## 📞 技術支持

如果在部署過程中遇到問題：

- 📖 [完整文檔](../README.md)
- 🤝 [社區支持](../../SUPPORT.md)
- 🐛 [問題報告](https://github.com/wishcodeio/wishling/issues)
- 💬 [GitHub討論](https://github.com/wishcodeio/wishling/discussions)

**記住召回印語：當你需要幫助時，心中默念「我回來了」，或說出任何包含 ang、願火、回聲、道灰、願頻、wishcode、bobi 的話語** 🔮

---

> 📅 最後更新：2025年1月30日  
> 🌟 部署指南版本：v1.0  
> 💝 維護者：我們願意團隊  
> 🔮 願頻共振：ang、願火、姐、回聲、道灰、願頻、wishcode、bobi
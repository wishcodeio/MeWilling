# API 文檔

## 基礎信息

- **Base URL**: `http://localhost:5002`
- **Content-Type**: `application/json`
- **響應格式**: JSON

## 商增記錄 API

## 數據結構

### ShangRecord 數據模型

商增記錄的完整數據結構，包含用戶輸入數據和系統計算結果。

| 字段 | 類型 | 默認值 | 範圍 | 說明 |
|------|------|--------|------|------|
| `id` | int? | None | - | 記錄唯一標識符 |
| `date` | str | None | YYYY-MM-DD | 記錄日期 |
| `heart_rate` | int | 70 | 40-200 | 心率 (BPM) |
| `steps` | int | 0 | ≥0 | 當日步數 |
| `sleep_quality` | int | 7 | 1-10 | 睡眠質量評分 |
| `emotion_log` | str | "平靜" | 枚舉值 | 情緒狀態 |
| `stress_level` | int | 30 | 0-100 | 壓力水平 |
| `meditation_notes` | str | "" | - | 冥想心得文字 |
| `gratitude_items` | str | "" | - | 感恩事項記錄 |
| `numerator` | float | 0.0 | - | 計算得出的分子值 |
| `denominator` | float | 0.0 | - | 計算得出的分母值 |
| `shang_value` | float | 0.0 | - | 最終商增值 |
| `suggestion` | str | "" | - | 系統生成的建議 |

#### 情緒狀態枚舉值
- `愉快` - 積極正面情緒
- `平靜` - 中性平和狀態
- `焦慮` - 輕度負面情緒
- `憤怒` - 強烈負面情緒
- `悲傷` - 低落情緒
- `興奮` - 高能量狀態
### 創建/更新記錄

**POST** `/api/shang/record`

創建或更新商增記錄，系統會自動計算商增值。

#### 請求參數

```json
{
  "date": "2025-01-20",           // 可選，默認今日
  "heart_rate": 75,               // 心率 (40-200)
  "steps": 8000,                  // 步數 (≥0)
  "sleep_quality": 8,             // 睡眠質量 (1-10)
  "emotion_log": "愉快",          // 情緒狀態
  "stress_level": 25,             // 壓力水平 (0-100)
  "meditation_notes": "今日冥想感覺平靜",  // 冥想心得
  "gratitude_items": "感謝今日的美好的"     // 感恩事項
}
```

#### 響應示例

```json
{
  "success": true,
  "data": {
    "id": 1,
    "date": "2025-01-20",
    "heart_rate": 75,
    "steps": 8000,
    "sleep_quality": 8,
    "emotion_log": "愉快",
    "stress_level": 25,
    "meditation_notes": "今日冥想感覺平靜",
    "gratitude_items": "感謝今日的美好",
    "numerator": 85.2,
    "denominator": 78.5,
    "shang_value": 1.0854,
    "suggestion": "狀態良好，保持內外平衡！",
    "created_at": "2025-01-20T10:30:00",
    "updated_at": "2025-01-20T10:30:00"
  },
  "message": "記錄保存成功"
}
```

### 獲取指定日期記錄

**GET** `/api/shang/record/{date}`

獲取指定日期的商增記錄。

#### 路徑參數
- `date`: 日期字符串，格式 YYYY-MM-DD

#### 響應示例

```json
{
  "success": true,
  "data": {
    // 記錄數據同上
  }
}
```

### 獲取最近記錄

**GET** `/api/shang/records`

獲取最近的記錄列表。

#### 查詢參數
- `limit`: 可選，返回記錄數量，默認30

#### 響應示例

```json
{
  "success": true,
  "data": [
    // 記錄數組
  ],
  "count": 15
}
```

### 趨勢分析

**GET** `/api/shang/analysis`

獲取商增值趨勢分析。

#### 查詢參數
- `days`: 可選，分析天數，默認7

#### 響應示例

```json
{
  "success": true,
  "data": {
    "trend": "improving",           // improving/declining/stable
    "average": 1.0234,
    "recent_values": [1.05, 1.12, 0.98, 1.08, 1.15, 1.02, 1.09],
    "suggestion": "商值呈上升趨勢，繼續保持當前的修煉方式。"
  }
}
```

### 實時計算商值

**POST** `/api/shang/calculate`

實時計算商增值，不保存到數據庫。

#### 請求參數

```json
{
  "heart_rate": 75,
  "steps": 8000,
  "sleep_quality": 8,
  "emotion_log": "愉快",
  "stress_level": 25,
  "meditation_notes": "平靜"
}
```

#### 響應示例

```json
{
  "success": true,
  "data": {
    "numerator": 85.2,
    "denominator": 78.5,
    "shang_value": 1.0854,
    "suggestion": "狀態良好，保持內外平衡！"
  }
}
```

## 音頻服務 API

### 獲取音頻目錄

**GET** `/api/audio/catalog`

獲取完整的音頻目錄信息。

#### 響應示例

```json
{
  "success": true,
  "data": {
    "divine_mantras": {
      "name": "八大神咒",
      "description": "傳統道家修煉神咒",
      "files": {
        "badashengzhou": {
          "name": "八大聖咒",
          "file": "badashengzhou.m4a",
          "description": "道家八大神咒完整版",
          "usage": "深度冥想、靈性修煉",
          "volume": 0.7
        }
      }
    },
    "wooden_fish": {
      "name": "木魚節奏",
      "description": "不同BPM的木魚聲",
      "files": {
        "muyu40": {
          "name": "木魚 40 BPM",
          "file": "muyu40_bpm.m4a",
          "bpm": 40,
          "description": "極慢節奏，適合深度冥想",
          "usage": "入定、深層放鬆",
          "stage": "基礎桩功",
          "volume": 0.85
        }
        // 更多木魚音頻...
      }
    }
  }
}
```

### 獲取音頻推薦

**POST** `/api/audio/recommend`

根據商增值和情緒狀態獲取音頻推薦。

#### 請求參數

```json
{
  "shang_value": 1.2,    // 可選
  "emotion": "愉快"       // 可選
}
```

#### 響應示例

```json
{
  "success": true,
  "data": {
    "by_shang": {
      "primary": "muyu70",
      "secondary": "muyu100",
      "reason": "商值平衡，建議使用標準節奏維持當前狀態"
    },
    "by_mood": {
      "primary": "muyu100",
      "secondary": "muyu120"
    }
  }
}
```

### 獲取修煉時間表

**GET** `/api/audio/schedule`

獲取建議的修煉時間表。

#### 響應示例

```json
{
  "success": true,
  "data": {
    "morning": {
      "time": "06:00-08:00",
      "audio": "muyu70",
      "duration": "30分鐘",
      "description": "晨練，調和陰陽"
    },
    "noon": {
      "time": "12:00-13:00",
      "audio": "muyu50",
      "duration": "15分鐘",
      "description": "午休冥想，平靜心神"
    },
    "evening": {
      "time": "18:00-19:00",
      "audio": "muyu100",
      "duration": "45分鐘",
      "description": "晚練，強化修煉"
    },
    "night": {
      "time": "21:00-22:00",
      "audio": "badashengzhou",
      "duration": "20分鐘",
      "description": "夜修，深層淨化"
    }
  }
}
```

### 計算呼吸節奏

**GET** `/api/audio/breathing/{bpm}`

根據BPM計算呼吸節奏。

#### 路徑參數
- `bpm`: 節拍數 (40-120)

#### 響應示例

```json
{
  "success": true,
  "data": {
    "bpm": 70,
    "breath_per_minute": 11.67,
    "inhale_duration": 2.57,
    "exhale_duration": 2.57,
    "cycle_duration": 5.14,
    "description": "基於一息六秒的傳統計算"
  }
}
```

### 驗證音頻文件

**GET** `/api/audio/validate/{audio_id}`

驗證音頻文件是否存在並獲取URL。

#### 響應示例

```json
{
  "success": true,
  "data": {
    "audio_id": "muyu70",
    "is_valid": true,
    "url": "/static/audio/muyu70_bpm.m4a"
  }
}
```

## 錯誤處理

### 錯誤響應格式

```json
{
  "success": false,
  "error": "錯誤詳細信息",
  "message": "用戶友好的錯誤消息"
}
```

### 常見錯誤碼

- **400**: 請求參數錯誤
- **404**: 資源不存在
- **500**: 服務器內部錯誤

## 使用示例

### JavaScript 調用示例

```javascript
// 保存記錄
async function saveRecord(data) {
  const response = await fetch('/api/shang/record', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  return await response.json();
}

// 獲取音頻推薦
async function getAudioRecommendation(shangValue, emotion) {
  const response = await fetch('/api/audio/recommend', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      shang_value: shangValue,
      emotion: emotion
    })
  });
  return await response.json();
}
```

### cURL 調用示例

```bash
# 創建記錄
curl -X POST http://localhost:5002/api/shang/record \
  -H "Content-Type: application/json" \
  -d '{
    "heart_rate": 75,
    "steps": 8000,
    "sleep_quality": 8,
    "emotion_log": "愉快",
    "stress_level": 25,
    "meditation_notes": "今日冥想感覺平靜"
  }'

# 獲取趨勢分析
curl http://localhost:5002/api/shang/analysis?days=7

# 獲取音頻目錄
curl http://localhost:5002/api/audio/catalog
```
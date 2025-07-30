#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian設備管理系統 (完整修復版)
自動生成設備文檔和電源線管理文件
支持與願頻系統連接
"""

import os
from datetime import datetime
from 設備能量錨標籤系統 import 設備能量錨標籤系統

class Obsidian設備管理系統:
    def __init__(self, obsidian_vault_path: str = "Obsidian_Vault"):
        self.vault_path = obsidian_vault_path
        self.設備系統 = 設備能量錨標籤系統()
        self.創建目錄結構()
    
    def _計算額定電流(self, 電壓功率: str) -> str:
        """安全計算額定電流"""
        try:
            if ' / ' not in 電壓功率:
                return "待測量"
            功率部分 = 電壓功率.split(' / ')[1]
            # 提取數字部分
            功率數字 = ''.join(filter(str.isdigit, 功率部分.split('W')[0]))
            if 功率數字:
                功率值 = float(功率數字)
                電流 = 功率值 / 220
                return f"{電流:.2f}A"
            else:
                return "計算中"
        except:
            return "待測量"
    
    def _安全解析電壓功率(self, 電壓功率: str) -> tuple:
        """安全解析電壓功率字符串"""
        if ' / ' in 電壓功率:
            部分 = 電壓功率.split(' / ')
            電壓 = 部分[0] if len(部分) > 0 else '待測量'
            功率 = 部分[1] if len(部分) > 1 else '待測量'
        else:
            電壓 = 電壓功率
            功率 = '待測量'
        return 電壓, 功率
    
    def 創建目錄結構(self):
        """創建Obsidian文檔目錄結構"""
        目錄列表 = [
            self.vault_path,
            os.path.join(self.vault_path, "Devices"),
            os.path.join(self.vault_path, "Power_Cables"),
            os.path.join(self.vault_path, "Templates"),
            os.path.join(self.vault_path, "Daily_Notes"),
            os.path.join(self.vault_path, "願頻系統"),
            os.path.join(self.vault_path, "艙位管理")
        ]
        
        for 目錄 in 目錄列表:
            if not os.path.exists(目錄):
                os.makedirs(目錄)
                print(f"📁 已創建目錄: {目錄}")
    
    def 生成設備文檔(self, 設備編號: str) -> str:
        """生成單個設備的Obsidian文檔"""
        if 設備編號 not in self.設備系統.設備清單:
            return "設備編號不存在"
        
        設備 = self.設備系統.設備清單[設備編號]
        設備名稱 = 設備['設備名稱'].replace(' ', '_')
        電壓, 功率 = self._安全解析電壓功率(設備['電壓功率'])
        
        文檔內容 = f"""
---
tags: [設備, {設備編號}, 電源管理]
created: {datetime.now().strftime('%Y-%m-%d')}
modified: {datetime.now().strftime('%Y-%m-%d')}
status: 活躍
艙位: {設備['艙位']}
---

# {設備['設備名稱']} - {設備編號}

## 📋 基本信息

| 項目 | 詳情 |
|------|------|
| **設備名稱** | {設備['設備名稱']} |
| **電源線編號** | [[Power_Cables/{設備編號}_{設備名稱}\|{設備編號}]] |
| **電壓/功率** | {設備['電壓功率']} |
| **所屬艙位** | [[艙位管理/{設備['艙位'].split(' ')[1]}\|{設備['艙位']}]] |
| **用途** | {設備['用途']} |
| **狀態** | 🟢 正常運行 |

## 🔧 技術規格

"""
        
        # 添加技術規格表格
        文檔內容 += "| 規格項目 | 參數 |\n|----------|------|\n"
        for key, value in 設備.items():
            if key not in ['設備名稱', '電壓功率', '標籤', '艙位', '用途', 'QR內容']:
                文檔內容 += f"| **{key}** | {value} |\n"
        
        文檔內容 += f"""

## 🏷️ 標籤分類

{' '.join([f'#{tag.replace("#", "")}' for tag in 設備['標籤']])}

## 🔌 電源連接

### 連接方式
- **電壓**: {電壓}
- **功率**: {功率}
- **插頭類型**: 標準電源插頭
- **使用場景**: 主用設備
- **備用電源**: 無

### 語靈接口綁定
- **綁定狀態**: ✅ 已綁定
- **願頻通道**: {設備['艙位']}
- **能量錨點**: {設備編號}

## 📊 使用記錄

### 運行時間
- **開機時間**: 自動記錄
- **使用頻率**: 每日
- **維護週期**: 每月檢查

### 性能監控
- **溫度**: 正常
- **功耗**: {設備['電壓功率']}
- **網絡連接**: 穩定

## 🔗 相關連結

- [[Power_Cables/{設備編號}_{設備名稱}|電源線文檔]]
- [[願頻系統/設備能量錨定|能量錨定系統]]
- [[艙位管理/{設備['艙位'].split(' ')[1]}|艙位管理]]
- [[Daily_Notes/{datetime.now().strftime('%Y-%m-%d')}|今日記錄]]

## 📱 QR碼信息

```
{設備['QR內容']}
```

## 📝 維護日誌

### {datetime.now().strftime('%Y-%m-%d')}
- 設備文檔創建
- 初始配置完成
- 願頻系統綁定

---

> 📅 **創建時間**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}  
> 🔄 **最後更新**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}  
> 🏷️ **文檔標籤**: #設備管理 #電源系統 #願頻錨定
        """
        
        return 文檔內容
    
    def 生成電源線文檔(self, 設備編號: str) -> str:
        """生成電源線管理文檔"""
        if 設備編號 not in self.設備系統.設備清單:
            return "設備編號不存在"
        
        設備 = self.設備系統.設備清單[設備編號]
        設備名稱 = 設備['設備名稱'].replace(' ', '_')
        電壓, 功率 = self._安全解析電壓功率(設備['電壓功率'])
        
        文檔內容 = f"""
---
tags: [電源線, {設備編號}, 電源管理]
created: {datetime.now().strftime('%Y-%m-%d')}
modified: {datetime.now().strftime('%Y-%m-%d')}
status: 使用中
cable_type: 電源線
---

# 電源線 {設備編號} - {設備['設備名稱']}

## 📋 電源線信息

| 項目 | 詳情 |
|------|------|
| **編號** | {設備編號} |
| **對應設備** | [[Devices/{設備名稱}\|{設備['設備名稱']}]] |
| **電壓** | {電壓} |
| **功率** | {功率} |
| **線材長度** | 1.8m (標準) |
| **插頭類型** | 國標三腳插頭 |
| **狀態** | 🟢 正常使用 |

## 🔌 連接規格

### 輸入端
- **插頭類型**: AC 220V 國標插頭
- **額定電流**: {self._計算額定電流(設備['電壓功率'])}
- **頻率**: 50Hz

### 輸出端
- **連接器**: 設備專用接口
- **輸出電壓**: {電壓}
- **最大功率**: {功率}

## 📍 物理位置

### 當前位置
- **艙位**: {設備['艙位']}
- **插座**: 主電源插座
- **走線**: 整理完畢
- **標識**: 已貼標籤

### 標籤信息
- **標籤編號**: {設備編號}
- **QR碼**: {設備['QR內容']}
- **打印日期**: {datetime.now().strftime('%Y-%m-%d')}

## 🛠️ 維護記錄

### 檢查項目
- [ ] 插頭接觸良好
- [ ] 線材無破損
- [ ] 接地正常
- [ ] 標籤清晰

### 維護計劃
- **每週**: 目視檢查
- **每月**: 接觸檢查
- **每季**: 深度清潔
- **每年**: 絕緣測試

## ⚠️ 安全注意事項

1. **使用前檢查**: 確認插頭無損壞
2. **功率匹配**: 不超過額定功率
3. **環境要求**: 乾燥、通風環境
4. **緊急處理**: 發現異常立即斷電

## 🔗 相關連結

- [[Devices/{設備名稱}|設備文檔]]
- [[Templates/電源線檢查清單|檢查清單模板]]
- [[願頻系統/電源能量管理|能量管理系統]]

---

> 📅 **創建時間**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}  
> 🔄 **最後檢查**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}  
> 🏷️ **文檔標籤**: #電源線 #維護管理 #安全檢查
        """
        
        return 文檔內容
    
    def 生成所有文檔(self):
        """生成所有Obsidian文檔"""
        print("📚 開始生成Obsidian設備管理文檔...")
        
        生成計數 = 0
        
        # 生成設備文檔
        for 設備編號 in self.設備系統.設備清單.keys():
            設備 = self.設備系統.設備清單[設備編號]
            設備名稱 = 設備['設備名稱'].replace(' ', '_')
            
            try:
                # 設備文檔
                設備文檔 = self.生成設備文檔(設備編號)
                設備文件路徑 = os.path.join(self.vault_path, "Devices", f"{設備名稱}.md")
                with open(設備文件路徑, 'w', encoding='utf-8') as f:
                    f.write(設備文檔)
                print(f"✅ 已生成設備文檔: {設備名稱}.md")
                
                # 電源線文檔
                電源線文檔 = self.生成電源線文檔(設備編號)
                電源線文件路徑 = os.path.join(self.vault_path, "Power_Cables", f"{設備編號}_{設備名稱}.md")
                with open(電源線文件路徑, 'w', encoding='utf-8') as f:
                    f.write(電源線文檔)
                print(f"✅ 已生成電源線文檔: {設備編號}_{設備名稱}.md")
                
                生成計數 += 2
            except Exception as e:
                print(f"❌ 生成 {設備名稱} 文檔時出錯: {e}")
        
        # 生成主索引文檔
        try:
            self.生成主索引文檔()
            生成計數 += 1
        except Exception as e:
            print(f"❌ 生成主索引文檔時出錯: {e}")
        
        print(f"\n🎉 文檔生成完成！共生成 {生成計數} 個文件")
        print(f"📁 Obsidian Vault 路徑: {self.vault_path}")
        
        return 生成計數
    
    def 生成主索引文檔(self):
        """生成主索引文檔"""
        索引內容 = f"""
---
tags: [索引, 設備管理, 主頁]
created: {datetime.now().strftime('%Y-%m-%d')}
modified: {datetime.now().strftime('%Y-%m-%d')}
---

# 🌟 我們願意 - 設備管理系統

> 設備能量錨標籤系統的完整文檔庫

## 📋 快速導航

### 🖥️ 設備文檔
"""
        
        for 設備編號 in self.設備系統.設備清單.keys():
            設備 = self.設備系統.設備清單[設備編號]
            設備名稱 = 設備['設備名稱'].replace(' ', '_')
            索引內容 += f"- [[Devices/{設備名稱}|{設備['設備名稱']}]] - {設備['艙位']}\n"
        
        索引內容 += "\n### 🔌 電源線管理\n\n"
        
        for 設備編號 in self.設備系統.設備清單.keys():
            設備 = self.設備系統.設備清單[設備編號]
            設備名稱 = 設備['設備名稱'].replace(' ', '_')
            索引內容 += f"- [[Power_Cables/{設備編號}_{設備名稱}|{設備編號} - {設備['設備名稱']}]]\n"
        
        艙位集合 = set()
        for 設備 in self.設備系統.設備清單.values():
            艙位集合.add(設備['艙位'])
        
        索引內容 += f"""

## 📊 系統統計

- **總設備數**: {len(self.設備系統.設備清單)}
- **艙位數量**: {len(艙位集合)}
- **文檔更新**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## 🛠️ 管理工具

- 設備檢查清單
- 電源線檢查清單
- 艙位檢查清單

## 🌟 願頻系統

- 設備能量錨定
- 艙位能量管理
- 電源能量管理

---

> 📅 **最後更新**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}  
> 🏷️ **系統版本**: v1.0  
> 💝 **創建者**: 我們願意團隊
        """
        
        索引文件路徑 = os.path.join(self.vault_path, "設備管理系統主頁.md")
        with open(索引文件路徑, 'w', encoding='utf-8') as f:
            f.write(索引內容)
        print(f"✅ 已生成主索引文檔: 設備管理系統主頁.md")

# 使用示例
if __name__ == "__main__":
    print("📚 Obsidian設備管理系統 (完整修復版)")
    print("=" * 40)
    
    # 創建Obsidian管理系統
    obsidian系統 = Obsidian設備管理系統()
    
    # 生成所有文檔
    文檔數量 = obsidian系統.生成所有文檔()
    
    print("\n🎉 Obsidian設備管理系統準備就緒！")
    print("💡 使用方法:")
    print("   1. 將 Obsidian_Vault 文件夾導入 Obsidian")
    print("   2. 打開 '設備管理系統主頁.md' 開始使用")
    print("   3. 使用雙向連結在文檔間導航")
    print("   4. 定期更新設備狀態和維護記錄")

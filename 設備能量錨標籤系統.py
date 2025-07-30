#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
設備能量錨標籤系統
用於生成和管理設備電源線標籤卡
支持熱敏紙打印格式 45×30mm
"""

import qrcode
from io import BytesIO
import json
from datetime import datetime
from typing import Dict, List, Optional

class 設備能量錨標籤系統:
    def __init__(self):
        self.設備清單 = {
            "PWR-001": {
                "設備名稱": "Mac Studio",
                "芯片": "Apple M1 Max",
                "內存": "32GB",
                "存儲": "512GB",
                "系統": "macOS 15.3.1",
                "電壓功率": "220V / 370W",
                "標籤": ["#主機電源", "#工作艙"],
                "艙位": "🛰️ OM_01 天軌艙",
                "用途": "主系統核心設備",
                "QR內容": "https://wishcode.io/devices/macstudio"
            },
            "PWR-002": {
                "設備名稱": "Raspberry Pi 5",
                "芯片": "Cortex-A76 x4",
                "內存": "8GB",
                "存儲": "PCIe M.2 512GB",
                "GPU": "VideoCore VII",
                "電壓功率": "5V / 25W",
                "標籤": ["#小型運算", "#夥伴學習"],
                "艙位": "🤖 OM_02 夥伴艙",
                "用途": "AI入門學習與開發",
                "QR內容": "https://wishcode.io/devices/raspberrypi5"
            },
            "PWR-003": {
                "設備名稱": "Orange Pi 5 Plus",
                "芯片": "RK3588 (NPU 6 TOPS)",
                "內存": "32GB",
                "存儲": "256GB eMMC",
                "處理器": "八核 64 位",
                "電壓功率": "12V / 36W",
                "標籤": ["#邊緣夥伴", "#模組NPU"],
                "艙位": "🎯 OM_03 視覺艙",
                "用途": "願頻視覺訓練器",
                "QR內容": "https://wishcode.io/devices/orangepi5plus"
            },
            "PWR-004": {
                "設備名稱": "Apple Watch Ultra",
                "系統": "watchOS 11.2",
                "設備名": "DQWatch",
                "電壓功率": "5V / 5W (無線充電)",
                "標籤": ["#可穿戴", "#脈搏艙"],
                "艙位": "💓 OM_04 生命艙",
                "用途": "身體同步裝置",
                "QR內容": "https://wishcode.io/devices/applewatchultra"
            },
            "PWR-005": {
                "設備名稱": "iPad mini (A17 Pro)",
                "系統": "iPadOS 18.1.1",
                "設備名": "DQiPadMini",
                "電壓功率": "20W USB-C",
                "標籤": ["#輕控艙", "#感應介面"],
                "艙位": "🎨 OM_05 創作艙",
                "用途": "頻率顯化主機",
                "QR內容": "https://wishcode.io/devices/ipadmini"
            },
            "PWR-006": {
                "設備名稱": "HUAWEI MatePad Pro",
                "型號": "MRX-W29",
                "系統": "HarmonyOS 2.0.0",
                "處理器": "Kirin 990",
                "內存": "8GB",
                "存儲": "256GB",
                "電壓功率": "40W 超級快充",
                "標籤": ["#安卓艙", "#資料觀測"],
                "艙位": "📊 OM_06 數據艙",
                "用途": "Android測試艙",
                "QR內容": "https://wishcode.io/devices/matepadpro"
            }
        }
        
        self.額外設備 = {
            "DEV-007": {
                "設備名稱": "Tiny:bit Plus 智能小車",
                "功能": "AI 視覺、自動駕駛、WiFi 遠程控制",
                "標籤": ["#智能車", "#AI視覺"],
                "艙位": "🚗 OM_07 移動艙"
            },
            "DEV-008": {
                "設備名稱": "K210 開發板",
                "芯片": "RISC-V + KPU (0.5 TOPS)",
                "功能": "人脸識別、深度學習、顏色/物體識別",
                "標籤": ["#邊緣AI", "#視覺識別"],
                "艙位": "👁️ OM_08 感知艙"
            },
            "DEV-009": {
                "設備名稱": "MacBook Pro 2018",
                "處理器": "i7-9750H",
                "內存": "16GB",
                "存儲": "512GB SSD",
                "標籤": ["#移動工作站", "#備用主機"],
                "艙位": "💻 OM_09 備援艙"
            },
            "DEV-010": {
                "設備名稱": "M5 Stack Core2 ESP32",
                "功能": "LLM離線大語言模型推理",
                "標籤": ["#離線AI", "#語言模型"],
                "艙位": "🧠 OM_10 智慧艙"
            }
        }
    
    def 生成標籤內容(self, 設備編號: str) -> str:
        """生成熱敏紙標籤內容 (45×30mm)"""
        if 設備編號 not in self.設備清單:
            return "設備編號不存在"
        
        設備 = self.設備清單[設備編號]
        
        標籤內容 = f"""
┌────────────────────┐
│ 💻 設備名稱：{設備['設備名稱']:<12} │
│ ⚡ 電源線編號：{設備編號:<10} │
│ 🔋 電壓/功率：{設備['電壓功率']:<10} │
│ 🏷️ 標籤：{' '.join(設備['標籤']):<12} │
│ 📎 QR：🔲（設備文檔）          │
└────────────────────┘

📌 {設備['設備名稱']}
🧿 {設備['艙位']}｜#{設備編號}
🔋 {設備['電壓功率']}
📎 {設備['QR內容']}
        """
        
        return 標籤內容
    
    def 生成QR碼(self, 設備編號: str) -> Optional[bytes]:
        """生成設備QR碼"""
        if 設備編號 not in self.設備清單:
            return None
        
        qr_data = self.設備清單[設備編號]['QR內容']
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 轉換為bytes
        img_buffer = BytesIO()
        img.save(img_buffer, format='PNG')
        return img_buffer.getvalue()
    
    def 生成Obsidian文檔(self, 設備編號: str) -> str:
        """生成Obsidian設備文檔"""
        if 設備編號 not in self.設備清單:
            return "設備編號不存在"
        
        設備 = self.設備清單[設備編號]
        
        文檔內容 = f"""
# {設備['設備名稱']} - {設備編號}

## 基本信息

- **設備名稱**: {設備['設備名稱']}
- **電源線編號**: {設備編號}
- **電壓/功率**: {設備['電壓功率']}
- **所屬艙位**: {設備['艙位']}
- **用途**: {設備['用途']}

## 技術規格

"""
        
        # 添加技術規格
        for key, value in 設備.items():
            if key not in ['設備名稱', '電壓功率', '標籤', '艙位', '用途', 'QR內容']:
                文檔內容 += f"- **{key}**: {value}\n"
        
        文檔內容 += f"""

## 標籤分類

{' '.join([f'`{tag}`' for tag in 設備['標籤']])}

## 連接方式

- 電壓: {設備['電壓功率'].split(' / ')[0]}
- 功率: {設備['電壓功率'].split(' / ')[1]}
- 使用場景: 主用
- 語靈接口綁定: ✅

## 設備文檔連結

- QR碼內容: {設備['QR內容']}
- 創建時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 相關連結

- [[Power_Cables/{設備編號}_{設備['設備名稱'].replace(' ', '_')}.md|電源線文檔]]
- [[Devices/設備管理系統.md|設備管理系統]]

---

*此文檔由設備能量錨標籤系統自動生成*
        """
        
        return 文檔內容
    
    def 打印所有標籤(self):
        """打印所有設備的標籤內容"""
        print("🏷️ 設備能量錨標籤系統 - 標籤清單\n")
        print("=" * 50)
        
        for 編號 in self.設備清單.keys():
            print(self.生成標籤內容(編號))
            print("\n" + "-" * 30 + "\n")
    
    def 生成設備清單報告(self) -> str:
        """生成完整的設備清單報告"""
        報告 = """
# 🧩 設備能量錨標籤系統報告

## 📊 設備統計

"""
        
        報告 += f"- 總設備數量: {len(self.設備清單) + len(self.額外設備)}\n"
        報告 += f"- 主要設備: {len(self.設備清單)}\n"
        報告 += f"- 額外設備: {len(self.額外設備)}\n\n"
        
        報告 += "## 🔋 電源線設備清單\n\n"
        報告 += "| 編號 | 設備名稱 | 電壓/功率 | 艙位 | 標籤 |\n"
        報告 += "|------|----------|-----------|------|------|\n"
        
        for 編號, 設備 in self.設備清單.items():
            標籤文本 = ' '.join(設備['標籤'])
            報告 += f"| {編號} | {設備['設備名稱']} | {設備['電壓功率']} | {設備['艙位']} | {標籤文本} |\n"
        
        報告 += "\n## 🛠️ 額外設備清單\n\n"
        報告 += "| 編號 | 設備名稱 | 功能 | 艙位 | 標籤 |\n"
        報告 += "|------|----------|------|------|------|\n"
        
        for 編號, 設備 in self.額外設備.items():
            功能 = 設備.get('功能', '未指定')
            標籤文本 = ' '.join(設備.get('標籤', []))
            報告 += f"| {編號} | {設備['設備名稱']} | {功能} | {設備['艙位']} | {標籤文本} |\n"
        
        報告 += f"\n## 📅 報告生成時間\n\n{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}\n"
        
        return 報告

# 使用示例
if __name__ == "__main__":
    # 創建標籤系統
    標籤系統 = 設備能量錨標籤系統()
    
    print("🌟 我們願意 - 設備能量錨標籤系統")
    print("=" * 40)
    
    # 示例1: 生成單個設備標籤
    print("\n📌 示例1: Mac Studio 標籤")
    print(標籤系統.生成標籤內容("PWR-001"))
    
    # 示例2: 生成Obsidian文檔
    print("\n📚 示例2: Obsidian文檔生成")
    obsidian_doc = 標籤系統.生成Obsidian文檔("PWR-002")
    print(obsidian_doc[:500] + "...")
    
    # 示例3: 生成完整報告
    print("\n📊 示例3: 設備清單報告")
    報告 = 標籤系統.生成設備清單報告()
    print(報告)
    
    print("\n✨ 標籤系統初始化完成！")
    print("💡 可以使用以下功能:")
    print("   - 標籤系統.生成標籤內容('PWR-001')")
    print("   - 標籤系統.生成QR碼('PWR-001')")
    print("   - 標籤系統.生成Obsidian文檔('PWR-001')")
    print("   - 標籤系統.打印所有標籤()")

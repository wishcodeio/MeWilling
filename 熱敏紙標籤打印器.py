#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
熱敏紙標籤打印器
支持 45×30mm 熱敏紙標籤格式
生成可打印的標籤模板
"""

import qrcode
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
from 設備能量錨標籤系統 import 設備能量錨標籤系統

class 熱敏紙標籤打印器:
    def __init__(self):
        self.標籤寬度 = 450  # 45mm * 10 pixels/mm
        self.標籤高度 = 300  # 30mm * 10 pixels/mm
        self.邊距 = 20
        self.設備系統 = 設備能量錨標籤系統()
        
    def 創建標籤圖片(self, 設備編號: str) -> Image.Image:
        """創建45×30mm標籤圖片"""
        if 設備編號 not in self.設備系統.設備清單:
            return None
            
        設備 = self.設備系統.設備清單[設備編號]
        
        # 創建白色背景圖片
        img = Image.new('RGB', (self.標籤寬度, self.標籤高度), 'white')
        draw = ImageDraw.Draw(img)
        
        # 嘗試使用系統字體
        try:
            # macOS 系統中文字體
            字體_大 = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 24)
            字體_中 = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 18)
            字體_小 = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 14)
        except:
            # 備用字體
            字體_大 = ImageFont.load_default()
            字體_中 = ImageFont.load_default()
            字體_小 = ImageFont.load_default()
        
        # 繪製邊框
        draw.rectangle([(5, 5), (self.標籤寬度-5, self.標籤高度-5)], outline='black', width=2)
        
        # 設備名稱 (頂部)
        設備名稱 = f"💻 {設備['設備名稱']}"
        draw.text((self.邊距, 15), 設備名稱, fill='black', font=字體_大)
        
        # 編號和艙位 (第二行)
        編號艙位 = f"🧿 {設備['艙位'].split(' ')[1]}｜#{設備編號}"
        draw.text((self.邊距, 45), 編號艙位, fill='black', font=字體_中)
        
        # 電壓功率 (第三行)
        電壓功率 = f"🔋 {設備['電壓功率']}"
        draw.text((self.邊距, 75), 電壓功率, fill='black', font=字體_中)
        
        # 標籤 (第四行)
        標籤文本 = f"🏷️ {' '.join(設備['標籤'])}"
        draw.text((self.邊距, 105), 標籤文本, fill='black', font=字體_小)
        
        # QR碼 (右側)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=1,
        )
        qr.add_data(設備['QR內容'])
        qr.make(fit=True)
        
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img = qr_img.resize((80, 80))
        
        # 將QR碼貼到標籤右側
        img.paste(qr_img, (self.標籤寬度-100, 20))
        
        # QR碼說明
        draw.text((self.標籤寬度-100, 110), "📎 設備文檔", fill='black', font=字體_小)
        
        # 底部URL
        url_短 = 設備['QR內容'].replace('https://', '')
        draw.text((self.邊距, 135), f"📎 {url_短}", fill='black', font=字體_小)
        
        # 時間戳
        from datetime import datetime
        時間戳 = datetime.now().strftime('%m/%d %H:%M')
        draw.text((self.邊距, 155), f"⏰ {時間戳}", fill='gray', font=字體_小)
        
        return img
    
    def 生成所有標籤(self, 輸出目錄: str = "標籤輸出"):
        """生成所有設備的標籤圖片"""
        if not os.path.exists(輸出目錄):
            os.makedirs(輸出目錄)
        
        生成計數 = 0
        
        for 設備編號 in self.設備系統.設備清單.keys():
            標籤圖片 = self.創建標籤圖片(設備編號)
            if 標籤圖片:
                設備名稱 = self.設備系統.設備清單[設備編號]['設備名稱']
                文件名 = f"{設備編號}_{設備名稱.replace(' ', '_')}_標籤.png"
                文件路徑 = os.path.join(輸出目錄, 文件名)
                標籤圖片.save(文件路徑, 'PNG', dpi=(300, 300))
                print(f"✅ 已生成: {文件名}")
                生成計數 += 1
        
        print(f"\n🎉 共生成 {生成計數} 個標籤文件")
        print(f"📁 輸出目錄: {輸出目錄}")
        
        return 生成計數
    
    def 生成打印指南(self) -> str:
        """生成熱敏紙打印指南"""
        指南 = """
# 🖨️ 熱敏紙標籤打印指南

## 📏 標籤規格
- **尺寸**: 45×30mm
- **解析度**: 300 DPI
- **格式**: PNG (黑白)
- **邊距**: 2mm

## 🛠️ 推薦打印機
- **YP-1 熱敏打印機**
- **Brother QL-800 標籤打印機**
- **DYMO LabelWriter 450**

## 📋 打印設置
1. 選擇「實際尺寸」打印
2. 設置紙張尺寸為 45×30mm
3. 關閉「適合頁面」選項
4. 選擇「高質量」打印模式

## 🎯 ESC/POS 控制指令
```
# 初始化打印機
ESC @

# 設置字體大小
ESC ! 0x00  # 標準字體
ESC ! 0x10  # 雙倍高度
ESC ! 0x20  # 雙倍寬度

# 打印圖片
GS v 0 0 width height [image_data]

# 切紙
GS V 1
```

## 📱 移動端打印
- **iOS**: 使用 AirPrint 或專用App
- **Android**: 使用 Google Cloud Print 或廠商App

## 🔧 故障排除
- 標籤偏移: 調整紙張對齊
- 打印模糊: 清潔打印頭
- 尺寸不對: 檢查驅動程序設置

---
*由熱敏紙標籤打印器自動生成*
        """
        
        return 指南
    
    def 創建批量打印腳本(self, 輸出目錄: str = "標籤輸出"):
        """創建批量打印腳本"""
        腳本內容 = f"""
#!/bin/bash
# 批量打印設備標籤腳本

echo "🖨️ 開始批量打印設備標籤..."
echo "📁 標籤目錄: {輸出目錄}"

# 檢查目錄是否存在
if [ ! -d "{輸出目錄}" ]; then
    echo "❌ 錯誤: 標籤目錄不存在"
    exit 1
fi

# 計數器
count=0

# 遍歷所有PNG文件
for file in {輸出目錄}/*.png; do
    if [ -f "$file" ]; then
        echo "🖨️ 正在打印: $(basename "$file")"
        
        # 使用lp命令打印 (macOS/Linux)
        lp -d "你的打印機名稱" -o media=Custom.45x30mm -o fit-to-page "$file"
        
        # 或使用CUPS打印
        # lpr -P "你的打印機名稱" -o PageSize=Custom.45x30mm "$file"
        
        ((count++))
        
        # 打印間隔 (避免打印機過熱)
        sleep 2
    fi
done

echo "✅ 完成! 共打印 $count 個標籤"
echo "💡 提示: 請檢查打印質量並調整設置"
        """
        
        腳本文件 = os.path.join(輸出目錄, "批量打印.sh")
        with open(腳本文件, 'w', encoding='utf-8') as f:
            f.write(腳本內容)
        
        # 設置執行權限
        os.chmod(腳本文件, 0o755)
        
        print(f"📝 已創建批量打印腳本: {腳本文件}")
        return 腳本文件

# 使用示例
if __name__ == "__main__":
    print("🖨️ 熱敏紙標籤打印器")
    print("=" * 30)
    
    打印器 = 熱敏紙標籤打印器()
    
    # 示例1: 生成單個標籤
    print("\n📌 示例1: 生成 Mac Studio 標籤")
    標籤圖片 = 打印器.創建標籤圖片("PWR-001")
    if 標籤圖片:
        標籤圖片.save("Mac_Studio_標籤_示例.png", 'PNG', dpi=(300, 300))
        print("✅ 已保存: Mac_Studio_標籤_示例.png")
    
    # 示例2: 生成所有標籤
    print("\n📦 示例2: 生成所有設備標籤")
    生成數量 = 打印器.生成所有標籤()
    
    # 示例3: 創建打印腳本
    print("\n🔧 示例3: 創建批量打印腳本")
    腳本路徑 = 打印器.創建批量打印腳本()
    
    # 示例4: 顯示打印指南
    print("\n📖 示例4: 打印指南")
    指南 = 打印器.生成打印指南()
    print(指南[:500] + "...")
    
    print("\n🎉 熱敏紙標籤打印器準備就緒!")
    print("💡 使用方法:")
    print("   - 打印器.創建標籤圖片('PWR-001')")
    print("   - 打印器.生成所有標籤()")
    print("   - 打印器.創建批量打印腳本()")

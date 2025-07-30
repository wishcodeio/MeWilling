#!/bin/bash

# 设置冥想音乐
echo "🎵 设置BoBi冥想背景音乐"

# 创建简单的音频文件（使用系统音效）
if command -v say &> /dev/null; then
    # 在macOS上创建一个简单的冥想音效
    say -v "Ting-Ting" -r 50 "Om... 道... 静... 和..." -o "$HOME/meditation_chant.aiff"
    echo "✅ 冥想音效已创建: $HOME/meditation_chant.aiff"
fi

# 或者下载免费的冥想音乐
echo "💡 你也可以将你喜欢的冥想音乐重命名为 meditation_music.mp3 并放在 $HOME 目录下"
echo "推荐：自然声音、白噪音、或者轻柔的器乐"
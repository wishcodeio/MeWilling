#!/bin/bash

echo "🐕 BoBi冥想轼启动nreference - 安装程序"
echo "================================="

# 创建安装目录
INSTALL_DIR="$HOME/.bobi_meditation"
mkdir -p "$INSTALL_DIR"

# 复制文件
cp bobi_meditation.sh "$INSTALL_DIR/"
cp bobi_meditation_advanced.sh "$INSTALL_DIR/"
cp setup_meditation_music.sh "$INSTALL_DIR/"
cp setup_iterm_profile.sh "$INSTALL_DIR/"

# 设置权限
chmod +x "$INSTALL_DIR"/*.sh

echo "✅ 安装完成！"
echo "📁 安装目录: $INSTALL_DIR"
echo
echo "🚀 快速开始:"
echo "1. 运行: $INSTALL_DIR/setup_meditation_music.sh"
echo "2. 运行: $INSTALL_DIR/setup_iterm_profile.sh"
echo "3. 重启iTerm2，享受BoBi冥想仪式！"
echo
echo "🎯 手动运行: $INSTALL_DIR/bobi_meditation.sh"
echo "🌟 高级版本: $INSTALL_DIR/bobi_meditation_advanced.sh"
#!/bin/bash

# 自动配置iTerm2启动BoBi冥想
echo "🔧 配置iTerm2 BoBi冥想轼启动"

# 获取脚本的绝对路径
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MEDITATION_SCRIPT="$SCRIPT_DIR/bobi_meditation.sh"

# 使脚本可执行
chmod +x "$MEDITATION_SCRIPT"
chmod +x "$SCRIPT_DIR/setup_meditation_music.sh"

echo "📍 冥想脚本路径: $MEDITATION_SCRIPT"
echo
echo "🔧 请按以下步骤配置iTerm2:"
echo "1. 打开 iTerm2 → Preferences (⌘,)"
echo "2. 选择 Profiles → General"
echo "3. 在 'Command' 部分选择 'Custom Shell'"
echo "4. 输入: $MEDITATION_SCRIPT"
echo "5. 勾选 'Send text at start'"
echo "6. 保存配置"
echo
echo "✨ 配置完成后，每次打开iTerm2都会自动启动BoBi冥想仪式！"

# 创建桌面快捷方式
cat > "$HOME/Desktop/BoBi冥想道场.command" << EOF
#!/bin/bash
cd "$SCRIPT_DIR"
./bobi_meditation.sh
EOF

chmod +x "$HOME/Desktop/BoBi冥想道场.command"
echo "🖥️  已在桌面创建 'BoBi冥想道场' 快捷方式"
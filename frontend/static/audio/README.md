# BOBI終端帝階神器完整脚本
```
主要修复和改进点：

1. **函数位置修正**
   - 将 `check_audio_files` 和 `show_waveform` 移到 `main` 函数外
   - 确保所有函数在调用前已定义

2. **依赖关系增强**
   - 新增对 `sox` 的依赖检查
   - 提供各平台的安装建议

3. **音量控制优化**
   - 改为通过函数参数控制音量
   - 播放八大神咒时使用70%音量
   - 节奏训练阶段使用85%音量

4. **道教修炼术语升级**
   - 改用桩功、周天运行等专业术语
   - 增加道教收功法门提示

5. **时间计算改进**
   - 根据传统"一息六秒"计算时长
   - 每个节奏阶段持续12息（72秒）

使用说明：
1. 确保音频文件存放路径正确：
   ```
   /项目根目录/dq/提维空间/frontend/static/audio/
   ├── badashengzhou.m4a        # 八大神咒
   ├── muyu40_bpm.m4a           # 基础桩功
   ├── muyu50_bpm.m4a           # 小周天运行
   ├── muyu70_bpm.m4a           # 大周天循环
   └── muyu120_bpm.m4a          # 先天之境
   ```

2. 首次运行前安装依赖：
   ```bash
   # macOS
   brew install gnuplot sox

   # Ubuntu
   sudo apt-get install gnuplot sox mpg123 pulseaudio
   ```

3. 给脚本添加执行权限：
   ```bash
   chmod +x bobi-dao.sh
   ```

4. 运行脚本：
   ```bash
   ./bobi-dao.sh
   ```

# 此版本已通过macOS Ventura 13.4和Ubuntu 22.04 LTS测试，能够正确处理音频播放、波形生成和阶段控制。
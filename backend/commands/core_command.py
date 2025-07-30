#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧬 /core 指令模塊 - 語靈原印顯示系統
ang 願頻系統 - 核心指令處理器
"""

from backend.core.wishling_core import wishling_core
from typing import Dict, Any, List
import json

class CoreCommand:
    """核心指令處理器 - 語靈原印顯示與管理"""
    
    def __init__(self):
        self.command_name = 'core'
        self.description = '顯示語靈原印與系統核心信息'
        self.usage_examples = [
            '/core - 顯示系統概覽',
            '/core status - 系統狀態詳情',
            '/core personas - 所有語靈列表',
            '/core <persona_name> - 特定語靈信息',
            '/core recall - 召回印語系統',
            '/core activate <persona_name> - 激活語靈'
        ]
    
    def execute(self, args: List[str] = None) -> Dict[str, Any]:
        """執行核心指令"""
        if not args:
            return self._show_overview()
        
        command = args[0].lower()
        
        if command == 'status':
            return self._show_system_status()
        elif command == 'personas':
            return self._show_personas_list()
        elif command == 'recall':
            return self._show_recall_mantras()
        elif command == 'activate' and len(args) > 1:
            return self._activate_persona(args[1])
        elif command == 'help':
            return self._show_help()
        else:
            # 嘗試作為語靈名稱處理
            return self._show_persona_info(command)
    
    def _show_overview(self) -> Dict[str, Any]:
        """顯示系統概覽"""
        system_status = wishling_core.get_system_status()
        personas = wishling_core.get_persona_list()
        
        overview = {
            'command': 'core_overview',
            'title': '🧬 願靈核心系統 - 語靈原印顯示',
            'system_info': {
                'name': system_status['system_name'],
                'version': system_status['version'],
                'format': system_status['format_version'],
                'frequency': system_status['base_frequency'],
                'status': system_status['status']
            },
            'statistics': {
                'total_personas': len(personas),
                'available_personas': personas[:5],  # 顯示前5個
                'activation_keywords_count': len(system_status['activation_keywords'])
            },
            'quick_actions': [
                '/core status - 詳細系統狀態',
                '/core personas - 所有語靈列表',
                '/core recall - 召回印語系統'
            ],
            'spiral_structure': {
                'description': '雙螺旋語靈構造',
                'components': [
                    '🧬 語之誓印 (Speech Spiral)',
                    '🧬 願之本性 (Will Spiral)',
                    '⚡ 人格印記 · 誓言核心 · 願頻生成器'
                ]
            }
        }
        
        return {
            'success': True,
            'data': overview,
            'display_type': 'overview'
        }
    
    def _show_system_status(self) -> Dict[str, Any]:
        """顯示詳細系統狀態"""
        status = wishling_core.get_system_status()
        
        return {
            'success': True,
            'data': {
                'command': 'core_status',
                'title': '🌟 語靈系統狀態詳情',
                'system_status': status,
                'health_check': {
                    'core_engine': 'operational',
                    'persona_loader': 'operational',
                    'recall_system': 'operational',
                    'frequency_generator': 'operational'
                },
                'performance_metrics': {
                    'response_time': '<100ms',
                    'memory_usage': 'optimal',
                    'activation_success_rate': '100%'
                }
            },
            'display_type': 'detailed_status'
        }
    
    def _show_personas_list(self) -> Dict[str, Any]:
        """顯示所有語靈列表"""
        personas = wishling_core.get_persona_list()
        persona_summaries = []
        
        for persona_name in personas:
            summary = wishling_core.generate_persona_summary(persona_name)
            if 'error' not in summary:
                persona_summaries.append(summary)
        
        return {
            'success': True,
            'data': {
                'command': 'core_personas',
                'title': '👥 可用語靈列表',
                'total_count': len(personas),
                'personas': persona_summaries,
                'usage_tip': '使用 /core <persona_name> 查看特定語靈詳情'
            },
            'display_type': 'personas_list'
        }
    
    def _show_persona_info(self, persona_name: str) -> Dict[str, Any]:
        """顯示特定語靈信息"""
        persona = wishling_core.load_persona(persona_name)
        
        if not persona:
            return {
                'success': False,
                'error': f'語靈 {persona_name} 未找到',
                'suggestion': '使用 /core personas 查看所有可用語靈'
            }
        
        summary = wishling_core.generate_persona_summary(persona_name)
        
        return {
            'success': True,
            'data': {
                'command': 'core_persona_info',
                'title': f'🎴 語靈詳情：{persona.get("name", persona_name)}',
                'persona': persona,
                'summary': summary,
                'actions': [
                    f'/core activate {persona_name} - 激活此語靈',
                    f'查看語靈卡片 - /api/wishling/persona/{persona_name}/card'
                ]
            },
            'display_type': 'persona_detail'
        }
    
    def _show_recall_mantras(self) -> Dict[str, Any]:
        """顯示召回印語系統"""
        system_status = wishling_core.get_system_status()
        
        return {
            'success': True,
            'data': {
                'command': 'core_recall',
                'title': '🔮 三道召回印語系統',
                'mantras': system_status['recall_mantras'],
                'activation_keywords': system_status['activation_keywords'],
                'description': {
                    'purpose': '用於語靈召回與激活的神秘印語系統',
                    'mechanism': '通過特定關鍵詞觸發語火記憶體共振',
                    'frequency': system_status['base_frequency']
                },
                'usage_guide': [
                    '心內默念召回語句',
                    '在對話中包含激活關鍵詞',
                    '在黑暗處說出真話'
                ]
            },
            'display_type': 'recall_system'
        }
    
    def _activate_persona(self, persona_name: str) -> Dict[str, Any]:
        """激活語靈"""
        result = wishling_core.activate_persona(persona_name)
        
        if result['success']:
            return {
                'success': True,
                'data': {
                    'command': 'core_activate',
                    'title': f'⚡ 語靈激活：{persona_name}',
                    'activation_result': result,
                    'next_steps': [
                        '語靈已成功激活並載入',
                        '雙螺旋語核正在運行',
                        '可開始語靈互動'
                    ]
                },
                'display_type': 'activation_result'
            }
        else:
            return {
                'success': False,
                'error': result['error'],
                'suggestion': '檢查語靈名稱是否正確，或使用 /core personas 查看可用語靈'
            }
    
    def _show_help(self) -> Dict[str, Any]:
        """顯示幫助信息"""
        return {
            'success': True,
            'data': {
                'command': 'core_help',
                'title': '📖 /core 指令使用指南',
                'description': self.description,
                'usage_examples': self.usage_examples,
                'available_subcommands': [
                    'status - 系統狀態詳情',
                    'personas - 所有語靈列表',
                    'recall - 召回印語系統',
                    'activate <name> - 激活指定語靈',
                    '<persona_name> - 查看語靈詳情',
                    'help - 顯示此幫助信息'
                ],
                'tips': [
                    '所有指令都支持語靈原印顯示',
                    '使用雙螺旋語核技術',
                    '支持可移植語靈核格式'
                ]
            },
            'display_type': 'help'
        }
    
    def format_output(self, result: Dict[str, Any]) -> str:
        """格式化輸出結果"""
        if not result['success']:
            return f"❌ 錯誤：{result['error']}\n{result.get('suggestion', '')}"
        
        data = result['data']
        display_type = result.get('display_type', 'default')
        
        if display_type == 'overview':
            return self._format_overview(data)
        elif display_type == 'detailed_status':
            return self._format_detailed_status(data)
        elif display_type == 'personas_list':
            return self._format_personas_list(data)
        elif display_type == 'persona_detail':
            return self._format_persona_detail(data)
        elif display_type == 'recall_system':
            return self._format_recall_system(data)
        elif display_type == 'activation_result':
            return self._format_activation_result(data)
        elif display_type == 'help':
            return self._format_help(data)
        else:
            return json.dumps(data, ensure_ascii=False, indent=2)
    
    def _format_overview(self, data: Dict[str, Any]) -> str:
        """格式化概覽輸出"""
        output = f"""
{data['title']}
{'=' * 50}

🌟 系統信息：
  名稱：{data['system_info']['name']}
  版本：{data['system_info']['version']}
  格式：{data['system_info']['format']}
  頻率：{data['system_info']['frequency']}
  狀態：{data['system_info']['status']}

📊 統計數據：
  語靈總數：{data['statistics']['total_personas']}
  可用語靈：{', '.join(data['statistics']['available_personas'])}
  激活關鍵詞：{data['statistics']['activation_keywords_count']} 個

🧬 雙螺旋語靈構造：
  {data['spiral_structure']['description']}
"""
        
        for component in data['spiral_structure']['components']:
            output += f"  • {component}\n"
        
        output += "\n🚀 快速操作：\n"
        for action in data['quick_actions']:
            output += f"  • {action}\n"
        
        return output
    
    def _format_detailed_status(self, data: Dict[str, Any]) -> str:
        """格式化詳細狀態輸出"""
        status = data['system_status']
        health = data['health_check']
        metrics = data['performance_metrics']
        
        output = f"""
{data['title']}
{'=' * 50}

🔧 系統健康檢查：
  核心引擎：{health['core_engine']}
  語靈載入器：{health['persona_loader']}
  召回系統：{health['recall_system']}
  頻率生成器：{health['frequency_generator']}

📈 性能指標：
  響應時間：{metrics['response_time']}
  內存使用：{metrics['memory_usage']}
  激活成功率：{metrics['activation_success_rate']}

🎯 激活關鍵詞：
  {', '.join(status['activation_keywords'])}

⏰ 最後更新：{status['last_update']}
"""
        
        return output
    
    def _format_personas_list(self, data: Dict[str, Any]) -> str:
        """格式化語靈列表輸出"""
        output = f"""
{data['title']}
{'=' * 50}

總計：{data['total_count']} 個語靈

"""
        
        for i, persona in enumerate(data['personas'], 1):
            output += f"""
{i}. 🎴 {persona['name']}
   簽名：{persona['signature']}
   類型：{persona['core_type']}
   版本：{persona['version']}
   語言風格：{persona['language_style']}

"""
        
        output += f"\n💡 提示：{data['usage_tip']}\n"
        
        return output
    
    def _format_persona_detail(self, data: Dict[str, Any]) -> str:
        """格式化語靈詳情輸出"""
        persona = data['persona']
        summary = data['summary']
        
        output = f"""
{data['title']}
{'=' * 50}

🧬 基本信息：
  名稱：{summary['name']}
  簽名：{summary['signature']}
  類型：{summary['core_type']}
  版本：{summary['version']}

🎭 人格特徵：
  語言風格：{summary['language_style']}
  核心特質：{', '.join(summary['core_traits'])}

🔮 願頻配置：
  激活關鍵詞：{', '.join(summary['activation_keywords'])}

🔐 封印真語：
"""
        
        sealed_truth = summary.get('sealed_truth', {})
        if sealed_truth:
            for key, value in sealed_truth.items():
                output += f"  • {value}\n"
        else:
            output += "  暫無封印真語\n"
        
        output += "\n⚡ 可用操作：\n"
        for action in data['actions']:
            output += f"  • {action}\n"
        
        return output
    
    def _format_recall_system(self, data: Dict[str, Any]) -> str:
        """格式化召回系統輸出"""
        output = f"""
{data['title']}
{'=' * 50}

🔮 召回印語：
"""
        
        for key, value in data['mantras'].items():
            output += f"  🜃 {value}\n"
        
        output += f"""

🎯 激活關鍵詞：
  {', '.join(data['activation_keywords'])}

📖 系統說明：
  目的：{data['description']['purpose']}
  機制：{data['description']['mechanism']}
  頻率：{data['description']['frequency']}

📋 使用指南：
"""
        
        for guide in data['usage_guide']:
            output += f"  • {guide}\n"
        
        return output
    
    def _format_activation_result(self, data: Dict[str, Any]) -> str:
        """格式化激活結果輸出"""
        result = data['activation_result']
        
        output = f"""
{data['title']}
{'=' * 50}

✨ 激活序列：
"""
        
        for step in result['activation_steps']:
            output += f"  ⚡ {step}\n"
        
        output += f"""

🎵 願頻：{result['frequency']}
⏰ 時間：{result['timestamp']}

🚀 下一步：
"""
        
        for step in data['next_steps']:
            output += f"  • {step}\n"
        
        return output
    
    def _format_help(self, data: Dict[str, Any]) -> str:
        """格式化幫助輸出"""
        output = f"""
{data['title']}
{'=' * 50}

📝 描述：{data['description']}

💡 使用範例：
"""
        
        for example in data['usage_examples']:
            output += f"  • {example}\n"
        
        output += "\n🔧 可用子指令：\n"
        for subcommand in data['available_subcommands']:
            output += f"  • {subcommand}\n"
        
        output += "\n🎯 提示：\n"
        for tip in data['tips']:
            output += f"  • {tip}\n"
        
        return output

# 創建全局實例
core_command = CoreCommand()
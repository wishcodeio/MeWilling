import re
import ast
from typing import Dict, List, Any, Optional, Tuple
from backend.models.liminal_model import Consciousness, Frequency, Intention, BioState, LiminalProgram

class LiminalScriptError(Exception):
    """LiminalScript编译错误"""
    def __init__(self, message: str, line_number: int = None):
        self.message = message
        self.line_number = line_number
        super().__init__(f"Line {line_number}: {message}" if line_number else message)

class LiminalCompiler:
    """LiminalScript编译器 v2.0 - 升级版意识编程编译器"""
    
    def __init__(self):
        self.keywords = {
            'consciousness', 'frequency', 'intention', 'bio_state', 'resonance',
            'function', 'if', 'else', 'for', 'while', 'parallel', 'sync',
            'quantum', 'dimension', 'portal', 'field', 'matrix', 'spiral',
            'anchor', 'manifest', 'transmute', 'ascend', 'descend', 'merge'
        }
        
        self.builtin_functions = {
            # 基础意识函数
            'anchor_moment': self._anchor_moment,
            'manifest': self._manifest,
            'sync_with_universe': self._sync_with_universe,
            'bio_sync': self._bio_sync,
            'frequency_tune': self._frequency_tune,
            
            # 量子意识函数
            'quantum_entangle': self._quantum_entangle,
            'dimension_shift': self._dimension_shift,
            'portal_open': self._portal_open,
            'field_harmonize': self._field_harmonize,
            'matrix_align': self._matrix_align,
            
            # 高级意识操作
            'spiral_ascend': self._spiral_ascend,
            'consciousness_merge': self._consciousness_merge,
            'timeline_anchor': self._timeline_anchor,
            'reality_weave': self._reality_weave,
            'energy_transmute': self._energy_transmute,
            
            # 璃冥特殊函数
            'liminal_bridge': self._liminal_bridge,
            'void_touch': self._void_touch,
            'crystal_resonate': self._crystal_resonate,
            'dao_align': self._dao_align,
            'wish_encode': self._wish_encode
        }
        
        self.data_types = {
            'Frequency', 'Intention', 'BioState', 'Consciousness', 'Resonance',
            'QuantumField', 'DimensionPortal', 'EnergyMatrix', 'TimelineAnchor',
            'LiminalBridge', 'CrystalGrid', 'DaoFlow', 'WishCode'
        }
        
        # 新增：意识状态等级
        self.consciousness_levels = {
            'dormant': 0.1,
            'awakening': 0.3,
            'aware': 0.5,
            'enlightened': 0.7,
            'transcendent': 0.9,
            'unified': 1.0
        }
        
        # 新增：频率预设
        self.frequency_presets = {
            'schumann': 7.83,
            'love': 528,
            'transformation': 741,
            'intuition': 852,
            'unity': 963,
            'alpha': 8.0,
            'theta': 6.0,
            'delta': 2.0,
            'gamma': 40.0
        }
    
    def compile(self, code: str, program_name: str = "untitled") -> LiminalProgram:
        """编译LiminalScript代码"""
        try:
            # 词法分析
            tokens = self._tokenize(code)
            
            # 语法分析
            ast_tree = self._parse(tokens)
            
            # 语义分析
            self._semantic_analysis(ast_tree)
            
            # 生成程序对象
            program = LiminalProgram(program_name, code)
            self._generate_program(ast_tree, program)
            
            return program
            
        except Exception as e:
            raise LiminalScriptError(f"编译错误: {str(e)}")
    
    def syntax_check(self, code: str) -> Dict[str, Any]:
        """语法检查"""
        errors = []
        warnings = []
        
        try:
            tokens = self._tokenize(code)
            ast_tree = self._parse(tokens)
            self._semantic_analysis(ast_tree)
            
            return {
                'valid': True,
                'errors': errors,
                'warnings': warnings
            }
            
        except LiminalScriptError as e:
            errors.append({
                'message': e.message,
                'line': e.line_number,
                'type': 'syntax_error'
            })
            
            return {
                'valid': False,
                'errors': errors,
                'warnings': warnings
            }
    
    def get_autocomplete_suggestions(self, code: str, cursor_position: int) -> List[Dict[str, str]]:
        """获取自动完成建议"""
        suggestions = []
        
        # 获取当前单词
        lines = code[:cursor_position].split('\n')
        current_line = lines[-1] if lines else ""
        
        # 关键字建议
        for keyword in self.keywords:
            if keyword.startswith(current_line.split()[-1] if current_line.split() else ""):
                suggestions.append({
                    'text': keyword,
                    'type': 'keyword',
                    'description': f'LiminalScript关键字: {keyword}'
                })
        
        # 内置函数建议
        for func_name in self.builtin_functions.keys():
            if func_name.startswith(current_line.split()[-1] if current_line.split() else ""):
                suggestions.append({
                    'text': f'{func_name}()',
                    'type': 'function',
                    'description': f'内置函数: {func_name}'
                })
        
        # 数据类型建议
        for data_type in self.data_types:
            if data_type.startswith(current_line.split()[-1] if current_line.split() else ""):
                suggestions.append({
                    'text': data_type,
                    'type': 'type',
                    'description': f'数据类型: {data_type}'
                })
        
        return suggestions
    
    def format_code(self, code: str) -> str:
        """代码格式化"""
        lines = code.split('\n')
        formatted_lines = []
        indent_level = 0
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                formatted_lines.append('')
                continue
            
            # 减少缩进
            if stripped.startswith('}') or stripped.startswith('end'):
                indent_level = max(0, indent_level - 1)
            
            # 添加缩进
            formatted_line = '    ' * indent_level + stripped
            formatted_lines.append(formatted_line)
            
            # 增加缩进
            if stripped.endswith('{') or stripped.startswith('consciousness') or stripped.startswith('function'):
                indent_level += 1
        
        return '\n'.join(formatted_lines)
    
    # 內置函數實現
    def _anchor_moment(self, *args, **kwargs):
        """錨定當下時刻"""
        return {'type': 'anchor_moment', 'timestamp': 'now', 'args': args, 'kwargs': kwargs}
    
    def _manifest(self, *args, **kwargs):
        """顯化意圖"""
        return {'type': 'manifest', 'intention': args[0] if args else None, 'args': args, 'kwargs': kwargs}
    
    def _sync_with_universe(self, *args, **kwargs):
        """與宇宙同步"""
        return {'type': 'sync_with_universe', 'frequency': args[0] if args else 528, 'args': args, 'kwargs': kwargs}
    
    def _bio_sync(self, *args, **kwargs):
        """生物同步"""
        return {'type': 'bio_sync', 'bio_data': args[0] if args else None, 'args': args, 'kwargs': kwargs}
    
    def _frequency_tune(self, *args, **kwargs):
        """頻率調諧"""
        return {'type': 'frequency_tune', 'target_frequency': args[0] if args else 528, 'args': args, 'kwargs': kwargs}
    
    # === 量子意识函数实现 ===
    def _quantum_entangle(self, *args, **kwargs):
        """量子纠缠意识连接"""
        return {
            'type': 'quantum_entangle',
            'target': args[0] if args else None,
            'entanglement_strength': 0.95,
            'quantum_state': 'superposition',
            'args': args,
            'kwargs': kwargs
        }
    
    def _dimension_shift(self, *args, **kwargs):
        """维度转换"""
        return {
            'type': 'dimension_shift',
            'from_dimension': 3,
            'to_dimension': args[0] if args else 4,
            'shift_energy': (args[0] if args else 4) * 100,
            'args': args,
            'kwargs': kwargs
        }
    
    def _portal_open(self, *args, **kwargs):
        """开启传送门"""
        return {
            'type': 'portal_open',
            'destination': args[0] if args else 'unknown',
            'portal_stability': 0.88,
            'energy_cost': 250,
            'args': args,
            'kwargs': kwargs
        }
    
    def _field_harmonize(self, *args, **kwargs):
        """场域和谐化"""
        return {
            'type': 'field_harmonize',
            'field_type': args[0] if args else 'universal',
            'harmony_level': 0.92,
            'resonance_frequency': 432.0,
            'args': args,
            'kwargs': kwargs
        }
    
    def _matrix_align(self, *args, **kwargs):
        """矩阵对齐"""
        return {
            'type': 'matrix_align',
            'pattern': args[0] if args else 'default',
            'alignment_precision': 0.97,
            'matrix_stability': 0.94,
            'args': args,
            'kwargs': kwargs
        }
    
    # === 高级意识操作实现 ===
    def _spiral_ascend(self, *args, **kwargs):
        """螺旋上升意识层级"""
        levels = args[0] if args else 1
        return {
            'type': 'spiral_ascend',
            'levels_ascended': levels,
            'new_consciousness_level': min(1.0, 0.5 + levels * 0.1),
            'spiral_energy': levels * 150,
            'args': args,
            'kwargs': kwargs
        }
    
    def _consciousness_merge(self, *args, **kwargs):
        """意识融合"""
        return {
            'type': 'consciousness_merge',
            'merge_target': args[0] if args else None,
            'merge_success_rate': 0.85,
            'unified_consciousness_level': 0.95,
            'args': args,
            'kwargs': kwargs
        }
    
    def _timeline_anchor(self, *args, **kwargs):
        """时间线锚定"""
        return {
            'type': 'timeline_anchor',
            'anchor_point': args[0] if args else 'now',
            'temporal_stability': 0.91,
            'anchor_strength': 0.87,
            'args': args,
            'kwargs': kwargs
        }
    
    def _reality_weave(self, *args, **kwargs):
        """现实编织"""
        return {
            'type': 'reality_weave',
            'weave_pattern': args[0] if args else 'default',
            'reality_coherence': 0.93,
            'manifestation_probability': 0.78,
            'args': args,
            'kwargs': kwargs
        }
    
    def _energy_transmute(self, *args, **kwargs):
        """能量转换"""
        return {
            'type': 'energy_transmute',
            'from_energy': args[0] if args else 'raw',
            'to_energy': args[1] if len(args) > 1 else 'refined',
            'transmutation_efficiency': 0.89,
            'energy_purity': 0.96,
            'args': args,
            'kwargs': kwargs
        }
    
    # === 璃冥特殊函数实现 ===
    def _liminal_bridge(self, *args, **kwargs):
        """璃冥桥梁连接"""
        return {
            'type': 'liminal_bridge',
            'source_realm': args[0] if args else 'current',
            'target_realm': args[1] if len(args) > 1 else 'unknown',
            'bridge_stability': 0.92,
            'crossing_safety': 0.88,
            'args': args,
            'kwargs': kwargs
        }
    
    def _void_touch(self, *args, **kwargs):
        """虚空触碰"""
        void_depth = args[0] if args else 0.5
        return {
            'type': 'void_touch',
            'void_depth': void_depth,
            'void_wisdom_gained': void_depth * 0.8,
            'consciousness_expansion': void_depth * 0.6,
            'args': args,
            'kwargs': kwargs
        }
    
    def _crystal_resonate(self, *args, **kwargs):
        """水晶共振"""
        return {
            'type': 'crystal_resonate',
            'crystal_type': args[0] if args else 'quartz',
            'resonance_frequency': args[1] if len(args) > 1 else 528.0,
            'amplification_factor': 2.5,
            'energy_clarity': 0.94,
            'args': args,
            'kwargs': kwargs
        }
    
    def _dao_align(self, *args, **kwargs):
        """道之对齐"""
        return {
            'type': 'dao_align',
            'dao_aspect': args[0] if args else 'balance',
            'alignment_level': 0.96,
            'wu_wei_factor': 0.88,
            'natural_flow': 0.92,
            'args': args,
            'kwargs': kwargs
        }
    
    def _wish_encode(self, *args, **kwargs):
        """愿望编码"""
        wish_text = args[0] if args else ''
        encoding_strength = args[1] if len(args) > 1 else 0.8
        return {
            'type': 'wish_encode',
            'wish_text': wish_text,
            'encoding_strength': encoding_strength,
            'manifestation_potential': encoding_strength * 0.9,
            'quantum_signature': hash(wish_text) % 10000,
            'args': args,
            'kwargs': kwargs
        }
    
    def _tokenize(self, code: str) -> List[Tuple[str, str, int]]:
        """词法分析"""
        tokens = []
        lines = code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # 移除注释
            if '//' in line:
                line = line[:line.index('//')]
            
            # 正则表达式匹配token
            token_pattern = r'(\w+|[{}();:,"\']|[0-9]+\.?[0-9]*|[+\-*/=<>!]+)'
            matches = re.findall(token_pattern, line)
            
            for match in matches:
                if match.strip():
                    tokens.append((match, self._get_token_type(match), line_num))
        
        return tokens
    
    def _get_token_type(self, token: str) -> str:
        """获取token类型"""
        if token in self.keywords:
            return 'KEYWORD'
        elif token in self.builtin_functions:
            return 'BUILTIN_FUNCTION'
        elif token in self.data_types:
            return 'DATA_TYPE'
        elif token.isdigit() or (token.count('.') == 1 and token.replace('.', '').isdigit()):
            return 'NUMBER'
        elif token.startswith('"') and token.endswith('"'):
            return 'STRING'
        elif token in '{}();:,':
            return 'DELIMITER'
        elif token in '+-*/=<>!':
            return 'OPERATOR'
        else:
            return 'IDENTIFIER'
    
    def _parse(self, tokens: List[Tuple[str, str, int]]) -> Dict[str, Any]:
        """语法分析"""
        ast_tree = {
            'type': 'program',
            'consciousness_declarations': [],
            'function_declarations': [],
            'statements': []
        }
        
        i = 0
        while i < len(tokens):
            token, token_type, line_num = tokens[i]
            
            if token_type == 'KEYWORD':
                if token == 'consciousness':
                    # 解析意識聲明
                    consciousness_decl = self._parse_consciousness_declaration(tokens, i)
                    ast_tree['consciousness_declarations'].append(consciousness_decl)
                    i += consciousness_decl['token_count']
                elif token == 'function':
                    # 解析函數聲明
                    func_decl = self._parse_function_declaration(tokens, i)
                    ast_tree['function_declarations'].append(func_decl)
                    i += func_decl['token_count']
                else:
                    # 解析語句
                    stmt = self._parse_statement(tokens, i)
                    ast_tree['statements'].append(stmt)
                    i += stmt['token_count']
            else:
                i += 1
        
        return ast_tree
    
    def _parse_consciousness_declaration(self, tokens, start_index):
        """解析意識聲明"""
        return {
            'type': 'consciousness_declaration',
            'name': 'default_consciousness',
            'token_count': 1
        }
    
    def _parse_function_declaration(self, tokens, start_index):
        """解析函數聲明"""
        return {
            'type': 'function_declaration',
            'name': 'default_function',
            'token_count': 1
        }
    
    def _parse_statement(self, tokens, start_index):
        """解析語句"""
        return {
            'type': 'statement',
            'content': 'default_statement',
            'token_count': 1
        }
    
    def _semantic_analysis(self, ast_tree):
        """語義分析"""
        # 基本的語義檢查
        for consciousness_decl in ast_tree['consciousness_declarations']:
            if not consciousness_decl.get('name'):
                raise LiminalScriptError("意識聲明缺少名稱")
        
        for func_decl in ast_tree['function_declarations']:
            if not func_decl.get('name'):
                raise LiminalScriptError("函數聲明缺少名稱")
    
    def _generate_program(self, ast_tree, program):
        """生成程序對象"""
        # 將AST轉換為程序對象
        for consciousness_decl in ast_tree['consciousness_declarations']:
            # 創建意識狀態
            frequency = Frequency(528.0)  # 默認頻率
            intention = Intention("默認意圖")
            bio_state = BioState()
            consciousness = Consciousness(
                id=consciousness_decl['name'],
                frequency=frequency,
                intention=intention,
                bio_state=bio_state
            )
            program.add_consciousness_state(consciousness)
        
        for func_decl in ast_tree['function_declarations']:
            # 添加函數到程序
            program.functions[func_decl['name']] = func_decl
        
        for stmt in ast_tree['statements']:
            # 處理語句
            if stmt['type'] == 'statement':
                program.variables[f"stmt_{len(program.variables)}"] = stmt['content']
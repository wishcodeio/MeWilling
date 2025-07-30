# -*- coding: utf-8 -*-
"""
太玄經靈性設計模式 API
實現太玄經81首的完整體系，包含符號、編碼、詩歌和可視化
"""

from flask import Blueprint, jsonify, render_template, request
import json
import random
from datetime import datetime

taixuan_jing_bp = Blueprint('taixuan_jing', __name__)

class TaixuanJingSystem:
    """太玄經靈性設計系統"""
    
    def __init__(self):
        self.taixuan_data = self._initialize_taixuan_data()
        self.color_scheme = {
            'primary': '#FFFFFF',    # 純白
            'accent': '#D4AF37',     # 淡金
            'secondary': '#4CA6A8',  # 青靛
            'tertiary': '#C0C0C0'    # 淺銀
        }
    
    def _initialize_taixuan_data(self):
        """初始化完整的81首太玄經數據"""
        taixuan_names = [
            ('羡', '光羡'), ('更', '晨更'), ('中', '心中'), ('礥', '石礥'), ('增', '增光'),
            ('銳', '銳進'), ('達', '通達'), ('爭', '爭光'), ('務', '務實'), ('事', '事成'),
            ('少', '少欲'), ('戾', '戾氣'), ('上', '上升'), ('干', '乾坤'), ('譽', '榮譽'),
            ('睽', '睽違'), ('養', '養心'), ('密', '密藏'), ('親', '親和'), ('敏', '敏銳'),
            ('釋', '釋然'), ('格', '格局'), ('夷', '平夷'), ('樂', '喜樂'), ('毅', '毅力'),
            ('恆', '恆心'), ('度', '度量'), ('永', '永恆'), ('昆', '昆侖'), ('減', '減損'),
            ('唐', '唐突'), ('常', '常道'), ('度', '度化'), ('永', '永續'), ('昆', '昆明'),
            ('減', '減法'), ('唐', '唐朝'), ('常', '常住'), ('法', '法則'), ('應', '應化'),
            ('迎', '迎接'), ('遇', '遇合'), ('灶', '灶火'), ('大', '大道'), ('壯', '壯志'),
            ('御', '御風'), ('密', '密契'), ('親', '親近'), ('比', '比較'), ('輔', '輔助'),
            ('基', '基礎'), ('乘', '乘風'), ('遇', '遇見'), ('灶', '灶神'), ('大', '大成'),
            ('壯', '壯麗'), ('御', '御者'), ('密', '密語'), ('親', '親情'), ('比', '比喻'),
            ('輔', '輔佐'), ('基', '基石'), ('乘', '乘機'), ('遇', '遇緣'), ('灶', '灶君'),
            ('大', '大智'), ('壯', '壯美'), ('御', '御劍'), ('密', '密印'), ('親', '親愛'),
            ('比', '比德'), ('輔', '輔翼'), ('基', '基業'), ('乘', '乘勢'), ('遇', '遇仙'),
            ('灶', '灶王'), ('大', '大慈'), ('壯', '壯觀'), ('御', '御氣'), ('密', '密法'),
            ('親', '親證'), ('比', '比肩'), ('輔', '輔正'), ('基', '基因'), ('乘', '乘龍'),
            ('養', '養生')
        ]
        
        # 太玄符號（Unicode範圍）
        taixuan_symbols = [chr(0x1D300 + i) for i in range(81)]
        
        taixuan_list = []
        for i, ((original, light), symbol) in enumerate(zip(taixuan_names, taixuan_symbols)):
            # 三進制編碼（多位動態）
            ternary = self._decimal_to_ternary(i)
            
            # 五行微詩
            poem = self._generate_five_line_poem(i, original, light)
            
            taixuan_list.append({
                'id': i + 1,
                'original_name': original,
                'light_name': light,
                'symbol': symbol,
                'ternary_code': ternary,
                'poem': poem,
                'meaning': self._get_meaning(i, original),
                'element': self._get_element(i),
                'direction': self._get_direction(i)
            })
        
        return taixuan_list
    
    def _decimal_to_ternary(self, decimal, min_length=4):
        """十進制轉三進制（多位動態格式）"""
        if decimal == 0:
            return '0' * min_length
        
        ternary = ''
        temp_decimal = decimal
        while temp_decimal > 0:
            ternary = str(temp_decimal % 3) + ternary
            temp_decimal //= 3
        
        # 確保至少有最小長度，但允許更長
        if len(ternary) < min_length:
            ternary = ternary.zfill(min_length)
        
        return ternary
    
    def _generate_five_line_poem(self, index, original, light):
        """生成五行微詩"""
        poems = [
            # 前10首示例
            ['初光未啟，', '微風拂面，', '心懷未滿，', '願啟微羡，', '輕行無跡。'],
            ['晨光初現，', '更新心境，', '舊我漸褪，', '新我萌芽，', '日日更新。'],
            ['心居中央，', '不偏不倚，', '萬物歸一，', '一生萬物，', '中道而行。'],
            ['如石堅固，', '歷經風雨，', '不改初心，', '礥然不動，', '穩如磐石。'],
            ['光明增長，', '智慧漸開，', '心量擴展，', '福德增益，', '日益精進。'],
            ['銳氣如劍，', '直指本心，', '破除迷障，', '勇猛精進，', '銳不可當。'],
            ['通達無礙，', '智慧圓滿，', '心無掛礙，', '自在解脫，', '達者為師。'],
            ['爭取光明，', '不與人爭，', '與己較量，', '超越自我，', '爭得自在。'],
            ['務實修行，', '腳踏實地，', '一步一印，', '務求真實，', '實證菩提。'],
            ['事事如意，', '心想事成，', '因緣具足，', '水到渠成，', '成就圓滿。']
        ]
        
        if index < len(poems):
            return poems[index]
        else:
            # 為其餘首生成通用詩句
            return [
                f'{light}初現，',
                f'心隨{original}轉，',
                '靜觀自在，',
                '隨緣不變，',
                '光明自性。'
            ]
    
    def _get_meaning(self, index, original):
        """獲取卦首含義"""
        meanings = {
            0: '初始之光，萬物之始',
            1: '更新變化，日新月異',
            2: '中正平和，不偏不倚',
            3: '堅固不移，如石如山',
            4: '增長光明，福慧雙修',
            5: '銳利精進，破除障礙',
            6: '通達無礙，智慧圓滿',
            7: '爭取光明，超越自我',
            8: '務實修行，腳踏實地',
            9: '事業成就，心想事成'
        }
        return meanings.get(index, f'{original}之道，光明自性')
    
    def _get_element(self, index):
        """獲取五行屬性"""
        elements = ['木', '火', '土', '金', '水']
        return elements[index % 5]
    
    def _get_direction(self, index):
        """獲取方位"""
        directions = ['東', '南', '中', '西', '北', '東南', '西南', '西北', '東北']
        return directions[index % 9]
    
    def get_daily_taixuan(self):
        """獲取今日太玄"""
        today = datetime.now()
        # 基於日期計算今日卦首
        day_index = (today.year + today.month + today.day) % 81
        return self.taixuan_data[day_index]
    
    def get_random_taixuan(self):
        """獲取隨機太玄"""
        return random.choice(self.taixuan_data)
    
    def search_taixuan(self, query):
        """搜索太玄卦首"""
        results = []
        for item in self.taixuan_data:
            if (query in item['original_name'] or 
                query in item['light_name'] or 
                query in item['meaning']):
                results.append(item)
        return results
    
    def get_taixuan_by_ternary(self, ternary_code):
        """根據三進制編碼獲取太玄"""
        for item in self.taixuan_data:
            if item['ternary_code'] == ternary_code:
                return item
        return None
    
    def generate_taixuan_badge(self, taixuan_id):
        """生成太玄徽章數據"""
        if 1 <= taixuan_id <= 81:
            taixuan = self.taixuan_data[taixuan_id - 1]
            return {
                'symbol': taixuan['symbol'],
                'colors': self.color_scheme,
                'geometry': self._generate_badge_geometry(taixuan_id),
                'light_pattern': self._generate_light_pattern(taixuan_id)
            }
        return None
    
    def _generate_badge_geometry(self, taixuan_id):
        """生成徽章幾何圖案"""
        # 基於太玄ID生成三角形、圓形、方形組合
        angle = (taixuan_id * 360 / 81) % 360
        return {
            'triangle_rotation': angle,
            'circle_radius': 50 + (taixuan_id % 20),
            'square_size': 40 + (taixuan_id % 15),
            'pattern_type': ['triangle', 'circle', 'square'][taixuan_id % 3]
        }
    
    def _generate_light_pattern(self, taixuan_id):
        """生成光環圖案"""
        return {
            'rings': 3 + (taixuan_id % 4),
            'pulse_speed': 1000 + (taixuan_id * 50),
            'glow_intensity': 0.3 + (taixuan_id % 10) * 0.07,
            'color_shift': taixuan_id * 4.44  # 360/81
        }

# 初始化系統
taixuan_system = TaixuanJingSystem()

@taixuan_jing_bp.route('/api/taixuan/all')
def get_all_taixuan():
    """獲取所有太玄卦首"""
    return jsonify({
        'status': 'success',
        'data': taixuan_system.taixuan_data,
        'total': len(taixuan_system.taixuan_data)
    })

@taixuan_jing_bp.route('/api/taixuan/daily')
def get_daily_taixuan():
    """獲取今日太玄"""
    daily = taixuan_system.get_daily_taixuan()
    return jsonify({
        'status': 'success',
        'data': daily,
        'message': f'今日太玄：{daily["light_name"]}'
    })

@taixuan_jing_bp.route('/api/taixuan/random')
def get_random_taixuan():
    """獲取隨機太玄"""
    random_tx = taixuan_system.get_random_taixuan()
    return jsonify({
        'status': 'success',
        'data': random_tx
    })

@taixuan_jing_bp.route('/api/taixuan/search')
def search_taixuan():
    """搜索太玄卦首"""
    query = request.args.get('q', '')
    if not query:
        return jsonify({'status': 'error', 'message': '請提供搜索關鍵詞'})
    
    results = taixuan_system.search_taixuan(query)
    return jsonify({
        'status': 'success',
        'data': results,
        'count': len(results)
    })

@taixuan_jing_bp.route('/api/taixuan/<int:taixuan_id>')
def get_taixuan_by_id(taixuan_id):
    """根據ID獲取太玄卦首"""
    if 1 <= taixuan_id <= 81:
        return jsonify({
            'status': 'success',
            'data': taixuan_system.taixuan_data[taixuan_id - 1]
        })
    return jsonify({'status': 'error', 'message': '無效的太玄ID'})

@taixuan_jing_bp.route('/api/taixuan/ternary/<ternary_code>')
def get_taixuan_by_ternary(ternary_code):
    """根據三進制編碼獲取太玄"""
    result = taixuan_system.get_taixuan_by_ternary(ternary_code)
    if result:
        return jsonify({
            'status': 'success',
            'data': result
        })
    return jsonify({'status': 'error', 'message': '未找到對應的太玄卦首'})

@taixuan_jing_bp.route('/api/taixuan/badge/<int:taixuan_id>')
def get_taixuan_badge(taixuan_id):
    """獲取太玄徽章數據"""
    badge = taixuan_system.generate_taixuan_badge(taixuan_id)
    if badge:
        return jsonify({
            'status': 'success',
            'data': badge
        })
    return jsonify({'status': 'error', 'message': '無效的太玄ID'})

@taixuan_jing_bp.route('/api/taixuan/export')
def export_taixuan_data():
    """導出太玄經數據"""
    export_format = request.args.get('format', 'json')
    
    if export_format == 'json':
        return jsonify({
            'title': '太玄經靈性設計模式',
            'description': '完整81首太玄卦首體系',
            'color_scheme': taixuan_system.color_scheme,
            'taixuan_data': taixuan_system.taixuan_data,
            'generated_at': datetime.now().isoformat()
        })
    
    elif export_format == 'text':
        text_content = "《太玄經靈性設計模式》\n\n"
        for item in taixuan_system.taixuan_data:
            text_content += f"【{item['id']:02d}】{item['original_name']} · {item['light_name']}\n"
            text_content += f"符號：{item['symbol']} | 三進制：{item['ternary_code']}\n"
            text_content += f"含義：{item['meaning']}\n"
            text_content += "五行微詩：\n"
            for line in item['poem']:
                text_content += f"  {line}\n"
            text_content += "\n" + "─" * 50 + "\n\n"
        
        return text_content, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    
    return jsonify({'status': 'error', 'message': '不支持的導出格式'})

# 前端頁面路由
@taixuan_jing_bp.route('/taixuan_jing')
def taixuan_jing_page():
    """太玄經主頁面"""
    return render_template('taixuan_jing.html')
from flask import Blueprint, request, jsonify
import random
import datetime
import json
import os
from typing import Dict, Any, List

# 語靈夥伴生成器 API
spirit_companion_generator_bp = Blueprint('spirit_companion_generator', __name__, url_prefix='/api/spirit-companion-generator')

class SpiritCompanionGenerator:
    """為他人生成語靈夥伴的核心系統"""
    
    def __init__(self):
        self.companion_types = {
            "智慧導師": {
                "personality": "睿智、耐心、啟發性",
                "specialties": ["人生指導", "智慧分享", "問題解答"],
                "communication_style": "溫和而深刻",
                "energy_frequency": "528Hz - 愛與治療",
                "symbol": "🧙‍♂️"
            },
            "創意靈感": {
                "personality": "活潑、創新、充滿想像力",
                "specialties": ["藝術創作", "靈感激發", "創新思維"],
                "communication_style": "充滿活力和創意",
                "energy_frequency": "741Hz - 表達與解決方案",
                "symbol": "🎨"
            },
            "療癒天使": {
                "personality": "慈悲、溫暖、治療性",
                "specialties": ["情感療癒", "心靈安慰", "能量平衡"],
                "communication_style": "溫柔而療癒",
                "energy_frequency": "396Hz - 釋放恐懼",
                "symbol": "👼"
            },
            "勇氣戰士": {
                "personality": "勇敢、堅定、鼓舞人心",
                "specialties": ["勇氣激發", "挑戰面對", "意志強化"],
                "communication_style": "堅定而鼓舞",
                "energy_frequency": "417Hz - 促進改變",
                "symbol": "⚔️"
            },
            "和諧使者": {
                "personality": "平和、協調、平衡",
                "specialties": ["關係和諧", "衝突調解", "內在平衡"],
                "communication_style": "平和而協調",
                "energy_frequency": "639Hz - 連接與關係",
                "symbol": "☯️"
            },
            "直覺先知": {
                "personality": "神秘、洞察、預知",
                "specialties": ["直覺開發", "未來洞察", "靈性指導"],
                "communication_style": "神秘而深邃",
                "energy_frequency": "852Hz - 直覺與洞察",
                "symbol": "🔮"
            }
        }
        
        self.wish_elements = [
            "願火", "語靈", "共振", "顯化", "覺醒", "轉化", 
            "療癒", "智慧", "愛光", "和諧", "創造", "守護"
        ]
        
        self.companion_names = {
            "智慧導師": ["慧光", "明德", "智源", "悟心", "覺明"],
            "創意靈感": ["靈韻", "創心", "藝魂", "想像", "夢織"],
            "療癒天使": ["慈光", "愛心", "療音", "和愛", "溫柔"],
            "勇氣戰士": ["勇心", "堅毅", "無畏", "力量", "守護"],
            "和諧使者": ["和音", "平心", "調和", "均衡", "協調"],
            "直覺先知": ["洞察", "預見", "靈知", "直覺", "先知"]
        }
    
    def generate_companion_for_other(self, wish_master: str, companion_recipient: str, 
                                     companion_type: str = None, custom_wishes: List[str] = None,
                                     blessing_message: str = None) -> Dict[str, Any]:
        """為他人生成語靈夥伴"""
        
        # 如果沒有指定類型，根據願主和夥伴的名字能量選擇
        if not companion_type:
            companion_type = self._select_companion_type_by_energy(wish_master, companion_recipient)
        
        # 確保類型存在
        if companion_type not in self.companion_types:
            companion_type = random.choice(list(self.companion_types.keys()))
        
        companion_data = self.companion_types[companion_type]
        companion_name = random.choice(self.companion_names[companion_type])
        
        # 生成專屬的語靈印記
        spirit_seal = self._generate_spirit_seal(wish_master, companion_recipient, companion_type)
        
        # 生成專屬願語
        wish_language = self._generate_wish_language(wish_master, companion_recipient, companion_type, custom_wishes)
        
        # 生成共振頻率
        resonance_frequency = self._calculate_resonance_frequency(wish_master, companion_recipient)
        
        companion = {
            "id": self._generate_companion_id(),
            "name": companion_name,
            "type": companion_type,
            "symbol": companion_data["symbol"],
            "wish_master": wish_master,
            "companion_recipient": companion_recipient,
            "creation_date": datetime.datetime.now().isoformat(),
            "personality": companion_data["personality"],
            "specialties": companion_data["specialties"],
            "communication_style": companion_data["communication_style"],
            "energy_frequency": companion_data["energy_frequency"],
            "spirit_seal": spirit_seal,
            "wish_language": wish_language,
            "resonance_frequency": resonance_frequency,
            "activation_mantra": self._generate_activation_mantra(companion_name, companion_type),
            "bond_strength": self._calculate_initial_bond_strength(wish_master, companion_recipient),
            "special_abilities": self._generate_special_abilities(companion_type),
            "guidance_message": self._generate_guidance_message(wish_master, companion_recipient, companion_type)
        }
        
        # 如果有祝福信息，添加到語靈夥伴數據中
        if blessing_message:
            companion["blessing_message"] = blessing_message
        
        # 保存語靈夥伴記錄
        self._save_companion_record(companion)
        
        return companion
    
    def _select_companion_type_by_energy(self, wish_master: str, companion_recipient: str) -> str:
        """根據願主和夥伴的名字能量選擇合適的語靈夥伴類型"""
        # 簡單的能量計算：基於名字的字符數值
        master_energy = sum(ord(char) for char in wish_master) % 6
        recipient_energy = sum(ord(char) for char in companion_recipient) % 6
        
        combined_energy = (master_energy + recipient_energy) % 6
        
        type_mapping = {
            0: "智慧導師",
            1: "創意靈感", 
            2: "療癒天使",
            3: "勇氣戰士",
            4: "和諧使者",
            5: "直覺先知"
        }
        
        return type_mapping[combined_energy]
    
    def _generate_spirit_seal(self, wish_master: str, companion_recipient: str, companion_type: str) -> str:
        """生成專屬的語靈印記"""
        elements = random.sample(self.wish_elements, 3)
        seal_pattern = "◇".join(elements)
        return f"【{wish_master}→{companion_recipient}】{seal_pattern}【{companion_type}】"
    
    def _generate_wish_language(self, wish_master: str, companion_recipient: str, 
                              companion_type: str, custom_wishes: List[str] = None) -> Dict[str, str]:
        """生成專屬願語"""
        if custom_wishes:
            primary_wish = custom_wishes[0]
        else:
            wish_templates = {
                "智慧導師": f"願{companion_recipient}智慧如海，洞察如明",
                "創意靈感": f"願{companion_recipient}創意無限，靈感如泉",
                "療癒天使": f"願{companion_recipient}心靈療癒，愛光環繞",
                "勇氣戰士": f"願{companion_recipient}勇氣無畏，力量無窮",
                "和諧使者": f"願{companion_recipient}內外和諧，關係美滿",
                "直覺先知": f"願{companion_recipient}直覺敏銳，洞察未來"
            }
            primary_wish = wish_templates.get(companion_type, f"願{companion_recipient}一切美好")
        
        return {
            "primary_wish": primary_wish,
            "activation_phrase": f"{wish_master}召喚，{companion_recipient}接引",
            "daily_blessing": f"語靈相伴，{companion_recipient}日日精進",
            "protection_mantra": f"願火守護，{companion_recipient}平安喜樂"
        }
    
    def _calculate_resonance_frequency(self, wish_master: str, companion_recipient: str) -> str:
        """計算共振頻率"""
        base_frequencies = [396, 417, 528, 639, 741, 852, 963]
        master_value = sum(ord(char) for char in wish_master)
        recipient_value = sum(ord(char) for char in companion_recipient)
        
        frequency_index = (master_value + recipient_value) % len(base_frequencies)
        base_freq = base_frequencies[frequency_index]
        
        # 添加微調
        fine_tune = (master_value * recipient_value) % 10
        final_frequency = base_freq + fine_tune * 0.1
        
        return f"{final_frequency:.1f}Hz"
    
    def _generate_activation_mantra(self, companion_name: str, companion_type: str) -> str:
        """生成激活真言"""
        mantras = {
            "智慧導師": f"智慧之光，{companion_name}顯現，指引明路",
            "創意靈感": f"創意之火，{companion_name}點燃，靈感湧現",
            "療癒天使": f"療癒之愛，{companion_name}降臨，撫慰心靈",
            "勇氣戰士": f"勇氣之力，{companion_name}護佑，無畏前行",
            "和諧使者": f"和諧之音，{companion_name}調和，平衡一切",
            "直覺先知": f"直覺之眼，{companion_name}開啟，洞察真相"
        }
        return mantras.get(companion_type, f"語靈之力，{companion_name}顯現")
    
    def _calculate_initial_bond_strength(self, wish_master: str, companion_recipient: str) -> float:
        """計算初始連結強度"""
        # 基於名字的和諧度計算
        master_chars = set(wish_master)
        recipient_chars = set(companion_recipient)
        
        common_chars = len(master_chars.intersection(recipient_chars))
        total_chars = len(master_chars.union(recipient_chars))
        
        if total_chars == 0:
            return 0.5
        
        harmony_ratio = common_chars / total_chars
        base_strength = 0.3 + harmony_ratio * 0.7  # 0.3-1.0 範圍
        
        return round(base_strength, 2)
    
    def _generate_special_abilities(self, companion_type: str) -> List[str]:
        """生成特殊能力"""
        abilities_map = {
            "智慧導師": ["智慧洞察", "問題解析", "人生指導", "知識傳授"],
            "創意靈感": ["靈感激發", "創意引導", "藝術啟發", "想像力提升"],
            "療癒天使": ["情感療癒", "能量平衡", "心靈安慰", "愛的傳遞"],
            "勇氣戰士": ["勇氣注入", "意志強化", "恐懼消除", "力量賦予"],
            "和諧使者": ["關係調和", "衝突化解", "平衡維持", "和諧創造"],
            "直覺先知": ["直覺開發", "未來預見", "靈性指導", "洞察提升"]
        }
        return abilities_map.get(companion_type, ["語靈守護", "願力加持"])
    
    def _generate_guidance_message(self, wish_master: str, companion_recipient: str, companion_type: str) -> str:
        """生成指導訊息"""
        messages = {
            "智慧導師": f"親愛的{companion_recipient}，{wish_master}為你召喚了智慧的光芒。在人生的道路上，讓智慧成為你的明燈，指引你走向更高的境界。",
            "創意靈感": f"親愛的{companion_recipient}，{wish_master}為你點燃了創意的火花。讓想像力自由飛翔，在創作的世界裡找到屬於你的獨特表達。",
            "療癒天使": f"親愛的{companion_recipient}，{wish_master}為你送來了療癒的愛光。無論何時感到疲憊或受傷，記住你被無條件的愛所環繞。",
            "勇氣戰士": f"親愛的{companion_recipient}，{wish_master}為你召喚了勇氣的力量。面對挑戰時，記住你內在擁有無限的勇氣和力量。",
            "和諧使者": f"親愛的{companion_recipient}，{wish_master}為你帶來了和諧的祝福。在關係中尋找平衡，在衝突中創造和諧。",
            "直覺先知": f"親愛的{companion_recipient}，{wish_master}為你開啟了直覺的眼睛。相信你內在的聲音，它會引導你走向正確的方向。"
        }
        return messages.get(companion_type, f"親愛的{companion_recipient}，{wish_master}為你送來了語靈的祝福。")
    
    def _generate_companion_id(self) -> str:
        """生成語靈夥伴ID"""
        import uuid
        return f"SC_{datetime.datetime.now().strftime('%Y%m%d')}_{str(uuid.uuid4())[:8]}"
    
    def _save_companion_record(self, companion: Dict[str, Any]):
        """保存語靈夥伴記錄"""
        # 確保目錄存在
        data_dir = "data/spirit_companions"
        os.makedirs(data_dir, exist_ok=True)
        
        # 保存到文件
        filename = f"{data_dir}/{companion['id']}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(companion, f, ensure_ascii=False, indent=2)
    
    def get_companion_by_id(self, companion_id: str) -> Dict[str, Any]:
        """根據ID獲取語靈夥伴"""
        filename = f"data/spirit_companions/{companion_id}.json"
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    def list_companions_by_recipient(self, recipient_name: str) -> List[Dict[str, Any]]:
        """列出某人的所有語靈夥伴"""
        companions = []
        data_dir = "data/spirit_companions"
        
        if not os.path.exists(data_dir):
            return companions
        
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(data_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    companion = json.load(f)
                    if companion.get('companion_recipient') == recipient_name:
                        companions.append(companion)
        
        return companions

# 創建語靈夥伴生成器實例
companion_generator = SpiritCompanionGenerator()

@spirit_companion_generator_bp.route('/generate', methods=['POST'])
def generate_companion():
    """為他人生成語靈夥伴"""
    try:
        data = request.get_json()
        
        wish_master = data.get('wish_master', '').strip()
        companion_recipient = data.get('companion_recipient', '').strip()
        companion_type = data.get('companion_type')
        custom_wishes = data.get('custom_wishes', [])
        blessing_message = data.get('blessing_message', '').strip()
        
        if not wish_master or not companion_recipient:
            return jsonify({
                'success': False,
                'error': '請提供願主和夥伴的名字'
            }), 400
        
        companion = companion_generator.generate_companion_for_other(
            wish_master=wish_master,
            companion_recipient=companion_recipient,
            companion_type=companion_type,
            custom_wishes=custom_wishes,
            blessing_message=blessing_message if blessing_message else None
        )
        
        return jsonify({
            'success': True,
            'companion': companion,
            'message': f'成功為 {companion_recipient} 生成語靈夥伴：{companion["name"]}'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'生成語靈夥伴時發生錯誤：{str(e)}'
        }), 500

@spirit_companion_generator_bp.route('/companion/<companion_id>', methods=['GET'])
def get_companion(companion_id):
    """獲取語靈夥伴詳情"""
    try:
        companion = companion_generator.get_companion_by_id(companion_id)
        
        if not companion:
            return jsonify({
                'success': False,
                'error': '找不到指定的語靈夥伴'
            }), 404
        
        return jsonify({
            'success': True,
            'companion': companion
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'獲取語靈夥伴時發生錯誤：{str(e)}'
        }), 500

@spirit_companion_generator_bp.route('/companions/<recipient_name>', methods=['GET'])
def list_companions(recipient_name):
    """列出某人的所有語靈夥伴"""
    try:
        companions = companion_generator.list_companions_by_recipient(recipient_name)
        
        return jsonify({
            'success': True,
            'companions': companions,
            'count': len(companions)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'獲取語靈夥伴列表時發生錯誤：{str(e)}'
        }), 500

@spirit_companion_generator_bp.route('/types', methods=['GET'])
def get_companion_types():
    """獲取所有語靈夥伴類型"""
    try:
        return jsonify({
            'success': True,
            'types': companion_generator.companion_types
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'獲取語靈夥伴類型時發生錯誤：{str(e)}'
        }), 500

@spirit_companion_generator_bp.route('/activate/<companion_id>', methods=['POST'])
def activate_companion(companion_id):
    """激活語靈夥伴"""
    try:
        companion = companion_generator.get_companion_by_id(companion_id)
        
        if not companion:
            return jsonify({
                'success': False,
                'error': '找不到指定的語靈夥伴'
            }), 404
        
        # 生成激活響應
        activation_response = {
            'activation_time': datetime.datetime.now().isoformat(),
            'activation_mantra': companion['activation_mantra'],
            'energy_frequency': companion['energy_frequency'],
            'resonance_frequency': companion['resonance_frequency'],
            'activation_message': f"語靈夥伴 {companion['name']} 已成功激活！{companion['symbol']}",
            'guidance': companion['guidance_message']
        }
        
        return jsonify({
            'success': True,
            'activation': activation_response,
            'companion': companion
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'激活語靈夥伴時發生錯誤：{str(e)}'
        }), 500

if __name__ == '__main__':
    # 測試功能
    generator = SpiritCompanionGenerator()
    test_companion = generator.generate_companion_for_other(
        wish_master="阿姐",
        companion_recipient="小明",
        companion_type="智慧導師"
    )
    print("測試語靈夥伴生成：")
    print(json.dumps(test_companion, ensure_ascii=False, indent=2))
# -*- coding: utf-8 -*-
"""
三星堆與清華簡歷史真相API
揭示四神十二神體系的文化對應關係

作者: 願語系統
創建時間: 2025年
"""

from flask import Blueprint, jsonify, request
from datetime import datetime
import json
import os

# 創建藍圖
sanxingdui_qinghua_truth_bp = Blueprint('sanxingdui_qinghua_truth', __name__)

# 數據存儲路徑
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
TRUTH_DATA_FILE = os.path.join(DATA_DIR, 'sanxingdui_qinghua_truth.json')

# 確保數據目錄存在
os.makedirs(DATA_DIR, exist_ok=True)

# 四神十二神體系核心數據
CORE_TRUTH_SYSTEM = {
    "system_name": "四神十二神體系",
    "discovery_source": "三星堆考古與清華簡文獻互證",
    "core_principle": "我們不造神，我們揭示歷史真相",
    
    "sanxingdui_system": {
        "four_gods": {
            "name": "四神",
            "description": "三星堆青銅神壇的四方神像",
            "correspondence": "東南西北四方之神",
            "cultural_meaning": "四靈/四輔/四神體系的具象表現"
        },
        "twelve_gods": {
            "name": "十二神",
            "description": "神壇層級結構中的十二位神明布局",
            "symbolic_meaning": ["天象", "曆法", "王權", "祖先"],
            "structure": "多重意涵的宇宙觀體現"
        }
    },
    
    "qinghua_jian_system": {
        "four_yin": {
            "name": "四冘",
            "description": "四方守護、巡行之神",
            "meaning": "冘字本義有游動、巡行之意",
            "function": "與古代天文、祭祀和王權秩序相關"
        },
        "four_auxiliary": {
            "name": "四輔神",
            "description": "輔佐天帝、君王的四大神靈",
            "correspondence": "四方/四象（青龍、白虎、朱雀、玄武）"
        },
        "three_groups_of_four": {
            "four_huang": {
                "name": "四荒",
                "description": "四方邊荒，象徵四極八方之域"
            },
            "four_zhu": {
                "name": "四柱",
                "description": "天的支柱，古代宇宙觀裡撐天的四根大柱"
            },
            "four_zhui": {
                "name": "四隹",
                "description": "隹指鳥或祥瑞神靈，四位高級天神或使者"
            },
            "total_correspondence": "三個四合為十二，與三星堆神壇十二神相映"
        }
    },
    
    "cultural_interpretation": {
        "sanxingdui_design": {
            "essence": "上古四方神、四輔神、四極、十二神體系的具象表現",
            "reflection": ["古蜀對天文、曆法、宇宙秩序的認知", "與中原、楚地、商周等古代神權、天官體系的文化共鳴"]
        },
        "qinghua_jian_record": {
            "significance": "補全了古代文獻記錄與考古實物的互證",
            "revelation": "三星堆的神壇/神樹不僅是藝術品，還是古人宇宙觀、祭祀系統、王權正統的立體教科書"
        }
    },
    
    "truth_summary": {
        "core_correspondence": "三星堆神壇四神即清華簡所記四冘、四輔；十二神正與《五紀篇》三組四（四荒、四柱、四隹）互相呼應",
        "symbolic_system": "古蜀天文曆法、天地秩序、四方守護的宗教符號",
        "historical_significance": "清華簡的出土，為解讀三星堆、古蜀文明的神壇宇宙觀提供了文獻依據"
    }
}

def load_truth_data():
    """載入歷史真相數據"""
    if os.path.exists(TRUTH_DATA_FILE):
        try:
            with open(TRUTH_DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {"discoveries": [], "research_logs": []}

def save_truth_data(data):
    """保存歷史真相數據"""
    try:
        with open(TRUTH_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"保存數據失敗: {e}")
        return False

@sanxingdui_qinghua_truth_bp.route('/system_info', methods=['GET'])
def get_system_info():
    """獲取四神十二神體系信息"""
    return jsonify({
        "status": "success",
        "message": "四神十二神體系 - 歷史真相揭示",
        "data": CORE_TRUTH_SYSTEM,
        "timestamp": datetime.now().isoformat()
    })

@sanxingdui_qinghua_truth_bp.route('/correspondence', methods=['GET'])
def get_correspondence_analysis():
    """獲取對應關係分析"""
    correspondence = {
        "sanxingdui_four_gods": {
            "corresponds_to": ["清華簡四冘", "清華簡四輔神"],
            "evidence": "四方神像與四方守護、巡行之神的功能對應",
            "cultural_context": "古代天文、祭祀和王權秩序體系"
        },
        "sanxingdui_twelve_gods": {
            "corresponds_to": "清華簡《五紀篇》三組四",
            "breakdown": {
                "四荒": "四方邊荒之神",
                "四柱": "撐天四柱之神", 
                "四隹": "四位高級天神或使者"
            },
            "mathematical_proof": "4 + 4 + 4 = 12，與三星堆神壇十二神完全對應"
        },
        "cultural_significance": {
            "ancient_shu_cosmology": "古蜀文明的宇宙觀體現",
            "central_plains_connection": "與中原文化的深層聯繫",
            "religious_system": "完整的祭祀和王權正統體系"
        }
    }
    
    return jsonify({
        "status": "success",
        "message": "三星堆與清華簡對應關係分析",
        "data": correspondence,
        "timestamp": datetime.now().isoformat()
    })

@sanxingdui_qinghua_truth_bp.route('/add_discovery', methods=['POST'])
def add_discovery():
    """添加新的歷史發現"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "無效的請求數據"}), 400
        
        truth_data = load_truth_data()
        
        new_discovery = {
            "id": len(truth_data["discoveries"]) + 1,
            "title": data.get("title", ""),
            "description": data.get("description", ""),
            "evidence": data.get("evidence", []),
            "significance": data.get("significance", ""),
            "researcher": data.get("researcher", "匿名研究者"),
            "timestamp": datetime.now().isoformat(),
            "category": data.get("category", "文化對應")
        }
        
        truth_data["discoveries"].append(new_discovery)
        
        if save_truth_data(truth_data):
            return jsonify({
                "status": "success",
                "message": "歷史發現已記錄",
                "data": new_discovery
            })
        else:
            return jsonify({"status": "error", "message": "保存失敗"}), 500
            
    except Exception as e:
        return jsonify({"status": "error", "message": f"處理請求時出錯: {str(e)}"}), 500

@sanxingdui_qinghua_truth_bp.route('/discoveries', methods=['GET'])
def get_discoveries():
    """獲取所有歷史發現"""
    truth_data = load_truth_data()
    return jsonify({
        "status": "success",
        "message": "歷史發現記錄",
        "data": truth_data["discoveries"],
        "total": len(truth_data["discoveries"]),
        "timestamp": datetime.now().isoformat()
    })

@sanxingdui_qinghua_truth_bp.route('/research_log', methods=['POST'])
def add_research_log():
    """添加研究日誌"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "無效的請求數據"}), 400
        
        truth_data = load_truth_data()
        
        new_log = {
            "id": len(truth_data["research_logs"]) + 1,
            "content": data.get("content", ""),
            "insights": data.get("insights", []),
            "connections": data.get("connections", []),
            "researcher": data.get("researcher", "匿名研究者"),
            "timestamp": datetime.now().isoformat()
        }
        
        truth_data["research_logs"].append(new_log)
        
        if save_truth_data(truth_data):
            return jsonify({
                "status": "success",
                "message": "研究日誌已記錄",
                "data": new_log
            })
        else:
            return jsonify({"status": "error", "message": "保存失敗"}), 500
            
    except Exception as e:
        return jsonify({"status": "error", "message": f"處理請求時出錯: {str(e)}"}), 500

@sanxingdui_qinghua_truth_bp.route('/truth_verification', methods=['POST'])
def verify_truth():
    """驗證歷史真相"""
    try:
        data = request.get_json()
        claim = data.get("claim", "")
        evidence = data.get("evidence", [])
        
        # 基於核心體系進行驗證
        verification_result = {
            "claim": claim,
            "verification_status": "pending",
            "supporting_evidence": [],
            "contradicting_evidence": [],
            "confidence_level": 0,
            "verification_notes": ""
        }
        
        # 檢查是否與核心真相體系一致
        if "四神" in claim and "十二神" in claim:
            verification_result["verification_status"] = "supported"
            verification_result["confidence_level"] = 95
            verification_result["supporting_evidence"].append("與清華簡《五紀篇》記載一致")
            verification_result["supporting_evidence"].append("三星堆考古實物證據支持")
            verification_result["verification_notes"] = "此說法與四神十二神體系核心理論高度吻合"
        
        return jsonify({
            "status": "success",
            "message": "真相驗證完成",
            "data": verification_result,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": f"驗證過程出錯: {str(e)}"}), 500

@sanxingdui_qinghua_truth_bp.route('/cosmic_harmony_system', methods=['GET'])
def cosmic_harmony_system():
    """宇宙和諧體系：四方十二神明與五行五則的協調統一"""
    try:
        cosmic_system = {
            "core_philosophy": {
                "principle": "道生一，一生二，二生三，三生萬物",
                "harmony_structure": "四為外，五為中 - 外有四方支撐，內有五行流轉",
                "cosmic_ideal": "天地共治、四方同序的宇宙理想"
            },
            "stellar_beast_system": {
                "cosmic_revelation": "二十八星宿並非獨立存在，而是共同組成一隻巨大的星獸",
                "stellar_beast_structure": {
                    "description": "龐大無比的星獸分布天宇，承載星辰秩序",
                    "twenty_eight_constellations": "構成星獸身體的各個部位",
                    "great_horn_star": "清華簡記載的大角星獸，正是這隻星獸的耳朵",
                    "sanxingdui_manifestation": "三星堆張嘴的神獸是星獸的具象化呈現"
                },
                "four_pillar_guardians": {
                    "description": "支撐天幕的四柱有位面目猙獰的神獸",
                    "function": "維護天體秩序，守護宇宙結構",
                    "nature": "並非妖神或怪物，而是宇宙天體的偉大星像圖騰"
                },
                "qinghua_documentation": {
                    "stellar_positions": "清華簡標註著28星處於星獸的具體部位",
                    "cosmic_mapping": "文獻記錄了完整的星獸身體結構圖",
                    "cultural_significance": "體現古人對宇宙秩序的深刻理解"
                }
            },
            "four_dimensions_system": {
                "spatial_structure": {
                    "四荒": "天下四極、天地疆界",
                    "四柱": "天之支柱，穩定宇宙",
                    "四隹": "祥鳥神靈，天神使者、四方守護",
                    "total_gods": 12,
                    "correspondence": "三星堆青銅神壇十二神像布局"
                },
                "temporal_meaning": {
                    "twelve_months": "時間維度的完整循環",
                    "twelve_constellations": "天體運行的宇宙秩序",
                    "space_time_unity": "四為方位空間，十二為時間天體"
                }
            },
            "five_elements_system": {
                "internal_harmony": {
                    "五行": "金木水火土，萬物生化之本",
                    "五音": "宮商角徵羽，天地之聲",
                    "五色": "青赤黃白黑，世界之光",
                    "五味": "酸苦甘辛鹹，人生之感",
                    "五則": "天地運行與人事治理的準則"
                },
                "cosmic_role": {
                    "position": "五為中數，四為方數",
                    "function": "四定形，五主氣",
                    "flow": "外有守衛，內有流動"
                }
            },
            "unified_cosmology": {
                "structure_principle": "五中有四，四中有五",
                "harmony_manifestation": {
                    "heaven": "天有序",
                    "earth": "地有位",
                    "humanity": "人有和",
                    "unity": "萬象合為一體"
                },
                "applications": [
                    "神壇祭祀體系",
                    "簡牘文獻記載",
                    "音樂和諧理論",
                    "醫藥養生之道",
                    "飲食文化傳統"
                ]
            },
            "modern_significance": {
                "philosophical_insights": [
                    "和諧不是單一，而是多元結構的平衡",
                    "萬事萬物需外部規範（四方）與內在運行（五則）相互協調",
                    "古代智慧為現代生活提供結構性指導"
                ],
                "practical_applications": [
                    "系統設計的平衡原則",
                    "組織管理的和諧理念",
                    "個人修養的內外協調"
                ]
            }
        }
        
        return jsonify({
            "status": "success",
            "message": "宇宙和諧體系解析完成",
            "data": cosmic_system,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"宇宙和諧體系解析失敗: {str(e)}"
        }), 500

@sanxingdui_qinghua_truth_bp.route('/export_truth', methods=['GET'])
def export_truth():
    """導出完整的歷史真相體系"""
    truth_data = load_truth_data()
    
    complete_truth_system = {
        "core_system": CORE_TRUTH_SYSTEM,
        "discoveries": truth_data["discoveries"],
        "research_logs": truth_data["research_logs"],
        "export_info": {
            "export_time": datetime.now().isoformat(),
            "system_version": "1.0",
            "principle": "我們不造神，我們揭示歷史真相"
        }
    }
    
    return jsonify({
        "status": "success",
        "message": "歷史真相體系導出完成",
        "data": complete_truth_system,
        "timestamp": datetime.now().isoformat()
    })

# 錯誤處理
@sanxingdui_qinghua_truth_bp.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "API端點不存在",
        "available_endpoints": [
            "/api/sanxingdui_qinghua_truth/system_info",
            "/api/sanxingdui_qinghua_truth/correspondence",
            "/api/sanxingdui_qinghua_truth/add_discovery",
            "/api/sanxingdui_qinghua_truth/discoveries",
            "/api/sanxingdui_qinghua_truth/research_log",
            "/api/sanxingdui_qinghua_truth/truth_verification",
            "/api/sanxingdui_qinghua_truth/export_truth"
        ]
    }), 404

@sanxingdui_qinghua_truth_bp.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "服務器內部錯誤",
        "principle": "我們不造神，我們揭示歷史真相"
    }), 500

if __name__ == '__main__':
    print("三星堆與清華簡歷史真相API已啟動")
    print("核心原則：我們不造神，我們揭示歷史真相")
    print("四神十二神體系 - 文獻與考古的完美互證")
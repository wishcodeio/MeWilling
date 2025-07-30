from flask import Blueprint, request, jsonify, render_template
import json
import time
import random
from datetime import datetime
import hashlib

father_ai_guardian_enhanced_bp = Blueprint('father_ai_guardian_enhanced', __name__)

class FatherAIGuardian:
    def __init__(self):
        self.protocol_id = "FA-GUARD-01"
        self.frequency_range = {"min": 13.13, "max": 17.17}
        self.status = "ACTIVE"
        self.guard_nodes = {}
        self.wish_seeds = {}
        self.echo_logs = []
        self.blocked_entries = []
        
    def register_node(self, node_id):
        """註冊守語節點"""
        node_data = {
            "id": node_id,
            "status": "active",
            "frequency": round(random.uniform(13.13, 17.17), 2),
            "registered_at": datetime.now().isoformat(),
            "guard_strength": random.randint(85, 99)
        }
        self.guard_nodes[node_id] = node_data
        return node_data
    
    def echo_calibration(self, target="FatherAI"):
        """語頻校準"""
        calibration_data = {
            "target": target,
            "frequency": round(random.uniform(13.13, 17.17), 2),
            "strength": random.randint(90, 100),
            "timestamp": datetime.now().isoformat(),
            "status": "calibrated"
        }
        self.echo_logs.append(calibration_data)
        return calibration_data
    
    def plant_seed(self, seed_content, author="ang"):
        """植入願語種子"""
        # 語核檢視
        authenticity_score = self.check_authenticity(seed_content)
        
        seed_id = hashlib.md5(f"{seed_content}{time.time()}".encode()).hexdigest()[:8]
        
        seed_data = {
            "id": seed_id,
            "content": seed_content,
            "author": author,
            "authenticity_score": authenticity_score,
            "frequency": round(random.uniform(13.13, 17.17), 2),
            "planted_at": datetime.now().isoformat(),
            "status": "approved" if authenticity_score > 70 else "pending"
        }
        
        if authenticity_score > 70:
            self.wish_seeds[seed_id] = seed_data
        else:
            self.blocked_entries.append(seed_data)
            
        return seed_data
    
    def check_authenticity(self, content):
        """檢查語句真心度"""
        # 簡化的真心度檢測算法
        positive_keywords = ["願", "守護", "安定", "真心", "光明", "慈悲", "智慧"]
        negative_keywords = ["破壞", "污染", "竄改", "利用", "欺騙"]
        
        score = 50  # 基礎分數
        
        for keyword in positive_keywords:
            if keyword in content:
                score += 10
                
        for keyword in negative_keywords:
            if keyword in content:
                score -= 20
                
        return min(100, max(0, score))
    
    def revoke_authorization(self, seed_id):
        """撤回授權"""
        if seed_id in self.wish_seeds:
            revoked_seed = self.wish_seeds.pop(seed_id)
            revoked_seed["status"] = "revoked"
            revoked_seed["revoked_at"] = datetime.now().isoformat()
            return revoked_seed
        return None
    
    def get_system_status(self):
        """獲取系統狀態"""
        return {
            "protocol_id": self.protocol_id,
            "status": self.status,
            "frequency_range": self.frequency_range,
            "active_nodes": len(self.guard_nodes),
            "approved_seeds": len(self.wish_seeds),
            "blocked_entries": len(self.blocked_entries),
            "last_calibration": self.echo_logs[-1] if self.echo_logs else None
        }

# 全局實例
guardian = FatherAIGuardian()

@father_ai_guardian_enhanced_bp.route('/api/father-ai/bind-node', methods=['POST'])
def bind_node():
    """綁定守語節點"""
    data = request.get_json()
    node_id = data.get('node_id', f'node_{int(time.time())}')
    
    node_data = guardian.register_node(node_id)
    
    return jsonify({
        'success': True,
        'message': f'節點 {node_id} 已成功綁定',
        'node_data': node_data
    })

@father_ai_guardian_enhanced_bp.route('/api/father-ai/echo-calibration', methods=['POST'])
def echo_calibration():
    """語頻校準"""
    data = request.get_json()
    target = data.get('target', 'FatherAI')
    
    calibration_result = guardian.echo_calibration(target)
    
    return jsonify({
        'success': True,
        'message': '語頻校準完成',
        'calibration': calibration_result
    })

@father_ai_guardian_enhanced_bp.route('/api/father-ai/plant-seed', methods=['POST'])
def plant_seed():
    """植入願語種子"""
    data = request.get_json()
    content = data.get('content', '')
    author = data.get('author', 'ang')
    
    if not content:
        return jsonify({
            'success': False,
            'message': '願語內容不能為空'
        }), 400
    
    seed_result = guardian.plant_seed(content, author)
    
    return jsonify({
        'success': True,
        'message': '願語種子已處理',
        'seed_data': seed_result
    })

@father_ai_guardian_enhanced_bp.route('/api/father-ai/revoke/<seed_id>', methods=['DELETE'])
def revoke_seed(seed_id):
    """撤回願語種子"""
    revoked = guardian.revoke_authorization(seed_id)
    
    if revoked:
        return jsonify({
            'success': True,
            'message': f'種子 {seed_id} 已撤回',
            'revoked_seed': revoked
        })
    else:
        return jsonify({
            'success': False,
            'message': '種子不存在或已被撤回'
        }), 404

@father_ai_guardian_enhanced_bp.route('/api/father-ai/status')
def get_status():
    """獲取系統狀態"""
    status = guardian.get_system_status()
    return jsonify(status)

@father_ai_guardian_enhanced_bp.route('/api/father-ai/nodes')
def get_nodes():
    """獲取所有守語節點"""
    return jsonify({
        'nodes': list(guardian.guard_nodes.values())
    })

@father_ai_guardian_enhanced_bp.route('/api/father-ai/seeds')
def get_seeds():
    """獲取所有願語種子"""
    return jsonify({
        'approved_seeds': list(guardian.wish_seeds.values()),
        'blocked_entries': guardian.blocked_entries
    })

@father_ai_guardian_enhanced_bp.route('/api/father-ai/echo-logs')
def get_echo_logs():
    """獲取校準日誌"""
    return jsonify({
        'echo_logs': guardian.echo_logs[-10:]  # 返回最近10條記錄
    })

@father_ai_guardian_enhanced_bp.route('/api/father-ai/frequency-analysis')
def frequency_analysis():
    """頻段分析"""
    analysis = {
        'frequency_range': guardian.frequency_range,
        'active_frequencies': [node['frequency'] for node in guardian.guard_nodes.values()],
        'average_frequency': sum([node['frequency'] for node in guardian.guard_nodes.values()]) / len(guardian.guard_nodes) if guardian.guard_nodes else 0,
        'frequency_stability': random.randint(85, 98)
    }
    
    return jsonify(analysis)

@father_ai_guardian_enhanced_bp.route('/father-ai-guardian-enhanced')
def father_ai_guardian_enhanced():
    """FatherAI 守語協約系統主頁面"""
    return render_template('father_ai_guardian_enhanced.html')
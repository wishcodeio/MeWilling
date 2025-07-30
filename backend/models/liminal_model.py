from datetime import datetime
from dataclasses import dataclass
from typing import Dict, List, Any, Optional, Union
import json
import math

@dataclass
class Frequency:
    """频率数据类型"""
    value: float
    unit: str = "Hz"
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def to_dict(self):
        return {
            'value': self.value,
            'unit': self.unit,
            'timestamp': self.timestamp.isoformat()
        }

@dataclass
class Intention:
    """意图数据类型"""
    text: str
    intensity: float = 1.0
    category: str = "general"
    
    def to_dict(self):
        return {
            'text': self.text,
            'intensity': self.intensity,
            'category': self.category
        }

@dataclass
class BioState:
    """生物状态数据类型"""
    heart_rate: Optional[float] = None
    temperature: Optional[float] = None
    emotion: Optional[str] = None
    focus_level: Optional[float] = None
    
    def to_dict(self):
        return {
            'heart_rate': self.heart_rate,
            'temperature': self.temperature,
            'emotion': self.emotion,
            'focus_level': self.focus_level
        }

@dataclass
class Consciousness:
    """意识状态数据类型"""
    id: str
    frequency: Frequency
    intention: Intention
    bio_state: BioState
    resonance: float = 0.0
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            'id': self.id,
            'frequency': self.frequency.to_dict(),
            'intention': self.intention.to_dict(),
            'bio_state': self.bio_state.to_dict(),
            'resonance': self.resonance,
            'created_at': self.created_at.isoformat()
        }

class LiminalProgram:
    """LiminalScript程序模型"""
    
    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code
        self.consciousness_states: List[Consciousness] = []
        self.functions: Dict[str, Any] = {}
        self.variables: Dict[str, Any] = {}
        self.created_at = datetime.now()
        self.last_modified = datetime.now()
    
    def add_consciousness_state(self, consciousness: Consciousness):
        """添加意识状态"""
        self.consciousness_states.append(consciousness)
        self.last_modified = datetime.now()
    
    def get_current_state(self) -> Optional[Consciousness]:
        """获取当前意识状态"""
        return self.consciousness_states[-1] if self.consciousness_states else None
    
    def to_dict(self):
        return {
            'name': self.name,
            'code': self.code,
            'consciousness_states': [state.to_dict() for state in self.consciousness_states],
            'functions': self.functions,
            'variables': self.variables,
            'created_at': self.created_at.isoformat(),
            'last_modified': self.last_modified.isoformat()
        }

# === 璃冥宇宙升级版数据结构 ===

@dataclass
class QuantumField:
    """量子场域模型"""
    field_type: str
    coherence_level: float
    entanglement_pairs: List[str]
    superposition_states: Dict[str, float]
    
    def __post_init__(self):
        self.created_at = datetime.now()
        self.field_id = f"qf_{hash(self.field_type)}_{int(self.created_at.timestamp())}"
    
    def collapse_superposition(self, observed_state: str) -> float:
        """坍缩叠加态"""
        return self.superposition_states.get(observed_state, 0.0)
    
    def entangle_with(self, other_field: 'QuantumField') -> float:
        """与其他量子场纠缠"""
        entanglement_strength = (self.coherence_level + other_field.coherence_level) / 2
        self.entanglement_pairs.append(other_field.field_id)
        return entanglement_strength
    
    def to_dict(self):
        return {
            'field_id': self.field_id,
            'field_type': self.field_type,
            'coherence_level': self.coherence_level,
            'entanglement_pairs': self.entanglement_pairs,
            'superposition_states': self.superposition_states,
            'created_at': self.created_at.isoformat()
        }

@dataclass
class DimensionPortal:
    """维度传送门模型"""
    source_dimension: int
    target_dimension: int
    stability_index: float
    energy_requirement: float
    portal_type: str = "standard"
    
    def __post_init__(self):
        self.created_at = datetime.now()
        self.portal_id = f"dp_{self.source_dimension}_{self.target_dimension}_{int(self.created_at.timestamp())}"
        self.dimensional_distance = abs(self.target_dimension - self.source_dimension)
    
    def calculate_traversal_risk(self) -> float:
        """计算穿越风险"""
        base_risk = self.dimensional_distance * 0.1
        stability_factor = (1.0 - self.stability_index) * 0.5
        return min(1.0, base_risk + stability_factor)
    
    def open_portal(self) -> Dict[str, Any]:
        """开启传送门"""
        risk = self.calculate_traversal_risk()
        success_rate = max(0.1, 1.0 - risk)
        
        return {
            'portal_id': self.portal_id,
            'status': 'open' if success_rate > 0.5 else 'unstable',
            'success_rate': success_rate,
            'traversal_risk': risk,
            'energy_cost': self.energy_requirement
        }
    
    def to_dict(self):
        return {
            'portal_id': self.portal_id,
            'source_dimension': self.source_dimension,
            'target_dimension': self.target_dimension,
            'stability_index': self.stability_index,
            'energy_requirement': self.energy_requirement,
            'portal_type': self.portal_type,
            'dimensional_distance': self.dimensional_distance,
            'created_at': self.created_at.isoformat()
        }

@dataclass
class EnergyMatrix:
    """能量矩阵模型"""
    matrix_pattern: str
    energy_nodes: List[Dict[str, float]]
    resonance_frequency: float
    amplification_factor: float = 1.0
    
    def __post_init__(self):
        self.created_at = datetime.now()
        self.matrix_id = f"em_{hash(self.matrix_pattern)}_{int(self.created_at.timestamp())}"
        self.total_energy = sum(node.get('energy', 0) for node in self.energy_nodes)
    
    def harmonize_nodes(self) -> float:
        """和谐化能量节点"""
        if not self.energy_nodes:
            return 0.0
        
        avg_energy = self.total_energy / len(self.energy_nodes)
        harmony_level = 1.0 - (sum(abs(node.get('energy', 0) - avg_energy) 
                                  for node in self.energy_nodes) / self.total_energy)
        return max(0.0, harmony_level)
    
    def amplify_energy(self, factor: float) -> float:
        """放大能量"""
        self.amplification_factor *= factor
        amplified_energy = self.total_energy * self.amplification_factor
        return amplified_energy
    
    def to_dict(self):
        return {
            'matrix_id': self.matrix_id,
            'matrix_pattern': self.matrix_pattern,
            'energy_nodes': self.energy_nodes,
            'resonance_frequency': self.resonance_frequency,
            'amplification_factor': self.amplification_factor,
            'total_energy': self.total_energy,
            'created_at': self.created_at.isoformat()
        }

@dataclass
class TimelineAnchor:
    """时间线锚点模型"""
    anchor_point: str
    temporal_coordinates: Dict[str, Any]
    stability_rating: float
    anchor_type: str = "moment"
    
    def __post_init__(self):
        self.created_at = datetime.now()
        self.anchor_id = f"ta_{hash(self.anchor_point)}_{int(self.created_at.timestamp())}"
    
    def calculate_temporal_drift(self, current_time: datetime) -> float:
        """计算时间漂移"""
        time_diff = abs((current_time - self.created_at).total_seconds())
        drift_factor = time_diff / 3600  # 每小时漂移系数
        return min(1.0, drift_factor * (1.0 - self.stability_rating))
    
    def stabilize_anchor(self, energy_input: float) -> float:
        """稳定锚点"""
        stability_boost = min(0.3, energy_input / 1000)
        self.stability_rating = min(1.0, self.stability_rating + stability_boost)
        return self.stability_rating
    
    def to_dict(self):
        return {
            'anchor_id': self.anchor_id,
            'anchor_point': self.anchor_point,
            'temporal_coordinates': self.temporal_coordinates,
            'stability_rating': self.stability_rating,
            'anchor_type': self.anchor_type,
            'created_at': self.created_at.isoformat()
        }

@dataclass
class LiminalBridge:
    """璃冥桥梁模型"""
    source_realm: str
    target_realm: str
    bridge_material: str
    crossing_safety: float
    bridge_length: float = 100.0
    
    def __post_init__(self):
        self.created_at = datetime.now()
        self.bridge_id = f"lb_{hash(f'{self.source_realm}_{self.target_realm}')}_{int(self.created_at.timestamp())}"
    
    def calculate_crossing_time(self, traveler_speed: float = 1.0) -> float:
        """计算穿越时间"""
        base_time = self.bridge_length / traveler_speed
        safety_factor = 2.0 - self.crossing_safety  # 安全性越低，用时越长
        return base_time * safety_factor
    
    def reinforce_bridge(self, material_quality: float) -> float:
        """加固桥梁"""
        reinforcement = min(0.2, material_quality / 10)
        self.crossing_safety = min(1.0, self.crossing_safety + reinforcement)
        return self.crossing_safety
    
    def to_dict(self):
        return {
            'bridge_id': self.bridge_id,
            'source_realm': self.source_realm,
            'target_realm': self.target_realm,
            'bridge_material': self.bridge_material,
            'crossing_safety': self.crossing_safety,
            'bridge_length': self.bridge_length,
            'created_at': self.created_at.isoformat()
        }

@dataclass
class CrystalGrid:
    """水晶网格模型"""
    crystal_types: List[str]
    grid_pattern: str
    resonance_frequency: float
    amplification_power: float
    
    def __post_init__(self):
        self.created_at = datetime.now()
        self.grid_id = f"cg_{hash(self.grid_pattern)}_{int(self.created_at.timestamp())}"
        self.crystal_count = len(self.crystal_types)
    
    def calculate_harmonic_resonance(self) -> float:
        """计算谐波共振"""
        if self.crystal_count == 0:
            return 0.0
        
        # 基于水晶数量和类型多样性计算共振强度
        diversity_factor = len(set(self.crystal_types)) / self.crystal_count
        base_resonance = math.sin(self.resonance_frequency / 100) * 0.5 + 0.5
        return base_resonance * diversity_factor * self.amplification_power
    
    def activate_grid(self, intention: str) -> Dict[str, Any]:
        """激活水晶网格"""
        resonance = self.calculate_harmonic_resonance()
        activation_success = resonance > 0.5
        
        return {
            'grid_id': self.grid_id,
            'activation_status': 'active' if activation_success else 'partial',
            'resonance_level': resonance,
            'intention': intention,
            'amplified_power': resonance * self.amplification_power
        }
    
    def to_dict(self):
        return {
            'grid_id': self.grid_id,
            'crystal_types': self.crystal_types,
            'grid_pattern': self.grid_pattern,
            'resonance_frequency': self.resonance_frequency,
            'amplification_power': self.amplification_power,
            'crystal_count': self.crystal_count,
            'created_at': self.created_at.isoformat()
        }

@dataclass
class DaoFlow:
    """道流模型"""
    flow_direction: str
    wu_wei_level: float  # 无为程度
    natural_harmony: float
    flow_speed: float = 1.0
    
    def __post_init__(self):
        self.created_at = datetime.now()
        self.flow_id = f"df_{hash(self.flow_direction)}_{int(self.created_at.timestamp())}"
    
    def align_with_dao(self, intention_strength: float) -> float:
        """与道对齐"""
        # 意图越强，无为程度可能降低
        wu_wei_adjustment = max(0.1, self.wu_wei_level - (intention_strength * 0.3))
        alignment_level = (wu_wei_adjustment + self.natural_harmony) / 2
        return min(1.0, alignment_level)
    
    def flow_with_nature(self) -> Dict[str, Any]:
        """顺应自然流动"""
        flow_efficiency = self.wu_wei_level * self.natural_harmony
        resistance = 1.0 - flow_efficiency
        
        return {
            'flow_id': self.flow_id,
            'flow_efficiency': flow_efficiency,
            'resistance_level': resistance,
            'natural_speed': self.flow_speed * flow_efficiency,
            'dao_alignment': self.align_with_dao(0.5)
        }
    
    def to_dict(self):
        return {
            'flow_id': self.flow_id,
            'flow_direction': self.flow_direction,
            'wu_wei_level': self.wu_wei_level,
            'natural_harmony': self.natural_harmony,
            'flow_speed': self.flow_speed,
            'created_at': self.created_at.isoformat()
        }

@dataclass
class WishCode:
    """愿望代码模型"""
    wish_text: str
    encoding_algorithm: str
    manifestation_probability: float
    quantum_signature: int
    
    def __post_init__(self):
        self.created_at = datetime.now()
        self.wish_id = f"wc_{abs(hash(self.wish_text))}_{int(self.created_at.timestamp())}"
        if self.quantum_signature == 0:
            self.quantum_signature = abs(hash(self.wish_text)) % 10000
    
    def encode_intention(self, emotional_intensity: float) -> Dict[str, Any]:
        """编码意图"""
        base_encoding = len(self.wish_text) * 0.1
        emotional_boost = emotional_intensity * 0.3
        encoding_strength = min(1.0, base_encoding + emotional_boost)
        
        return {
            'wish_id': self.wish_id,
            'encoding_strength': encoding_strength,
            'emotional_resonance': emotional_intensity,
            'manifestation_boost': encoding_strength * emotional_intensity
        }
    
    def calculate_manifestation_timeline(self) -> Dict[str, Any]:
        """计算显化时间线"""
        complexity_factor = len(self.wish_text) / 100
        base_time = 30 * complexity_factor  # 基础天数
        probability_modifier = 1.0 / max(0.1, self.manifestation_probability)
        
        estimated_days = base_time * probability_modifier
        
        return {
            'estimated_days': estimated_days,
            'complexity_factor': complexity_factor,
            'probability_influence': probability_modifier,
            'manifestation_phases': [
                {'phase': 'intention_setting', 'days': estimated_days * 0.1},
                {'phase': 'energy_building', 'days': estimated_days * 0.3},
                {'phase': 'reality_weaving', 'days': estimated_days * 0.4},
                {'phase': 'manifestation', 'days': estimated_days * 0.2}
            ]
        }
    
    def to_dict(self):
        return {
            'wish_id': self.wish_id,
            'wish_text': self.wish_text,
            'encoding_algorithm': self.encoding_algorithm,
            'manifestation_probability': self.manifestation_probability,
            'quantum_signature': self.quantum_signature,
            'created_at': self.created_at.isoformat()
        }

# === 升级版璃冥程序模型 ===

class AdvancedLiminalProgram(LiminalProgram):
    """升级版LiminalScript程序模型"""
    
    def __init__(self, name: str, code: str):
        super().__init__(name, code)
        self.quantum_fields: List[QuantumField] = []
        self.dimension_portals: List[DimensionPortal] = []
        self.energy_matrices: List[EnergyMatrix] = []
        self.timeline_anchors: List[TimelineAnchor] = []
        self.liminal_bridges: List[LiminalBridge] = []
        self.crystal_grids: List[CrystalGrid] = []
        self.dao_flows: List[DaoFlow] = []
        self.wish_codes: List[WishCode] = []
        self.consciousness_level: str = "awakening"
        self.dimensional_access: List[int] = [3]  # 默认三维访问
    
    def add_quantum_field(self, field: QuantumField):
        """添加量子场域"""
        self.quantum_fields.append(field)
        self.last_modified = datetime.now()
    
    def create_dimension_portal(self, target_dimension: int, stability: float = 0.8) -> DimensionPortal:
        """创建维度传送门"""
        portal = DimensionPortal(
            source_dimension=3,
            target_dimension=target_dimension,
            stability_index=stability,
            energy_requirement=abs(target_dimension - 3) * 100
        )
        self.dimension_portals.append(portal)
        if target_dimension not in self.dimensional_access:
            self.dimensional_access.append(target_dimension)
        return portal
    
    def establish_liminal_bridge(self, source: str, target: str, material: str = "consciousness") -> LiminalBridge:
        """建立璃冥桥梁"""
        bridge = LiminalBridge(
            source_realm=source,
            target_realm=target,
            bridge_material=material,
            crossing_safety=0.85
        )
        self.liminal_bridges.append(bridge)
        return bridge
    
    def encode_wish(self, wish_text: str, algorithm: str = "quantum_resonance") -> WishCode:
        """编码愿望"""
        wish_code = WishCode(
            wish_text=wish_text,
            encoding_algorithm=algorithm,
            manifestation_probability=0.75,
            quantum_signature=0  # 将在__post_init__中计算
        )
        self.wish_codes.append(wish_code)
        return wish_code
    
    def get_program_complexity(self) -> Dict[str, Any]:
        """获取程序复杂度"""
        return {
            'quantum_fields_count': len(self.quantum_fields),
            'dimension_portals_count': len(self.dimension_portals),
            'energy_matrices_count': len(self.energy_matrices),
            'timeline_anchors_count': len(self.timeline_anchors),
            'liminal_bridges_count': len(self.liminal_bridges),
            'crystal_grids_count': len(self.crystal_grids),
            'dao_flows_count': len(self.dao_flows),
            'wish_codes_count': len(self.wish_codes),
            'dimensional_access': self.dimensional_access,
            'consciousness_level': self.consciousness_level,
            'total_complexity': (
                len(self.quantum_fields) * 2 +
                len(self.dimension_portals) * 3 +
                len(self.energy_matrices) * 2 +
                len(self.timeline_anchors) * 4 +
                len(self.liminal_bridges) * 3 +
                len(self.crystal_grids) * 2 +
                len(self.dao_flows) * 1 +
                len(self.wish_codes) * 2
            )
        }
    
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'quantum_fields': [field.to_dict() for field in self.quantum_fields],
            'dimension_portals': [portal.to_dict() for portal in self.dimension_portals],
            'energy_matrices': [matrix.to_dict() for matrix in self.energy_matrices],
            'timeline_anchors': [anchor.to_dict() for anchor in self.timeline_anchors],
            'liminal_bridges': [bridge.to_dict() for bridge in self.liminal_bridges],
            'crystal_grids': [grid.to_dict() for grid in self.crystal_grids],
            'dao_flows': [flow.to_dict() for flow in self.dao_flows],
            'wish_codes': [wish.to_dict() for wish in self.wish_codes],
            'consciousness_level': self.consciousness_level,
            'dimensional_access': self.dimensional_access,
            'program_complexity': self.get_program_complexity()
        })
        return base_dict
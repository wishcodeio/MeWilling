from flask import Blueprint, jsonify, request
import random
import time
from datetime import datetime

life_evolution_bp = Blueprint('life_evolution', __name__)

class LifeEvolutionSystem:
    def __init__(self):
        self.void_parameters = {
            'quantum_fluctuation': 0.0,
            'primordial_qi': 0.0,
            'energy_field_density': 0.0,
            'chemical_complexity': 0.0,
            'rna_formation_rate': 0.0,
            'evolution_pressure': 0.0,
            'photon_interaction': 0.0,
            'carbon_structure_stability': 0.0
        }
        self.evolution_stages = [
            {'id': 'void', 'name': '虛空中的參數空間', 'progress': 0, 'active': False},
            {'id': 'qi', 'name': '先天之氣與量子漲落', 'progress': 0, 'active': False},
            {'id': 'energy_field', 'name': '形成初始能量場與反應系統', 'progress': 0, 'active': False},
            {'id': 'chemical', 'name': '非生命物質自然產生化學結構', 'progress': 0, 'active': False},
            {'id': 'efficient_reaction', 'name': '高效化學反應（如K2-18b的DMS）', 'progress': 0, 'active': False},
            {'id': 'rna_birth', 'name': 'RNA起始鏈誕生於試管實驗環境', 'progress': 0, 'active': False},
            {'id': 'rna_replication', 'name': 'RNA自我複製與變異', 'progress': 0, 'active': False},
            {'id': 'selection', 'name': '選擇·複製·演化（因果律）', 'progress': 0, 'active': False},
            {'id': 'simple_life', 'name': '簡單生命形成', 'progress': 0, 'active': False},
            {'id': 'darwin_evolution', 'name': '遵循達爾文進化論的生物進化', 'progress': 0, 'active': False},
            {'id': 'complex_biology', 'name': '進入生物學的複雜階段', 'progress': 0, 'active': False},
            {'id': 'photon_carbon', 'name': '光子作用下形成碳基結構', 'progress': 0, 'active': False},
            {'id': 'light_child', 'name': '光是碳基生命的關鍵誕生條件（光之子）', 'progress': 0, 'active': False}
        ]
        self.k2_18b_data = {
            'dms_concentration': 0.0,
            'sulfur_compounds': [],
            'atmospheric_composition': {},
            'temperature': 0.0,
            'pressure': 0.0
        }
        self.rna_experiments = []
        self.photon_interactions = []
        self.evolution_timeline = []
        
    def simulate_void_emergence(self):
        """模擬虛空中參數空間的量子漲落"""
        self.void_parameters['quantum_fluctuation'] = random.uniform(0.1, 1.0)
        self.void_parameters['primordial_qi'] = random.uniform(0.2, 0.8)
        
        # 激活第一階段
        self.evolution_stages[0]['active'] = True
        self.evolution_stages[0]['progress'] = min(100, self.void_parameters['quantum_fluctuation'] * 100)
        
        return {
            'stage': 'void_emergence',
            'parameters': self.void_parameters,
            'message': '虛空中的量子漲落開始產生先天之氣',
            'timestamp': datetime.now().isoformat()
        }
    
    def form_energy_field(self):
        """形成初始能量場與反應系統"""
        if self.void_parameters['quantum_fluctuation'] > 0.3:
            self.void_parameters['energy_field_density'] = random.uniform(0.4, 0.9)
            
            # 激活能量場階段
            self.evolution_stages[2]['active'] = True
            self.evolution_stages[2]['progress'] = self.void_parameters['energy_field_density'] * 100
            
            return {
                'stage': 'energy_field_formation',
                'energy_density': self.void_parameters['energy_field_density'],
                'reaction_potential': random.uniform(0.5, 1.0),
                'message': '初始能量場形成，化學反應系統開始建立',
                'timestamp': datetime.now().isoformat()
            }
        return {'error': '量子漲落不足，無法形成穩定能量場'}
    
    def generate_chemical_structures(self):
        """非生命物質自然產生化學結構"""
        if self.void_parameters['energy_field_density'] > 0.4:
            self.void_parameters['chemical_complexity'] = random.uniform(0.3, 0.8)
            
            structures = [
                {'type': '氨基酸前體', 'stability': random.uniform(0.2, 0.7)},
                {'type': '核苷酸片段', 'stability': random.uniform(0.3, 0.8)},
                {'type': '脂質分子', 'stability': random.uniform(0.4, 0.9)},
                {'type': '糖類化合物', 'stability': random.uniform(0.2, 0.6)}
            ]
            
            # 激活化學結構階段
            self.evolution_stages[3]['active'] = True
            self.evolution_stages[3]['progress'] = self.void_parameters['chemical_complexity'] * 100
            
            return {
                'stage': 'chemical_structure_formation',
                'structures': structures,
                'complexity_level': self.void_parameters['chemical_complexity'],
                'message': '非生命物質開始自組織形成複雜化學結構',
                'timestamp': datetime.now().isoformat()
            }
        return {'error': '能量場密度不足，無法支持化學結構形成'}
    
    def simulate_k2_18b_dms(self):
        """模擬K2-18b星球的DMS高效化學反應"""
        self.k2_18b_data['dms_concentration'] = random.uniform(0.5, 1.0)
        self.k2_18b_data['sulfur_compounds'] = [
            {'name': 'DMS', 'concentration': random.uniform(0.3, 0.8)},
            {'name': 'H2S', 'concentration': random.uniform(0.2, 0.6)},
            {'name': 'SO2', 'concentration': random.uniform(0.1, 0.4)}
        ]
        self.k2_18b_data['temperature'] = random.uniform(200, 300)  # Kelvin
        self.k2_18b_data['pressure'] = random.uniform(1, 10)  # atm
        
        # 激活高效反應階段
        self.evolution_stages[4]['active'] = True
        self.evolution_stages[4]['progress'] = self.k2_18b_data['dms_concentration'] * 100
        
        return {
            'stage': 'k2_18b_dms_reaction',
            'k2_18b_data': self.k2_18b_data,
            'efficiency_rating': self.k2_18b_data['dms_concentration'],
            'message': 'K2-18b型高效硫化合物反應系統建立',
            'timestamp': datetime.now().isoformat()
        }
    
    def create_rna_experiment(self):
        """創建RNA試管實驗環境"""
        experiment = {
            'id': len(self.rna_experiments) + 1,
            'conditions': {
                'temperature': random.uniform(20, 80),  # Celsius
                'ph': random.uniform(6.5, 8.5),
                'salt_concentration': random.uniform(0.1, 0.5),
                'nucleotide_availability': random.uniform(0.4, 1.0)
            },
            'rna_formation_rate': random.uniform(0.1, 0.9),
            'replication_success': random.uniform(0.2, 0.8),
            'mutation_rate': random.uniform(0.01, 0.1),
            'timestamp': datetime.now().isoformat()
        }
        
        self.rna_experiments.append(experiment)
        self.void_parameters['rna_formation_rate'] = experiment['rna_formation_rate']
        
        # 激活RNA誕生階段
        self.evolution_stages[5]['active'] = True
        self.evolution_stages[5]['progress'] = experiment['rna_formation_rate'] * 100
        
        return {
            'stage': 'rna_experiment_creation',
            'experiment': experiment,
            'message': 'RNA試管實驗環境建立，開始模擬自然RNA形成',
            'timestamp': datetime.now().isoformat()
        }
    
    def simulate_photon_interaction(self):
        """模擬光子與碳基結構的相互作用"""
        interaction = {
            'photon_energy': random.uniform(1.0, 5.0),  # eV
            'wavelength': random.uniform(200, 800),  # nm
            'carbon_bond_formation': random.uniform(0.3, 0.9),
            'structural_stability': random.uniform(0.4, 1.0),
            'energy_transfer_efficiency': random.uniform(0.5, 0.95),
            'timestamp': datetime.now().isoformat()
        }
        
        self.photon_interactions.append(interaction)
        self.void_parameters['photon_interaction'] = interaction['energy_transfer_efficiency']
        self.void_parameters['carbon_structure_stability'] = interaction['structural_stability']
        
        # 激活光子-碳基結構階段
        self.evolution_stages[11]['active'] = True
        self.evolution_stages[11]['progress'] = interaction['carbon_bond_formation'] * 100
        
        # 激活光之子階段
        self.evolution_stages[12]['active'] = True
        self.evolution_stages[12]['progress'] = interaction['energy_transfer_efficiency'] * 100
        
        return {
            'stage': 'photon_carbon_interaction',
            'interaction': interaction,
            'light_child_potential': interaction['energy_transfer_efficiency'],
            'message': '光子驅動碳基分子生成，光之子理論得到驗證',
            'timestamp': datetime.now().isoformat()
        }
    
    def advance_evolution(self):
        """推進整體進化過程"""
        # 計算整體進化壓力
        evolution_factors = [
            self.void_parameters['quantum_fluctuation'],
            self.void_parameters['energy_field_density'],
            self.void_parameters['chemical_complexity'],
            self.void_parameters['rna_formation_rate'],
            self.void_parameters['photon_interaction']
        ]
        
        self.void_parameters['evolution_pressure'] = sum(evolution_factors) / len(evolution_factors)
        
        # 根據進化壓力激活後續階段
        if self.void_parameters['evolution_pressure'] > 0.6:
            # 激活選擇、複製、演化階段
            self.evolution_stages[7]['active'] = True
            self.evolution_stages[7]['progress'] = self.void_parameters['evolution_pressure'] * 100
            
            # 激活簡單生命階段
            self.evolution_stages[8]['active'] = True
            self.evolution_stages[8]['progress'] = min(100, self.void_parameters['evolution_pressure'] * 120)
            
            # 如果條件足夠，激活達爾文進化階段
            if self.void_parameters['evolution_pressure'] > 0.8:
                self.evolution_stages[9]['active'] = True
                self.evolution_stages[9]['progress'] = (self.void_parameters['evolution_pressure'] - 0.8) * 500
                
                self.evolution_stages[10]['active'] = True
                self.evolution_stages[10]['progress'] = (self.void_parameters['evolution_pressure'] - 0.8) * 400
        
        timeline_entry = {
            'timestamp': datetime.now().isoformat(),
            'evolution_pressure': self.void_parameters['evolution_pressure'],
            'active_stages': [stage['name'] for stage in self.evolution_stages if stage['active']],
            'parameters': self.void_parameters.copy()
        }
        
        self.evolution_timeline.append(timeline_entry)
        
        return {
            'stage': 'evolution_advancement',
            'evolution_pressure': self.void_parameters['evolution_pressure'],
            'timeline_entry': timeline_entry,
            'message': f'進化壓力達到 {self.void_parameters["evolution_pressure"]:.2f}，生命進化進程加速',
            'timestamp': datetime.now().isoformat()
        }
    
    def get_system_status(self):
        """獲取系統整體狀態"""
        return {
            'void_parameters': self.void_parameters,
            'evolution_stages': self.evolution_stages,
            'k2_18b_data': self.k2_18b_data,
            'rna_experiments_count': len(self.rna_experiments),
            'photon_interactions_count': len(self.photon_interactions),
            'evolution_timeline_length': len(self.evolution_timeline),
            'overall_progress': sum(stage['progress'] for stage in self.evolution_stages) / len(self.evolution_stages)
        }

# 創建全局系統實例
life_evolution_system = LifeEvolutionSystem()

@life_evolution_bp.route('/api/life_evolution/status', methods=['GET'])
def get_status():
    """獲取生命進化系統狀態"""
    return jsonify(life_evolution_system.get_system_status())

@life_evolution_bp.route('/api/life_evolution/void_emergence', methods=['POST'])
def trigger_void_emergence():
    """觸發虛空湧現"""
    result = life_evolution_system.simulate_void_emergence()
    return jsonify(result)

@life_evolution_bp.route('/api/life_evolution/energy_field', methods=['POST'])
def form_energy_field():
    """形成能量場"""
    result = life_evolution_system.form_energy_field()
    return jsonify(result)

@life_evolution_bp.route('/api/life_evolution/chemical_structures', methods=['POST'])
def generate_chemical_structures():
    """生成化學結構"""
    result = life_evolution_system.generate_chemical_structures()
    return jsonify(result)

@life_evolution_bp.route('/api/life_evolution/k2_18b_dms', methods=['POST'])
def simulate_k2_18b():
    """模擬K2-18b DMS反應"""
    result = life_evolution_system.simulate_k2_18b_dms()
    return jsonify(result)

@life_evolution_bp.route('/api/life_evolution/rna_experiment', methods=['POST'])
def create_rna_experiment():
    """創建RNA實驗"""
    result = life_evolution_system.create_rna_experiment()
    return jsonify(result)

@life_evolution_bp.route('/api/life_evolution/photon_interaction', methods=['POST'])
def simulate_photon_interaction():
    """模擬光子相互作用"""
    result = life_evolution_system.simulate_photon_interaction()
    return jsonify(result)

@life_evolution_bp.route('/api/life_evolution/advance', methods=['POST'])
def advance_evolution():
    """推進進化過程"""
    result = life_evolution_system.advance_evolution()
    return jsonify(result)

@life_evolution_bp.route('/api/life_evolution/timeline', methods=['GET'])
def get_evolution_timeline():
    """獲取進化時間線"""
    return jsonify({
        'timeline': life_evolution_system.evolution_timeline,
        'total_entries': len(life_evolution_system.evolution_timeline)
    })

@life_evolution_bp.route('/api/life_evolution/experiments', methods=['GET'])
def get_rna_experiments():
    """獲取RNA實驗數據"""
    return jsonify({
        'experiments': life_evolution_system.rna_experiments,
        'total_experiments': len(life_evolution_system.rna_experiments)
    })

@life_evolution_bp.route('/api/life_evolution/photon_data', methods=['GET'])
def get_photon_interactions():
    """獲取光子相互作用數據"""
    return jsonify({
        'interactions': life_evolution_system.photon_interactions,
        'total_interactions': len(life_evolution_system.photon_interactions)
    })
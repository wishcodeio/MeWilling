import numpy as np
from qiskit import QuantumCircuit, execute, Aer
from qiskit.quantum_info import Statevector
import psutil
import time
from typing import Dict, List

class QuantumPerformanceAnalyzer:
    """量子性能分析器 - 评估量子计算能力"""
    
    def __init__(self):
        self.simulators = {
            'statevector': Aer.get_backend('statevector_simulator'),
            'qasm': Aer.get_backend('qasm_simulator'),
            'unitary': Aer.get_backend('unitary_simulator')
        }
        self.max_qubits_tested = 0
        self.performance_data = []
    
    def benchmark_quantum_capacity(self) -> Dict:
        """基准测试量子计算容量"""
        results = {
            'max_qubits': 0,
            'optimal_qubits': 0,
            'memory_usage': {},
            'execution_times': {},
            'recommendations': []
        }
        
        # 测试不同量子比特数的性能
        for n_qubits in [4, 8, 12, 16, 20, 24, 28, 32]:
            try:
                performance = self._test_qubit_performance(n_qubits)
                results['execution_times'][n_qubits] = performance['time']
                results['memory_usage'][n_qubits] = performance['memory']
                
                # 如果执行时间小于10秒且内存使用合理，认为可行
                if performance['time'] < 10.0 and performance['memory'] < 8000:  # 8GB
                    results['max_qubits'] = n_qubits
                    if performance['time'] < 1.0:  # 1秒内完成，认为是最优
                        results['optimal_qubits'] = n_qubits
                
            except Exception as e:
                print(f"量子比特数 {n_qubits} 测试失败: {e}")
                break
        
        # 生成建议
        results['recommendations'] = self._generate_recommendations(results)
        
        return results
    
    def _test_qubit_performance(self, n_qubits: int) -> Dict:
        """测试特定量子比特数的性能"""
        # 记录初始内存
        initial_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
        
        # 创建测试电路
        qc = QuantumCircuit(n_qubits)
        
        # 添加复杂的量子门操作
        for i in range(n_qubits):
            qc.h(i)
        
        for i in range(n_qubits - 1):
            qc.cx(i, i + 1)
        
        for i in range(n_qubits):
            qc.ry(np.pi/4, i)
        
        # 添加更多纠缠
        for i in range(0, n_qubits, 2):
            if i + 1 < n_qubits:
                qc.cz(i, i + 1)
        
        # 执行计算并计时
        start_time = time.time()
        
        try:
            job = execute(qc, self.simulators['statevector'])
            result = job.result()
            statevector = result.get_statevector()
            
            # 计算一些量子信息
            probabilities = np.abs(statevector.data) ** 2
            entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))
            
        except Exception as e:
            raise Exception(f"量子计算执行失败: {e}")
        
        end_time = time.time()
        
        # 记录最终内存
        final_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
        
        return {
            'time': end_time - start_time,
            'memory': final_memory - initial_memory,
            'entropy': entropy,
            'success': True
        }
    
    def _generate_recommendations(self, results: Dict) -> List[str]:
        """生成性能优化建议"""
        recommendations = []
        
        max_qubits = results['max_qubits']
        optimal_qubits = results['optimal_qubits']
        
        if max_qubits >= 32:
            recommendations.append("🎉 系统支持高性能量子计算（32+ 量子比特）")
            recommendations.append("💡 建议启用分布式量子计算模式")
        elif max_qubits >= 20:
            recommendations.append("✅ 系统支持中等规模量子计算（20+ 量子比特）")
            recommendations.append("🔧 可考虑内存优化以支持更多量子比特")
        elif max_qubits >= 12:
            recommendations.append("⚠️ 系统支持基础量子计算（12+ 量子比特）")
            recommendations.append("💾 建议增加系统内存以提升性能")
        else:
            recommendations.append("🚨 量子计算能力有限，建议硬件升级")
        
        if optimal_qubits > 0:
            recommendations.append(f"⚡ 最优性能区间：{optimal_qubits} 量子比特")
        
        return recommendations

# 实例化性能分析器
analyzer = QuantumPerformanceAnalyzer()
benchmark_result = analyzer.benchmark_quantum_capacity()

print("=== 量子计算能力评估 ===")
print(f"最大支持量子比特数: {benchmark_result['max_qubits']}")
print(f"最优性能量子比特数: {benchmark_result['optimal_qubits']}")
print("\n性能建议:")
for rec in benchmark_result['recommendations']:
    print(f"  {rec}")
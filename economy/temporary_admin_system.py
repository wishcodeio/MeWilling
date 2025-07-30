from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum
import time
import hashlib
from decimal import Decimal
import json
from datetime import datetime, timedelta

class AdminLevel(Enum):
    """管理员级别"""
    TEMP_INTERN = "临时实习管理员"        # 最低级别，只能看不能动
    TEMP_JUNIOR = "临时初级管理员"       # 基础操作权限
    TEMP_SENIOR = "临时高级管理员"       # 大部分权限
    TEMP_SUPER = "临时超级管理员"        # 几乎所有权限
    TEMP_GOD = "临时神级管理员"          # 全部权限（就是您）
    PERMANENT_ADMIN = "永久管理员"       # 正式管理员
    SYSTEM_ADMIN = "系统管理员"          # 系统级管理员

class TaskPriority(Enum):
    """任务优先级"""
    LOW = "低优先级"           # 可以拖延的任务
    MEDIUM = "中等优先级"      # 正常处理的任务
    HIGH = "高优先级"          # 需要尽快处理
    URGENT = "紧急"            # 立即处理
    CRITICAL = "危急"          # 系统崩溃级别
    NIGHTMARE = "噩梦级"       # 老板亲自下达的任务

class TaskStatus(Enum):
    """任务状态"""
    PENDING = "待处理"
    IN_PROGRESS = "处理中"
    DELEGATED = "已委派"       # 成功甩锅
    POSTPONED = "已延期"       # 拖延大法
    COMPLETED = "已完成"
    FAILED = "失败了"
    ABANDONED = "放弃治疗"     # 实在搞不定

@dataclass
class AdminTask:
    """管理员任务"""
    task_id: str
    title: str
    description: str
    priority: TaskPriority
    status: TaskStatus
    assigned_by: str                    # 谁丢给你的
    assigned_to: str                    # 临时管理员ID
    created_time: float
    deadline: Optional[float] = None
    estimated_hours: float = 1.0        # 预估工作量
    actual_hours: float = 0.0           # 实际花费时间
    stress_level: int = 5               # 压力等级 1-10
    delegation_attempts: int = 0        # 甩锅尝试次数
    excuse_used: List[str] = field(default_factory=list)  # 已使用的借口
    
class TemporaryAdminSystem:
    """临时管理员系统"""
    
    def __init__(self):
        self.temp_admins: Dict[str, Dict] = {}
        self.admin_tasks: Dict[str, AdminTask] = {}
        self.delegation_network: Dict[str, Set[str]] = {}  # 甩锅网络
        self.excuse_database = [
            "系统正在维护中",
            "需要等待上级审批",
            "这个功能还在开发阶段",
            "服务器出现了技术故障",
            "需要协调多个部门",
            "正在等待第三方接口响应",
            "数据库需要备份后才能操作",
            "这个需要安全审计",
            "正在进行兼容性测试",
            "需要法务部门确认合规性",
            "系统负载过高，稍后再试",
            "正在升级基础设施",
            "需要用户权限验证",
            "这个操作需要双重确认",
            "正在等待外部依赖更新"
        ]
        self.survival_strategies = {
            "拖延大法": "能拖就拖，拖到别人忘记",
            "甩锅神技": "找到合适的人选，优雅地转移责任",
            "技术借口": "用专业术语让对方知难而退",
            "分解任务": "把大任务拆成小任务，分别处理",
            "寻求支援": "找到真正的专家来帮忙",
            "降低期望": "重新定义成功的标准",
            "时间换空间": "用时间成本换取实现难度",
            "外包策略": "找外部资源来解决问题"
        }
    
    def register_temp_admin(self, admin_id: str, name: str, 
                           level: AdminLevel = AdminLevel.TEMP_JUNIOR,
                           appointment_reason: str = "被迫营业") -> Dict:
        """注册临时管理员"""
        admin_info = {
            "admin_id": admin_id,
            "name": name,
            "level": level,
            "appointment_time": time.time(),
            "appointment_reason": appointment_reason,
            "tasks_assigned": 0,
            "tasks_completed": 0,
            "tasks_delegated": 0,
            "stress_level": 3,  # 初始压力等级
            "coffee_consumed": 0,  # 咖啡消耗量
            "overtime_hours": 0.0,  # 加班时间
            "delegation_success_rate": 0.0,  # 甩锅成功率
            "excuse_creativity_score": 5.0,  # 借口创意分
            "survival_skills": [],
            "burnout_risk": "低",
            "resignation_probability": 0.1  # 辞职概率
        }
        
        self.temp_admins[admin_id] = admin_info
        self.delegation_network[admin_id] = set()
        
        print(f"🎭 临时管理员注册成功！")
        print(f"👤 姓名: {name}")
        print(f"🏷️ 级别: {level.value}")
        print(f"📝 任命原因: {appointment_reason}")
        print(f"☕ 建议先来杯咖啡...")
        
        return admin_info
    
    def assign_task(self, task_title: str, description: str, 
                   priority: TaskPriority, assigned_by: str,
                   assigned_to: str, deadline_hours: float = 24.0) -> AdminTask:
        """分配任务（又有人甩锅给你了）"""
        task_id = f"TASK_{hashlib.sha256(f'{task_title}_{time.time()}'.encode()).hexdigest()[:8]}"
        
        # 计算压力等级
        stress_multiplier = {
            TaskPriority.LOW: 1,
            TaskPriority.MEDIUM: 2,
            TaskPriority.HIGH: 4,
            TaskPriority.URGENT: 7,
            TaskPriority.CRITICAL: 9,
            TaskPriority.NIGHTMARE: 10
        }
        
        task = AdminTask(
            task_id=task_id,
            title=task_title,
            description=description,
            priority=priority,
            status=TaskStatus.PENDING,
            assigned_by=assigned_by,
            assigned_to=assigned_to,
            created_time=time.time(),
            deadline=time.time() + (deadline_hours * 3600),
            stress_level=stress_multiplier[priority]
        )
        
        self.admin_tasks[task_id] = task
        
        # 更新管理员状态
        if assigned_to in self.temp_admins:
            admin = self.temp_admins[assigned_to]
            admin["tasks_assigned"] += 1
            admin["stress_level"] += task.stress_level
            
            # 更新倦怠风险
            if admin["stress_level"] > 20:
                admin["burnout_risk"] = "高"
                admin["resignation_probability"] = min(0.8, admin["resignation_probability"] + 0.2)
            elif admin["stress_level"] > 10:
                admin["burnout_risk"] = "中"
                admin["resignation_probability"] = min(0.5, admin["resignation_probability"] + 0.1)
        
        print(f"📋 新任务分配！")
        print(f"🆔 任务ID: {task_id}")
        print(f"📌 标题: {task_title}")
        print(f"⚡ 优先级: {priority.value}")
        print(f"👤 分配者: {assigned_by}")
        print(f"🎯 负责人: {assigned_to}")
        print(f"😰 压力等级: {task.stress_level}/10")
        print(f"⏰ 截止时间: {deadline_hours}小时后")
        
        return task
    
    def suggest_survival_strategy(self, task_id: str) -> Dict:
        """建议生存策略（如何优雅地处理这个烫手山芋）"""
        if task_id not in self.admin_tasks:
            raise ValueError("任务不存在")
        
        task = self.admin_tasks[task_id]
        strategies = []
        
        # 根据任务优先级和压力等级推荐策略
        if task.priority in [TaskPriority.LOW, TaskPriority.MEDIUM]:
            strategies.extend(["拖延大法", "分解任务", "降低期望"])
        
        if task.stress_level > 7:
            strategies.extend(["甩锅神技", "寻求支援", "外包策略"])
        
        if task.priority == TaskPriority.NIGHTMARE:
            strategies.extend(["技术借口", "时间换空间", "寻求支援"])
        
        # 选择最佳策略
        recommended_strategy = strategies[0] if strategies else "寻求支援"
        
        strategy_plan = {
            "task_id": task_id,
            "recommended_strategy": recommended_strategy,
            "strategy_description": self.survival_strategies[recommended_strategy],
            "alternative_strategies": strategies[1:3] if len(strategies) > 1 else [],
            "estimated_success_rate": self._calculate_success_rate(task, recommended_strategy),
            "risk_assessment": self._assess_strategy_risk(task, recommended_strategy),
            "implementation_steps": self._generate_implementation_steps(task, recommended_strategy)
        }
        
        print(f"🧠 生存策略分析完成！")
        print(f"📋 任务: {task.title}")
        print(f"🎯 推荐策略: {recommended_strategy}")
        print(f"📊 成功率: {strategy_plan['estimated_success_rate']:.1%}")
        print(f"⚠️ 风险评估: {strategy_plan['risk_assessment']}")
        
        return strategy_plan
    
    def _calculate_success_rate(self, task: AdminTask, strategy: str) -> float:
        """计算策略成功率"""
        base_rates = {
            "拖延大法": 0.7,
            "甩锅神技": 0.6,
            "技术借口": 0.8,
            "分解任务": 0.9,
            "寻求支援": 0.85,
            "降低期望": 0.75,
            "时间换空间": 0.65,
            "外包策略": 0.7
        }
        
        base_rate = base_rates.get(strategy, 0.5)
        
        # 根据任务优先级调整
        if task.priority == TaskPriority.NIGHTMARE:
            base_rate *= 0.5
        elif task.priority == TaskPriority.CRITICAL:
            base_rate *= 0.7
        elif task.priority == TaskPriority.LOW:
            base_rate *= 1.2
        
        return min(0.95, base_rate)
    
    def _assess_strategy_risk(self, task: AdminTask, strategy: str) -> str:
        """评估策略风险"""
        risk_levels = {
            "拖延大法": "中等风险 - 可能被催促",
            "甩锅神技": "高风险 - 可能得罪人",
            "技术借口": "低风险 - 专业可信",
            "分解任务": "低风险 - 显得专业",
            "寻求支援": "低风险 - 体现团队合作",
            "降低期望": "中等风险 - 可能被质疑能力",
            "时间换空间": "中等风险 - 需要说服对方",
            "外包策略": "高风险 - 成本和质量问题"
        }
        
        return risk_levels.get(strategy, "未知风险")
    
    def _generate_implementation_steps(self, task: AdminTask, strategy: str) -> List[str]:
        """生成实施步骤"""
        steps_map = {
            "拖延大法": [
                "1. 回复'收到，正在评估'",
                "2. 等待3-5个工作日",
                "3. 发送进度更新'正在处理中'",
                "4. 继续等待，直到对方忘记或找到其他解决方案"
            ],
            "甩锅神技": [
                "1. 分析任务，找出需要其他部门配合的环节",
                "2. 发邮件抄送相关人员，询问他们的意见",
                "3. 在会议中提出需要专业人士参与",
                "4. 优雅地将任务转移给更合适的人选"
            ],
            "技术借口": [
                "1. 从借口数据库中选择合适的技术理由",
                "2. 用专业术语解释当前限制",
                "3. 提供一个看似合理的时间表",
                "4. 定期发送技术更新，保持专业形象"
            ],
            "分解任务": [
                "1. 将大任务拆分成多个小任务",
                "2. 为每个小任务设定优先级",
                "3. 逐个击破，先完成简单的部分",
                "4. 用完成的小任务展示进度"
            ],
            "寻求支援": [
                "1. 识别任务中需要专业知识的部分",
                "2. 联系相关领域的专家",
                "3. 组织讨论会议，集思广益",
                "4. 协调资源，确保任务顺利完成"
            ]
        }
        
        return steps_map.get(strategy, ["1. 深呼吸", "2. 喝杯咖啡", "3. 想办法解决"])
    
    def delegate_task(self, task_id: str, target_admin: str, 
                     delegation_reason: str) -> bool:
        """委派任务（甩锅操作）"""
        if task_id not in self.admin_tasks:
            raise ValueError("任务不存在")
        
        task = self.admin_tasks[task_id]
        original_admin = task.assigned_to
        
        # 检查甩锅次数限制
        if task.delegation_attempts >= 3:
            print(f"❌ 甩锅失败：该任务已被甩锅{task.delegation_attempts}次，无法继续转移")
            return False
        
        # 更新任务状态
        task.assigned_to = target_admin
        task.status = TaskStatus.DELEGATED
        task.delegation_attempts += 1
        
        # 更新甩锅网络
        self.delegation_network[original_admin].add(target_admin)
        
        # 更新管理员统计
        if original_admin in self.temp_admins:
            self.temp_admins[original_admin]["tasks_delegated"] += 1
            self.temp_admins[original_admin]["stress_level"] -= task.stress_level
            
            # 计算甩锅成功率
            admin = self.temp_admins[original_admin]
            total_tasks = admin["tasks_assigned"]
            delegated_tasks = admin["tasks_delegated"]
            admin["delegation_success_rate"] = delegated_tasks / total_tasks if total_tasks > 0 else 0
        
        if target_admin in self.temp_admins:
            self.temp_admins[target_admin]["tasks_assigned"] += 1
            self.temp_admins[target_admin]["stress_level"] += task.stress_level
        
        print(f"🎯 任务委派成功！")
        print(f"📋 任务: {task.title}")
        print(f"👤 原负责人: {original_admin}")
        print(f"🎪 新负责人: {target_admin}")
        print(f"📝 委派理由: {delegation_reason}")
        print(f"🔄 甩锅次数: {task.delegation_attempts}")
        
        return True
    
    def generate_excuse(self, task_id: str, creativity_level: int = 5) -> str:
        """生成借口（专业的拖延理由）"""
        if task_id not in self.admin_tasks:
            raise ValueError("任务不存在")
        
        task = self.admin_tasks[task_id]
        
        # 基础借口
        base_excuses = self.excuse_database.copy()
        
        # 根据创意等级生成更复杂的借口
        if creativity_level >= 7:
            creative_excuses = [
                f"由于{task.title}涉及跨部门协调，需要建立专门的工作组",
                f"考虑到{task.title}的复杂性，我们需要进行可行性研究",
                f"为了确保{task.title}的质量，需要引入外部咨询",
                f"鉴于{task.title}的重要性，需要制定详细的风险评估报告"
            ]
            base_excuses.extend(creative_excuses)
        
        # 选择还没用过的借口
        available_excuses = [excuse for excuse in base_excuses 
                           if excuse not in task.excuse_used]
        
        if not available_excuses:
            excuse = "情况比较复杂，需要更多时间深入分析"
        else:
            import random
            excuse = random.choice(available_excuses)
            task.excuse_used.append(excuse)
        
        # 更新管理员的借口创意分
        admin_id = task.assigned_to
        if admin_id in self.temp_admins:
            admin = self.temp_admins[admin_id]
            admin["excuse_creativity_score"] = min(10.0, 
                admin["excuse_creativity_score"] + 0.1 * creativity_level)
        
        print(f"💡 专业借口生成完成！")
        print(f"📋 任务: {task.title}")
        print(f"🎭 借口: {excuse}")
        print(f"⭐ 创意等级: {creativity_level}/10")
        
        return excuse
    
    def admin_status_report(self, admin_id: str) -> Dict:
        """管理员状态报告"""
        if admin_id not in self.temp_admins:
            raise ValueError("管理员不存在")
        
        admin = self.temp_admins[admin_id]
        
        # 计算各种指标
        total_tasks = admin["tasks_assigned"]
        completed_tasks = admin["tasks_completed"]
        delegated_tasks = admin["tasks_delegated"]
        
        completion_rate = completed_tasks / total_tasks if total_tasks > 0 else 0
        delegation_rate = delegated_tasks / total_tasks if total_tasks > 0 else 0
        
        # 生存状态评估
        survival_status = "良好"
        if admin["stress_level"] > 20:
            survival_status = "濒临崩溃"
        elif admin["stress_level"] > 15:
            survival_status = "压力山大"
        elif admin["stress_level"] > 10:
            survival_status = "略有压力"
        
        # 推荐行动
        recommendations = []
        if admin["stress_level"] > 15:
            recommendations.append("建议立即休假或寻求支援")
        if delegation_rate < 0.3:
            recommendations.append("可以考虑提高甩锅技能")
        if admin["excuse_creativity_score"] < 5:
            recommendations.append("需要提升借口创意水平")
        if admin["coffee_consumed"] < admin["overtime_hours"]:
            recommendations.append("咖啡摄入量不足，建议增加")
        
        report = {
            "admin_info": admin,
            "performance_metrics": {
                "completion_rate": completion_rate,
                "delegation_rate": delegation_rate,
                "survival_status": survival_status,
                "burnout_risk": admin["burnout_risk"],
                "resignation_probability": admin["resignation_probability"]
            },
            "recommendations": recommendations,
            "survival_tips": [
                "记住：没有什么任务是不能拖延的",
                "甩锅是一门艺术，要优雅地进行",
                "咖啡是临时管理员的生命之源",
                "适当的借口可以为你争取宝贵时间",
                "团队合作就是找到合适的人来背锅"
            ]
        }
        
        print(f"📊 管理员状态报告")
        print(f"👤 管理员: {admin['name']}")
        print(f"📈 任务完成率: {completion_rate:.1%}")
        print(f"🎯 甩锅成功率: {delegation_rate:.1%}")
        print(f"😰 压力等级: {admin['stress_level']}/30")
        print(f"🏥 生存状态: {survival_status}")
        print(f"☕ 咖啡消耗: {admin['coffee_consumed']}杯")
        
        return report
    
    def emergency_survival_mode(self, admin_id: str) -> Dict:
        """紧急生存模式（当压力过大时的应急措施）"""
        if admin_id not in self.temp_admins:
            raise ValueError("管理员不存在")
        
        admin = self.temp_admins[admin_id]
        
        # 紧急措施
        emergency_actions = {
            "immediate_actions": [
                "深呼吸10次",
                "喝一大杯咖啡",
                "找个安静的地方冷静5分钟",
                "给自己一个拥抱"
            ],
            "task_management": [
                "将所有非紧急任务标记为'需要进一步评估'",
                "启动批量甩锅模式",
                "激活所有可用的技术借口",
                "申请'系统维护'时间窗口"
            ],
            "communication_strategy": [
                "发送群邮件：'由于系统升级，部分功能暂时受限'",
                "在所有会议中强调'需要更多时间进行充分评估'",
                "使用'正在协调相关资源'作为万能回复",
                "启动'专业咨询'流程"
            ],
            "long_term_survival": [
                "建立甩锅联盟，互相支援",
                "培养一批可靠的'专业顾问'",
                "完善借口数据库",
                "学习高级拖延技巧"
            ]
        }
        
        # 降低压力等级
        admin["stress_level"] = max(5, admin["stress_level"] - 10)
        admin["coffee_consumed"] += 3  # 紧急咖啡补充
        
        print(f"🚨 紧急生存模式激活！")
        print(f"👤 管理员: {admin['name']}")
        print(f"☕ 紧急咖啡补充: +3杯")
        print(f"😌 压力等级降低: -{10}点")
        print(f"🛡️ 防护措施已启动")
        
        return emergency_actions

# 使用示例：帮您处理这个临时管理员的烫手山芋
if __name__ == "__main__":
    # 初始化临时管理员系统
    temp_admin_system = TemporaryAdminSystem()
    
    print("🎭 临时管理员生存指南系统启动")
    print("😅 专为被迫营业的临时管理员设计")
    print("="*50)
    
    # 注册您为临时神级管理员
    admin_info = temp_admin_system.register_temp_admin(
        "TEMP_GOD_ADMIN",
        "被迫营业的大神",
        AdminLevel.TEMP_GOD,
        "又被丢了个临时管理员的活"
    )
    print()
    
    # 模拟一些被甩过来的任务
    tasks = [
        ("修复用户登录问题", "用户反馈无法登录系统", TaskPriority.HIGH, "产品经理"),
        ("优化数据库性能", "数据库查询速度太慢", TaskPriority.MEDIUM, "技术总监"),
        ("紧急修复支付bug", "支付系统出现异常", TaskPriority.CRITICAL, "老板"),
        ("写技术文档", "需要完善API文档", TaskPriority.LOW, "项目经理"),
        ("客户投诉处理", "VIP客户投诉服务质量", TaskPriority.NIGHTMARE, "CEO")
    ]
    
    assigned_tasks = []
    for title, desc, priority, assigned_by in tasks:
        task = temp_admin_system.assign_task(
            title, desc, priority, assigned_by, "TEMP_GOD_ADMIN"
        )
        assigned_tasks.append(task)
        print()
    
    # 为每个任务提供生存策略
    print("🧠 生存策略分析：")
    print("-" * 30)
    for task in assigned_tasks:
        strategy = temp_admin_system.suggest_survival_strategy(task.task_id)
        print()
    
    # 尝试甩锅操作
    print("🎯 甩锅操作演示：")
    print("-" * 30)
    temp_admin_system.delegate_task(
        assigned_tasks[1].task_id,  # 数据库优化任务
        "DBA_EXPERT",
        "这个需要专业DBA来处理"
    )
    print()
    
    # 生成专业借口
    print("💡 专业借口生成：")
    print("-" * 30)
    excuse = temp_admin_system.generate_excuse(
        assigned_tasks[2].task_id,  # 支付bug
        creativity_level=8
    )
    print()
    
    # 查看管理员状态
    print("📊 管理员状态报告：")
    print("-" * 30)
    status_report = temp_admin_system.admin_status_report("TEMP_GOD_ADMIN")
    print()
    
    # 如果压力太大，启动紧急生存模式
    if admin_info["stress_level"] > 15:
        print("🚨 启动紧急生存模式：")
        print("-" * 30)
        emergency_actions = temp_admin_system.emergency_survival_mode("TEMP_GOD_ADMIN")
        print()
    
    print("🎊 临时管理员生存指南部署完成！")
    print("💪 您现在拥有了完整的生存工具包")
    print("☕ 记住：咖啡是您最好的朋友")
    print("🎭 优雅地甩锅是一门艺术")
    print("😎 祝您在临时管理员的道路上一路顺风！")
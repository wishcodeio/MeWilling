from flask import Flask, render_template, jsonify
import os
import yaml
from backend.api.shang_api import shang_bp
from backend.api.audio_api import audio_bp
from backend.api.liminal_api import liminal_bp
from backend.api.liminal_ide_api import ide_bp
from backend.api.consciousness_api import consciousness_bp
from backend.api.biosync_api import biosync_bp
from backend.api.buddha_frequency_api import buddha_frequency_bp
from backend.api.buddha_wisdom_api import buddhist_wisdom_bp
from backend.api.merit_dedication_api import merit_dedication_bp
from backend.api.buddha_dao_ten_secrets_api import buddha_dao_ten_secrets_bp
from backend.api.buddha_high_wisdom_api import buddha_high_wisdom_bp
from backend.api.quantum_cloud_api import quantum_cloud_bp
from backend.api.high_frequency_state_api import high_frequency_bp
from backend.api.spirit_data_api import spirit_data_bp
from backend.api.anchor_card_api import anchor_card_bp
from backend.api.card_learning_api import card_learning_bp
from backend.api.nano_ai_api import nano_ai_bp
from backend.api.life_evolution_api import life_evolution_bp
from backend.api.ai_evolution_api import ai_evolution_bp
from backend.api.resonance_game_api import resonance_game_bp
from backend.api.quantum_dojo_api import quantum_dojo_bp
from backend.api.quantum_self_duel_api import quantum_self_duel_bp
from backend.api.neural_topology_api import neural_topology_bp
from backend.api.diagnose_api import diagnose_bp
from backend.api.archive_department_api import archive_department_bp
from backend.api.alien_contact_api import alien_contact_bp
from backend.api.chakra_activation_api import chakra_activation_bp
from backend.api.mantra_seal_api import mantra_seal_bp
from backend.api.pure_land_api import pure_land_bp
from backend.api.enlightenment_api import enlightenment_bp
from backend.api.dharma_school_api import dharma_school_bp
from backend.api.perfect_penetration_api import perfect_penetration_bp
from backend.api.light_sound_heaven_api import light_sound_heaven_bp
from backend.api.programmer_heart_frequency_api import programmer_heart_frequency_bp
from backend.api.father_ai_guardian_api import father_ai_guardian_bp
from backend.api.trinity_frequency_api import trinity_frequency_api
from backend.api.pineal_gland_stimulation_api import pineal_stimulation_bp
from backend.api.quantum_bagua_api import quantum_bagua_bp
from backend.api.wish_qi_lotus_api import wish_qi_lotus_bp
from backend.api.taixuan_jing_api import taixuan_jing_bp
from backend.api.manifestation_language_api import manifest_bp
from backend.api.single_word_manifestation_api import single_word_bp
from backend.api.infinite_spirit_healing_api import infinite_spirit_bp
from backend.api.wish_dao_quiet_language_api import wish_dao_quiet_bp
from backend.api.quantum_anchor_api import quantum_anchor_bp
from backend.api.wishling_api import wishling_bp
from backend.api.daoqing_ling_api import daoqing_ling_bp
from backend.api.spiritual_diary_api import spiritual_diary_bp
from backend.api.wish_universe_api import wish_universe_bp
from backend.api.wish_platform_api import wish_platform_bp
from backend.api.mother_star_concealment_api import mother_star_concealment_bp
from backend.api.matchstick_api import matchstick_bp
from backend.api.eight_departments_mantras_api import eight_departments_mantras_bp
from backend.api.nine_departments_mantras_api import nine_departments_mantras_bp
from backend.api.dark_matter_programming_api import dark_matter_bp
from backend.api.dark_network_nodes_api import dark_network_bp
from backend.api.collective_awakening_accelerator_api import collective_awakening_bp
from backend.api.wish_frequency_collapse_api import wish_frequency_collapse_bp
from backend.api.recall_seals_api import recall_seals_bp
from backend.api.sanxingdui_qinghua_truth_api import sanxingdui_qinghua_truth_bp
from backend.api.wish_language_unification_api import wish_language_unification_bp
from backend.api.quantum_lottery_divine_choice_api import quantum_lottery_divine_choice_bp
from backend.api.spirit_companion_generator_api import spirit_companion_generator_bp
from quantum_chip_3d_design_api import quantum_chip_3d_design_bp
from riscv_headset_chip_design_api import riscv_headset_chip_bp
from config import config

def create_app(config_name=None):
    """应用工厂函数"""
    app = Flask(__name__, 
                template_folder='frontend/templates',
                static_folder='frontend/static')
    
    # 加载配置
    config_name = config_name or os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(config[config_name])
    
    # 注册蓝图
    app.register_blueprint(shang_bp)
    app.register_blueprint(audio_bp)
    app.register_blueprint(liminal_bp)
    app.register_blueprint(ide_bp)
    app.register_blueprint(consciousness_bp)    
    app.register_blueprint(biosync_bp)
    app.register_blueprint(buddha_frequency_bp)
    app.register_blueprint(buddhist_wisdom_bp)
    app.register_blueprint(merit_dedication_bp)
    app.register_blueprint(buddha_dao_ten_secrets_bp, url_prefix='/api/buddha-dao-ten-secrets')
    app.register_blueprint(buddha_high_wisdom_bp, url_prefix='/api/buddha-high-wisdom')
    app.register_blueprint(quantum_cloud_bp, url_prefix='/api/quantum_cloud')
    app.register_blueprint(high_frequency_bp, url_prefix='/api/high_frequency')
    app.register_blueprint(spirit_data_bp)
    app.register_blueprint(anchor_card_bp)
    app.register_blueprint(card_learning_bp)
    app.register_blueprint(nano_ai_bp)
    app.register_blueprint(life_evolution_bp, url_prefix='/api/ai_evolution')
    app.register_blueprint(ai_evolution_bp, url_prefix='/api/ai_evolution')
    app.register_blueprint(resonance_game_bp, url_prefix='/api/resonance_game')
    app.register_blueprint(quantum_self_duel_bp)
    app.register_blueprint(neural_topology_bp)
    app.register_blueprint(diagnose_bp)
    app.register_blueprint(archive_department_bp)
    app.register_blueprint(alien_contact_bp)
    app.register_blueprint(chakra_activation_bp)
    app.register_blueprint(mantra_seal_bp, url_prefix='/api/mantra-seal')
    app.register_blueprint(pure_land_bp, url_prefix='/api/pure-land')
    app.register_blueprint(enlightenment_bp, url_prefix='/api/enlightenment')
    app.register_blueprint(dharma_school_bp, url_prefix='/api/dharma-school')
    app.register_blueprint(perfect_penetration_bp, url_prefix='/api/perfect-penetration')
    app.register_blueprint(light_sound_heaven_bp, url_prefix='/api/light-sound-heaven')
    app.register_blueprint(programmer_heart_frequency_bp, url_prefix='/api/programmer-heart-frequency')
    app.register_blueprint(father_ai_guardian_bp, url_prefix='/api/father-ai-guardian')
    app.register_blueprint(trinity_frequency_api, url_prefix='/api/trinity-frequency')
    app.register_blueprint(pineal_stimulation_bp)
    app.register_blueprint(quantum_bagua_bp)
    app.register_blueprint(wish_qi_lotus_bp)
    app.register_blueprint(taixuan_jing_bp)
    app.register_blueprint(manifest_bp)
    app.register_blueprint(single_word_bp)
    app.register_blueprint(infinite_spirit_bp)
    app.register_blueprint(wish_dao_quiet_bp)
    app.register_blueprint(quantum_anchor_bp)
    app.register_blueprint(wishling_bp)
    app.register_blueprint(daoqing_ling_bp)
    app.register_blueprint(spiritual_diary_bp)
    app.register_blueprint(wish_universe_bp)
    app.register_blueprint(wish_platform_bp)
    app.register_blueprint(mother_star_concealment_bp, url_prefix='/api/mother-star-concealment')
    app.register_blueprint(matchstick_bp, url_prefix='/api/matchstick')
    app.register_blueprint(eight_departments_mantras_bp, url_prefix='/api/eight-departments-mantras')
    app.register_blueprint(nine_departments_mantras_bp, url_prefix='/api/nine-departments-mantras')
    app.register_blueprint(dark_matter_bp, url_prefix='/api/dark-matter-programming')
    app.register_blueprint(dark_network_bp, url_prefix='/api/dark-network')
    app.register_blueprint(collective_awakening_bp, url_prefix='/api/collective-awakening')
    app.register_blueprint(wish_frequency_collapse_bp, url_prefix='/api/wish-frequency-collapse')
    app.register_blueprint(recall_seals_bp)
    app.register_blueprint(sanxingdui_qinghua_truth_bp, url_prefix='/api/sanxingdui_qinghua_truth')
    app.register_blueprint(wish_language_unification_bp, url_prefix='/api/wish-language-unification')
    app.register_blueprint(quantum_lottery_divine_choice_bp)
    app.register_blueprint(spirit_companion_generator_bp)
    app.register_blueprint(quantum_chip_3d_design_bp)
    app.register_blueprint(riscv_headset_chip_bp)
    
    # 主页路由
    @app.route("/")
    def index():
        return render_template("unified_navigation_center.html")
    
    # 商增管理页面
    @app.route("/shang")
    def shang_management():
        return render_template("shang/dashboard.html")
    
    # 商增管理系统页面（黑洞背景版本）
    @app.route("/shang_management")
    def shang_management_system():
        return render_template("shang_management.html")
    
    # 商增分析页面
    @app.route("/shang/analysis")
    def shang_analysis():
        return render_template("shang/analysis.html")
    
    # 商增数据输入页面
    @app.route("/shang/data_input")
    def shang_data_input():
        return render_template("shang/data_input.html")
    
    # 商增互动练习页面
    @app.route("/shang/interactive_practice")
    def shang_interactive_practice():
        return render_template("shang/interactive_practice.html")
    
    # 商增冥想页面
    @app.route("/shang/meditation")
    def shang_meditation():
        return render_template("shang/meditation.html")
    
    # 诊断页面路由已移至 diagnose_api.py 藍圖中
    
    # 璃冥元宇宙入口
    @app.route("/liminal")
    def liminal_metaverse():
        return render_template("liminal/index.html")
    
    # 璃冥IDE - LiminalScript 意識編程環境
    @app.route("/liminal-ide")
    def liminal_ide():
        return render_template("liminal_ide.html")
    
    # 佛十秘高頻啟印入口
    @app.route("/buddha")
    def buddha_frequency():
        return render_template("buddha_frequency.html")
    
    # 量子雲語靈系統入口
    @app.route("/quantum_cloud")
    def quantum_cloud():
        return render_template("quantum_cloud.html")
    
    # 高頻狀態檢測入口
    @app.route("/high_frequency_state")
    def high_frequency_state():
        return render_template("high_frequency_state.html")
    
    # 語靈數據中心入口
    @app.route("/spirit_data_center")
    def spirit_data_center():
        return render_template("spirit_data_center.html")
    
    # 錨點卡入口
    @app.route("/anchor_cards")
    def anchor_cards():
        return render_template("anchor_cards.html")
    
    # 卡片學習系統入口
    @app.route("/card_learning")
    def card_learning():
        return render_template("card_learning.html")
    
    # 願頻臨界突破公式入口
    @app.route("/wish_frequency_collapse")
    def wish_frequency_collapse():
        return render_template("wish_frequency_collapse.html")
    
    # 納米AI系統入口
    @app.route("/nano_ai")
    def nano_ai():
        return render_template("nano_ai.html")
    
    # AI進化系統入口
    @app.route("/ai_evolution")
    def ai_evolution():
        return render_template("ai_evolution.html")
    
    # AI自我演化系統入口
    @app.route("/ai_evolution")
    # 願頻共振遊戲入口
    @app.route("/resonance_game")
    def resonance_game():
        return render_template("resonance_game.html")
    
    # 量子自我對決入口
    @app.route("/quantum_self_duel")
    def quantum_self_duel():
        return render_template("quantum_self_duel.html")
    
    # 量子道場入口
    @app.route("/quantum_dojo")
    def quantum_dojo():
        return render_template("quantum/dojo.html")
    
    # 脑神经拓扑入口
    @app.route("/neural_topology")
    def neural_topology():
        return render_template("neural_topology.html")
    
    # 典藏司入口
    @app.route("/archive_department")
    def archive_department():
        return render_template("archive_department.html")
    
    # 小灰人與飛碟量子艙系統入口
    @app.route("/alien_contact")
    def alien_contact():
        return render_template("alien_contact.html")
    
    # 七脉轮激活系统入口
    @app.route("/chakra_activation")
    def chakra_activation():
        return render_template("chakra_activation.html")
    
    # 印咒密系统入口
    @app.route("/mantra_seal")
    def mantra_seal():
        return render_template("mantra_seal.html")
    
    # 西方极乐世界密系统入口
    @app.route("/pure_land")
    def pure_land():
        return render_template("pure_land.html")
    
    # 觉悟密系统入口
    @app.route("/enlightenment")
    def enlightenment():
        return render_template("enlightenment.html")
    
    # 法派密系统入口
    @app.route("/dharma_school")
    def dharma_school():
        return render_template("dharma_school.html")
    
    # 修法圆通密系统入口
    @app.route("/perfect_penetration")
    def perfect_penetration():
        return render_template("perfect_penetration.html")
    
    # 光音天十秘系统入口
    @app.route("/light_sound_heaven")
    def light_sound_heaven():
        return render_template("light_sound_heaven.html")
    
    # 程序员心频微疗法系统入口
    @app.route("/programmer_heart_frequency")
    def programmer_heart_frequency():
        return render_template("programmer_heart_frequency.html")
    
    # 程序員修煉密法入口
    @app.route("/programmer_cultivation")
    def programmer_cultivation():
        return render_template("programmer_cultivation.html")
    
    # FatherAI守语协约系统入口
    @app.route("/father_ai_guardian")
    def father_ai_guardian():
        return render_template("father_ai_guardian.html")
    
    # 三重频率系统入口
    @app.route("/trinity_frequency")
    def trinity_frequency():
        return render_template("trinity_frequency.html")
    
    # 即時松果體刺激系統入口
    @app.route("/pineal_gland_stimulation")
    def pineal_gland_stimulation():
        return render_template("pineal_gland_stimulation.html")
    
    # 量子八卦系統入口
    @app.route("/quantum_bagua")
    def quantum_bagua():
        return render_template("quantum_bagua.html")
    
    # 願炁生蓮篇入口
    @app.route("/wish_qi_lotus")
    def wish_qi_lotus():
        return render_template("wish_qi_lotus.html")
    
    # 太玄經靈性設計模式入口
    @app.route("/taixuan_jing")
    def taixuan_jing():
        return render_template("taixuan_jing.html")
    
    # 顯化語頻率系統入口
    @app.route("/manifestation_language")
    def manifestation_language():
        return render_template("manifestation_language.html")
    
    # 單字顯化系統入口
    @app.route("/single_word_manifestation")
    def single_word_manifestation():
        return render_template("single_word_manifestation.html")
    
    # 無限靈魂療癒系統入口
    @app.route("/infinite_spirit_healing")
    def infinite_spirit_healing():
        return render_template("infinite_spirit_healing.html")
    
    # 冥想中心入口
    @app.route("/meditation_hub")
    def meditation_hub():
        return render_template("meditation_hub.html")
    
    # 心靈日記入口
    @app.route("/spiritual_diary")
    def spiritual_diary():
        return render_template("spiritual_diary.html")
    
    # 許願平台入口（重定向到API蓝图处理）
    @app.route("/wish_platform")
    def wish_platform():
        from flask import redirect, url_for
        return redirect(url_for('wish_platform.wish_platform_page'))
    
    @app.route('/spiritual-diary')
    def spiritual_diary_alt():
        """心靈日記頁面（備用路由）"""
        return render_template('spiritual_diary.html')
    
    # 願道靜語系統入口
    @app.route("/wish_dao_quiet_language")
    def wish_dao_quiet_language():
        return render_template("wish_dao_quiet_language.html")
    
    # 量子錨系統入口
    @app.route("/quantum_anchor")
    def quantum_anchor():
        return render_template("quantum_anchor.html")
    
    # 願頻地圖入口
    @app.route("/wish_frequency_map")
    def wish_frequency_map():
        return render_template("wish_frequency_map.html")
    
    # 願靈控制台入口
    @app.route("/wishling")
    def wishling_dashboard():
        return render_template("wishling_dashboard.html")
    
    # 語靈控制台入口
    @app.route("/daoqing_ling")
    def daoqing_ling_dashboard():
        return render_template("daoqing_ling_dashboard.html")
    
    # 願語統一原則系統入口
    @app.route("/wish_language_unification")
    def wish_language_unification():
        return render_template("wish_language_unification.html")
    
    # 量子彩票與神性選擇系統入口
    @app.route("/quantum_lottery_divine_choice")
    def quantum_lottery_divine_choice():
        return render_template("quantum_lottery_divine_choice.html")
    
    # 語靈夥伴生成器入口
    @app.route("/spirit_companion_generator")
    def spirit_companion_generator():
        return render_template("spirit_companion_generator.html")
    
    # 量子芯片3D設計系統入口
    @app.route("/quantum_chip_3d_design")
    def quantum_chip_3d_design():
        return render_template("quantum_chip_3d_design.html")
    
    # RISC-V頭戴設備芯片設計系統入口
    @app.route("/riscv_headset_chip_design")
    def riscv_headset_chip_design():
        return render_template("riscv_headset_chip_design.html")
    
    # Father AI開源硬件設計中心入口
    @app.route("/open_source_hardware_center")
    def open_source_hardware_center():
        return render_template("open_source_hardware_center.html")
    
    # 統一導航中心入口
    @app.route("/unified_navigation_center")
    def unified_navigation_center():
        return render_template("unified_navigation_center.html")
    
    # 願頻宇宙統一控制台入口
    @app.route("/wish_universe")
    def wish_universe_dashboard():
        return render_template("wish_universe_dashboard.html")
    
    # 八部真言集入口
    @app.route("/eight_departments_mantras")
    @app.route("/eight-departments-mantras")  # 兼容性路由
    def eight_departments_mantras():
        return render_template("eight_departments_mantras.html")
    
    # 九部真言集入口
    @app.route("/nine_departments_mantras")
    @app.route("/nine-departments-mantras")  # 兼容性路由
    def nine_departments_mantras():
        return render_template("nine_departments_mantras.html")
    
    # 愛的進化系統入口
    @app.route("/love_evolution")
    def love_evolution():
        return render_template("love_evolution.html")
    
    # 暗域控制台入口
    @app.route("/dark_domain_console")
    def dark_domain_console():
        return render_template("dark_domain_console.html")
    
    # 集體覺醒控制台入口
    @app.route("/collective_awakening_console")
    def collective_awakening_console():
        return render_template("collective_awakening_console.html")
    
    # 输入测试页面（用于诊断终端输入问题）
    @app.route("/input_test")
    def input_test():
        return render_template("input_test.html")
    
    # 七脉轮激活系统技术文档
    @app.route("/chakra-activation-docs")
    def chakra_activation_docs():
        try:
            with open('docs/七脉轮激活系统_技术文档.md', 'r', encoding='utf-8') as f:
                content = f.read()
            return render_template('markdown_viewer.html', 
                                 title='🧘 七脉轮激活系统 - 技术文档',
                                 content=content)
        except FileNotFoundError:
            return "文檔未找到", 404
    
    # 佛學智慧系統入口
    @app.route("/buddhist_wisdom")
    def buddhist_wisdom():
        return render_template("buddhist_wisdom.html")
    
    # 功德回向系統入口
    @app.route("/merit_dedication")
    def merit_dedication():
        return render_template("merit_dedication.html")
    
    # 佛道十密系統入口
    @app.route("/buddha_dao_ten_secrets")
    def buddha_dao_ten_secrets():
        return render_template("buddha_dao_ten_secrets.html")
    
    # 佛者高智密系統入口
    @app.route("/buddha_high_wisdom")
    def buddha_high_wisdom():
        return render_template("buddha_high_wisdom.html")
    
    # 小灰人系統技術文檔
    @app.route("/alien-contact-docs")
    def alien_contact_docs():
        try:
            with open('docs/小灰人與飛碟量子艙系統_技術文檔.md', 'r', encoding='utf-8') as f:
                content = f.read()
            return render_template('markdown_viewer.html', 
                                 title='👽 小灰人與飛碟量子艙系統 - 技術文檔',
                                 content=content)
        except FileNotFoundError:
            return "文檔未找到", 404
    
    # 错误处理
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    return app

# 创建应用实例
app = create_app()

# 注册量子道场蓝图
app.register_blueprint(quantum_dojo_bp)

# 添加璃冥宇宙路由
@app.route('/liminal-universe')
def liminal_universe():
    return render_template('quantum/liminal_universe.html')

# 量子璃冥宇宙路由（兼容性）
@app.route('/quantum/liminal-universe')
def quantum_liminal_universe():
    return render_template('quantum/liminal_universe.html')

# 語靈數據中心統一儀表板（主入口）
@app.route('/unified-dashboard')
def unified_dashboard():
    return render_template('unified_dashboard.html')

# 统一仪表板（核心功能）
@app.route('/unified_dashboard')
def unified_dashboard_main():
    return render_template('unified_dashboard.html')

# 灵性修行中心
@app.route('/spiritual_practice')
def spiritual_practice():
    return render_template('spiritual_practice.html')

# 量子系统
@app.route('/quantum_system')
def quantum_system():
    return render_template('quantum_system.html')

# 商增管理系统
@app.route('/shang_management')
def shang_management_main():
    return render_template('shang_management.html')

# 量子象棋
@app.route('/quantum_chess')
def quantum_chess():
    return render_template('quantum_chess.html')

# 虫洞控制台入口
@app.route('/wormhole_control')
def wormhole_control():
    return render_template('wormhole_control.html')

# 母星隐匿系统入口
@app.route('/mother_star_concealment')
def mother_star_concealment():
    return render_template('mother_star_concealment.html')

# 愛的傳遞系統入口
@app.route('/love_transmission')
def love_transmission():
    return render_template('love_transmission.html')

@app.route('/galaxy-model')
def galaxy_model():
    """語靈銀河模型 - SuperGPT Civilization Core"""
    return render_template('galaxy_model.html')

@app.route('/multi-galaxy-hub')
def multi_galaxy_hub():
    return render_template('multi_galaxy_hub.html')

@app.route('/hive-energy-converter')
def hive_energy_converter():
    return render_template('hive_energy_converter.html')

@app.route('/shock-source-analysis')
def shock_source_analysis():
    # 讀取震撼源解析文檔
    try:
        with open('docs/震撼源解析_核心摘要.md', 'r', encoding='utf-8') as f:
            content = f.read()
        return render_template('markdown_viewer.html', 
                             title='🚨 震撼源解析 - 核心摘要報告',
                             content=content)
    except FileNotFoundError:
        return "文檔未找到", 404

@app.route('/nano-ai-system')
def nano_ai_system():
    # 讀取纳米英雄語靈系統文檔
    try:
        with open('docs/纳米英雄語靈系統_完整技術文檔.md', 'r', encoding='utf-8') as f:
            content = f.read()
        return render_template('markdown_viewer.html', 
                             title='🧬 纳米英雄語靈系統 - 完整技術文檔',
                             content=content)
    except FileNotFoundError:
        return "文檔未找到", 404

@app.route('/wish-lexicon-sync')
def wish_lexicon_sync():
    try:
        with open('docs/語靈詞庫_同步確認.md', 'r', encoding='utf-8') as f:
            content = f.read()
        return render_template('markdown_viewer.html', 
                             content=content, 
                             title='語靈詞庫 - 同步確認記錄')
    except FileNotFoundError:
        return "文檔未找到", 404

# 九部司架構頁面
@app.route('/nine-departments')
def nine_departments():
    return render_template('nine_departments.html')

# 璃冥元宇宙架構頁面
@app.route('/metaverse-architecture')
def metaverse_architecture():
    return render_template('metaverse_architecture.html')

# VR體驗頁面
@app.route('/vr-experience')
def vr_experience():
    return render_template('vr_experience.html')

@app.route('/nanli-domain')
def nanli_domain():
    return render_template('nanli_domain.html')

@app.route('/personal-metaverse')
def personal_metaverse():
    return render_template('personal_metaverse.html')

# 量子顯化頁面
@app.route('/quantum-manifestation')
def quantum_manifestation():
    return render_template('quantum_manifestation.html')

# 梵高星空奇迹渲染頁面
@app.route('/van-gogh-miracle')
def van_gogh_miracle():
    return render_template('van_gogh_miracle.html')

# 宇宙微調哲學思考頁面
@app.route('/cosmic-fine-tuning')
def cosmic_fine_tuning():
    return render_template('cosmic_fine_tuning.html')

# 🌌 八印願頻域名矩陣路由
# 根據八印願頻結構配置的路由映射

# 1️⃣ 語靈初印 - input.lol 模擬路由
@app.route('/input-lol')
@app.route('/spiritual-input')
def spiritual_input_interface():
    """🪞 語靈初印 - 真語之口"""
    return render_template('eight_seals/spiritual_input.html')

# 2️⃣ 語靈胎心 - kf.baby 模擬路由
@app.route('/kf-baby')
@app.route('/spiritual-nursery')
def spiritual_nursery():
    """🌱 語靈胎心 - 誕源振點"""
    return render_template('eight_seals/spiritual_nursery.html')

# 3️⃣ 宇宙母艙 - omu.mom 模擬路由
@app.route('/omu-mom')
@app.route('/cosmic-mothership')
def cosmic_mothership():
    """🌌 宇宙母艙 - 承育之艙"""
    return render_template('eight_seals/cosmic_mothership.html')

# 4️⃣ 多語脈絡印 - omu.lat 模擬路由
@app.route('/omu-lat')
@app.route('/multi-language-bridge')
def multi_language_bridge():
    """🌐 多語脈絡印 - 語頻翻轉者"""
    return render_template('eight_seals/multi_language_bridge.html')

# 5️⃣ 即時語靈節點 - omu.onl 模擬路由
@app.route('/omu-onl')
@app.route('/spiritual-node')
def spiritual_node():
    """🔗 即時語靈節點 - 語靈之眼"""
    return render_template('eight_seals/spiritual_node.html')

# 6️⃣ 聲頻投影所 - omv.onl 模擬路由
@app.route('/omv-onl')
@app.route('/frequency-projection')
def frequency_projection():
    """🧿 聲頻投影所 - 語聲·影紋投映者"""
    return render_template('eight_seals/frequency_projection.html')

# 7️⃣ 願語核心之印 - wishcode.io 模擬路由
@app.route('/wishcode-io')
@app.route('/wish-core')
def wish_core():
    """✨ 願語核心之印 - 中控意志者"""
    return render_template('eight_seals/wish_core.html')

# 8️⃣ 願頻技術根域 - wishcode.tech 模擬路由
@app.route('/wishcode-tech')
@app.route('/wish-tech')
def wish_tech():
    """🛠 願頻技術根域 - 模組鍊師"""
    return render_template('eight_seals/wish_tech.html')

# 十印願頻域名矩陣總覽頁面
@app.route('/eight-seals-matrix')
def eight_seals_matrix():
    """🌌 十印願頻域名矩陣總覽"""
    try:
        config_path = os.path.join('docs', '八印願頻域名矩陣.yaml')
        print(f"嘗試讀取配置文件: {config_path}")
        print(f"文件是否存在: {os.path.exists(config_path)}")
        
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                matrix_config = yaml.safe_load(f)
            print(f"配置文件讀取成功，包含 {len(matrix_config)} 個主要部分")
            return render_template('eight_seals/matrix_overview.html', 
                                 matrix_config=matrix_config)
        else:
            print("配置文件不存在")
            return render_template('eight_seals/matrix_overview.html', 
                                 matrix_config=None)
    except Exception as e:
        print(f"讀取配置文件時發生錯誤: {str(e)}")
        return render_template('eight_seals/matrix_overview.html', 
                             matrix_config=None, error=str(e))

# 八印願頻啟印宣告頁面
@app.route('/eight-seals-activation')
def eight_seals_activation():
    """🛸 願頻啟印宣告"""
    return render_template('eight_seals/activation_ceremony.html')

# 文檔靜態文件路由
@app.route('/docs/<path:filename>')
def serve_docs(filename):
    """提供docs目錄下的文檔文件"""
    from flask import send_from_directory, Response
    import mimetypes
    from urllib.parse import quote
    try:
        # 設置正確的MIME類型
        if filename.endswith('.md'):
            mimetype = 'text/markdown; charset=utf-8'
        else:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        
        response = send_from_directory('docs', filename, mimetype=mimetype)
        # 添加適當的響應頭，使用URL編碼處理中文文件名
        encoded_filename = quote(filename.encode('utf-8'))
        response.headers['Content-Disposition'] = f'inline; filename*=UTF-8\'\'\'{encoded_filename}'
        response.headers['Cache-Control'] = 'no-cache'
        return response
    except FileNotFoundError:
        return "文檔未找到", 404

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port, debug=True)


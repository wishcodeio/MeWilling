#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 讀取原始文件
with open('./frontend/templates/unified_navigation_center.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 定義要添加的模塊
additional_modules = {
    '🧘 靈性修行系統': [
        ('/buddha', '佛陀智慧'),
        ('/buddha_high_wisdom', '佛陀高智慧'),
        ('/buddha_dao_ten_secrets', '佛道十秘'),
        ('/buddhist_wisdom', '佛學智慧'),
        ('/dharma_school', '法學院'),
        ('/pure_land', '淨土'),
        ('/eight_departments_mantras', '八部咒語'),
        ('/merit_dedication', '功德迴向'),
        ('/perfect_penetration', '圓通'),
        ('/light_sound_heaven', '光音天'),
        ('/taixuan_jing', '太玄經'),
        ('/high_frequency_state', '高頻狀態'),
        ('/infinite_spirit_healing', '無限靈療'),
        ('/pineal_gland_stimulation', '松果體激活'),
        ('/trinity_frequency', '三位一體頻率'),
        ('/collective_awakening_console', '集體覺醒控制台'),
        ('/daoqing_ling', '語靈')
    ],
    '🌟 願頻系統': [
        ('/wish_universe', '願宇宙'),
        ('/wish_platform', '願平台'),
        ('/wish_language_unification', '願語統一'),
        ('/wishling', '願靈'),
        ('/single_word_manifestation', '單字顯化'),
        ('/manifestation_language', '顯化語言')
    ],
    '⚛️ 量子系統': [
        ('/quantum_lottery_divine_choice', '量子彩票神選')
    ],
    '💻 開發者工具': [
        ('/liminal', '臨界'),
        ('/liminal-ide', '臨界IDE')
    ]
}

# 新增系統管理分類
new_category = '''
            <!-- 系統管理 -->
            <div class="category-card">
                <h3 class="category-title">⚙️ 系統管理</h3>
                <p class="category-description">系統管理與數據中心平台</p>
                <ul class="module-list">
                    <li class="module-item">
                        <a href="/shang" class="module-link missing-template">商系統</a>
                    </li>
                    <li class="module-item">
                        <a href="/shang_management" class="module-link missing-template">商管理</a>
                    </li>
                    <li class="module-item">
                        <a href="/spirit_data_center" class="module-link missing-template">靈性數據中心</a>
                    </li>
                    <li class="module-item">
                        <a href="/archive_department" class="module-link missing-template">檔案部門</a>
                    </li>
                    <li class="module-item">
                        <a href="/unified_navigation_center" class="module-link missing-template">統一導航中心</a>
                    </li>
                    <li class="module-item">
                        <a href="/input_test" class="module-link missing-template">輸入測試</a>
                    </li>
                </ul>
            </div>
'''

# 為每個分類添加模塊
for category_title, modules in additional_modules.items():
    # 找到分類的結束標籤
    pattern = rf'(<h3 class="category-title">{re.escape(category_title)}</h3>.*?</ul>)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        category_content = match.group(1)
        # 在</ul>前添加新模塊
        new_items = ''
        for url, name in modules:
            new_items += f'''                    <li class="module-item">
                        <a href="{url}" class="module-link missing-template">{name}</a>
                    </li>
'''
        
        updated_category = category_content.replace('</ul>', new_items + '                </ul>')
        content = content.replace(category_content, updated_category)

# 在統計信息前添加新的系統管理分類
stats_pattern = r'(\s*<!-- 統計信息 -->)'
match = re.search(stats_pattern, content)
if match:
    content = content.replace(match.group(1), new_category + match.group(1))

# 寫入更新後的文件
with open('./frontend/templates/unified_navigation_center.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("導航文件已成功更新！")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
典藏司API
八部典藏司的核心API，負責古籍管理、學習卡片生成等功能
"""

from flask import Blueprint, request, jsonify, send_file
import os
import json
from datetime import datetime
from backend.services.ancient_text_generator import AncientTextGenerator
from backend.api.card_learning_api import CardLearningSystem

# 創建藍圖
archive_department_bp = Blueprint('archive_department', __name__)

# 初始化服務
ancient_text_generator = AncientTextGenerator()
card_learning_system = CardLearningSystem()

@archive_department_bp.route('/api/archive/categories', methods=['GET'])
def get_categories():
    """獲取古籍分類信息"""
    try:
        categories = ancient_text_generator.get_categories_info()
        dynasties = ancient_text_generator.get_dynasties_info()
        
        return jsonify({
            'success': True,
            'categories': categories,
            'dynasties': dynasties
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@archive_department_bp.route('/api/archive/generate_sample_json', methods=['POST'])
def generate_sample_json():
    """生成示例古籍JSON文件"""
    try:
        json_file_path = ancient_text_generator.export_sample_json()
        
        # 讀取生成的文件內容
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_content = json.load(f)
        
        return jsonify({
            'success': True,
            'message': '示例JSON文件生成成功',
            'file_path': json_file_path,
            'content': json_content,
            'download_url': f'/api/archive/download_json/{os.path.basename(json_file_path)}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@archive_department_bp.route('/api/archive/generate_custom_json', methods=['POST'])
def generate_custom_json():
    """生成自定義古籍JSON文件"""
    try:
        data = request.get_json()
        custom_texts = data.get('texts', [])
        
        if not custom_texts:
            return jsonify({
                'success': False,
                'error': '請提供古籍文本數據'
            }), 400
        
        json_file_path = ancient_text_generator.generate_ancient_text_json(custom_texts)
        
        # 讀取生成的文件內容
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_content = json.load(f)
        
        return jsonify({
            'success': True,
            'message': f'自定義JSON文件生成成功，包含 {len(custom_texts)} 個古籍',
            'file_path': json_file_path,
            'content': json_content,
            'download_url': f'/api/archive/download_json/{os.path.basename(json_file_path)}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@archive_department_bp.route('/api/archive/json_to_cards', methods=['POST'])
def convert_json_to_cards():
    """將JSON文件轉換為學習卡片"""
    try:
        data = request.get_json()
        
        # 支持兩種方式：文件路徑或直接JSON數據
        if 'file_path' in data:
            json_file_path = data['file_path']
            if not os.path.exists(json_file_path):
                return jsonify({
                    'success': False,
                    'error': '指定的JSON文件不存在'
                }), 400
            cards = ancient_text_generator.create_learning_cards_from_json(json_file_path)
        elif 'json_data' in data:
            # 臨時保存JSON數據到文件
            temp_file = f'data/ancient_texts/temp_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
            os.makedirs(os.path.dirname(temp_file), exist_ok=True)
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(data['json_data'], f, ensure_ascii=False, indent=2)
            cards = ancient_text_generator.create_learning_cards_from_json(temp_file)
            # 清理臨時文件
            os.remove(temp_file)
        else:
            return jsonify({
                'success': False,
                'error': '請提供file_path或json_data參數'
            }), 400
        
        # 將卡片保存到學習系統
        saved_cards = []
        for card_data in cards:
            try:
                # 使用古籍專用的創建方法
                saved_card = card_learning_system.create_ancient_text_card({
                    'title': card_data['title'],
                    'content': card_data['content'],
                    'category': card_data['ancient_metadata']['category'],
                    'dynasty': card_data['ancient_metadata']['dynasty'],
                    'author': card_data['ancient_metadata']['author'],
                    'source_library': card_data['ancient_metadata']['source_library'],
                    'manuscript_type': card_data['ancient_metadata']['manuscript_type'],
                    'preservation_level': card_data['ancient_metadata']['preservation_level'],
                    'difficulty': card_data['difficulty'],
                    'tags': card_data['tags']
                })
                saved_cards.append(saved_card)
            except Exception as card_error:
                print(f"創建卡片失敗: {card_error}")
                continue
        
        return jsonify({
            'success': True,
            'message': f'成功創建 {len(saved_cards)} 張學習卡片',
            'cards_count': len(saved_cards),
            'cards': saved_cards[:5]  # 只返回前5張卡片作為預覽
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@archive_department_bp.route('/api/archive/download_json/<filename>', methods=['GET'])
def download_json_file(filename):
    """下載JSON文件"""
    try:
        file_path = os.path.join('data/ancient_texts', filename)
        if not os.path.exists(file_path):
            return jsonify({
                'success': False,
                'error': '文件不存在'
            }), 404
        
        return send_file(file_path, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@archive_department_bp.route('/api/archive/list_json_files', methods=['GET'])
def list_json_files():
    """列出所有古籍JSON文件"""
    try:
        data_dir = 'data/ancient_texts'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)
            return jsonify({
                'success': True,
                'files': []
            })
        
        files = []
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(data_dir, filename)
                file_stat = os.stat(file_path)
                
                # 嘗試讀取文件元數據
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = json.load(f)
                        metadata = content.get('metadata', {})
                except:
                    metadata = {}
                
                files.append({
                    'filename': filename,
                    'size': file_stat.st_size,
                    'created_at': datetime.fromtimestamp(file_stat.st_ctime).isoformat(),
                    'modified_at': datetime.fromtimestamp(file_stat.st_mtime).isoformat(),
                    'metadata': metadata
                })
        
        # 按修改時間排序
        files.sort(key=lambda x: x['modified_at'], reverse=True)
        
        return jsonify({
            'success': True,
            'files': files
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@archive_department_bp.route('/api/archive/ancient_texts_stats', methods=['GET'])
def get_ancient_texts_stats():
    """獲取古籍統計信息"""
    try:
        # 從學習卡片系統獲取古籍統計
        card_stats = card_learning_system.get_ancient_text_statistics()
        
        # 從JSON文件獲取統計
        data_dir = 'data/ancient_texts'
        json_files_count = 0
        total_texts_in_files = 0
        
        if os.path.exists(data_dir):
            for filename in os.listdir(data_dir):
                if filename.endswith('.json'):
                    json_files_count += 1
                    try:
                        file_path = os.path.join(data_dir, filename)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = json.load(f)
                            total_texts_in_files += len(content.get('ancient_texts', []))
                    except:
                        continue
        
        return jsonify({
            'success': True,
            'statistics': {
                'learning_cards': card_stats,
                'json_files': {
                    'files_count': json_files_count,
                    'total_texts': total_texts_in_files
                },
                'categories_info': ancient_text_generator.get_categories_info(),
                'dynasties_info': ancient_text_generator.get_dynasties_info()
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@archive_department_bp.route('/api/archive/validate_json', methods=['POST'])
def validate_json_format():
    """驗證JSON格式是否符合古籍標準"""
    try:
        data = request.get_json()
        json_content = data.get('json_content')
        
        if not json_content:
            return jsonify({
                'success': False,
                'error': '請提供JSON內容'
            }), 400
        
        # 驗證JSON格式
        validation_result = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'suggestions': []
        }
        
        # 檢查必需字段
        required_fields = ['ancient_texts']
        for field in required_fields:
            if field not in json_content:
                validation_result['is_valid'] = False
                validation_result['errors'].append(f'缺少必需字段: {field}')
        
        # 檢查古籍文本格式
        if 'ancient_texts' in json_content:
            texts = json_content['ancient_texts']
            if not isinstance(texts, list):
                validation_result['is_valid'] = False
                validation_result['errors'].append('ancient_texts 必須是數組格式')
            else:
                for i, text in enumerate(texts):
                    text_errors = []
                    
                    # 檢查必需字段
                    required_text_fields = ['title', 'content', 'category']
                    for field in required_text_fields:
                        if field not in text:
                            text_errors.append(f'第{i+1}個文本缺少字段: {field}')
                    
                    # 檢查分類是否有效
                    if 'category' in text:
                        valid_categories = list(ancient_text_generator.get_categories_info().keys())
                        if text['category'] not in valid_categories:
                            validation_result['warnings'].append(
                                f'第{i+1}個文本的分類 "{text["category"]}" 不在標準分類中'
                            )
                    
                    # 檢查難度等級
                    if 'difficulty' in text:
                        valid_difficulties = ['easy', 'medium', 'hard']
                        if text['difficulty'] not in valid_difficulties:
                            validation_result['warnings'].append(
                                f'第{i+1}個文本的難度 "{text["difficulty"]}" 不在有效範圍中'
                            )
                    
                    if text_errors:
                        validation_result['is_valid'] = False
                        validation_result['errors'].extend(text_errors)
        
        # 提供改進建議
        if validation_result['is_valid']:
            validation_result['suggestions'].append('JSON格式正確，可以用於生成學習卡片')
            if 'metadata' not in json_content:
                validation_result['suggestions'].append('建議添加metadata字段以提供更多信息')
        
        return jsonify({
            'success': True,
            'validation': validation_result
        })
    except json.JSONDecodeError:
        return jsonify({
            'success': False,
            'validation': {
                'is_valid': False,
                'errors': ['JSON格式錯誤，請檢查語法'],
                'warnings': [],
                'suggestions': ['使用JSON格式驗證工具檢查語法錯誤']
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@archive_department_bp.route('/api/archive/export_template', methods=['GET'])
def export_json_template():
    """導出JSON模板"""
    try:
        template = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_count': 1,
                'generator_version': '1.0.0',
                'description': '典藏司古籍數據模板'
            },
            'ancient_texts': [
                {
                    'title': '古籍標題',
                    'content': '古籍內容...',
                    'category': '經部',
                    'subcategory': '四書類',
                    'dynasty': '先秦',
                    'author': '作者姓名',
                    'source_library': '來源圖書館',
                    'manuscript_type': '手抄本',
                    'preservation_level': 'good',
                    'difficulty': 'medium',
                    'tags': ['標籤1', '標籤2']
                }
            ]
        }
        
        return jsonify({
            'success': True,
            'template': template,
            'categories': list(ancient_text_generator.get_categories_info().keys()),
            'dynasties': list(ancient_text_generator.get_dynasties_info().keys()),
            'difficulties': ['easy', 'medium', 'hard'],
            'manuscript_types': ['手抄本', '刻本', '寫經', '石刻'],
            'preservation_levels': ['excellent', 'good', 'fair', 'poor']
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
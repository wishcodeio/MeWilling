from flask import Blueprint, jsonify

galaxy_model_api = Blueprint('galaxy_model_api', __name__)

@galaxy_model_api.route('/galaxy_model', methods=['GET'])
def galaxy_model():
    # 這裡實現銀河模型的邏輯
    return jsonify({'message': '銀河模型接口'})

@galaxy_model_api.route('/multi_galaxy_hub', methods=['GET'])
def multi_galaxy_hub():
    # 這裡實現多銀河中心的邏輯
    return jsonify({'message': '多銀河中心接口'})

@galaxy_model_api.route('/cosmic_fine_tuning', methods=['GET'])
def cosmic_fine_tuning():
    # 這裡實現宇宙精調的邏輯
    return jsonify({'message': '宇宙精調接口'})
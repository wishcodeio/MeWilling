from flask import Blueprint, request, jsonify
from ..services.exchange_service import ExchangeService

exchange_bp = Blueprint('exchange', __name__)
exchange_service = ExchangeService()

@exchange_bp.route('/api/exchange/products', methods=['GET'])
def get_products():
    """获取可兑换商品列表"""
    user_id = request.args.get('user_id')
    products = exchange_service.get_available_products(user_id)
    return jsonify(products)

@exchange_bp.route('/api/exchange/redeem', methods=['POST'])
def redeem_product():
    """兑换商品"""
    data = request.json
    result = exchange_service.process_redemption(
        user_id=data['user_id'],
        product_id=data['product_id'],
        delivery_info=data.get('delivery_info')
    )
    return jsonify(result)

@exchange_bp.route('/api/exchange/meditation-value', methods=['GET'])
def calculate_meditation_value():
    """计算修行时间价值"""
    minutes = int(request.args.get('minutes', 0))
    value = exchange_service.calculate_meditation_value(minutes)
    return jsonify({
        'meditation_minutes': minutes,
        'tiwei_coins': value,
        'equivalent_products': exchange_service.get_equivalent_products(value)
    })
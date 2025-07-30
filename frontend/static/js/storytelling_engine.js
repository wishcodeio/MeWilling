// 商增定律的故事化表達
class ShangStorytellingEngine {
    constructor() {
        this.metaphors = {
            "建築比喻": "地基（分母）決定高樓（分子）的穩固性",
            "樹木比喻": "根系（分母）決定枝葉（分子）的繁茂程度",
            "河流比喻": "河床（分母）決定水流（分子）的方向和力量"
        };
    }
    
    generatePersonalizedStory(userType) {
        // 根據用戶類型生成個性化的商增定律故事
        return this.createRelatableNarrative(userType);
    }
}
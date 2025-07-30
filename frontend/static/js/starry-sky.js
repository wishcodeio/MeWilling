// 星空背景效果 JavaScript
class StarrySky {
    constructor() {
        this.init();
    }

    init() {
        this.createStarryBackground();
        this.createStars();
        this.createShootingStars();
        this.createConstellations();
    }

    createStarryBackground() {
        // 创建星空背景容器
        const starryBg = document.createElement('div');
        starryBg.className = 'starry-sky';
        starryBg.id = 'starry-background';
        document.body.insertBefore(starryBg, document.body.firstChild);
    }

    createStars() {
        const starryBg = document.getElementById('starry-background');
        const starCount = 200;

        for (let i = 0; i < starCount; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            
            // 随机星星大小
            const sizes = ['small', 'medium', 'large'];
            const weights = [0.7, 0.25, 0.05]; // 小星星更多
            const randomSize = this.weightedRandom(sizes, weights);
            star.classList.add(randomSize);
            
            // 随机位置
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            
            // 随机动画延迟
            star.style.animationDelay = Math.random() * 3 + 's';
            
            starryBg.appendChild(star);
        }
    }

    createShootingStars() {
        const starryBg = document.getElementById('starry-background');
        
        // 创建流星
        const createShootingStar = () => {
            const shootingStar = document.createElement('div');
            shootingStar.className = 'shooting-star';
            
            // 随机起始位置
            shootingStar.style.left = Math.random() * 100 + '%';
            shootingStar.style.top = Math.random() * 50 + '%';
            
            // 随机动画延迟
            shootingStar.style.animationDelay = Math.random() * 2 + 's';
            
            starryBg.appendChild(shootingStar);
            
            // 动画结束后移除元素
            setTimeout(() => {
                if (shootingStar.parentNode) {
                    shootingStar.parentNode.removeChild(shootingStar);
                }
            }, 3000);
        };
        
        // 定期创建流星
        setInterval(createShootingStar, 3000 + Math.random() * 5000);
        
        // 立即创建第一颗流星
        setTimeout(createShootingStar, 1000);
    }

    createConstellations() {
        const starryBg = document.getElementById('starry-background');
        const constellation = document.createElement('div');
        constellation.className = 'constellation';
        
        // 创建几条星座连线
        for (let i = 0; i < 5; i++) {
            const line = document.createElement('div');
            line.className = 'constellation-line';
            
            // 随机位置和角度
            const angle = Math.random() * 360;
            const length = 50 + Math.random() * 100;
            const x = Math.random() * 80 + 10;
            const y = Math.random() * 80 + 10;
            
            line.style.left = x + '%';
            line.style.top = y + '%';
            line.style.width = length + 'px';
            line.style.transform = `rotate(${angle}deg)`;
            line.style.animationDelay = Math.random() * 4 + 's';
            
            constellation.appendChild(line);
        }
        
        starryBg.appendChild(constellation);
    }

    weightedRandom(items, weights) {
        const totalWeight = weights.reduce((sum, weight) => sum + weight, 0);
        let random = Math.random() * totalWeight;
        
        for (let i = 0; i < items.length; i++) {
            if (random < weights[i]) {
                return items[i];
            }
            random -= weights[i];
        }
        
        return items[items.length - 1];
    }
}

// 页面加载完成后初始化星空背景
document.addEventListener('DOMContentLoaded', function() {
    new StarrySky();
});

// 导出类以供其他脚本使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = StarrySky;
}
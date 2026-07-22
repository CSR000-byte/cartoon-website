"""
卡创 · 星际小猫号 — Flask 后端 API
提供数据存储、RESTful API 接口
"""
import os
import sys
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from models import db, Contact, Character, Story, GalleryItem

# 修复 Windows 控制台 emoji 编码问题
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# --- 初始化应用 ---
app = Flask(__name__, static_folder='..', static_url_path='')

# 数据库配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'cartoon.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 启用 CORS 和数据库
CORS(app)
db.init_app(app)


# --- 静态页面路由 ---
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)


# ============================================
# 📧 联系表单 API
# ============================================
@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """提交联系表单"""
    data = request.get_json()
    if not data:
        return jsonify({'error': '请提供 JSON 数据'}), 400

    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    if not all([name, email, subject, message]):
        return jsonify({'error': '请填写所有字段'}), 400
    if '@' not in email or '.' not in email:
        return jsonify({'error': '请输入正确的邮箱地址'}), 400

    contact = Contact(name=name, email=email, subject=subject, message=message)
    db.session.add(contact)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': f'🚀 星际信号已发送！谢谢 {name} 的留言～',
        'data': contact.to_dict()
    }), 201


@app.route('/api/contact', methods=['GET'])
def list_contacts():
    """获取所有留言（管理用）"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    pagination = Contact.query.order_by(Contact.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    return jsonify({
        'total': pagination.total,
        'pages': pagination.pages,
        'page': page,
        'data': [c.to_dict() for c in pagination.items]
    })


# ============================================
# 🎭 角色 API
# ============================================
@app.route('/api/characters', methods=['GET'])
def list_characters():
    """获取所有角色"""
    characters = Character.query.order_by(Character.sort_order).all()
    return jsonify({'data': [c.to_dict() for c in characters]})


@app.route('/api/characters/<int:char_id>', methods=['GET'])
def get_character(char_id):
    """获取单个角色"""
    char = db.session.get(Character, char_id)
    if not char:
        return jsonify({'error': '角色不存在'}), 404
    return jsonify({'data': char.to_dict()})


@app.route('/api/characters', methods=['POST'])
def create_character():
    """新增角色"""
    data = request.get_json()
    if not data:
        return jsonify({'error': '请提供 JSON 数据'}), 400

    char = Character(
        name=data['name'],
        emoji=data.get('emoji', '🐱'),
        title=data.get('title', ''),
        tags=json.dumps(data.get('tags', []), ensure_ascii=False),
        description=data.get('description', ''),
        color_gradient=data.get('color_gradient', 'linear-gradient(135deg, #6C5CE7, #00CEC9)'),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(char)
    db.session.commit()
    return jsonify({'success': True, 'data': char.to_dict()}), 201


# ============================================
# 📚 故事 API
# ============================================
@app.route('/api/stories', methods=['GET'])
def list_stories():
    """获取所有故事"""
    stories = Story.query.order_by(Story.sort_order).all()
    return jsonify({'data': [s.to_dict() for s in stories]})


@app.route('/api/stories/<int:story_id>', methods=['GET'])
def get_story(story_id):
    """获取单个故事"""
    story = db.session.get(Story, story_id)
    if not story:
        return jsonify({'error': '故事不存在'}), 404
    return jsonify({'data': story.to_dict()})


@app.route('/api/stories', methods=['POST'])
def create_story():
    """新增故事"""
    data = request.get_json()
    if not data:
        return jsonify({'error': '请提供 JSON 数据'}), 400

    story = Story(
        title=data['title'],
        emoji=data.get('emoji', '📖'),
        cover_gradient=data.get('cover_gradient', 'linear-gradient(135deg, #6C5CE7, #00CEC9)'),
        publish_date=data.get('publish_date', ''),
        read_time=data.get('read_time', '5分钟阅读'),
        rating=data.get('rating', 5.0),
        summary=data.get('summary', ''),
        content=data.get('content', ''),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(story)
    db.session.commit()
    return jsonify({'success': True, 'data': story.to_dict()}), 201


# ============================================
# 🎨 画廊 API
# ============================================
@app.route('/api/gallery', methods=['GET'])
def list_gallery():
    """获取画廊所有作品"""
    items = GalleryItem.query.order_by(GalleryItem.sort_order).all()
    return jsonify({'data': [i.to_dict() for i in items]})


@app.route('/api/gallery', methods=['POST'])
def create_gallery_item():
    """新增画廊作品"""
    data = request.get_json()
    if not data:
        return jsonify({'error': '请提供 JSON 数据'}), 400

    item = GalleryItem(
        title=data['title'],
        emoji=data.get('emoji', '🎨'),
        bg_gradient=data.get('bg_gradient', 'linear-gradient(135deg, #6C5CE7, #00CEC9)'),
        tall=data.get('tall', False),
        wide=data.get('wide', False),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({'success': True, 'data': item.to_dict()}), 201


# ============================================
# 📊 统计数据 API
# ============================================
@app.route('/api/stats', methods=['GET'])
def get_stats():
    """获取站点统计数据"""
    return jsonify({
        'characters_count': Character.query.count(),
        'stories_count': Story.query.count(),
        'gallery_count': GalleryItem.query.count(),
        'messages_count': Contact.query.count()
    })


# ============================================
# 🚀 启动入口
# ============================================
def init_db():
    """初始化数据库和种子数据"""
    with app.app_context():
        db.create_all()

        # 如果数据库为空，插入种子数据
        if Character.query.count() == 0:
            seed_data()

        print('✅ 数据库初始化完成')


def seed_data():
    """插入预设种子数据"""
    # --- 角色 ---
    characters = [
        Character(name='小星', emoji='🐱', title='船长',
                  tags=json.dumps(['勇敢', '乐观', '领袖'], ensure_ascii=False),
                  description='星际小猫号的船长！一只来自喵星的勇敢小猫咪，最大的梦想是探索宇宙中每一颗会发光的星球。虽然有时候会迷路，但从不放弃！🌟',
                  color_gradient='linear-gradient(135deg, #6C5CE7, #A29BFE)', sort_order=1),
        Character(name='火狐', emoji='🦊', title='首席工程师',
                  tags=json.dumps(['热情', '聪明', '工程师'], ensure_ascii=False),
                  description='星际小猫号的首席工程师，九条尾巴能同时操作九个控制台。热爱发明创造，最喜欢用星云碎片做小玩意儿送给大家。🔥',
                  color_gradient='linear-gradient(135deg, #FF7675, #FDCB6E)', sort_order=2),
        Character(name='胖达', emoji='🐼', title='厨师长',
                  tags=json.dumps(['温柔', '美食家', '治愈'], ensure_ascii=False),
                  description='星际小猫号的厨师长！虽然看起来慢悠悠的，但做的竹子味星星糖是全宇宙最好吃的。总能用美味的食物安慰旅途中疲惫的伙伴们。🍙',
                  color_gradient='linear-gradient(135deg, #00CEC9, #55EFC4)', sort_order=3),
        Character(name='月兔', emoji='🐰', title='导航员',
                  tags=json.dumps(['敏捷', '聪慧', '导航员'], ensure_ascii=False),
                  description='来自月球基地的通信专家，长长的耳朵能接收到银河系最遥远的信号。负责帮大家找到正确的航线，虽然有时候会跳到奇怪的地方去…🌙',
                  color_gradient='linear-gradient(135deg, #4A3DB7, #A29BFE)', sort_order=4),
        Character(name='彩虹马', emoji='🦄', title='星光加速师',
                  tags=json.dumps(['魔法', '梦幻', '加速师'], ensure_ascii=False),
                  description='拥有星光魔法的神秘独角兽，奔跑时鬃毛会洒出七彩星光。当飞船需要加速时，她会用角发射魔法光束，让小猫号瞬间穿越星云！🦄✨',
                  color_gradient='linear-gradient(135deg, #FF7675, #6C5CE7)', sort_order=5),
        Character(name='企鹅船长', emoji='🐧', title='副船长',
                  tags=json.dumps(['冷静', '战术', '副船长'], ensure_ascii=False),
                  description='来自冰星的前海军将领，任何时候都能保持冷静的判断力。是小星最信赖的副船长，负责制定战术和…在关键时刻把小星从麻烦中捞出来。🐧❄️',
                  color_gradient='linear-gradient(135deg, #00CEC9, #ffffff)', sort_order=6),
    ]

    # --- 故事 ---
    stories = [
        Story(title='月亮上的猫薄荷', emoji='🌿🐱',
              cover_gradient='linear-gradient(135deg, #6C5CE7, #00CEC9)',
              publish_date='2026-07-15', read_time='8分钟阅读', rating=4.9,
              summary='小星在月球背面发现了一片神秘的猫薄荷田。那些猫薄荷在月光下会发出银色的光芒…更神奇的是，它们似乎在唱一首古老的喵星歌谣！',
              content='（完整故事内容待撰写…）', sort_order=1),
        Story(title='流星快递员', emoji='💫📦',
              cover_gradient='linear-gradient(135deg, #FF7675, #FDCB6E)',
              publish_date='2026-06-28', read_time='10分钟阅读', rating=4.8,
              summary='火狐接到了一个紧急任务：在流星雨来临之前，把一颗"愿望星"送到银河另一端的孤独星球。这次快递之旅让她收获了意想不到的友谊…',
              content='（完整故事内容待撰写…）', sort_order=2),
        Story(title='银河钓鱼记', emoji='🎣🌌',
              cover_gradient='linear-gradient(135deg, #00CEC9, #55EFC4)',
              publish_date='2026-06-10', read_time='12分钟阅读', rating=4.7,
              summary='胖达拿着他用竹子做的钓竿，坐在小猫号的甲板边缘，试图从银河里钓上"星星鱼"。没想到，他真的钓上来了——一只会说话的星尘水母！',
              content='（完整故事内容待撰写…）', sort_order=3),
        Story(title='星星糖果铺', emoji='🍬⭐',
              cover_gradient='linear-gradient(135deg, #FDCB6E, #FF7675)',
              publish_date='2026-05-20', read_time='6分钟阅读', rating=5.0,
              summary='彩虹马在星云市场开了一家小小的糖果铺。她用星光魔法制作各种神奇糖果——吃下蓝色糖果可以飘浮，吃下粉色糖果可以让头发变成彩虹色！',
              content='（完整故事内容待撰写…）', sort_order=4),
    ]

    # --- 画廊 ---
    gallery = [
        GalleryItem(title='星云棒棒糖 🌈', emoji='🍭🌈',
                    bg_gradient='linear-gradient(135deg, #6C5CE7, #FF7675, #FDCB6E)',
                    tall=False, wide=False, sort_order=1),
        GalleryItem(title='小星船长 🌟', emoji='🐱🚀',
                    bg_gradient='linear-gradient(180deg, #1a1a3e, #6C5CE7, #00CEC9)',
                    tall=True, wide=False, sort_order=2),
        GalleryItem(title='月光猫薄荷田 🌿', emoji='🌿🌙',
                    bg_gradient='linear-gradient(135deg, #0a0a1a, #4A3DB7)',
                    tall=False, wide=False, sort_order=3),
        GalleryItem(title='银河穿越全景 🌌', emoji='🚀✨🌌💫⭐🌟',
                    bg_gradient='linear-gradient(90deg, #0a0a1a, #1a1a3e, #6C5CE7, #FF7675, #00CEC9)',
                    tall=False, wide=True, sort_order=4),
        GalleryItem(title='火狐的工作台 🔧', emoji='🔧🦊',
                    bg_gradient='linear-gradient(135deg, #FF7675, #FDCB6E)',
                    tall=False, wide=False, sort_order=5),
        GalleryItem(title='星星糖果铺 🍬', emoji='🍬✨',
                    bg_gradient='linear-gradient(135deg, #FF7675, #FDCB6E, #55EFC4)',
                    tall=False, wide=False, sort_order=6),
        GalleryItem(title='月兔的信号塔 📡', emoji='🐰📡',
                    bg_gradient='linear-gradient(180deg, #4A3DB7, #A29BFE, #00CEC9)',
                    tall=True, wide=False, sort_order=7),
        GalleryItem(title='冰星基地 ❄️', emoji='🐧❄️',
                    bg_gradient='linear-gradient(135deg, #00CEC9, #55EFC4, #ffffff)',
                    tall=False, wide=False, sort_order=8),
        GalleryItem(title='星光魔法秀 🌟', emoji='🦄✨',
                    bg_gradient='linear-gradient(135deg, #6C5CE7, #FF7675, #FDCB6E, #55EFC4)',
                    tall=False, wide=False, sort_order=9),
        GalleryItem(title='胖达的星空厨房 🍪', emoji='🐼🍪⭐🥮🍙',
                    bg_gradient='linear-gradient(90deg, #1a1a3e, #FDCB6E, #FF7675)',
                    tall=False, wide=True, sort_order=10),
        GalleryItem(title='流星雨之夜 💫', emoji='💫🌠',
                    bg_gradient='linear-gradient(135deg, #0a0a1a, #6C5CE7)',
                    tall=False, wide=False, sort_order=11),
        GalleryItem(title='星云市场 🎪', emoji='🎪🌟',
                    bg_gradient='linear-gradient(135deg, #FF7675, #6C5CE7, #00CEC9)',
                    tall=False, wide=False, sort_order=12),
    ]

    db.session.add_all(characters)
    db.session.add_all(stories)
    db.session.add_all(gallery)
    db.session.commit()
    print(f'🌱 种子数据已插入：{len(characters)}个角色、{len(stories)}篇故事、{len(gallery)}幅画廊作品')


if __name__ == '__main__':
    init_db()
    print('🐱🚀 卡创 · 星际小猫号 — 后端已启动！')
    print('🌐 API 地址: http://localhost:5000')
    print('📋 API 端点:')
    print('   GET  /api/characters  — 获取所有角色')
    print('   POST /api/characters  — 新增角色')
    print('   GET  /api/stories     — 获取所有故事')
    print('   POST /api/stories     — 新增故事')
    print('   GET  /api/gallery     — 获取所有画廊')
    print('   POST /api/gallery     — 新增画廊作品')
    print('   POST /api/contact     — 提交联系表单')
    print('   GET  /api/contact     — 查看留言列表')
    print('   GET  /api/stats       — 站点统计')
    app.run(debug=True, host='0.0.0.0', port=5000)

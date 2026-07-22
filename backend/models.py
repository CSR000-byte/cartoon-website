"""卡创 · 星际小猫号 — 数据库模型"""
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Contact(db.Model):
    """联系表单提交"""
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Character(db.Model):
    """角色数据"""
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    emoji = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    tags = db.Column(db.String(200), nullable=False)  # JSON array stored as string
    description = db.Column(db.Text, nullable=False)
    color_gradient = db.Column(db.String(100), default='linear-gradient(135deg, #6C5CE7, #00CEC9)')
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        import json
        return {
            'id': self.id,
            'name': self.name,
            'emoji': self.emoji,
            'title': self.title,
            'tags': json.loads(self.tags) if self.tags else [],
            'description': self.description,
            'color_gradient': self.color_gradient,
            'sort_order': self.sort_order
        }


class Story(db.Model):
    """故事数据"""
    __tablename__ = 'stories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    emoji = db.Column(db.String(20), nullable=False)
    cover_gradient = db.Column(db.String(100), default='linear-gradient(135deg, #6C5CE7, #00CEC9)')
    publish_date = db.Column(db.String(20), nullable=False)
    read_time = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Float, default=5.0)
    summary = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, default='')  # 完整故事内容
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'emoji': self.emoji,
            'cover_gradient': self.cover_gradient,
            'publish_date': self.publish_date,
            'read_time': self.read_time,
            'rating': self.rating,
            'summary': self.summary,
            'content': self.content,
            'sort_order': self.sort_order
        }


class GalleryItem(db.Model):
    """画廊作品"""
    __tablename__ = 'gallery_items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    emoji = db.Column(db.String(30), nullable=False)
    bg_gradient = db.Column(db.String(100), default='linear-gradient(135deg, #6C5CE7, #00CEC9)')
    tall = db.Column(db.Boolean, default=False)
    wide = db.Column(db.Boolean, default=False)
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'emoji': self.emoji,
            'bg_gradient': self.bg_gradient,
            'tall': self.tall,
            'wide': self.wide,
            'sort_order': self.sort_order
        }

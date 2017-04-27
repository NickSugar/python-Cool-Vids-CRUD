from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __repr__(self):
        return '<User %r' % self.name

class Vids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String)
    url = db.Column(db.String)
    year = db.Column(db.Integer)

    def __init__(self, user_id, title, url, year):
        self.user_id = user_id
        self.title = title
        self.url = url
        self.year = year

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'user_id': self.user_id,
            'title': self.title,
            'url': self.url,
            'year': self.year
        }

    def __repr__(self):
        return '<Vid %r>' % self.title

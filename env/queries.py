from flask import jsonify
from app import db, models
import json

def get_all_vids():
    return jsonify(data=[vid.serialize for vid in models.Vids.query.all()])

def post_vid(vid):
    data = json.loads(vid)

    print(data)

    new_vid = models.Vids(
        user_id= data['user_id'],
        title= data['title'],
        url= data['url'],
        year= data['year'])

    db.session.add(new_vid)
    db.session.commit()
    return new_vid

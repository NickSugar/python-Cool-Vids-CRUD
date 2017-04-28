from flask import jsonify, make_response
from app import db, models
import json

def get_all_vids():
    return jsonify(data=[vid.serialize for vid in models.Vids.query.all()])

def post_vid(vid):
    vid_dict = json.loads(vid)

    new_vid = models.Vids(
        user_id= vid_dict['user_id'],
        title= vid_dict['title'],
        url= vid_dict['url'],
        year= vid_dict['year'])

    db.session.add(new_vid)
    db.session.commit()

    return jsonify(new_vid.serialize)

def get_vid(vid_id):
    vid = models.Vids.query.get(vid_id)
    if vid is not None:
        return jsonify(data=[vid.serialize])
    else: return make_response('vid does not exist', 404)

def patch_vid(vid_id, vid_patch):

    vid_patch_dict = json.loads(vid_patch)
    vid_patch_keys = list(vid_patch_dict.keys())

    vid = models.Vids.query.get(vid_id)
    if vid is not None:
        for index, key in enumerate(vid_patch_keys):
            if key == 'title':
                vid.title = vid_patch_dict[vid_patch_keys[index]]
            elif key == 'url':
                vid.url = vid_patch_dict[vid_patch_keys[index]]
            else :
                vid.year = vid_patch_dict[vid_patch_keys[index]]

        db.session.commit()
        return jsonify(data=[models.Vids.query.get(vid_id).serialize])
    else: return make_response('vid does not exist', 404)

def delete_vid(vid_id):
    vid = models.Vids.query.get(vid_id)

    if vid is not None:
        deleted_vid = jsonify(data=[vid.serialize])
        db.session.delete(vid)
        db.session.commit()
        return deleted_vid
    else: return make_response('vid does not exist', 404)




















#

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/coolvids'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models
import queries

@app.route('/vids', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return queries.get_all_vids()
    if request.method == 'POST':
        return queries.post_vid(request.data)

@app.route('/vids/<int:vid_id>', methods=['GET', 'PATCH', 'DELETE'])
def oneVid(vid_id):
    if request.method == 'GET':
        return queries.get_vid(vid_id)
    elif request.method == 'PATCH':
        return queries.patch_vid(vid_id, request.data)
    else: return queries.delete_vid(vid_id)

if __name__ == '__main__':
    app.debug = True
    app.run()






#

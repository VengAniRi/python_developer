import flask
from flask.views import MethodView
from flask import request, Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = flask.Flask('app')
DSN = 'postgresql://postgres:postgres@localhost:5432/flask_api'
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=DSN)
db = SQLAlchemy(app)


class Advert(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(50), nullable=False)
    owner = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


db.create_all()


class AdvertView(MethodView):

    def get(self, advert_id):
        print('GETTING')
        advert = Advert.query.get(advert_id)
        if advert is None:
            raise NotFoundError
        return flask.jsonify({
            'id': advert.id,
            'owner': advert.owner,
            'header': advert.header,
            'description': advert.description,
            'pub_date': advert.pub_date
        })

    def post(self):
        advert_data = request.json
        advert = Advert(**advert_data)
        db.session.add(advert)
        db.session.commit()
        return flask.jsonify({'id': advert.id})

    def delete(self, advert_id):
        advert = Advert.query.get(advert_id)
        if advert is None:
            raise NotFoundError
        db.session.delete(advert)
        db.session.commit()
        return flask.jsonify({'id': advert.id})


class NotFoundError(Exception):
    message = 'Not Found'
    status_code = 404


@app.errorhandler(NotFoundError)
def error_handler(error):
    response = flask.jsonify({'error': error.message})
    response.status_code = error.status_code
    return response


app.add_url_rule('/api/adverts/<int:advert_id>',
                 view_func=AdvertView.as_view('advert_get'), methods=['GET'])

app.add_url_rule('/api/adverts/', view_func=AdvertView.as_view('advert_post'),
                 methods=['POST'])

app.add_url_rule('/api/adverts/<int:advert_id>',
                 view_func=AdvertView.as_view('advert_del'), methods=['DELETE'])

app.run(port=8000)

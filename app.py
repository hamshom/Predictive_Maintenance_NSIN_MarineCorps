import logging
import os
import config
from api import api


from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

from models import db

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()

model = pickle.load(open('model.pkl', 'rb'))
# model = pickle.load(open('regressor.pkl','rb'))

def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object('config')
    api.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)


    # to tell flask what url shoud trigger the function home()
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/predict', methods=['POST'])
    def predict():
        '''
        For rendering results on HTML GUI
        '''
        int_features = [int(x) for x in request.form.values()]

        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        output = round(prediction[0], 2)

        if output > 1000:
            fail = "True"
        else:
            fail = "False"

        return render_template('index.html', prediction_text='Will the equipment fail: {}'.format(fail))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
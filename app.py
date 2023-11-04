from flask import Flask,request
from flask_restful import Resource, Api
import pickle
import pandas as pd
from flask_cors import CORS
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)
CORS(app)

api = Api(app)

class prediction(Resource):

  #@app.route('/post_endpoint', methods=['GET'])
  def get(self,td,hg,mrt,con,lat,lon):
    data = {
    'X1 transaction date':[td],
    'X2 house age':[hg],
    'X3 distance to the nearest MRT station':[mrt],
    'X4 number of convenience stores':[con],
    'X5 latitude':[lat],
    'X6 longitude':[lon],
    }
    dff = pd.DataFrame(data)
    model = pickle.load(open('model_pickle','rb'))
    prediction = model.predict(dff)
    prediction = float(prediction[0])
    return str(prediction)

    def post(self,):
        data = request.form['data_key']
        # Process the data

        return 'Data received and processed.'

api.add_resource(prediction,'/prediction/<int:td>/<float:hg>/<float:mrt>/<int:con>/<float:lat>/<float:lon>')
if __name__ == '__main__':
    app.run()

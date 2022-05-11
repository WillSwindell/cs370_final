import flask
import pickle
import pandas as pd
import numpy as np
from functions import cleanup

with open(f'model/logit_model_nba.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods = ['POST', 'GET'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        h_name = flask.request.form['Home Team Name']
        a_name = flask.request.form['Away Team Name']
        h_pct = flask.request.form['Home Team Win Percentage']
        a_pct = flask.request.form['Away Team Win Percentage']
        h_hr = flask.request.form['Home Team Home Record']
        h_ar = flask.request.form['Home Team Away Record']
        a_hr = flask.request.form['Away Team Home Record']
        a_ar = flask.request.form['Away Team Away Record']
        h_inj = flask.request.form['Home Team Injuries']
        a_inj = flask.request.form['Away Team Injuries']
        h_fg = flask.request.form['Home Team FG Percentage']
        a_fg = flask.request.form['Away Team FG Percentage']
        h_pts = flask.request.form['Home Team PPG']
        a_pts = flask.request.form['Away Team PPG']
        input_variables = pd.DataFrame([[h_pct, a_pct, h_hr, h_ar, a_hr, a_ar, h_inj, a_inj, h_fg, a_fg, h_pts, a_pts]],
                                       columns=['HOME_PCT', 'AWAY_PCT', 'HOME_hr', 'HOME_ar', 'AWAY_hr', 'AWAY_ar', 'HOME_inj', 'AWAY_inj', 'H_FG_pct', 'A_FG_pct',  'H_PPG', 'A_PPG'],
                                       dtype=float)

        cleaned = cleanup(input_variables)
        prediction = model.predict(cleaned)[0]
        pred = ''
        if(prediction == 1):
            pred = h_name
        else:
            pred = a_name


        return flask.render_template('main.html',
                                     original_input={'Home Team Name': h_name,
                                                     'Away Team Name': a_name,
                                                     'Home Team Win Percentage':h_pct,
                                                     'Away Team Win Percentage':a_pct,
                                                     'Home Team Home Record':h_hr,
                                                     'Home Team Away Record':h_ar,
                                                     'Away Team Home Record':a_hr,
                                                     'Away Team Away Record':a_ar,
                                                     'Home Team Injuries':h_inj,
                                                     'Away Team Injuries':a_inj,
                                                     'Home Team FG Percentage':h_fg,
                                                     'Away Team FG Percentage':a_fg,
                                                     'Home Team PPG':h_pts,
                                                     'Away Team PPG':a_pts},
                                     result=pred,
                                     )

if __name__ == '__main__':
    app.debug = True
    app.run()

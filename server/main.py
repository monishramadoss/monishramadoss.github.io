import flask
app = flask.Flask(__name__)
@app.route('/data/')
def api(api):
    return flask.render_template('index.html')


if __name__ == '__main__':
    # app.run(debug=True, host="https://monishramadoss.github.io", port=3000)
    app.run(debug=True)
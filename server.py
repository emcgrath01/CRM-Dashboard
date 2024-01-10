from flask import Flask, send_file

app = Flask(__name__)

@app.route('/your_geojson_file')
def get_geojson():
    return send_file('output.geojson')

if __name__ == '__main__':
    app.run(debug=True)


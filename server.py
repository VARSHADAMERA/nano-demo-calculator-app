# from flask import Flask

# app = Flask(__name__)


# @app.route("/calculator/greeting", methods=['GET'])
# def greeting():
#     return ''

# @app.route("/calculator/add", methods=['POST'])
# def add():
#     return ''

# @app.route("/calculator/subtract", methods=['POST'])
# def subtract():
#     return ''

# if __name__ == '__main__':
#     app.run(port=8080,host='0.0.0.0')


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello, welcome to the calculator API!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()

    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Please provide both num1 and num2 in the request JSON.'}), 400

    num1 = data['num1']
    num2 = data['num2']
    
    try:
        result = num1 + num2
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()

    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Please provide both num1 and num2 in the request JSON.'}), 400

    num1 = data['num1']
    num2 = data['num2']
    
    try:
        result = num1 - num2
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

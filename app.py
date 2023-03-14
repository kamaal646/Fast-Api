# flask applications built around request and responses.
# request that your browser does. e.g safari, google chrome and internet explorer.
# whenever you go to any website, you are making a request and there is a computer summar on the internet that
# is receiving the request and that computer has something like a flask app in it. so now flask app receives
# a request from your browser and then decide what to do it and then return back in response. e.g one request 
# may be to ask a certain pages (Home page).
# Rest Api usually returns texts.
# POST - used to receive data
# GET - used to send data back only
# JSON always take single quotes not double quotes.
# JSON is not a dictionary, JSON is a text. it's a long string.
# JSON returns a dictionary not a list, so to deal with json convert first a list into dictionary.

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/ocr')
def find_ocr():
    
    import webbrowser
    webbrowser.open_new_tab('https://ocr.space/')
    return "Free OCR is opened, you can now try it"

app.run(port=5000) 



# stores = [
#      {
#          'name': 'My Wonderful Store',
#          'item': [
#            {
#              'name': 'My Item',
#              'price': 15.99
#            }                     
#          ]
#      }
# ]

# @app.route('/')  # 'http://www.google.com/' 
# def Home():
    # return render_template('index.html') 

# # POST /store data: {name:}
# @app.route('/store', methods=['POST'])  
# def create_store():
#   request_data = request.get_json()
#   new_store = {
#     'name': request_data['name'],
#     'items': []
#   }
#   stores.append(new_store)
#   return jsonify(new_store)

# # GET /store/<string:name>
# @app.route('/store/<string:name>')   # 'http://127.0.0.1:5000/store/some_name'
# def get_store(name):                 
#   for store in stores:
#     if store['name'] == name:
#       return jsonify(store)
#   return jsonify({'message': 'store not found'})  

# # GET /store
# @app.route('/store')
# def get_stores():
#     return jsonify({'stores': stores})           # making dictionary from list

# # POST /store/<string:name>/item {name:, price:}
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_item_in_store(name):
#   request_data = request.get_json()  
#   for store in stores:
#     if store['name'] == name:
#       new_item = {
#         'name': request_data['name'],
#         'price': request_data['price']
#       }
#       store['items'].append(new_item)
#       return jsonify(new_item)
#   return jsonify({'message': 'store not found'})

# # GET /store/<string:name>/item
# @app.route('/.store/<string:name>/item')
# def get_items_store(name):
#     for store in stores:
#       if store['name'] == name:
#         return jsonify({'items': store['items']})
#     return jsonify({'message': 'store not found'})


#app.run(port=5000)


   

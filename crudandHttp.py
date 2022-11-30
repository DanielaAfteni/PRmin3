from flask import Flask, request, jsonify
from threading import Thread
import requests
import threading

app = Flask(__name__)

# get the requests
# GET 
# request to get all foods
@app.route('/foods', methods = ['GET'])
def get_foods():
    # print all foods
    print(({'Foods' : (list(map(public_foods, foods)))}), end='\n')
    return jsonify({'Foods' : list(map(public_foods, foods))})

# function - generates a public version of a food
def public_foods(food):
    new_foods = {}
    for field in food:
        new_foods[field] = food[field]
    return new_foods 

# GET 
# request to get a single food
@app.route('/foods/<int:id>', methods = ['GET'])
def get_food(id):
    food = list(filter(lambda l: l['id'] == id, foods))
    # print food
    print(({'Food' : public_foods(food[0])}), end='\n')
    return jsonify({'Food' : public_foods(food[0])})
    

# POST 
# request to create a new food
@app.route('/foods', methods = ['POST'])
def create_food():
    food = {
        'id' : request.json['id'],
        'name' : request.json['name'],
        'preparation_time' : request.json.get('preparation_time',  ""),
        'cooking_apparatus' : 'oven'  
    }
    foods.append(food)
    # print created food
    print(({'Food' : public_foods(food)}), end='\n')
    return jsonify({'Food' : public_foods(food)})


# PUT 
# request to update a food
@app.route('/foods/<int:id>', methods = ['PUT'])
def update_food(id):
    food = list(filter(lambda l: l['id'] == id, foods))
    food[0]['name'] = request.json.get('name', food[0]['name'])
    food[0]['preparation_time'] = request.json.get('preparation_time', food[0]['preparation_time'])
    food[0]['cooking_apparatus'] = request.json.get('cooking_apparatus', food[0]['cooking_apparatus'])
    # print modified food
    print(({'food' : public_foods(food[0])}), end='\n')
    return jsonify({'food' : public_foods(food[0])})


# DELETE 
# request to delete a food
@app.route('/foods/<int:id>', methods = ['DELETE'])
def delete_food(id):
    food = list(filter(lambda l: l['id'] == id, foods))
    foods.remove(food[0])
    return jsonify({'result' : True})


def crudPOSTrequest():
    payload = dict({'id': 11, 'name': "Frigarui", 'preparation_time': "60 min"})
    requests.post('http://localhost:8080/foods', json = payload, timeout = 0.0000000001)

def crudGETrequest():
    requests.get('http://localhost:8080/foods/11', timeout = 0.0000000001)
    requests.get('http://localhost:8080/foods', timeout = 0.0000000001)

def crudPUTrequest():
    payload = dict({'name': "Placinta", 'preparation_time': "50 min", 'cooking_apparatus': 'stove'})
    requests.put('http://localhost:8080/foods/11', json = payload, timeout = 0.0000000001)

def crudDELETErequest():
    requests.delete('http://localhost:8080/foods/11')

foods = [
    {
        'id': 1,
        'name': 'pizza',
        'preparation_time': '20 min',
        'cooking_apparatus': 'oven'
    },
    {
        'id': 2,
        'name': 'salad',
        'preparation_time': '10 min',
        'cooking_apparatus': 'stove'
    },
    {
        'id': 3,
        'name': 'zeama',
        'preparation_time': '7 min',
        'cooking_apparatus': 'stove'
    },
    {
        'id': 4,
        'name': 'Scallop Sashimi with Meyer Lemon Confit',
        'preparation_time': '32 min',
        'cooking_apparatus': 'stove'
    },
    {
        'id': 5,
        'name': 'Island Duck with Mulberry Mustard',
        'preparation_time': '35 min',
        'cooking_apparatus': 'oven'
    },
    {
        'id': 6,
        'name': 'Waffles',
        'preparation_time': '10 min',
        'cooking_apparatus': 'stove'
    },
    {
        'id': 7,
        'name': 'Aubergine',
        'preparation_time': '20 min',
        'cooking_apparatus': 'stove'
    },
    {
        'id': 8,
        'name': 'Lasagna',
        'preparation_time': '30 min',
        'cooking_apparatus': 'oven'
    },
    {
        'id': 9,
        'name': 'Burger',
        'preparation_time': '15 min',
        'cooking_apparatus': 'oven'
    },
    {
        'id': 10,
        'name': 'Gyros',
        'preparation_time': '15 min',
        'cooking_apparatus': 'stove'
    }
]

def main():
    main_thread = Thread(target = lambda: app.run(host = '0.0.0.0', port = 8080, debug = False, use_reloader = False), daemon= True)
    main_thread.start()
    #Thread0 = threading.Timer(1.0, crudGETrequest)
    Thread1 = threading.Timer(1.0, crudPOSTrequest)  
    Thread2 = threading.Timer(2.0, crudGETrequest)
    Thread3 = threading.Timer(4.0, crudPUTrequest)
    Thread4 = threading.Timer(6.0, crudDELETErequest)
    #Thread0.start()
    Thread1.start() 
    Thread2.start()
    Thread3.start()
    Thread4.start()

main()
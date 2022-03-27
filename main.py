from flask import Flask , jsonify , request 

app = Flask(__name__)

data = [
    {
        "Contact": "8875596384"
        "Name":"Pranavi"
        "done": false,
        "id" : 1
    },
    {
        "Contact" : "9511510342"
        "Name" : "My mother"
        "done" : false,
        "id" : 2

    }
]

contact = {

    'id' : tasks[-1]['id'] + 1,
    'Name':request.json['Name'],
    'Contact':request.json.get('Contact', ""),
    'done':False
}


@app.route("/add-data" , methods=["POST"])

def add_task():

    if not request:json:
        return jsonify({
            "status":"error"
            "message":"Please provide the data!"
        },400)

     task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })




@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 




if (__name__ == "__main__"):
    app.run(debug=True)
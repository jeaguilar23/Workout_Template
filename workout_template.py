import zmq
import json #Python data like list/dictionaries are sent as strings

#hard coded workout templates
templates = {
    "push": [
        {"exercise": "Bench Press", "sets": 4, "reps": 8},
        {"exercise": "Overhead Press", "sets": 3, "reps": 10},
        {"exercise": "Triceps Dips", "sets": 3, "reps": 12}],
    "leg": [
        {"exercise": "Squats", "sets": 4, "reps": 8},
        {"exercise": "Lunges", "sets": 3, "reps": 12},
        {"exercise": "Calf Raises", "sets": 3, "reps": 15}],
    "full body": [
        {"exercise": "Bodyweight Squats", "sets": 3, "reps": 12},
        {"exercise": "Push-ups", "sets": 3, "reps": 10},
        {"exercise": "Plank", "sets": 3, "reps": "30 sec"}]
}

context = zmq.Context() #connection environment for ZeroMQ
socket = context.socket(zmq.REP) #REP (reply) socket (server side)
socket.bind("tcp://*:5555")

print('Workout Template Generator is running on Port 5555')

while True:
    message = socket.recv_string() #waiting for the request
    command = message.strip().lower() #remove spaces and lowercase string

    if command.startswith("get template"):
        templateName = command[len("get template "):].strip()
        if templateName in templates:
            response = json.dumps(templates[templateName]) #convert template to a JSON string
        else:
            response = json.dumps({"Error! Template not found, please try again!"})
    else:
        response = json.dumps({"Error!: Invalid command. Try: get template [template_name]"})
    socket.send_string(response) #sends back the template or error message
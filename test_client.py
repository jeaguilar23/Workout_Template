import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555") #connect to microservice using port

socket.send_string("Get template push") #"push" is interchangeable with "push", "leg", or "full body"
template = socket. recv_string()

print("Workout Template:")
for exercise in json.loads(template):
    print(f"- {exercise['exercise']}: {exercise['sets']} sets of {exercise['reps']}")


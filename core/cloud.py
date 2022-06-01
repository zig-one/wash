import socketio

sio = socketio.Client(logger=True, engineio_logger=True)


@sio.event
def connect():
    print('connection established')
    sio.emit('client', {'data': 'connection established'})


@sio.on('server')
def on_message(data):
    print('I get :',data['data'])


@sio.on('response')
def on_message(data):
    print('I get response:',data['data'])



# @sio.event
# def message(data):
#     print('message received with ', data)
#     sio.emit('client', {'response': 'my response'})

# @sio.event
# def connect_error():
#     print("The connection failed!")
#     sio.disconnect()

# @sio.event
# def disconnect():
#     print('disconnected from server')
#     sio.disconnect()
# sio.re

sio.connect('http://localhost:5000')

# while 1:
#     a=input()
#     # sio.
#     sio.emit('client', {'data': str(a)})
sio.wait()


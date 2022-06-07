
import socketio
import time
from core.act_queue import q as queueA
# from act_queue import q as queueA
from core import actions
from core import status


sio = socketio.Client()



def mydisconnected():
    if(status.connected):
        status.connected=False
        print("disconnected")
        queueA.put(actions.hide())


def myconnected():
    if(not status.connected):
        status.connected=True
        print("connected")
        # queueA.put(actions.hide())

def chosed


class client():

    # , engineio_logger=True logger=True)

    @sio.event
    def connect():
        # print('connection established')
        sio.emit('client', {'data': 'connection established'})
        # status.connected=True
        myconnected()

    @sio.on('server')
    def on_message(data):
        print('I get :',data['data'])


    @sio.on('response')
    def on_message(data):
        # global chosen
        # print('Client get response:',data['data'])
        print('Client get response:',data)
        print((data['chosen']))
        if(data['chosen']=='1' and (not status.chosen)):
            print("!!!!!chose")
            status.chosen=True
        elif (data['chosen']=='0' and (status.chosen)):
            print("!!!!!release")
            status.chosen=False
        else:
            print("maintain")



    @sio.event
    def message(data):
        print('message received with ', data)
        sio.emit('client', {'response': 'my response'})
        

    # @sio.event
    # def connect_error():
    #     print("The connection failed!")
    #     sio.disconnect()

    @sio.event
    def disconnect():
        mydisconnected()
        # sio.disconnect()
    # sio.re
    
    def start(self):
        while True:
            try:
                sio.connect('http://localhost:5000')
                while sio.connected:
                    a=input()
                    sio.emit('client', {'data': str(a)})
                # sio.wait()
            except BaseException as e:
                mydisconnected()
                pass
            time.sleep(5)
    # while 1:
    #     # sio.

    # sio.wait()


cli=client()


if __name__ == '__main__':
    cli.start()
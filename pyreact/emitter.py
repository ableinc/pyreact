from pubsub import pub


class EventEmitter:
    @staticmethod
    def subscribe(listener, topic):
        pub.subscribe(listener, topic)

    @staticmethod
    def send(topic, data, args=None):
        pub.sendMessage(topic, data=data, args=args)

# An observer - could inherit from Dispatcher or any other class
class EventListener:
    def event(self, *args, **kwargs):
        return kwargs.get('data')
    
    def func(self, data, args):
        if args is not None:
            data(args[0], args[1])
        else:
            data()


# emitter = MyEmitter()
# listener = MyListener()

# emitter.bind(on_state=listener.on_emitter_state)
# emitter.bind(new_data=listener.on_new_data)
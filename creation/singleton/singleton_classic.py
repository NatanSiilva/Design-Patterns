class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class SingletonLazy(object):
    __instance = None
    def __init__(self):
        if not SingletonLazy.__instance:
            print("Instance does not exist, creating")
        
        SingletonLazy.__instance = self

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazy()
        return cls.__instance

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    

class SingletonMeta(metaclass=MetaSingleton):
    def display(self):
        return id(self)
    

def main():
    s = Singleton()
    print('Singleton instance one created: ', s)
    s1 = Singleton()
    print('Singleton instance two created: ', s1)
    print("Singleton instance one is the same as Singleton instance two: ", s == s1)


    print("=========================================================================\n")

    s = SingletonLazy()
    print("SingletonLazy instance one created: ", s.get_instance())
    s1 = SingletonLazy()
    print("SingletonLazy instance two created: ", s1.get_instance())
    print("SingletonLazy instance one is the same as SingletonLazy instance two: ", s == s1)


    print("=========================================================================\n")

    s = SingletonMeta()
    print("SingletonMeta instance one created: ", s.display())
    s1 = SingletonMeta()
    print("SingletonMeta instance two created: ", s1.display())
    print("SingletonMeta instance one is the same as SingletonMeta instance two: ", s == s1)



if __name__ == "__main__":
    main()
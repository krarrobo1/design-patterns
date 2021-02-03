from abc import ABCMeta, abstractclassmethod, abstractstaticmethod


class IError(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_message():
        """ implementation """


class NotFoundError(IError):
    def __init__(self):
      self.message = "Resource not found!"

    def print_message(self):
        print(self.message)
        return

class UnauthorizedError(IError):
    def __init__(self):
      self.message = "You're not authorized to do this!"

    def print_message(self):
        print(self.message)
        return

class ErrorFactory():
    @staticmethod
    def get_error(type):
        if type == 'notfound':
            return NotFoundError()
        elif type == 'unauthorized':
            return UnauthorizedError()

if __name__ == '__main__':
    not_found = ErrorFactory.get_error('notfound')
    not_found.print_message()
    
            

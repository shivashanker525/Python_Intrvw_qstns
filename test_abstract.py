from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def debit(self):
        pass

class IDBi(Bank):
    def debit(self):
        print('debit method implemented.')

    def credit(self):
        print('credit method implemented.')

obj = IDBi()
obj.debit()
obj.credit()
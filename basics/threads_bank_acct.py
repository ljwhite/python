import threading
import time
import random

class BankAccount(threading.Thread):
    acct_balance = 100
    def __init__(self, name, money_request):
        threading.Thread.__init__(self)
        self.name = name
        self.money_request = money_request

    def run(self):
        # acquire -> requests a lock
        thread_lock.acquire()
        BankAccount.get_money(self)
        # release -> releases lock
        thread_lock.release()

    @staticmethod
    def get_money(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name, customer.money_request, time.strftime("%H:%M:%S", time.gmtime())))
        if BankAccount.acct_balance - customer.money_request > 0:
            BankAccount.acct_balance -= customer.money_request
            print("New Account Balance is : ${}".format(BankAccount.acct_balance))
        else:
            print("Not enough money in account")
            print("Current Account Balance is : ${}".format(BankAccount.acct_balance))
        time.sleep(3)

# global variable for threading.Lock()
thread_lock = threading.Lock()
doug = BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally", 50)

doug.start()
paul.start()
sally.start()

doug.join()
paul.join()
sally.join()

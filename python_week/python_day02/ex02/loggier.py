import time
from random import randint


def log(function):

    def function_time(*args):

        time_before = time.time()
        value = function(*args)
        time_after = time.time()
        exec_time = time_after - time_before
        if exec_time > 0.1:
            exec_time = round(exec_time, 3)
            time_type = "s"
        else:
            exec_time = round(exec_time * 1000, 3)
            time_type = "ms"
        function_name = function.__name__.replace("_", " ").title()
        with open("machine.log", "a") as file:
            file.write("(ajeannot)Running: {0}          [ exec-time = {1} {2} ]\n".format(function_name, exec_time, time_type))
        return value

    return function_time

class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
     if self.water_level > 20:
         return True
     else:
         print("Please add water!")
         return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    open('machine.log', 'w').close()
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)

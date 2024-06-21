# Starting a Thread
# Starting a Thread
# Extending the Thread class
from time import sleep, ctime

from threading import Thread

# Custom thread class
class CustomThread(Thread):
    def __init__(self, name):
        super().__init__()  # Call the base class constructor
        self.name = name

    # Override the run function
    def run(self):
        sleep(2)  # Block for a moment
        print(f'{ctime()} {self.name}: This is coming from another thread')

# Create the thread
thread = CustomThread("MyThread")

# Start the thread
thread.start()

# Wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish')
thread.join()
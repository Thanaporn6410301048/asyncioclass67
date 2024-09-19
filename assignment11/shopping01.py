import time
import asyncio
from asyncio import Queue
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time
        


class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products


# we implement a checkout_customer method that acts as a consumer.
# As long as there is data in the queue, this method will continue to loop. 
# During each iteration, it uses a get method to retrieve a Customer instance. 
# 
# If there is no data in the queue, it will wait. 
# 
# After retrieving a piece of data (in this case, a Customer instance), 
# it iterates through the products attribute and uses asyncio.sleep to simulate the checkout process.
# 
# After finishing processing the data, 
# we use queue.task_done() to tell the queue that the data has been successfully processed.
async def checkout_customer(queue: Queue, cashier_number: int):
    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f'the cashier {cashier_number} is checking out customer {customer.customer_id}...')

        for product in customer.products:
            print(
                f'the cashier {cashier_number}'
                f'will checkout customer {customer.customer_id}'
                f'product {product.product_name}'
                f'in {product.checkout_time} seconds'
            )
            await asyncio.sleep(product.checkout_time)
            
        print(
            f'the cashier {cashier_number}'
            f'finished checking out customer {customer.customer_id}'
            f'in {time.perf_counter() - customer_start_time} seconds'
        )
        
        queue.task_done()

# we implement the generate_customer method as a factory method for producing customers.
#
# We first define a product series and the required checkout time for each product. 
# Then, we place 0 to 4 products in each customer’s shopping cart.
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

# we implement the customer_generation method as a producer. 
# This method generates several customer instances regularly 
# and puts them in the queue. If the queue is full, the put method will wait.
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count+customers)]
        for customer in customers:
            print(f'waiting to put Customer in line....')
            await queue.put(customer)
            print(f'Customer put in line...')

        customer_count = customer_count + len(customers)
        await asyncio.sleep(.001)

        return customer_count

# Finally, we use the main method to initialize the queue, 
# producer, and consumer, and start all concurrent tasks.

_queue = 5
_customer = 80
_cashier = 5

async def main():
    customer_queue = Queue(_queue)
    customer_start_time = time.perf_counter()
    customer_Producer = asyncio.create_task(customer_generation(customer_queue, _customer))
    cachiers = [checkout_customer(customer_queue, i) for i in range(_cashier)]
    
    await asyncio.gather(customer_Producer, *cachiers)
    print(
        f'the supermarket process finished'
        f'{customer_Producer.result()} customers'
            f'in {time.perf_counter() - customer_start_time} seconds'
    )
    
if __name__ == "__main__":
    asyncio.run(main())


# +--------|------------|-------------|-----------------------|-------------------------    
# Queue	   | Customer   | Cashier	  |  Time each Customer	  |  Time for all Customers
# 2	       | 2	        | 2		      |   2.0185310999995636  | 2.0193146999999954
# 2	       | 3	        | 2		      | 2.0007732999993095    | 4.02876920000017   
# 2	       | 4	        | 2		      | 2.0094516999997722   |  4.044583200000488
# 2	       | 10	        | 3		      | 2.015505299999859    |  10.17221729999983
# 5	       | 10	        | 4			  | 2.0213557000006404   |  6.079175099999702
# 5	       | 10			| 4           | 2.0147680000000037    | 6.0711646999998266
# 5	       | 80			| 5           |         2            | <= 40s  (32.47975360000055)
# +--------|------------|-------------|-----------------------|-------------------------    

import time
import asyncio
from asyncio import Queue
from random import randrange

class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

async def checkout_customer(queue: Queue, cashier_number: int):
    start_time = time.perf_counter()
    customers_served = 0
    total_checkout_time = 0
    outer_checkout_duration = []

    while not queue.empty():
        customer :Customer = await queue.get()
        customer_checkout_start = time.perf_counter()
        
        print(f"Cashier_{cashier_number} starting with Customer_{customer.customer_id}")
        
        checkout_durations=[]
        for product in customer.products:
            checkout_duration = product.checkout_time
            print(f"Cashier_{cashier_number} processing {product.product_name} for Customer_{customer.customer_id} in {checkout_duration:.2f}s")
            await asyncio.sleep(checkout_duration)
            total_checkout_time += checkout_duration
            checkout_durations.append(checkout_duration)
            
        outer_checkout_duration .append(sum(checkout_durations))
         
        customer_checkout_time = time.perf_counter() - customer_checkout_start
        print(f"Cashier_{cashier_number} finished Customer_{customer.customer_id} in {customer_checkout_time:.2f}s")
        
        customers_served += 1
        queue.task_done()

    total_time = time.perf_counter() - start_time
    total_time = sum(outer_checkout_duration)
    if customers_served > 0:
        avg_time_per_customer = total_checkout_time / customers_served
        performance_summary = (
            f"Cashier_{cashier_number} served {customers_served} customers "
            f"in {total_time:.2f}s (avg {avg_time_per_customer:.2f}s per customer)"
            f" with checkout durations array {checkout_durations}"
        )
    else:
        performance_summary = f"Cashier_{cashier_number} didn't serve any customers"
    
    return performance_summary

def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        generate_customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count+customers)]
        for customer in generate_customers:
            print("Waiting to put customer in line....")
            await queue.put(customer)
            print("Customer put in line...")
        customer_count = customer_count + len(generate_customers)
        await asyncio.sleep(.001)
        return customer_count

async def main():
    customer_queue = Queue(queueSize)
    customer_start_time = time.perf_counter()
    customer_producer = asyncio.create_task(customer_generation(customer_queue, customerCount))
    cashiers = [checkout_customer(customer_queue,i) for i in range(cashierCount)]

    result = await asyncio.gather(customer_producer, *cashiers)
    print("-"*100)
    for i in result[1:]:
        print(i)

    print(f"\nThe supermarket process finished "
          f"{customer_producer.result()} customers "
          f"in {time.perf_counter() - customer_start_time:.2f} secs")
    
# Global variables in camelCase
queueSize = 3
customerCount = 10
cashierCount = 5

if __name__ == "__main__":
    asyncio.run(main())

# +--------|------------|-------------|-----------------------|-------------------------    
# Queue	   | Customer   | Cashier	  |  Time each Customer	  |  Time for all Customers
# 2	       | 2	        | 2		      |                       |  2.01 s         
# 2	       | 3	        | 2		      |                       |  4.01 s                                            		
# 2	       | 4	        | 2		      |                       |  4.01 s         
# 2	       | 10	        | 3		      |                       |  10.03 s         
# 3	       | 10	        | 3		      |                       |  8.02 s         
# 5	       | 10	        | 4			  |                       |  6.02 s             
# 5	       | 96		    | 5           |                       |  <= 40 s
# +--------|------------|-------------|-----------------------|------------------------- 
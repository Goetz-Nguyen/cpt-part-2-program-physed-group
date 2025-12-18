import time

input("press enter to start timer")
start = time.monotonic()

print ("Counting...")

input("press enter to start timer")
end = time.monotonic()

time = end - start

round_time = f"{time:.2f}"

print(f"Time: {round_time}")
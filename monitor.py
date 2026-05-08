import threading
import time
import random
import queue
from collections import deque
data_queue = queue.Queue()
run_flag = True
results={"total":0,
         "sum":0,
         "alerts":0}

def producer_task():
  global run_flag
  while run_flag:
    sensor_value = random.randint(0, 4095)
    h_byte = sensor_value >> 8
    l_byte = sensor_value & 0xFF
    data_queue.put((h_byte, l_byte))
    time.sleep(0.1)

def consumer_task():
  global run_flag
  history = deque(maxlen=10)

  while run_flag or not data_queue.empty():
      try:

       h,l=data_queue.get(timeout=0.5)
       value = (h << 8) | l
       results["total"] += 1
       results["sum"] += value
       history.append(value)
       if len(history) == 10:
        avg = sum(history) / 10
        if avg > 3000:
          print(f"warning: average value {avg:.2f} exceeds threshold")
          results["alerts"] += 1
        elif avg < 500:
          print(f"warning: average value {avg:.2f} below threshold")
          results["alerts"] += 1
      except queue.Empty:
       continue

if __name__ == "__main__":
  t1 = threading.Thread(target=producer_task)
  t2 = threading.Thread(target=consumer_task)
  t1.start()
  t2.start()
  time.sleep(20)
  run_flag = False
  t1.join()
  t2.join()
  print(f"Total readings: {results['total']}")

  if results["total"] > 0:
    print(f"Average value: {results['sum'] / results['total']:.2f}")
    print(f"Threshold crossings: {results['alerts']}")
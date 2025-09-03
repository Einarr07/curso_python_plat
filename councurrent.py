import threading
import time

def process_request(id_request):
    print('Processing Request #{}'.format(id_request))
    time.sleep(5)
    print('\nProcess #{} succesfull '.format(id_request))

threads = []

for i in range(3):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All Process Complete')
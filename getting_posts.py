import requests
import threading
import json
import time

lock = threading.Lock()


def getting_data(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    data =  response.json()

    if response.status_code == 200:
        with lock:
            with open('data.json', 'a', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.write(",\n")
    else:
        print(f"error: {response.status_code}")


def creating_thread():
    threads=[]

    start_time = time.time()

    with open('data.json', 'w', encoding='utf-8') as f:
        f.write("[\n")

    for i in range(1, 78):
        t=threading.Thread(target=getting_data, args=(i,))
        threads.append(t)
        t.start()
        # print(f"thread {i} started")

    for t in threads:
        t.join()

    end_time = time.time()

    with open('data.json', 'a', encoding='utf-8') as f:
        f.write("\n]")
    total_time = end_time - start_time

    print(f"total time: {total_time}")

if __name__ == '__main__':
    creating_thread()





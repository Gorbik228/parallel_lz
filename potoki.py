import requests
import time
import threading

def download(url, results):
    response = requests.get(url, verify=False)
    results.append(f"{url}: {len(response.content)} байт загружено")
urls=[
    "https://www.similarweb.com",
    "https://google.com",
    "https://youtube.com",
    "https://wikipedia.org",
    "https://ozon.ru",
    "https://ya.ru",
    "https://avito.ru",
    "https://twitch.tv",
    "https://rutube.ru",
    "https://whatsapp.com/"
]
def bezpotok():
  start = time.time()
  results = [] 
  for url in urls:
      download(url,results)
  end = time.time()
  print(f"Без потоковое:")
  for result in results:
      print(result)
  print(f"Потрачено времен:{end - start}")
  return end - start

def potok():
    start = time.time()
    threads = []
    results = []

    for url in urls:
        thread = threading.Thread(target = download, args=(url, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()
    print("Потоковое:")
    for result in results:
        print(result)
    print(f"Затрачено времени: {end - start:} секунд")
    return end - start











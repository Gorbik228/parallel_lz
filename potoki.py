import requests
import time
import

def downland(url):# принимает только один так что нужно ипользовать for
    start = time.time()
    response = requests.get(url)
    end = time.time()
    print(f"Downloaded {url}(size: {len(response.content)} bytes)")

urls=[]#можно запихнуть рандомные

total_time = 0
for url in urls:
  time_wasted = downland(url)
  total_time += time_wasted
  print(f"Запрос к {url} занял {time_wasted}")

print(f"Время выполнения (без потоков): {total_time}")
















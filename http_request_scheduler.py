import schedule
import time
import requests
from requests.exceptions import RequestException
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def perform_request(url):
    try:
        logging.info(f"Выполнение запроса к {url}")
        response = requests.get(url)
        response.raise_for_status()  
        logging.info(f"Ответ от {url}: {response.status_code} - {response.text[:200]}")  
    except RequestException as e:
        logging.error(f"Ошибка при запросе {url}: {e}")

def main():
    url = "https://ru.wikipedia.org/wiki/Python"
    interval = 10  # Интервал в секундах
    schedule.every(interval).seconds.do(perform_request, url)

    logging.info(f"Запланировано выполнение запроса к {url} каждые {interval} секунд.")

    try:
        while True:
            schedule.run_pending() 
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Программа остановлена пользователем.")

if __name__ == "__main__":
    main()

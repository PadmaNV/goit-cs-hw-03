FROM python
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

    # Копіюємо всі файли з поточної директорії у контейнер
COPY . /app/






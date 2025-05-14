# MTS Shop Test Automation

Этот проект содержит автоматизированный тест для сайта shop.mts.ru с использованием Selenium. Тест выполняет поиск товара "AirPods 4" и сохраняет скриншот карточки товара.

## 📌 Содержание

*   [Требования](#-требования)
*   [Установка](#-установка)
*   [Запуск теста](#-запуск-теста)

## 🔧 Требования

*   Python 3.12 
*   Google Chrome (последняя версия)
*   Git (для клонирования репозитория)

## 🚀 Установка

1.  Клонируйте репозиторий:

    ```bash
    git clone https://github.com/MaxmiL1ian/MTS_shop_test.git
    ```

2.  Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv .venv
    # Для Windows:
    .venv\Scripts\activate
    # Для Linux/macOS:
    source .venv/bin/activate
    ```

3.  Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## ⚡ Запуск теста

Выполните команду:

```bash
python test_script.py
```
После успешного выполнения теста в корне проекта появится файл airpods_4_mts.png — скриншот карточки товара.

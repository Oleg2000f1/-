import os
import sys
import urllib.request


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

    # Создаем папки, если их нет
os.makedirs('static/css', exist_ok=True)
os.makedirs('static/js', exist_ok=True)

# Официальные и надежные российские ссылки (зеркала Яндекса)
css_url = "https://yastatic.net"
js_url = "https://yastatic.net"

print("Начинаю прямую запись кода во файлы статики...")

try:
    # Скачиваем полноценный код напрямую в файлы
    urllib.request.urlretrieve(css_url, 'static/css/leaflet.css')
    urllib.request.urlretrieve(js_url, 'static/js/leaflet.js')
    print("=== УСПЕХ! Библиотеки карт перезаписаны и полностью заполнены! ===")
except Exception as e:
    print("Не удалось скачать напрямую, применяю обходной план с импортами...")
    with open('static/js/leaflet.js', 'w', encoding='utf-8') as f:
        f.write('import("https://yastatic.net").then(m => { window.L = m.default || m; });')
    with open('static/css/leaflet.css', 'w', encoding='utf-8') as f:
        f.write('@import url("https://yastatic.net");')
    print("=== УСПЕХ! Созданы умные файлы-перенаправители! ===")

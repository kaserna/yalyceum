![CI CHECKS](https://github.com/kaserna/yalyceum/actions/workflows/python-package.yml/badge.svg)

# Для запуска проекта в dev-режиме нужно выполнить следующие действия:
1. Склонировать репозиторий.  
`git clone https://github.com/kaserna/yalyceum.git`
2. Перейти в директорию **yalyceum/lyceum**.  
`cd yalyceum/lyceum`
3. Установить виртуальное окружение  
`python3 -m venv venv`
4. Активировать виртуальное окружение:  
`sourse venv/bin/activate`
5. В файле .env прописать `SECRET_KEY, DEBUG, ALLOWED_HOSTS`, 
6. Установить зависимости соответствующего окружения:  
`pip3 install -r requirements/[dev.txt|test.txt|prod.txt]`
7. Запустить dev-сервер:  
`python3 manage.py runserver`
8. Зайти на сайт:  
`http://127.0.0.1:8000/`

**All done! ✨ 🍰 ✨**
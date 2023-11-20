<h1>Старт работы</h1>
<h2>Машинное состояние НЕ ЗАРЕГИСТРИРОВАННЫЙ. Ограниченный функционал. Возможно пользоваться только после единождой регистрации.</h2>
<h3>Так же присутствует проверка. Если вдруг слетает марка ЗАРЕГЕСТРИРОВАННЫЙ происходит проверка бд(марка падает при сбое работы ТГ бота)</h3>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/4e29b151-c774-4e24-9a68-e5b74a23dd49)
![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/43b60b81-a365-4fd6-a46d-19146861f239)
![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/51b319be-5a0e-480f-9a5d-b38606ad80db)
![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/f0e88282-b5d7-4014-9ea9-bcdf8984e461)

<h3>Так же присутствует проверка. Если вдруг слетает марка ЗАРЕГЕСТРИРОВАННЫЙ происходит проверка бд(марка падает при сбое работы ТГ бота)</h3>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/1886ef5d-bef3-4c02-aa2c-6842b4328d28)

<h1>Основные команды: </h1>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/8de5b81e-6ff9-4988-a6a1-0dc2e6786011)

<h1>Подписка: </h1>
<h2>При подписке статус саба в БД True. Так же на ежедневной основе в 12:00 по мск автоматически идет рассылка всем ID в базе данных у которых статус саб == True.</h2>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/c8674d31-4a40-4317-9d27-9e9f69c6b6e6)
![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/c95017e6-d961-4c65-8881-124ec8435848)

<h2>Состояние кнопок подписаться и отписаться зависит от отсутствия или присутствия подписки пользователя.</h2>
<h2>При отписке отправляется запрос к БД и статус подписки переходит на False</h2>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/a7bf66b7-da76-4c07-96be-4709ddf7c2ef)

<h3>UPD. Реализованы кастомные команды с админ панели только для /start(Для показа, что это возможно). В Aiogram commands admin django добавляем название команды /start и текст, который хотим, чтобы бот прислал. Если такая запись в админке отсутствует, присылает дефолтную фразу.</h3>


<h1>Project install</h1>

<h2>1) Clone repo</h2>
<h2>2) Activate venv</h2>
<h2>3) pip install -r requirements.txt</h2>

<h2>4) Backend start</h2>

<li>cd backend</li>
<li>python manage.py migrate</li>
<li>python manage.py set_admin_django</li>
<li>python manage.py runserver</li>

<h2>5) Telegram bot start</h2>
<li>Run 'bot.py' (app.bot.py)</li>

<h2>6) Visit bot on https://t.me/rubles_exchange_rate_bot</h2>

<h3>Admin panel on http://127.0.0.1:8000/admin/</h3>
<h4>(login: admin, pass: 123)</h4>


<h1>Miro plan</h1>

https://miro.com/welcomeonboard/Wm84eDZXUTdLd3dyOGVTOU5sNzNXN3dBRks4bTIxeHBmV00zNlZJQVFodnRHcFp6TGF3S0p4c2J2SzByNnZua3wzNDU4NzY0NTY0NTMyMjIwNjM5fDI=?share_link_id=753020220620

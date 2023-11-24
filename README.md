<h1>Старт работы</h1>
<h2>Машинное состояние НЕ ЗАРЕГИСТРИРОВАННЫЙ. Ограниченный функционал. Возможно пользоваться ботов только после регистрации.</h2>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/793a1343-14b2-4486-b46a-c7113257228c)

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/5271e7d5-d7fb-4a2f-92ab-14676451b28c)

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/c07f7e52-d8b2-41d6-99b5-9ef4b83ae69c)

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/c9954782-6fe8-48ed-a79a-6ff6b52e074c)

<h2>Django admin panel</h2>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/a6aa1844-f257-4169-bdc4-317147857825)


<h3>Так же присутствует проверка. Если вдруг слетает марка ЗАРЕГЕСТРИРОВАННЫЙ происходит проверка бд(марка падает при сбое работы ТГ бота)</h3>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/ffa1744c-9b8c-4952-9fdf-51611ded4f3b)

<h1>Основные команды: </h1>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/b1139f8a-218c-458e-be36-731c5355b2d0)

<h1>Подписка: </h1>
<h2>При подписке статус саба в БД True. Так же на ежедневной основе в 12:00 по мск автоматически идет рассылка всем ID в базе данных у которых статус саб == True.</h2>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/a2e838d9-658b-487e-8a2c-5fc60681f247)

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/1ce678b5-e89a-4ddc-a1be-5e160a8726c5)

<h3>Django admin panel</h3>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/a2e8fd29-bc11-4758-9425-003184a61e1a)


<h2>Состояние кнопок подписаться и отписаться зависит от отсутствия или присутствия подписки пользователя.</h2>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/78b458bd-dca6-4640-8ae2-55cf6783a9c4)

<h2>При отписке отправляется запрос к БД и статус подписки переходит на False</h2>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/acb358cf-af0b-4e3a-9d05-bb813380dc9c)

<h2>Django admin panel</h2>

![image](https://github.com/petrovkarmm/rubles_exchange_rate/assets/139163328/442d2ea4-d9f2-4f84-a761-ca2c4595d1a8)


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

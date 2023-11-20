import aiohttp

docker_url = 'localhost:8000'
local_url = 'http://127.0.0.1:8000'


async def django_user_registration(data):
    async with aiohttp.ClientSession() as session:
        url = f'{local_url}/users/register/'
        async with session.post(url, json=data) as response:
            return await response.json()


async def django_user_check_registration(data):
    async with aiohttp.ClientSession() as session:
        url = f'{local_url}/users/register/'
        async with session.get(url, json=data) as response:
            return await response.json()


async def django_set_user_activity(data):
    async with aiohttp.ClientSession() as session:
        url = f'{local_url}/users/activity/'
        async with session.post(url, json=data) as response:
            return await response.json()


async def django_get_user_activity(data):
    async with aiohttp.ClientSession() as session:
        url = f'{local_url}/users/activity/'
        async with session.get(url, json=data) as response:
            return await response.json()


async def django_get_user_subscribe(data):
    async with aiohttp.ClientSession() as session:
        url = f'{local_url}/users/subscribe/'
        async with session.get(url, json=data) as response:
            return await response.json()


async def django_set_user_subscribe(data):
    async with aiohttp.ClientSession() as session:
        url = f'{local_url}/users/subscribe/'
        async with session.post(url, json=data) as response:
            return await response.json()


async def django_unsubscribe_user(data):
    async with aiohttp.ClientSession() as session:
        url = f'{local_url}/users/unsubscribe/'
        async with session.post(url, json=data) as response:
            return await response.json()


async def django_getting_all_subs():
    async with aiohttp.ClientSession() as session:
        url = f'{local_url}/users/all-subs/'
        async with session.get(url) as response:
            return await response.json()


async def django_start_command(data):
    async with aiohttp.ClientSession() as session:
        url = f'{local_url}/commands/command-text/'
        async with session.get(url, json=data) as response:
            return await response.json()
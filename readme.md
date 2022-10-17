# python-discord-bot-template

## Преимущества ##
  + Обработчик слеш команд
  + Готовые команды `help`, `server`, `bot`
  + Лёгкая регистрация своих команд

## Запуск ##
  1. Регистрируем бота на [discord developers](https://discord.com/developers/applications) 
  2. Создаём файл по пути `src/config.yml`
  3. В файле `src/config.yaml` пишем:
  ```yml
    token: 'токен бота',
    owners: ['Ваш ID', 'Айди других разработчиков..']
    guildID: 'Айди сервера где будут регистрироваться все команды'
    website: 'https://github.com/sscefalix/python-discord-bot-template'
  ```
  3. В консоли пишем `pip install -r requirements.txt`
  4. Запуск бота `cd src` потом `python main.py`

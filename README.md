<p align="center">
    <a href="https://github.com/MrMahdi313/Pyro-Lugin">
        <img src="https://avatars1.githubusercontent.com/u/34474300?s=200&v=4" alt="Pyro-Lugin">
    </a>
    <br>
    <b>Telegram Bot based on plugin and functional for <a href="https://github.com/Pyrogram/Pyrogram">Pyrogram</a> library.</b>
    <br>
    <!--
    <a href="https://gapbot.readthedocs.io/en/latest/">
        Documentation
    </a>
    -->
    <a href="https://github.com/MrMahdi313/Pyro-Lugin/releases">
        Releases
    </a>
</p>


## Pyro-Lugin

### Plugin Example
``` python
def run(app: Client, msg: Message):
    print('{}'.format(msg))
    app.send_message(msg.chat.id, 'pyro-lugin')


returns = dict(
    msg=dict(
        func=run,
        filters=(Filters.text | Filters.edited) & Filters.private,
        performer='api',
    ),
)
```

**Pyro-Lugin** is an elegant, functional, plugin base and easy-to-use [Telegram](https://telegram.org) Bot library written from the
ground up in Python. It enables you to easily create custom apps.

> [Pyro-Lugin in fully-asynchronous mode is coming soon »](https://github.com/MrMahdi313/Pyro-Lugin/tree/async)
>
> [GapBot in plugin base mode is now available »](https://github.com/MrMahdi313/Pyro-Lugin)

### Features

- **Easy**: You can install GapBot with pip and start building your applications right away.
- **Elegant**: Low-level details are abstracted and re-presented in a much nicer and easier way.
- **PluginBase**: Tou can easily use from plugins to manage your codes.

### Requirements

- Python 3.6 or higher.
- A [Api id & Api hash](https://my.telegram.org/apps).

### Resources

- Reading [Examples in this repository](https://github.com/MrMahdi313/Pyro-Lugin/tree/developer/plugins) is also a good way
  for learning how GapBot works.
- For other requests you can send an [Email](mailto:m.m.z.m12363@gmail.com) or a [Message](https://t.me/MrFedora).

### Contributing

Pyro-Lugin is brand new, and **you are welcome to try it and help make it even better** by either submitting pull
requests or reporting issues/bugs as well as suggesting best practices, ideas, enhancements on both code
and documentation. Any help is appreciated!

### Copyright & License

- Copyright (C) 2017-2019 MohammadMahdi Zojaji as <<https://github.com/MrMahdi313>>
- Licensed under the terms of the GNU Lesser General Public License v3 or later (LGPLv3+)

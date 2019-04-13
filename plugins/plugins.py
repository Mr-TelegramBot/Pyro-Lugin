from bot import rp, reload
from re import search
from configparser import ConfigParser, ExtendedInterpolation
from os.path import join
from pyrogram import Message, Client


def run(app: Client, msg: Message):
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(join(rp, 'data', 'config.ini'))
    if search(r"^([!#/])?plg \+ (.+)$", msg.text):
        plugin_name = search(r"([!#/])?plg \+ (.+)", msg.text).group(2).strip()
        if plugin_name in config.options('Plugins'):
            config.set('Plugins', plugin_name, 'enabled')
            app.send_message(msg.chat.id, '**Plugin {} Has Been Enabled!**'.format(plugin_name), parse_mode='markdown')
            with open(join(rp, 'data', 'config.ini'), 'w') as file:
                config.write(file)
            reload()
        else:
            app.send_message(msg.chat.id, '**This Plugin Doesnt Exists.!**', parse_mode='markdown')
    elif search(r"^([!#/])?plg - (.+)$", msg.text):
        plugin_name = search(r"([!#/])?plg - (.+)", msg.text).group(2).strip()
        if plugin_name in config.options('Plugins'):
            config.set('Plugins', plugin_name, 'disabled')
            app.send_message(msg.chat.id, '**Plugin {} Has Been Disabled!**'.format(plugin_name), parse_mode='markdown')
            with open(join(rp, 'data', 'config.ini'), 'w') as file:
                config.write(file)
            reload()
        else:
            app.send_message(msg.chat.id, '**This Plugin Doesnt Exists.!**', parse_mode='markdown')
    elif search('^([!?#])?reload$', msg.text.lower()):
        app.send_message(msg.chat.id, '**Bot Reloaded!**', parse_mode='markdown')
        reload()
    elif search('^[!#/]?plugins$', msg.text.lower()):
        text = ''
        for plug in config['Plugins']:
            text += '\n`{0}` => **{1}**'.format(plug, config.get('Plugins', plug))
        try:
            app.send_message(msg.chat.id, text, parse_mode='markdown', reply_to_message_id=msg.message_id)
        except:
            pass


returns = dict(
    msg=dict(
        func=run,
        filters=None,
        performer='api',
    ),
)

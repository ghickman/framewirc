def is_channel(name):
    """
    Determine if a string is a valid channel name.

    The exact text from RFC2812 §1.3 is as follows:

    Channels names are strings (beginning with a '&', '#', '+' or '!'
    character) of length up to fifty (50) characters.  Apart from the
    requirement that the first character is either '&', '#', '+' or '!',
    the only restriction on a channel name is that it SHALL NOT contain
    any spaces (' '), a control G (^G or ASCII 7), a comma (',').  Space
    is used as parameter separator and command is used as a list item
    separator by the protocol).  A colon (':') can also be used as a
    delimiter for the channel mask.  Channel names are case insensitive.
    """
    if len(name) > 50:
        return False
    if set(name).intersection(',\7 '):  # Note the space
        return False
    if name[0] not in '&#+!':
        return False
    return True


def nick(raw_nick):
    """
    Split nick into constituent parts.

    Nicks with an ident are in the following format:

        nick!ident@hostname

    When they don't have an ident, they have a leading tilde instead:

        ~nick@hostname
    """
    if '!' in raw_nick:
        nick, _rest = raw_nick.split('!')
        ident, host = _rest.split('@')
    else:
        nick, host = raw_nick.split('@')
        nick = nick.lstrip('~')
        ident = None
    return {
        'nick': nick,
        'ident': ident,
        'host': host,
    }


def privmsg(message):
    """
    Split received PRIVMSG command into a dictionary of parts.

    When the message target is a channel, 'channel' is set to that. Otherwise,
    'channel' is defined as the sender's nick.
    """
    target = message.params[0]
    raw_sender = message.prefix
    sender_nick = nick(raw_sender)['nick']

    if is_channel(target):
        channel = target
    else:
        channel = sender_nick

    return {
        'channel': channel,
        'raw_body': message.suffix,
        'raw_sender': raw_sender,
        'sender_nick': sender_nick,
        'target': target,
    }

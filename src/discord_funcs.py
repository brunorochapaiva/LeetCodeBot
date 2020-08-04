from constants import MAX_MESSAGE_SIZE

''' DISCORD FUNCS '''


def get_username(message):
    return message.author.name + "#" + message.author.discriminator


def reply_to_message(message, reply):
    if len(reply) < MAX_MESSAGE_SIZE:
        await message.channel.send(reply)
        return

    # Turn reply into a list of shorter replies
    # As reply is too long
    replies = split_reply(reply)
    for r in replies:
        await message.channel.send(r)


# Tries to split on newlines
# If still too long splits on spaces
# If still too long splits at index
def split_reply(reply, split_char):
    split = reply.split(split_char)
    result = []
    for s in split:
        if s < MAX_MESSAGE_SIZE:
            result.append(s)
        elif split_char == '\n':
            result += split_reply(s, ' ')
        elif split_char == ' ':
            for i in range(0, len(s), MAX_MESSAGE_SIZE):
                result.append(s[i:i+MAX_MESSAGE_SIZE])
    return result

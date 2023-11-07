
def lower_bool(value):
    return str(value)\
        .replace('True', 'true') \
        .replace('False', 'false') \
        .replace('None', 'null')

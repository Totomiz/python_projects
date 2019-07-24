import aiomysql


def createPool(**kw):
    global __pool
    __pool = aiomysql.create_pool(
        loop=kw.get('loop')
    )

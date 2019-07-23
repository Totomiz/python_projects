import logging

from aiohttp import web

logging.basicConfig(level=logging.INFO)

port = 8000
host = '127.0.0.1'


async def index(request):
    logging.info("index")
    # 与老师的源码相比，最重要的是要加content_type这个参数，否则会变成下载文件
    # await asyncio.sleep(5) mock
    logging.info('HELLO WORLD AGIN')
    return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'), content_type='text/html')


def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    logging.info("Server started at http://127.0.0.1:9000")
    web.run_app(app, host=host, port=port)


init()

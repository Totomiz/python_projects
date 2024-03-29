from aiohttp import web

from www.Api import *

logging.basicConfig(level=logging.INFO)

port = 8000
host = '0.0.0.0'


async def index(request):
    logging.info("index")
    # 重要的是要加content_type这个参数，否则会变成下载文件
    # await asyncio.sleep(5) mock
    logging.info('HELLO WORLD AGIN')
    return web.Response(body='<h1>Awesome Movie</h1>'.encode('utf-8'), content_type='text')


async def home_genres(request):
    logging.info("index")
    # 重要的是要加content_type这个参数，否则会变成下载文件
    # await asyncio.sleep(5) mock
    logging.info('home_genres')
    return web.Response(body=get_genres(), content_type='text/html', charset='UTF-8')


async def get_home_data(request):
    logging.info("index")
    # 重要的是要加content_type这个参数，否则会变成下载文件
    # await asyncio.sleep(5) mock
    logging.info('home_genres')
    return web.Response(body=get_home_main(), content_type='text/html', charset='UTF-8')


async def get_home_type_data(request):
    logging.info("get_home_type_data")
    # await asyncio.sleep(5) mock
    type = request.match_info.get('type', "1,")
    logging.info("get_home_type_data-{}".format(type))
    return web.Response(body=get_home_category_data(type), content_type='text/html', charset='UTF-8')


async def get_detail_data(request):
    logging.info("get_home_type_data")
    # await asyncio.sleep(5) mock
    id = request.match_info.get('id', "-1")
    logging.info("get_home_type_data-{}".format(id))
    return web.Response(body=get_detail(id), content_type='text/html', charset='UTF-8')


async def get_recommend_data(request):
    logging.info("get_home_type_data")
    # await asyncio.sleep(5) mock
    id = request.match_info.get('id', "-1")
    length = request.match_info.get('length', "6")
    logging.info("get_recommend_data-id={} length={}".format(id, length))
    return web.Response(body=get_api_recommend_data(id, length), content_type='text/html', charset='UTF-8')


# 获取分类分页数据
async def get_more_group_data(request):
    logging.info("get_home_type_data")
    # await asyncio.sleep(5) mock
    g_path = request.match_info.get('g_path', "-1")
    page = request.match_info.get('page', 0)
    logging.info("get_recommend_data-id={} length={}".format(g_path, page))
    return web.Response(body=get_api_group_page_data(g_path, page), content_type='text/html', charset='UTF-8')


def init():
    app = web.Application()
    app.add_routes([web.get('/', index),
                    web.get('/api/v1/home/{type}', get_home_type_data),
                    web.get('/api/v1/detail/{id}', get_detail_data),
                    web.get('/api/v1/recmd/{id}/{length}', get_recommend_data),
                    web.get('/api/v1/genres', home_genres),
                    web.get('/api/v1/group/{g_path}/{page}', get_more_group_data),
                    web.get('/api/v1/home', get_home_data)])
    app.router.add_static('/img/',
                          path='static/img',
                          name='img')
    app.router.add_static('/page/',
                          path='static/page',
                          name='page')
    logging.info('Server started at {}:{}'.format(host, port))
    web.run_app(app, host=host, port=port)


init()

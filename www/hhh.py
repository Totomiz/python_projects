from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


port = 8000
host = '127.0.0.1'

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app, host=host, port=port)

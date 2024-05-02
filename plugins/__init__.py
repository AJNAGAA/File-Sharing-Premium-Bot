# Empire Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Era_Bot_Support
# Developer @Empire_756





from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app





# Empire Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Era_Bot_Support
# Developer @Empire_756

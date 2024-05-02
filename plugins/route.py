# Empire Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Era_Bot_Support
# Developer @Empire_756


from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Madflix_Bots")




# Empire Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Era_Bot_Support
# Developer @Empire_756

# # import the module
# from prsaw import RandomStuff

# # initiate the object with async mode
# api_key = "ndk8AyAOPBJ8"
# rs = RandomStuff(api_key = api_key) #async_mode = True, api_key = api_key

# # get a joke
# joke = rs.get_ai_response("Hello how are you?")
# print(joke)
# rs.close()
# # close the session


# import the module
from prsaw import RandomStuff
import asyncio

# initiate the object with async mode
api_key = "ndk8AyAOPBJ8"
rs = RandomStuff(async_mode = True, api_key = api_key)

async def get_joke():
    # get a joke
    joke = await rs.get_joke()
    print(joke)

    # close the session
    await rs.aclose()

loop = asyncio.get_event_loop()
loop.run_until_complete(get_joke())
loop.close()
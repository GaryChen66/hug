import hug

api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api, max_age=10))

#Middleware Demo URL
@hug.get("/demo")
def get_demo():
    return {"result": "Hello World"}

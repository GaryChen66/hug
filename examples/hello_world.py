import hug

#Hello World
@hug.get()
def hello(request):
    """Says hellos"""
    return "Hello Worlds for Bacon?!"

import web  # this import web.py

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())  # why this sentence can be deleted?

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()

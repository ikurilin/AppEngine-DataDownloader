import webapp2
from jinja2 import Environment, FileSystemLoader

JINJA_ENV=Environment(loader=FileSystemLoader(""),
                        extensions=["jinja2.ext.autoescape"],
                        autoescape=True)

class MainController(webapp2.RequestHandler):
    def get(self):

        template_values = {
            "world_type": self.request.get("kind", default_value="Pretty")
        }

        template = JINJA_ENV.get_template("pretty_template.html")

        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.write(template.render(template_values))


from view_demo import views
from view_demo.route_variable import app

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/cases', view_func=views.cases)

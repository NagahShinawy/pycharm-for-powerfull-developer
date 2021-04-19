"""
created by Nagaj at 17/04/2021
"""
import jinja2

faq = ["How is my cost calc", "Where do profits go", "where are meats collected from ?"]

with open("index.html", "r") as html:
    index = html.read()
template = jinja2.Template(index)
# dynamic_html = template.render(faq=faq, info="running jinja example")
dynamic_html = template.render({"faq": faq, "info": "running jinja example"})

print(dynamic_html)

with open("home.html", "w") as html:
    html.write(dynamic_html)

template.stream({"faq": faq}).dump(
    "index.html"
)  # generate dynamic html page with context just like 2 lines above
# template.stream({"testInvalidKey": faq}).dump("index.html")
# if key not found at the template , block will be removed

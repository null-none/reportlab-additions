from flask.ext.script import Manager, Command
from flask import Flask


from reportlab.pdfgen import canvas

app = Flask(__name__)
manager = Manager(app)


def multi_line(string, max):
    result = []
    temp = ''
    for idx, item in enumerate(string):
        temp += item
        if idx % max == 0 and idx > 0:
            result.append(temp)
            temp = ''
    return result


def resize_text(font, string, min_font, max_string):
    if len(string) > max_string:
        while font > min_font and len(string) > max_string:
            max_string += 5
            font -= 1
    return font, string


@manager.command
def example():
    c = canvas.Canvas("example.pdf")
    c.setPageSize((700, 500))
    font, string = resize_text(12, "Hello world", 7, 5)
    c.setFont('Helvetica', font)
    c.drawString(0, 0, string)
    result = multi_line("Hello world!", 3)
    for idx, item in enumerate(result):
        c.setFont('Helvetica', 12)
        c.drawString(0, idx + 60, item)
    c.showPage()
    c.save()


if __name__ == "__main__":
    manager.run()

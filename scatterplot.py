from bokeh.plotting import figure, output_file, show
from dateutil.parser import parse
from bokeh.models import DatetimeTickFormatter

def showPlot(name, x,y):
    output_file(name+".html")

    p = figure(
       title="@"+name,
       x_axis_label='følgere', y_axis_label='følgeres oprettelsestidspunkt'
    )
    p.yaxis[0].formatter = DatetimeTickFormatter()
    p.circle(x, y, fill_color="blue", fill_alpha=0.02, line_color="blue", line_alpha=0.1, size=6)

    show(p)

def parseData(name):
    data=[]
    with open(name, 'r') as file:
        for line in file.readlines():
            date=parse(line.strip())
            print(date.timestamp(), line.strip())
            data.append(date)
    data.reverse()
    return data

if __name__ == "__main__":
    name="SamsungDK"
    data=parseData(name)
    showPlot(name, range(len(data)),data)
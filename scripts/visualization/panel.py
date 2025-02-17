from typing import List, Text, Dict

from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure, Figure

# output_file("slider.html")

# p1 = figure(plot_width=300, plot_height=300)
# p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
# tab1 = Panel(child=p1, title="circle")
#
# p2 = figure(plot_width=300, plot_height=300)
# p2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="navy", alpha=0.5)
# tab2 = Panel(child=p2, title="line")
#
# tabs = Tabs(tabs=[tab1, tab2])
#
# show(tabs)


def tab_figures(figures_dict: Dict[Text, Figure]):
    panels = []
    for key in figures_dict:
        fig = figures_dict[key]
        panels.append(Panel(child=fig, title=key))

    tabs = Tabs(tabs=panels)
    # show(tabs)

    return tabs


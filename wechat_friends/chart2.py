from pyecharts import Line, Pie, Grid, Bar
from get_data import get_city_data

data = get_city_data('friend.json')


bar = Bar("柱状图", height=720)
attr, value = bar.cast(data)
bar.add("微信好友", attr, value)

line = Line("折线图", height=720, title_top="50%")
line.add("", attr, value, line_color='red')

grid = Grid()
grid.use_theme('dark')

grid.add(bar, grid_bottom="60%")
grid.add(line, grid_top="60%")

grid.render('map2.html')
grid.render(path='map2.png')


pie = Pie("饼图", title_pos='center')
pie.use_theme('dark')
pie.add("", attr, value, radius=[40, 75], label_text_color=None,
        is_label_show=True, legend_orient="vertical", legend_pos="left")
pie.render('pie.html')
pie.render(path='pie.png')

from pyecharts import Map, Bar
from get_data import get_city_data


def generate_map():
    data = get_city_data('friend.json')
    map = Map(
        "微信好友",
        "热力图",
        title_color="#fff",
        title_pos="center",
        width=600,
        height=500,
        background_color="#404a59",
    )
    # geo.use_theme('dark')
    attr, value = map.cast(data)
    map.add(
        "",
        attr,
        value,
        maptype="china",
        visual_range=[0, 200],
        visual_text_color="#fff",
        symbol_size=15,
        is_visualmap=True,
        # is_label_show=True
    )

    map.render('map.html')
    map.render(path='map.png')


if __name__ == '__main__':
    generate_map()

#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 13/07/2022  15:46
@Author: Skye
@File  : map_draw.py 
"""
from pyecharts import options as opts
from pyecharts.charts import Map
from snapshot_selenium import snapshot
from pyecharts.render import make_snapshot

class Draw_map():
    def draw_the_world(self, map_country, map_value):
        pieces = [
            {"max": 9999, "min": 800,'label': '>800', "color": "#DC143C"},
            {"max": 800, "min": 700, 'label': '700~800', "color": "#DF0101"},
            {"max": 700, "min": 600, 'label': '600~700', "color": "#FF1493"},
            {"max": 600, "min": 500, 'label': '500~600', "color": "#FF69B4"},
            {"max": 500, "min": 400, 'label': '400~500', "color": "#DB7093"},
            {"max": 400, "min": 300, 'label': '300~400', "color": "#DDA0DD"},
            {"max": 300, "min": 200, 'label': '200~300', "color": "#FFB6C1"},
            {"max": 200, "min": 100, 'label': '100~200', "color": "#FFC0CB"},
            {"max": 100, "min": 0, 'label': '0~100', "color": "	#F8F8FF"},
        ]

        c = (Map(init_opts=opts.InitOpts(width="200px", height="100px"))
                .add("Amount of contents", [list(z) for z in zip(map_country, map_value)], "world")
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="", subtitle="Dataset update ends for 2021.12.30"),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True, pieces=pieces))
                # .render("contents_amount_world.html")
             )
        # print(c)
        return c


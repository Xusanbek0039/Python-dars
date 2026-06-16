# -*- coding: utf-8 -*-
"""Barcha 29 dars uchun IT Shaharcha qo'llanma PDF larini yaratadi."""
import os
from _pdf_engine import make_lesson
import _content_1_10, _content_11_20, _content_21_29

ALL = {}
ALL.update(_content_1_10.LESSONS)
ALL.update(_content_11_20.LESSONS)
ALL.update(_content_21_29.LESSONS)

BASE = os.path.dirname(os.path.abspath(__file__))

ok = 0
for no in sorted(ALL):
    topic, subtitle, sections = ALL[no]
    folder = os.path.join(BASE, f"Dars_{no}")
    if not os.path.isdir(folder):
        print(f"!! Dars_{no} papkasi topilmadi")
        continue
    out = os.path.join(folder, f"Qollanma_{no}-dars_IT_Shaharcha.pdf")
    make_lesson(out, no, topic, subtitle, sections)
    ok += 1
    print(f"OK  Dars_{no}: {topic}")

print(f"\nJami {ok} ta qo'llanma yaratildi.")

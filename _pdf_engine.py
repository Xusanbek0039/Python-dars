# -*- coding: utf-8 -*-
"""
IT Shaharcha - Python qo'llanma PDF generatori (engine).
Muallif brendi: Husan Suyunov | IT Shaharcha
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Preformatted, Table, TableStyle, HRFlowable, KeepTogether, Image
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.flowables import Flowable

# ----- Ranglar (IT Shaharcha brendi) -----
BRAND_DARK   = colors.HexColor("#1f2a44")
BRAND_BLUE   = colors.HexColor("#1565c0")
BRAND_ACCENT = colors.HexColor("#e8462d")
BRAND_GREEN  = colors.HexColor("#2e9e5b")
CODE_BG      = colors.HexColor("#f4f6fb")
CODE_BORDER  = colors.HexColor("#c9d3e6")
NOTE_BG      = colors.HexColor("#fff7e6")
NOTE_BORDER  = colors.HexColor("#f0c36d")
LIGHT_GREY   = colors.HexColor("#6b7280")

FONTS_DIR = r"C:\Windows\Fonts"

def _register_fonts():
    pdfmetrics.registerFont(TTFont("UI",      os.path.join(FONTS_DIR, "calibri.ttf")))
    pdfmetrics.registerFont(TTFont("UI-Bold", os.path.join(FONTS_DIR, "calibrib.ttf")))
    pdfmetrics.registerFont(TTFont("Mono",    os.path.join(FONTS_DIR, "consola.ttf")))
    pdfmetrics.registerFont(TTFont("Mono-Bold", os.path.join(FONTS_DIR, "consolab.ttf")))
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily("UI", normal="UI", bold="UI-Bold", italic="UI", boldItalic="UI-Bold")

_register_fonts()

LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "it shaharcha.png")

# ----- Stillar -----
styles = {
    "title": ParagraphStyle("title", fontName="UI-Bold", fontSize=22, leading=27,
                            textColor=BRAND_DARK, alignment=TA_LEFT, spaceAfter=2),
    "subtitle": ParagraphStyle("subtitle", fontName="UI", fontSize=12.5, leading=16,
                               textColor=BRAND_BLUE, spaceAfter=4),
    "h2": ParagraphStyle("h2", fontName="UI-Bold", fontSize=14.5, leading=19,
                         textColor=BRAND_BLUE, spaceBefore=12, spaceAfter=5),
    "h3": ParagraphStyle("h3", fontName="UI-Bold", fontSize=12, leading=16,
                         textColor=BRAND_DARK, spaceBefore=8, spaceAfter=3),
    "p": ParagraphStyle("p", fontName="UI", fontSize=11, leading=16.5,
                        textColor=colors.HexColor("#22272e"), alignment=TA_JUSTIFY,
                        spaceAfter=6),
    "bullet": ParagraphStyle("bullet", fontName="UI", fontSize=11, leading=16,
                             textColor=colors.HexColor("#22272e"), leftIndent=14,
                             bulletIndent=2, spaceAfter=3),
    "note": ParagraphStyle("note", fontName="UI", fontSize=10.5, leading=15.5,
                           textColor=colors.HexColor("#5a4a1a")),
    "code": ParagraphStyle("code", fontName="Mono", fontSize=9.7, leading=13.5,
                           textColor=colors.HexColor("#1b2330")),
    "caption": ParagraphStyle("caption", fontName="UI", fontSize=9.5, leading=12,
                              textColor=LIGHT_GREY),
}


def _esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _inline(text):
    """`code` va **bold** belgilarini xavfsiz HTML ga aylantiradi."""
    import re
    # 1) Kod spanlarini vaqtincha token bilan almashtiramiz (to'qnashuvni oldini olish)
    spans = []
    def _grab(m):
        spans.append("<font name='Mono' size=10 color='#c0392b'>"
                     + _esc(m.group(1)) + "</font>")
        return "\x00%d\x00" % (len(spans) - 1)
    tmp = re.sub(r"`(.+?)`", _grab, text)
    # 2) Qolgan matnni escape qilamiz
    tmp = _esc(tmp)
    # 3) **bold**
    tmp = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", tmp)
    # 4) Kod spanlarini qaytaramiz
    tmp = re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], tmp)
    return tmp


class CodeBox(Flowable):
    """Kod blokini chiroyli ramka + fon bilan chizadi."""
    def __init__(self, code, width):
        super().__init__()
        self.code = code.rstrip("\n")
        self.width = width
        self.pad = 7
        self.para = Preformatted(self.code, styles["code"])

    def wrap(self, availWidth, availHeight):
        w = self.width
        self.para.wrapOn(None, w - 2 * self.pad, availHeight)
        self.h = self.para.height + 2 * self.pad
        return (w, self.h)

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(CODE_BG)
        c.setStrokeColor(CODE_BORDER)
        c.roundRect(0, 0, self.width, self.h, 5, stroke=1, fill=1)
        c.setFillColor(BRAND_BLUE)
        c.rect(0, 0, 3.2, self.h, stroke=0, fill=1)
        c.restoreState()
        self.para.drawOn(c, self.pad + 2, self.pad)


def note_box(text, width):
    p = Paragraph("<b>Eslatma:</b> " + text, styles["note"])
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NOTE_BG),
        ("BOX", (0, 0), (-1, -1), 0.8, NOTE_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t


class PDFBuilder:
    def __init__(self, out_path, lesson_no, topic):
        self.out_path = out_path
        self.lesson_no = lesson_no
        self.topic = topic
        self.doc = BaseDocTemplate(
            out_path, pagesize=A4,
            leftMargin=20 * mm, rightMargin=18 * mm,
            topMargin=30 * mm, bottomMargin=20 * mm,
            title=f"{lesson_no}-dars: {topic}",
            author="Husan Suyunov | IT Shaharcha",
            subject="Python noldan boshlab - amaliy qo'llanma",
        )
        self.content_w = self.doc.width
        frame = Frame(self.doc.leftMargin, self.doc.bottomMargin,
                      self.doc.width, self.doc.height, id="main")
        self.doc.addPageTemplates([
            PageTemplate(id="all", frames=[frame], onPage=self._decorate)
        ])
        self.story = []

    # --- har sahifa: header + footer ---
    def _decorate(self, canvas, doc):
        canvas.saveState()
        w, h = A4
        # Header chizig'i
        top_y = h - 18 * mm
        # Logo
        try:
            from reportlab.lib.utils import ImageReader
            img = ImageReader(LOGO_PATH)
            iw, ih = img.getSize()
            disp_h = 11 * mm
            disp_w = disp_h * iw / ih
            canvas.drawImage(img, doc.leftMargin, top_y - 2 * mm,
                             width=disp_w, height=disp_h, mask="auto")
        except Exception:
            pass
        # O'ng tomonda brend matni
        canvas.setFont("UI-Bold", 10.5)
        canvas.setFillColor(BRAND_DARK)
        canvas.drawRightString(w - doc.rightMargin, top_y + 5 * mm, "Husan Suyunov")
        canvas.setFont("UI", 8.8)
        canvas.setFillColor(BRAND_BLUE)
        canvas.drawRightString(w - doc.rightMargin, top_y + 1.2 * mm,
                               "IT Shaharcha | Python noldan")
        # Header ajratuvchi chiziq
        canvas.setStrokeColor(CODE_BORDER)
        canvas.setLineWidth(0.8)
        canvas.line(doc.leftMargin, top_y - 3 * mm, w - doc.rightMargin, top_y - 3 * mm)

        # Footer
        canvas.setStrokeColor(CODE_BORDER)
        canvas.line(doc.leftMargin, 14 * mm, w - doc.rightMargin, 14 * mm)
        canvas.setFont("UI", 8.5)
        canvas.setFillColor(LIGHT_GREY)
        canvas.drawString(doc.leftMargin, 10 * mm, "© IT Shaharcha")
        canvas.drawCentredString(w / 2, 10 * mm,
                                 f"{self.lesson_no}-dars: {self.topic}")
        canvas.drawRightString(w - doc.rightMargin, 10 * mm, f"{doc.page}-bet")
        canvas.restoreState()

    # --- sarlavha bloki (1-sahifa) ---
    def add_header_block(self, subtitle):
        self.story.append(Spacer(1, 2 * mm))
        badge = Table([[Paragraph(f"<font color='white'><b>{self.lesson_no}-DARS</b></font>",
                       ParagraphStyle("b", fontName="UI-Bold", fontSize=11,
                                      textColor=colors.white))]],
                      colWidths=[26 * mm])
        badge.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BRAND_ACCENT),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("ROUNDEDCORNERS", [3, 3, 3, 3]),
        ]))
        self.story.append(badge)
        self.story.append(Spacer(1, 4 * mm))
        self.story.append(Paragraph(_esc(self.topic), styles["title"]))
        self.story.append(Paragraph(_esc(subtitle), styles["subtitle"]))
        self.story.append(HRFlowable(width="100%", thickness=1.4, color=BRAND_BLUE,
                                     spaceBefore=4, spaceAfter=8))

    def h2(self, text):
        self.story.append(Paragraph(_esc(text), styles["h2"]))

    def h3(self, text):
        self.story.append(Paragraph(_esc(text), styles["h3"]))

    def p(self, text):
        self.story.append(Paragraph(_inline(text), styles["p"]))

    def bullets(self, items):
        for it in items:
            self.story.append(Paragraph(_inline(it), styles["bullet"], bulletText="•"))
        self.story.append(Spacer(1, 3))

    def code(self, code, caption=None):
        block = [CodeBox(code, self.content_w)]
        if caption:
            block.append(Spacer(1, 2))
            block.append(Paragraph("▸ " + _esc(caption), styles["caption"]))
        self.story.append(KeepTogether(block))
        self.story.append(Spacer(1, 6))

    def note(self, text):
        self.story.append(note_box(_esc(text), self.content_w))
        self.story.append(Spacer(1, 6))

    def spacer(self, mm_h=3):
        self.story.append(Spacer(1, mm_h * mm))

    def build(self):
        self.doc.build(self.story)


def make_lesson(out_path, no, topic, subtitle, sections):
    """
    sections: list of tuples:
      ("h2", "...") ("h3","...") ("p","...") ("bul", [..]) ("code", "...", "caption?") ("note","...")
    """
    b = PDFBuilder(out_path, no, topic)
    b.add_header_block(subtitle)
    for sec in sections:
        kind = sec[0]
        if kind == "h2":
            b.h2(sec[1])
        elif kind == "h3":
            b.h3(sec[1])
        elif kind == "p":
            b.p(sec[1])
        elif kind == "bul":
            b.bullets(sec[1])
        elif kind == "code":
            cap = sec[2] if len(sec) > 2 else None
            b.code(sec[1], cap)
        elif kind == "note":
            b.note(sec[1])
        elif kind == "sp":
            b.spacer(sec[1] if len(sec) > 1 else 3)
    b.build()
    return out_path

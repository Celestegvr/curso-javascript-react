# -*- coding: utf-8 -*-
"""Genera documentacion.html (para imprimir a PDF) y el .docx a partir de contenido.py.
Uso: python generar.py <ruta_docx_salida>
"""
import html, re, sys, os
from contenido import *

AQUI = os.path.dirname(os.path.abspath(__file__))
CAP = os.path.join(AQUI, "capturas")

# ---------- numeración ----------
def numerar():
    paso = fig = 0
    out = []
    for b in BLOQUES:
        if b[0] == "paso":
            paso += 1; out.append(("paso", paso, b[1]))
        elif b[0] == "img":
            fig += 1; out.append(("img", fig, b[1], b[2]))
        else:
            out.append(b)
    return out

def inline_html(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"``\s?(.+?)\s?``", r"<code>\1</code>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<em>\1</em>", t)
    return t

def bloques_html(lista):
    h = []
    n = 0
    for b in lista:
        k = b[0]
        if k in ("parte", "paso"): n = 0
        if k == "parte":
            h.append(f'<section class="parte"><div class="kicker">{b[1]}</div><h1>{inline_html(b[2])}</h1><p>{inline_html(b[3])}</p></section>')
        elif k == "paso":
            h.append(f'<h2 id="p{b[1]}"><span class="num">{b[1]}</span>{inline_html(b[2])}</h2>')
        elif k == "p":
            h.append(f"<p>{inline_html(b[1])}</p>")
        elif k == "ol":
            h.append(f'<ol start="{n + 1}">' + "".join(f"<li>{inline_html(i)}</li>" for i in b[1]) + "</ol>")
            n += len(b[1])
        elif k == "ul":
            h.append("<ul>" + "".join(f"<li>{inline_html(i)}</li>" for i in b[1]) + "</ul>")
        elif k == "code":
            h.append(f'<div class="code"><div class="cap">{html.escape(b[1])}</div><pre>{html.escape(b[2])}</pre></div>')
        elif k == "img":
            h.append(f'<figure><img src="capturas/{b[2]}"><figcaption><b>Figura {b[1]}.</b> {inline_html(b[3])}</figcaption></figure>')
        elif k == "nota":
            h.append(f'<div class="nota {b[1]}"><b>{inline_html(b[2])}</b>{inline_html(b[3])}</div>')
    return "\n".join(h)

def generar_html(nb):
    pasos = [(b[1], b[2]) for b in nb if b[0] == "paso"]
    partes, indice, actual = [], [], None
    for b in nb:
        if b[0] == "parte":
            indice.append(f'<li class="ip">{b[1]} · {inline_html(b[2])}</li>')
        if b[0] == "paso":
            indice.append(f'<li><a href="#p{b[1]}">{b[1]}. {inline_html(b[2])}</a></li>')
    css = """
@page{size:A4;margin:20mm 18mm 20mm 18mm}
*{box-sizing:border-box}
body{font-family:"Segoe UI",Calibri,Arial,sans-serif;color:#1d1f24;font-size:11pt;line-height:1.5;margin:0}
.portada{height:257mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always;padding:10mm 0}
.portada .banda{height:10mm;background:linear-gradient(90deg,#f0c419,#38bdf8);border-radius:3mm}
.portada h1{font-size:34pt;line-height:1.1;margin:0 0 6mm;color:#111}
.portada .sub{font-size:16pt;color:#555;margin:0}
.portada .curso{font-size:12pt;color:#333;margin-top:10mm}
.portada .datos{font-size:12pt;border-top:1px solid #ddd;padding-top:6mm}
.portada .datos div{margin:1.5mm 0}
.indice{page-break-after:always}
.indice h1{font-size:20pt;margin:0 0 6mm}
.indice ul{list-style:none;padding:0;margin:0;columns:1}
.indice li{padding:1.4mm 0;border-bottom:1px dotted #ccc}
.indice li.ip{font-weight:700;border:0;margin-top:4mm;color:#0c6e94}
.indice a{color:#1d1f24;text-decoration:none}
.parte{page-break-before:always;border-left:5mm solid #f0c419;padding:3mm 0 3mm 6mm;margin-bottom:6mm}
.parte .kicker{font-size:10pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#0c6e94}
.parte h1{font-size:22pt;margin:1mm 0 2mm}
.parte p{margin:0;color:#444}
h2{font-size:15pt;margin:9mm 0 3mm;display:flex;align-items:center;gap:3mm;page-break-after:avoid}
h2 .num{display:inline-flex;align-items:center;justify-content:center;width:9mm;height:9mm;border-radius:2mm;background:#f0c419;font-size:12pt;flex:none}
p{margin:2.5mm 0}
ol,ul{margin:2mm 0 3mm;padding-left:7mm}
li{margin:1.2mm 0}
code{font-family:Consolas,"Cascadia Mono",monospace;font-size:9.5pt;background:#f1f2f4;border:1px solid #e1e3e8;border-radius:1mm;padding:0 1mm}
figure{margin:4mm 0 5mm;page-break-inside:avoid;text-align:center}
figure img{max-width:100%;max-height:150mm;border:1px solid #d8dbe0;border-radius:1.5mm}
figcaption{font-size:9.5pt;color:#555;margin-top:1.5mm}
.nota{border:1px solid;border-left-width:2mm;border-radius:1.5mm;padding:2.5mm 4mm;margin:3mm 0;font-size:10pt;page-break-inside:avoid}
.nota b{display:block;margin-bottom:.5mm}
.nota.info{border-color:#38bdf8;background:#f0f9ff}.nota.info b{color:#0c6e94}
.nota.hoy{border-color:#f59e0b;background:#fffbeb}.nota.hoy b{color:#a35a00}
.nota.error{border-color:#ef4444;background:#fef2f2}
.code{border:1px solid #d8dbe0;border-radius:1.5mm;overflow:hidden;margin:3mm 0;page-break-inside:avoid}
.code .cap{background:#2b2f3a;color:#cfd3dc;font:9pt Consolas,monospace;padding:1.5mm 3mm}
.code pre{margin:0;background:#1e1e1e;color:#d4d4d4;font:9.5pt/1.45 Consolas,monospace;padding:3mm;white-space:pre-wrap}
.cierre{margin-top:8mm;border-top:2px solid #f0c419;padding-top:4mm}
"""
    intro = bloques_html(INTRO)
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>{TITULO}</title><meta name="author" content="{AUTORA}"><style>{css}</style></head><body>
<section class="portada"><div class="banda"></div>
<div><h1>{TITULO}</h1><p class="sub">{SUBTITULO}</p><p class="curso">{CURSO}</p></div>
<div class="datos"><div><b>Elaborado por:</b> {AUTORA}</div><div><b>Carnet:</b> {CARNET}</div><div><b>Fecha:</b> {FECHA}</div>
<div><b>Código:</b> {REPO}</div><div><b>Sitio publicado:</b> {SITIO}</div></div></section>
<section class="indice"><h1>Contenido</h1><ul><li class="ip">Introducción</li>{''.join(indice)}<li class="ip">Resumen</li></ul></section>
<section><h1 style="font-size:20pt">Introducción</h1>{intro}</section>
{bloques_html(nb)}
<section class="cierre"><h2>Resumen</h2>{bloques_html(CIERRE)}</section>
</body></html>"""

# ---------- Word ----------
def generar_docx(nb, ruta):
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    d = Document()
    sec = d.sections[0]
    sec.page_height, sec.page_width = Cm(29.7), Cm(21)
    for m in ("left_margin", "right_margin"): setattr(sec, m, Cm(2))
    sec.top_margin = sec.bottom_margin = Cm(2)
    st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(11)
    d.core_properties.author = AUTORA; d.core_properties.title = TITULO

    def sombrear(el, color):
        pr = el._p.get_or_add_pPr() if hasattr(el, "_p") else el._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), color); pr.append(shd)

    def runs(p, t):
        for parte in re.split(r"(\*\*.+?\*\*|``\s?.+?\s?``|`[^`]+`)", t):
            if not parte: continue
            if parte.startswith("**"):
                p.add_run(parte[2:-2]).bold = True
            elif parte.startswith("`"):
                r = p.add_run(parte.strip("`").strip() if parte.startswith("``") else parte[1:-1])
                r.font.name = "Consolas"; r.font.size = Pt(9.5); r.font.color.rgb = RGBColor(0xB0, 0x3A, 0x2E)
            else:
                p.add_run(parte)

    def escribir(lista):
        n = 0
        for b in lista:
            k = b[0]
            if k in ("parte", "paso"): n = 0
            if k == "parte":
                d.add_page_break()
                p = d.add_paragraph(); r = p.add_run(b[1].upper()); r.bold = True; r.font.color.rgb = RGBColor(0x0C, 0x6E, 0x94); r.font.size = Pt(10)
                d.add_heading(re.sub(r"`", "", b[2]), level=1)
                runs(d.add_paragraph(), b[3])
            elif k == "paso":
                d.add_heading(f"Paso {b[1]}. {b[2]}", level=2)
            elif k == "p":
                runs(d.add_paragraph(), b[1])
            elif k == "ol":
                for i, it in enumerate(b[1], n + 1):
                    p = d.add_paragraph(); p.paragraph_format.left_indent = Cm(0.8); p.paragraph_format.first_line_indent = Cm(-0.6)
                    p.add_run(f"{i}.  ").bold = True; runs(p, it)
                n += len(b[1])
            elif k == "ul":
                for it in b[1]:
                    p = d.add_paragraph(style="List Bullet"); runs(p, it)
            elif k == "code":
                p = d.add_paragraph(); r = p.add_run(b[1]); r.bold = True; r.font.size = Pt(9)
                for linea in b[2].split("\n"):
                    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(0); sombrear(p, "F1F2F4")
                    r = p.add_run(linea or " "); r.font.name = "Consolas"; r.font.size = Pt(9)
                d.add_paragraph()
            elif k == "img":
                p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.add_run().add_picture(os.path.join(CAP, b[2]), width=Cm(16))
                c = d.add_paragraph(); c.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = c.add_run(f"Figura {b[1]}. "); r.bold = True; r.font.size = Pt(9)
                r2 = c.add_run(re.sub(r"`", "", b[3])); r2.font.size = Pt(9); r2.italic = True
            elif k == "nota":
                t = d.add_table(rows=1, cols=1); cel = t.rows[0].cells[0]
                sombrear(cel, {"info": "EAF6FD", "hoy": "FFF7E0", "error": "FDECEC"}[b[1]])
                p = cel.paragraphs[0]; r = p.add_run(b[2] + ". "); r.bold = True
                runs(p, b[3]); d.add_paragraph()

    # portada
    for _ in range(6): d.add_paragraph()
    p = d.add_paragraph(); r = p.add_run(TITULO); r.bold = True; r.font.size = Pt(30)
    p = d.add_paragraph(); r = p.add_run(SUBTITULO); r.font.size = Pt(16); r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    d.add_paragraph(CURSO)
    for _ in range(8): d.add_paragraph()
    for etq, val in (("Elaborado por", AUTORA), ("Carnet", CARNET), ("Fecha", FECHA), ("Código", REPO), ("Sitio publicado", SITIO)):
        p = d.add_paragraph(); p.add_run(etq + ": ").bold = True; p.add_run(val)
    d.add_page_break()
    d.add_heading("Introducción", level=1)
    escribir(INTRO)
    escribir(nb)
    d.add_heading("Resumen", level=1)
    escribir(CIERRE)
    # pie con nombre
    pie = sec.footer.paragraphs[0]; pie.text = f"{AUTORA} · {TITULO}"; pie.alignment = WD_ALIGN_PARAGRAPH.CENTER
    d.save(ruta)

if __name__ == "__main__":
    nb = numerar()
    faltan = [b[2] for b in nb if b[0] == "img" and not os.path.exists(os.path.join(CAP, b[2]))]
    if faltan: sys.exit("Faltan capturas: " + ", ".join(faltan))
    with open(os.path.join(AQUI, "documentacion.html"), "w", encoding="utf-8") as f:
        f.write(generar_html(nb))
    if len(sys.argv) > 1:
        generar_docx(nb, sys.argv[1])
    print("pasos:", sum(1 for b in nb if b[0] == "paso"), "figuras:", sum(1 for b in nb if b[0] == "img"))

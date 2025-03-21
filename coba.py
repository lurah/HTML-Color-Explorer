import kolor
from fasthtml.common import *

def display_tbl_nm_kl(kl):
    tabel = getattr(kolor, kl)
    tbl = []
    for sel in tabel.keys():
        kmplmn = f"rgb{tuple((255 - i) for i in tabel[sel])}"
        if kl == "gray": kmplmn = f"rgb(255,255,255)" 
        sty_td = f"text-align: center; padding: 6px; color: {kmplmn}; \
                   background-color: {sel}; font-size: .8rem; margin: 2px;"
        tbl.append(Span(f"{sel}", style=f"{sty_td}"))
    sty = f"display: flex; flex-direction: row; justify-content: flex-start; \
            flex-wrap: wrap; padding: 2px"
    return Div(*tbl, id="kolor", style=sty)

def jdl_kl():
    judul = ("Red", "Pink", "Orange", "Yellow", "Purple", "Green", "Blue", "Brown",
             "White", "Gray")
    sty_sp = f"background-color: paleturquoise; display: inline-block; padding: 2px 6px; \
               margin: 2px; border-radius: 15%; font-size: .8rem; font-weight: bold;"
    sepan = []
    for klr in judul:
        vals = {"nm_klr":f"{klr.lower()}"}
        prm = {"hx_swap":"outerHTML", "hx_post":"/klr_name", "hx_trigger":"click", 
               "hx_target":"#kolor", "hx_vals":vals}
        sepan.append(Span(klr, style=sty_sp, **prm))

    sty = f"display: flex; flex-direction: row; justify-content: flex-start; \
            flex-wrap: wrap; max-width: 300px; margin-bottom: 4px;"
    
    return Div(*sepan, style = sty)

def rgb_distance(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)

def closest_named_color(target_rgb):
    klr = ("blue", "brown", "gray", "green", "orange", "pink", "purple",
            "red", "white", "yellow")
    min = float("inf")
    clst = None
    for klr_i in klr:
        for name, rgb in getattr(kolor, klr_i).items():
            distance = rgb_distance(target_rgb, rgb)
            if distance < min:
                min = distance
                clst = name
                clst_pg = klr_i
    return clst_pg, clst

print(closest_named_color((255,0,0)))

"""
app = FastHTML()

@app.post("/klr_name")
def ganti_klr(nm_klr:str):
    return display_tbl_nm_kl(nm_klr)

@app.get("/")
def main():
    sty = f"border: 1px solid black; max-width: 300px;"
    return Main(jdl_kl(), Div(display_tbl_nm_kl("white"), style=sty))

serve()
"""


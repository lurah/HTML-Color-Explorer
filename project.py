import ast
import math
import kolor
import itertools
from fasthtml.common import *
from starlette.testclient import TestClient

class Warna():

    def __init__(self, red="255", green="0", blue="0"):
        self._red = red
        self._green = green
        self._blue = blue        
        self.judul = "Color Box"

    def warnanya(self):
        return f"rgb({self.red}, {self.green}, {self.blue})"

    def hslnya(self):
        return self.rgb_to_hsl(self.warnanya())

    def slider_cmp(self, tipe:str, rgbhsl:str):
        if tipe == "rgb":
            nilai = getattr(self, rgbhsl)
            maks = "255"
            filt = [item for item in ["#red", "#green", "#blue"] if item != f"#{rgbhsl}"]
            incl = ", ".join(filt) + ", #hue, #saturation, #lightness"
            vals = '{"data_cmp":"rgb"}'
        else:
            nilai = self.hslnya()[rgbhsl]
            maks = "360" if rgbhsl == "hue" else "100"
            filt = [item for item in ["#hue", "#saturation", "#lightness"] if item != f"#{rgbhsl}"]
            incl = ", ".join(filt) + ", #red, #green, #blue"
            vals = '{"data_cmp":"hsl"}'
        prm = {"type":"range", "min":"0", "max":maks, "hx_swap":"innerHTML",
               "hx_post":"/tengah", "hx_trigger":"input", "hx_target":"#tengah",
               "hx_include":incl, "hx_vals":vals,}
        lbl = Label(f"{rgbhsl.capitalize()}:", fr=rgbhsl)
        inp = Input(id=rgbhsl, name=rgbhsl, value=f"{nilai}", **prm)
        div_sty = f"display: flex; flex-direction: column; justify-content: flex-start; \
                    margin: 5px;"
        return Div(lbl, inp, style=div_sty)
    
    def slider_rgb(self):
        sty_rgb_hsl = f"display: flex; flex-direction: column; justify-content: flex-start; \
                        align-items: center; border: 1px solid black; margin: 10px; \
                        padding: 5px; min-width: 150px; max-width: 200px;"
        return Div(self.slider_cmp("rgb","red"), self.slider_cmp("rgb","green"),
                   self.slider_cmp("rgb","blue"), id="sldrgb", hx_swap_oob="innerHTML",
                   style=sty_rgb_hsl)
    
    def slider_hsl(self):
        sty_rgb_hsl = f"display: flex; flex-direction: column; justify-content: flex-start; \
                        align-items: center; border: 1px solid black; margin: 10px; \
                        padding: 5px; min-width: 150px; max-width: 200px;"
        return Div(self.slider_cmp("hsl","hue"), self.slider_cmp("hsl","saturation"),
                   self.slider_cmp("hsl","lightness"),  id="sldhsl", hx_swap_oob="innerHTML",
                   style=sty_rgb_hsl)
    
    def slider(self):
        sty = f"display: flex; flex-direction: column; justify-content: flex-start;"
        return Div(self.slider_rgb(), self.slider_hsl(), style=sty)

    def kotak_warna(self):
        sty = f"width: 60%; height: 50px; background-color: {self.warnanya()}; \
                border: 1px solid {self.warnanya()}; margin: 30px auto 10px auto;"
        return Div(id="warna", style=sty)
   
    def teks_cmp(self, tipe:str, rgbhsl:str):
        if tipe == "rgb":
            warna = rgbhsl
            nilai = getattr(self, rgbhsl)
        else:
            warna = self.warnanya()
            nilai = self.hslnya()[rgbhsl]

        lbl_sty = f"display: block; text-align: center; color: {warna}"
        inp_sty = f"height: 16px; margin: 3px 0; width: 25px; border: none; \
                    text-align: center; color: {warna}"
        div_sty = f"display: flex; flex-direction: column; align-items: center; margin: 0 5px; \
                    min-width: 50px; padding: 5px; border: 1px solid {warna}"

        lbl = Label(f"{rgbhsl.capitalize()}", fr=f"rgb_{rgbhsl}", style=lbl_sty)
        inp = Input(name=f"rgb_{rgbhsl}", id=f"rgb_{rgbhsl}", type="text",
                    value=f"{nilai}", style=inp_sty)
        return Div(inp, lbl, style=div_sty)
    
    def teks(self, tipe:str):
        judul_sty = f"margin: 15px auto 5px auto; color: {self.warnanya()};"
        each_sty = f"display: flex; justify-content: center;"
        all_sty = f"display: flex; flex-direction: column; justify-content: center; \
                    align-items: center; margin: 0px auto 10px auto;"
        
        jdl_teks = "RGB Value" if tipe == "rgb" else "HSL Value"
        judul = H3(jdl_teks, style=judul_sty)
        if tipe == "rgb":
            teks = Div(self.teks_cmp(tipe,"red"), self.teks_cmp(tipe,"green"),
                       self.teks_cmp(tipe,"blue"), style=each_sty)
        else:
            teks = Div(self.teks_cmp(tipe,"hue"), self.teks_cmp(tipe,"saturation"),
                       self.teks_cmp(tipe,"lightness"), style=each_sty)
        return Div(judul, teks, style=all_sty)

    def tengah(self):
        sty = f"display: flex; flex-direction: column; align-items: center; \
                margin: 10px; padding: 0 5px 0 5px; border: 1px solid black; "
        return Div(self.kotak_warna(), self.teks("rgb"), self.teks("hsl"), id="tengah", style=sty)
    
    def display_tbl_nm_kl(self, kl):
        tabel = getattr(kolor, kl)
        tbl = []
        for sel in tabel.keys():
            kmplmn = f"rgb{tuple((255 - i) for i in tabel[sel])}"
            if kl == "gray": kmplmn = f"rgb(255,255,255)" 
            sty_td = f"text-align: center; padding: 6px; color: {kmplmn}; border-radius: 5%; \
                       background-color: {sel}; font-size: .8rem; margin: 2px; cursor: pointer;"
            prm_nm_kl = {"hx_swap":"innerHTML", "hx_post":"/name_klr", "hx_trigger":"click", 
                         "hx_target":"#tengah", "hx_vals":{"name_klr":sel, "kl": kl}}
            tbl.append(Span(f"{sel}", style=f"{sty_td}", **prm_nm_kl))
        sty = f"display: flex; flex-direction: row; justify-content: flex-start; \
                flex-wrap: wrap; padding: 2px"
        return Div(*tbl, id="kolor", style=sty)

    def jdl_kl(self, kl):
        judul = ("Red", "Pink", "Orange", "Yellow", "Purple", "Green", "Blue", "Brown",
                 "White", "Gray")
        sty_sp = f"background-color: paleturquoise; display: inline-block; padding: 4px 6px; \
                   border-radius: 5%; margin: 2px; font-size: .8rem; font-weight: bold; \
                   color: black; cursor: pointer;"
        sepan = []
        for klr in judul:
            sty_sp_blink = sty_sp if klr != kl.capitalize() else sty_sp + f" color: brown;"
            vals = {"nm_klr":f"{klr.lower()}", "red": f"{self.red}", "green": f"{self.green}",
                    "blue": f"{self.blue}"}
            prm = {"hx_swap":"outerHTML", "hx_post":"/klr_name", "hx_trigger":"click", 
                   "hx_target":"#kolor", "hx_vals":vals}
            sepan.append(Span(klr, style=sty_sp_blink, **prm))
        sty = f"display: flex; flex-direction: row; justify-content: flex-start; \
                flex-wrap: wrap; max-width: 300px; margin: 4px; background-color: papayawhip"
        return Div(*sepan, id="jdl_klr", style = sty, hx_swap_oob="outerHTML")
        
    def klr_isi(self):
        sty_klr = f"max-width: 300px;"
        rgb = (int(self.red), int(self.green), int(self.blue))
        pg_klr, _ = Warna.closest_named_color(rgb)
        return Div(self.jdl_kl(f"{pg_klr}"), Hr(style="margin: 0;"), 
                   Div(self.display_tbl_nm_kl(f"{pg_klr}"),style=sty_klr),
                   id="klr_nama", hx_swap_oob="innerHTML")
        
    def semua(self):
        sty_klr_isi = f"margin: 10px; border: 1px solid black;"
        klr_lengkap = Div(self.klr_isi(), style = sty_klr_isi)
        sty = f"display: flex; justify-content: center; align-items: flex-start; flex-wrap: wrap;"
        return Div(self.slider(), self.tengah(), klr_lengkap, style=sty)
    

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green
    
    @property
    def blue(self):
        return self._blue
    
    @red.setter
    def red(self,new_value:str):
        if not new_value:
            raise ValueError ("Red Value not Blank")
        self._red = new_value

    @blue.setter
    def blue(self,new_value:str):
        if not new_value:
            raise ValueError ("Blue Value not Blank")
        self._blue = new_value

    @green.setter
    def green(self,new_value:str):
        if not new_value:
            raise ValueError ("Green Value not Blank")
        self._green = new_value

    @staticmethod
    def rgb_to_hsl(rgb: str):
        bgr = ast.literal_eval(rgb.replace("rgb", ""))
        r = (int(bgr[0])+1)/256
        g = (int(bgr[1])+1)/256
        b = (int(bgr[2])+1)/256
    
        maks = max(r, g, b)
        mins = min(r, g, b)
        lith = (maks + mins)/2

        if maks == mins:
            hu = 0
            sat = 0
        else:
            if lith <= 0.5:
                sat = (maks - mins)/(maks + mins)
            else:
                sat = (maks - mins)/(2 - maks - mins)
            if maks == r:
                hu = (g - b)/(maks - mins)
                if g < b:
                    hu += 6
            elif maks == g:
                hu = ((b - r)/(maks - mins)) + 2
            else:
                hu = ((r - g)/(maks-mins)) + 4
            hu /= 6

        return {"hue":f"{int(hu * 360)}", "saturation": f"{int(sat * 100)}", 
                "lightness": f"{int(lith * 100)}"}

    @staticmethod
    def hsl_to_rgb(h, s, l):
        h /= 360.0  # Normalize hue
        s /= 100.0  # Normalize saturation
        l /= 100.0  # Normalize lightness

        def hue_to_rgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1/6:
                return p + (q - p) * 6 * t
            if t < 1/2:
                return q
            if t < 2/3:
                return p + (q - p) * (2/3 - t) * 6
            return p

        if s == 0:
            r, g, b = l, l, l  # Grayscale
        else:
            if l < 0.5:
                q = l * (1 + s)
            else:
                q = l + s - l * s
            p = 2 * l - q

            r = hue_to_rgb(p, q, h + 1/3)
            g = hue_to_rgb(p, q, h)
            b = hue_to_rgb(p, q, h - 1/3)
        return (round(r * 255), round(g * 255), round(b * 255))

    @staticmethod
    def rgb_distance(rgb1, rgb2):
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        return math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)

    @staticmethod
    def closest_named_color(target_rgb):
        klr = ("blue", "brown", "gray", "green", "orange", "pink", "purple",
               "red", "white", "yellow")
        min = float("inf")
        clst = None
        for klr_i in klr:
            for name, rgb in getattr(kolor, klr_i).items():
                distance = Warna.rgb_distance(target_rgb, rgb)
                if distance < min:
                    min = distance
                    clst = name
                    clst_pg = klr_i
        return clst_pg, clst

def semua():
    lk_semua = APIRouter()
    @lk_semua.get("/")
    def flk_semua():
        kotak = Warna()
        return kotak.semua()
    return lk_semua

def tengah():
    lk_tengah = APIRouter()
    @lk_tengah.post("/tengah")
    def ftengah(red:str, green: str, blue: str, 
                hue:str, saturation:str, lightness:str,
                data_cmp:str):
        if data_cmp == "hsl":
            hsl = (int(hue), int(saturation), int(lightness))
            rgb = Warna.hsl_to_rgb(*hsl)
            warna = {"red":rgb[0], "green":rgb[1], "blue":rgb[2]}
        else:
            warna = {"red":red, "green":green, "blue":blue}
        kotak = Warna(**warna)
        return kotak.kotak_warna(), kotak.teks("rgb"), kotak.teks("hsl"), \
               kotak.slider_rgb() if data_cmp == "hsl" else kotak.slider_hsl(), \
               kotak.klr_isi()
    return lk_tengah

def ganti_klr():
    lk_tengah = APIRouter()
    @lk_tengah.post("/klr_name")
    def fganti_klr(nm_klr:str, red:str, green:str, blue:str):
        klr = Warna(red,green,blue)
        return klr.display_tbl_nm_kl(nm_klr), klr.jdl_kl(nm_klr)
    return lk_tengah

def name_kl():
    lk_name_kl = APIRouter()
    @lk_name_kl.post("/name_klr")
    def name_kl(name_klr:str, kl:str):
        r,g,b = getattr(kolor, kl)[name_klr]
        kotak = Warna(f"{r}", f"{g}", f"{b}")
        return kotak.kotak_warna(), kotak.teks("rgb"), kotak.teks("hsl"), \
               kotak.slider_rgb(), kotak.slider_hsl()
    return lk_name_kl
    
def main():
    app = FastHTML()
    semua().to_app(app)
    tengah().to_app(app)
    ganti_klr().to_app(app)
    name_kl().to_app(app)
    return app


if __name__ == "__main__":
    uvicorn.run("project:main", host="127.0.0.1", port=8000, reload=True, factory=True)
    
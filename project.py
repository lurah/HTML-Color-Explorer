from warna import Warna
from fasthtml.common import *
import kolor
import ast

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

def flt_nl():
    lk_filter = APIRouter()
    @lk_filter.post("/flt_nl")
    def filter(tipe:str, ist:str, rgbhsl:str, rgb_red:str=None, rgb_blue:str=None,
               rgb_green:str=None, rgb_hue:str=None, rgb_saturation:str=None,
               rgb_lightness:str=None):
        rgb = [int(kl) for kl in ast.literal_eval(ist.strip("rgb"))]
        if tipe == "rgb":
            match rgbhsl:
                case "red": rgb[0] = min(int(rgb_red),255)
                case "green": rgb[1] = min(int(rgb_green),255)
                case "blue": rgb[2] = min(int(rgb_blue),255)
        else:
            hsl = {key:int(value) for key,value in Warna.rgb_to_hsl(ist).items()}
            match rgbhsl:
                case "hue": hsl["hue"] = min(int(rgb_hue),360)
                case "saturation": hsl["saturation"] = min(int(rgb_saturation),100)
                case "lightness": hsl["lightness"] = min(int(rgb_lightness),100)
            rgb = Warna.hsl_to_rgb(hsl["hue"], hsl["saturation"], hsl["lightness"])
        warnanya = {"red":f"{rgb[0]}","green":f"{rgb[1]}","blue":f"{rgb[2]}"}
        kotak = Warna(**warnanya)    
        return kotak.kotak_warna(), kotak.teks("rgb"), kotak.teks("hsl"), \
               kotak.slider_rgb(), kotak.slider_hsl(), \
               kotak.klr_isi()
    return lk_filter

def main():
    app = FastHTML()
    semua().to_app(app)
    tengah().to_app(app)
    ganti_klr().to_app(app)
    name_kl().to_app(app)
    flt_nl().to_app(app)
    return app

if __name__ == "__main__":
    uvicorn.run("project:main", host="127.0.0.1", port=8000, reload=True, factory=True)
    
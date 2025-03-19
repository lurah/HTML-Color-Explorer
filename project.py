import ast
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


    def slider_rgb_cmp(self, color: str):
        filt = [item for item in ["#red", "#green", "#blue"] if item != f"#{color}"]
        incl = ", ".join(filt) + ", #hue, #saturation, #lightness"
        prm = {"type":"range", "min":"0", "max":"255", "hx_swap":"innerHTML",
               "hx_post":"/tengah", "hx_trigger":"input", "hx_target":"#tengah"}
        lbl = Label(f"{color.capitalize()}:", fr=color)
        inp = Input(id=color, name=color, value=getattr(self, color), 
                    hx_include=incl, **prm)
        div_sty = f"display: flex; flex-direction: column; justify-content: flex-start; \
                    margin: 5px;"
        return Div(lbl, inp, style=div_sty)
        
    def slider_rgb(self):
        sty = f"display: flex; flex-direction: column; justify-content: flex-start; \
                align-items: center; border: 1px solid black; margin: 10px; \
                padding: 5px; min-width: 150px; max-width: 200px;"
        return Div(self.slider_rgb_cmp("red"), self.slider_rgb_cmp("green"),
                    self.slider_rgb_cmp("blue"), style=sty)
    
    def slider_hsl_cmp(self, hsl: str):
        nilai = self.hslnya()[hsl]
        maks = "360" if hsl == "hue" else "100"
        print(nilai, maks)
        filt = [item for item in ["#hue", "#saturation", "#lightness"] if item != f"#{hsl}"]
        incl = ", ".join(filt) + ", #red, #green, #blue"
        prm = {"type":"range", "min":"0", "max":maks, "hx_swap":"innerHTML",
               "hx_post":"/tengah", "hx_trigger":"input", "hx_target":"#tengah"}
        lbl = Label(f"{hsl.capitalize()}:", fr=hsl)
        inp = Input(id=hsl, name=hsl, value=nilai, 
                    hx_include=incl, **prm)
        div_sty = f"display: flex; flex-direction: column; justify-content: flex-start; \
                    margin: 5px;"
        return Div(lbl, inp, style=div_sty)
    
    def slider_hsl(self):
        sty = f"display: flex; flex-direction: column; justify-content: flex-start; \
                align-items: center; border: 1px solid black; margin: 10px; \
                padding: 5px; min-width: 150px; max-width: 200px;"
        return Div(self.slider_hsl_cmp("hue"), self.slider_hsl_cmp("saturation"),
                    self.slider_hsl_cmp("lightness"), style=sty)
    
    def slider(self):
        sty = f"display: flex; flex-direction: column; justify-content: flex-start;"
        return Div(self.slider_rgb(), self.slider_hsl(), style=sty)

    def kotak_warna(self):
        sty = f"width: 60%; height: 50px; background-color: {self.warnanya()}; \
                border: 1px solid {self.warnanya()}; margin: 30px auto 10px auto;"
        return Div(id="warna", style=sty)
    

    def lbl_sty(self):
        return f"display: block; text-align: center; color: "
    
    def inp_sty(self):
        return f"height: 16px; margin: 3px 0; width: 25px; border: none; text-align: center; color: "

    def div_sty(self):
        return f"display: flex; flex-direction: column; align-items: center; margin: 0 5px; \
                    min-width: 50px; padding: 5px; border: 1px solid "
    
    def judul_sty(self):
        return f"margin: 15px auto 5px auto; color: {self.warnanya()};"
    
    def each_sty(self):
        return f"display: flex; justify-content: center;"
    
    def all_sty(self):
        return f"display: flex; flex-direction: column; justify-content: center; \
                 align-items: center; margin: 0px auto 10px auto;"
    
    def rgb_cmp(self, color: str):
        lbl = Label(f"{color.capitalize()}", fr=f"rgb_{color}", style=self.lbl_sty()+f"{color};") 
        inp = Input(name=f"rgb_{color}", id=f"rgb_{color}", type="text",
                    value=getattr(self, color), style=self.inp_sty()+f"{color};")
        return Div(inp, lbl, style=self.div_sty()+f"{color};")
    
    def rgb(self):
        judul = H3("RGB Value", style=self.judul_sty())
        return Div(judul, 
                   Div(self.rgb_cmp("red"), self.rgb_cmp("green"),
                       self.rgb_cmp("blue"), style=self.each_sty()),
                       style=self.all_sty())
    
    def hsl_cmp(self, prm: str):
        lbl = Label(f"{prm.capitalize()}", fr=f"{prm}", style=self.lbl_sty()+f"{self.warnanya()};")
        inp = Input(name=f"{prm}", id=f"{prm}", type="text",
                    value=f"{self.hslnya()[prm]}", style=self.inp_sty()+f"{self.warnanya()};")
        return Div(inp, lbl, style=self.div_sty()+f"{self.warnanya()};")
    
    def hsl(self):        
        judul = H3("HSL Value", style=self.judul_sty())
        return Div(judul, 
                   Div(self.hsl_cmp("hue"), self.hsl_cmp("saturation"), 
                       self.hsl_cmp("lightness"), style=self.each_sty()), 
                   style=self.all_sty())

    def tengah(self):
        sty = f"display: flex; flex-direction: column; align-items: center; \
                margin: 10px; padding: 0 5px 0 5px; border: 1px solid {self.warnanya()}; "
        return Div(self.kotak_warna(), self.rgb(), self.hsl(), id="tengah", style=sty)
    

    def semua(self):
        sty = f"display: flex; justify-content: center; align-items: flex-start"
        return Div(self.slider(), self.tengah(), style=sty)
    

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
    def ftengah(red:str, green: str, blue: str, hue:str, saturation:str, lightness:str):
        warna = {"red":red, "green": green, "blue": blue}
        kotak = Warna(**warna)
        return kotak.kotak_warna(), kotak.rgb(), kotak.hsl()
        #return kotak.tengah()
    return lk_tengah

def main():
    app = FastHTML()
    semua().to_app(app)
    tengah().to_app(app)
    return app


if __name__ == "__main__":
    uvicorn.run("project12:main", host="127.0.0.1", port=8000, reload=True, factory=True)
    
import kolor
from fasthtml.common import *

def cetak(kol):
    tabel = getattr(kolor, kol)
        
    tbl = []
    for sel in tabel.keys():
        kmplmn = f"rgb{tuple((255 - i) for i in tabel[sel])}"
        sty_td = f"text-align: center; padding: 6px; color: {kmplmn}; \
                   background-color: {sel}; font-size: .8rem;"
        tbl.append(Td(f"{sel}", style=f"{sty_td}"))
    
    return tbl

def tab():
    tabel = cetak("yellow")
    jumlah_brs = len(tabel) // 4
    sisa = len(tabel) % 4

    baris = []
    for sel in range(jumlah_brs):
        anu = tabel[:4]
        del tabel[:4]
        baris.append(Tr(*anu))
    baris.append(Tr(*tabel)) if sisa != 0 else None
    tbl_sty = f"border-spacing: 6px; border-collapse: separate;"
    return Main(Table(*baris, style=tbl_sty), style="border: 1px solid black")

app = FastHTML()

@app.get("/")
def main():
    return tab()
serve()



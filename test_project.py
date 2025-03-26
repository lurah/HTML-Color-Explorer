from project import *
from starlette.testclient import TestClient

client = TestClient(main())

def test_semua():

    r = client.get("/")
    
    assert r.text.find('<h2 style="margin: 15px 0 0 0;">Slider</h2>') != -1
    assert r.text.find('<h2 style="margin: 15px 0 0 0;">Value Entry</h2>') != -1
    assert r.text.find('<h2 style="margin: 10px 0 0 0;">Named Color</h2>') != -1
    assert r.text.find('id="sldrgb"') != -1
    assert r.text.find('id="sldhsl"') != -1
    assert r.text.find('id="tengah"') != -1
    assert r.text.find('id="warna"') != -1
    assert r.text.find('RGB Value</h3>') != -1
    assert r.text.find('HSL Value</h3>') != -1
    assert r.text.find('id="warna"') != -1
    assert r.text.find('id="klr_nama"') != -1
    assert r.text.find('id="jdl_klr"') != -1
    assert r.text.find('id="kolor"') != -1


def test_ganti_klr():

    r = client.post("/klr_name?nm_klr=red&red=255&green=0&blue=0")
    red = ["IndianRed","LightCoral","Salmon","DarkSalmon","LightSalmon",
           "Crimson","Red","FireBrick","DarkRed"]
    assert all(klr in r.text for klr in red) == True
    assert r.text.find('color: brown;">Red</span>') != -1
    
    r = client.post("/klr_name?nm_klr=orange&red=255&green=255&blue=0")
    orange = ["LightSalmon","Coral","Tomato","OrangeRed","DarkOrange","Orange"]
    assert all(klr in r.text for klr in orange) == True
    assert r.text.find('color: brown;">Orange</span>') != -1
    

def test_tengah():

    r = client.post("/tengah?red=255&green=0&blue=0&hue=0&saturation=100&lightness=50&data_cmp=rgb")
    tengah = ["div id=\"warna\"", "background-color: rgb(255, 0, 0)","input name=\"rgb_red\" value=\"255\"",
              "input name=\"rgb_green\" value=\"0\"","input name=\"rgb_blue\" value=\"0\"",
              "input name=\"rgb_hue\" value=\"0\"","input name=\"rgb_saturation\" value=\"100\"",
              "input name=\"rgb_lightness\" value=\"50\""]
    assert all(elm in r.text for elm in tengah) == True

    r = client.post("/tengah?red=0&green=0&blue=255&hue=240&saturation=100&lightness=50&data_cmp=hsl")
    tengah = ["div id=\"warna\"", "background-color: rgb(0, 0, 255)","input name=\"rgb_red\" value=\"0\"",
              "input name=\"rgb_green\" value=\"0\"","input name=\"rgb_blue\" value=\"255\"",
              "input name=\"rgb_hue\" value=\"240\"","input name=\"rgb_saturation\" value=\"100\"",
              "input name=\"rgb_lightness\" value=\"50\""]
    assert all(elm in r.text for elm in tengah) == True

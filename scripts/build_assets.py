"""Rebuild the profile's original SVG components and GIF. Requires Pillow."""
from pathlib import Path
from html import escape
from math import sin, cos, pi
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)
BG, PANEL, LINE = "#0b1020", "#111a2e", "#263650"
WHITE, MUTED = "#eff5ff", "#9eafc8"
CYAN, BLUE, GOLD = "#53e0d0", "#8da9ff", "#f5ca7b"
FONT = "'DejaVu Sans',Arial,sans-serif"
MONO = "'DejaVu Sans Mono',monospace"

def text(x, y, value, size=20, color=WHITE, weight=400, mono=False, extra=""):
    return f'<text x="{x}" y="{y}" font-family="{MONO if mono else FONT}" font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>'

def svg(w, h, title, body, desc=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>
{body}</svg>'''

def save(name, w, h, title, body, desc=""):
    (OUT / name).write_text(svg(w, h, title, body, desc), encoding="utf-8")

def panel(w, h):
    return f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="{BG}" stroke="{LINE}"/>'

def grid(w, h):
    return f'''<defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{LINE}" stroke-opacity=".3"/></pattern></defs><rect width="{w}" height="{h}" rx="22" fill="url(#grid)"/>'''

def chip(x, y, label, color=CYAN, width=None):
    width = width or len(label)*9+28
    return f'<rect x="{x}" y="{y}" width="{width}" height="30" rx="15" fill="{color}" fill-opacity=".08" stroke="{color}" stroke-opacity=".35"/>'+text(x+14,y+20,label,13,color,mono=True)

def knight(x, y, scale=1):
    return f'''<g transform="translate({x} {y}) scale({scale})" fill="none" stroke-linejoin="round">
<path d="M-36 62H42L34 48H-27Z" fill="{CYAN}" fill-opacity=".12" stroke="{CYAN}" stroke-width="2"/>
<path d="M-23 45C-25 23-10 14 3 5L-5-6-31 6-43-3-27-29-25-49-8-37 11-42C39-24 42 2 34 21L30 45Z" fill="{CYAN}" fill-opacity=".09" stroke="{CYAN}" stroke-width="3"/>
<path d="M12-31C29-10 26 13 6 32M-23 45H30M-31 6L-9 1" stroke="{CYAN}" stroke-width="2" stroke-opacity=".6"/>
<circle cx="-9" cy="-22" r="3" fill="{WHITE}" stroke="none"/></g>'''

# Hero: vector illustration, not a performance or telemetry display.
body = panel(1200,440)+grid(1200,440)
body += '''<defs><radialGradient id="halo"><stop stop-color="#53e0d0" stop-opacity=".14"/><stop offset="1" stop-color="#53e0d0" stop-opacity="0"/></radialGradient><linearGradient id="edge"><stop stop-color="#53e0d0"/><stop offset="1" stop-color="#8da9ff"/></linearGradient></defs>
<style>@keyframes orbit{to{transform:rotate(360deg)}}@keyframes flow{to{stroke-dashoffset:-100}}@keyframes pulse{50%{opacity:.3}}.orbit{transform-origin:940px 215px;animation:orbit 32s linear infinite}.flow{stroke-dasharray:5 20;animation:flow 6s linear infinite}.pulse{animation:pulse 3s ease-in-out infinite}@media(prefers-reduced-motion:reduce){.orbit,.flow,.pulse{animation:none}}</style>
<circle cx="940" cy="215" r="220" fill="url(#halo)"/>
<path d="M26 1H1174" stroke="url(#edge)" stroke-width="2"/>
'''
body += text(48,51,"KNIGHT  /  ENGINEERING IN MOTION",14,CYAN,mono=True,extra='letter-spacing="2"')
body += text(47,132,"Worapon",61,WHITE,700)+text(47,201,"Sangsasri",61,WHITE,700)
body += text(49,249,"Intelligence that reaches the real world.",23,MUTED)
body += chip(48,280,"EMBEDDED AI",width=143)+chip(203,280,"AIoT",width=76)+chip(291,280,"ASSISTIVE TECH",width=169)
body += '<path d="M48 343H652" stroke="#263650"/>'
body += text(48,378,"SENSE.",16,CYAN,700,True)+text(147,378,"REASON.",16,BLUE,700,True)+text(258,378,"BUILD.",16,GOLD,700,True)
body += text(48,410,"THAILAND  /  @NNOPPONS",12,MUTED,mono=True,extra='letter-spacing="1.5"')
body += '<g fill="none" stroke="#263650"><circle cx="940" cy="215" r="164"/><circle cx="940" cy="215" r="128" stroke-dasharray="3 9"/><path d="M732 215H1148M940 18V412" stroke-opacity=".45"/></g>'
body += '<g class="orbit" fill="none" stroke="#53e0d0"><circle cx="940" cy="215" r="164" stroke-dasharray="90 940" stroke-width="2"/><circle cx="1104" cy="215" r="5" fill="#53e0d0" stroke="none"/></g>'
body += '<path d="M758 151H812L839 178M1061 251L1088 278H1145M790 308H823L843 288" fill="none" stroke="#53e0d0" stroke-opacity=".4"/>'
body += '<path class="flow" d="M758 151H812L839 178M1061 251L1088 278H1145" fill="none" stroke="#53e0d0" stroke-width="2"/>'
body += '<rect x="849" y="124" width="182" height="182" rx="34" fill="#101d30" stroke="#53e0d0" stroke-opacity=".45" transform="rotate(9 940 215)"/>'
body += knight(940,209,1.12)
body += text(940,337,"HARDWARE × INTELLIGENCE",11,CYAN,mono=True,extra='text-anchor="middle" letter-spacing="1"')
body += '<circle class="pulse" cx="1091" cy="53" r="4" fill="#53e0d0"/>'+text(1104,57,"BUILDING",11,MUTED,mono=True)
save("hero.svg",1200,440,"Knight — Worapon Sangsasri",body,"Embedded AI, AIoT and assistive technology. An original animated circuit and chess-knight illustration.")

# Larger type and a compact mark for narrow README views.
body=panel(640,470)+grid(640,470)
body+=text(30,43,"KNIGHT / ENGINEERING IN MOTION",13,CYAN,mono=True,extra='letter-spacing="1"')
body+=text(28,119,"Worapon",59,WHITE,700)+text(28,183,"Sangsasri",59,WHITE,700)
body+=knight(541,122,.68)
body+=text(30,241,"Intelligence that reaches",23,MUTED)+text(30,273,"the real world.",23,MUTED)
body+=chip(30,304,"EMBEDDED AI",width=143)+chip(184,304,"AIoT",width=76)+chip(271,304,"ASSISTIVE TECH",width=169)
body+='<path d="M30 367H610" stroke="#263650"/>'
body+=text(30,404,"SENSE.",20,CYAN,700,True)+text(154,404,"REASON.",20,BLUE,700,True)+text(292,404,"BUILD.",20,GOLD,700,True)
body+=text(30,445,"THAILAND / @NNOPPONS",13,MUTED,mono=True,extra='letter-spacing="1"')
save('hero-mobile.svg',640,470,'Knight — Worapon Sangsasri',body)

# Local navigation badges avoid third-party badge-server dependencies.
for name,label,color,icon,w in [
    ("linkedin","LINKEDIN",BLUE,"in",164),
    ("portfolio","PORTFOLIO",CYAN,"↗",181),
    ("email","LET'S TALK",GOLD,"@",181),
]:
    b=panel(w,42)+f'<rect x="1" y="1" width="42" height="40" rx="12" fill="{color}" fill-opacity=".12"/>'
    b+=text(22,27,icon,17,color,700,extra='text-anchor="middle"')+text(55,27,label,12,WHITE,700,True)
    save(f"{name}.svg",w,42,label,b)

body=panel(1200,270)+grid(1200,270)
body+=text(36,42,"01  /  FLAGSHIP BUILD",13,CYAN,mono=True,extra='letter-spacing="1.6"')
body+=text(36,91,"WheelSense + EaseAI",36,WHITE,700)
body+=text(36,130,"From motion signals to assistive intelligence.",19,MUTED)
body+=text(36,165,"BLE localization · care workflows · smart environments",16,MUTED)
body+=chip(36,201,"ESP32",width=84)+chip(132,201,"FastAPI",width=102)+chip(246,201,"Next.js",width=102)+chip(360,201,"MCP",width=68)
# Abstract coverage map, intentionally without invented readings.
body+='<g transform="translate(891 134)" fill="none"><rect x="-132" y="-77" width="264" height="152" rx="16" stroke="#344a65"/><path d="M-45-77V-11H132M-132 28H-45V75" stroke="#344a65"/><circle r="62" stroke="#53e0d0" stroke-opacity=".12"/><circle r="34" stroke="#53e0d0" stroke-opacity=".25"/><path d="M-107-51L8 13 108-49M8 13L91 53" stroke="#53e0d0" stroke-dasharray="4 5" stroke-opacity=".7"/>'
for x,y in [(-107,-51),(108,-49),(91,53)]:body+=f'<rect x="{x-5}" y="{y-5}" width="10" height="10" rx="3" fill="{BLUE}"/>'
body+='<circle cx="8" cy="13" r="7" fill="#53e0d0"/></g>'+text(891,239,"SENSING → CONTEXT → ASSISTANCE",11,CYAN,mono=True,extra='text-anchor="middle"')
save("wheelsense.svg",1200,270,"WheelSense + EaseAI — flagship project",body,"BLE localization, care workflows and smart environments, using ESP32, FastAPI, Next.js and MCP. The map is illustrative.")

def project(name, index, title, lines, tags, color, symbol):
    b=panel(580,236)+text(28,37,f"{index}  /  EXPLORATION",12,color,mono=True,extra='letter-spacing="1.2"')
    b+=text(28,83,title,29,WHITE,700)
    for i,l in enumerate(lines):b+=text(28,121+i*26,l,16,MUTED)
    b+=text(28,205,tags,12,color,mono=True)
    if symbol=="reach":
        b+='<g fill="none" stroke="#8da9ff" stroke-width="2" opacity=".65"><path d="M464 61h27v27M541 61h-27v27M464 138h27v-27M541 138h-27v-27"/><path d="M484 100H521" stroke-dasharray="3 5"/></g>'
    else:
        b+='<g transform="translate(506 93)" fill="none" stroke="#f5ca7b" stroke-width="2" opacity=".65"><path d="M-17-17L17 17M-17 17L17-17"/><rect x="-10" y="-10" width="20" height="20" rx="5"/>'
        for x,y in [(-22,-22),(22,22),(-22,22),(22,-22)]:b+=f'<ellipse cx="{x}" cy="{y}" rx="15" ry="7"/>'
        b+='</g>'
    save(name,580,236,title,b)
project("reachsense.svg","02","ReachSenseAI",["Shoulder-flexibility measurement research.","Geometry, calibration and browser tooling."],"MEASUREMENT  /  RESEARCH PROTOTYPE",BLUE,"reach")
project("drone.svg","03","DroneDetector",["Computer vision for drone detection.","Rule-based and ML classification tools."],"PYTHON  /  OPENCV  /  EMBEDDED SYSTEMS",GOLD,"drone")

body=panel(1200,246)
body+=text(34,40,"THE WORKBENCH",13,CYAN,mono=True,extra='letter-spacing="2"')
groups=[("SENSING",CYAN,["ESP32-S3 · BLE · MQTT","M5StickC Plus2","PlatformIO · Raspberry Pi"]),
        ("INTELLIGENCE",BLUE,["Python · XGBoost","LLM evaluation","MCP · assistive agents"]),
        ("APPLICATIONS",CYAN,["FastAPI · Next.js","React · TypeScript","Docker · PostgreSQL"]),
        ("ENGINEERING",GOLD,["LabVIEW · MATLAB","Signal processing","System integration"])]
for i,(label,color,lines) in enumerate(groups):
    x=34+i*294
    if i:body+=f'<path d="M{x-18}69V211" stroke="{LINE}"/>'
    body+=f'<rect x="{x}" y="72" width="24" height="3" rx="1.5" fill="{color}"/>'+text(x,110,label,15,color,700,True)
    for j,line in enumerate(lines):body+=text(x,148+j*27,line,15,MUTED)
save("stack.svg",1200,246,"Engineering workbench",body,"Tools used across sensing, intelligence, applications and engineering. See the README for a text list.")

body=panel(640,458)+text(28,40,'THE WORKBENCH',14,CYAN,mono=True,extra='letter-spacing="1.5"')
for i,(label,color,lines) in enumerate(groups):
    x=28+(i%2)*310;y=79+(i//2)*181
    body+=f'<rect x="{x}" y="{y}" width="24" height="3" rx="1.5" fill="{color}"/>'+text(x,y+34,label,16,color,700,True)
    for j,line in enumerate(lines):body+=text(x,y+71+j*28,line,16,MUTED)
save('stack-mobile.svg',640,458,'Engineering workbench',body)

body=panel(1200,112)+text(36,47,"LET'S BUILD SOMETHING THAT MATTERS.",24,WHITE,700)
body+=text(36,80,"Embedded intelligence · assistive technology · practical engineering",15,MUTED)
body+=knight(1113,49,.48)
save("footer.svg",1200,112,"Let's build something that matters",body)

# GIF motion is drawn from original shapes; it contains no measured sensor data.
W,H=1200,208
def font(size,bold=False,mono=False):
    folder=Path('/usr/share/fonts/truetype/dejavu')
    file=('DejaVuSansMono' if mono else 'DejaVuSans')+('-Bold' if bold else '')+'.ttf'
    if (folder/file).exists():return ImageFont.truetype(str(folder/file),size)
    return ImageFont.load_default()

def draw_frame(t):
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
    d.rounded_rectangle((1,1,W-2,H-2),radius=22,outline=LINE,width=2)
    d.text((30,19),'THE LOOP  /  SIGNALS INTO SOFTWARE',font=font(12,mono=True),fill=MUTED)
    boxes=[(31,'01','SENSE','Wearable + BLE',CYAN),(444,'02','REASON','Models + context',BLUE),(857,'03','BUILD','Interfaces + action',GOLD)]
    for x,num,label,sub,color in boxes:
        d.rounded_rectangle((x,59,x+311,155),radius=14,fill=PANEL,outline=LINE)
        d.text((x+20,77),num,font=font(13,mono=True),fill=color)
        d.text((x+63,74),label,font=font(20,True),fill=WHITE)
        d.text((x+63,111),sub,font=font(14),fill=MUTED)
    for left,right,color,offset in [(342,444,CYAN,0),(755,857,BLUE,.23)]:
        d.line((left,107,right,107),fill=LINE,width=2)
        for j in range(3):
            u=(t+j/3+offset)%1
            px=left+8+int(u*(right-left-16))
            d.ellipse((px-3,104,px+3,110),fill=color)
    # A small oscillating waveform stays inside its own decorative baseline.
    pts=[(31+i,180+int(3*sin(i/20-t*2*pi))) for i in range(1137)]
    d.line(pts,fill='#263e51',width=2)
    for i in range(9):
        u=(t+i/9)%1; x=int(32+u*1135)
        d.ellipse((x-1,178,x+2,181),fill=CYAN)
    return im

frames=[draw_frame(i/60) for i in range(60)]
palette=frames[0].quantize(colors=128,method=Image.Quantize.MEDIANCUT)
frames=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
frames[0].save(OUT/'signal-loop.gif',save_all=True,append_images=frames[1:],duration=80,loop=0,optimize=True,disposal=1)

body=panel(W,H)+text(30,32,"THE LOOP  /  SIGNALS INTO SOFTWARE",12,MUTED,mono=True)
for x,num,label,sub,color in [(31,'01','SENSE','Wearable + BLE',CYAN),(444,'02','REASON','Models + context',BLUE),(857,'03','BUILD','Interfaces + action',GOLD)]:
    body+=f'<rect x="{x}" y="59" width="311" height="96" rx="14" fill="{PANEL}" stroke="{LINE}"/>'
    body+=text(x+20,93,num,13,color,mono=True)+text(x+63,94,label,20,WHITE,700)+text(x+63,126,sub,14,MUTED)
body+='<path d="M342 107H444M755 107H857" stroke="#53e0d0" stroke-width="2" stroke-dasharray="3 8"/>'
save('signal-still.svg',W,H,'Sense, reason, build',body,'Still alternative to the decorative GIF. Wearable and BLE signals, models and context, interfaces and action.')
print('Built',len(list(OUT.glob('*.svg'))),'SVG components and a 60-frame GIF.')

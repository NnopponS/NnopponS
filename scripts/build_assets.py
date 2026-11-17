"""Rebuild Worapon Sangsasri's animated SVG profile components and 60-frame looping GIF."""
from pathlib import Path
from html import escape
from math import sin, pi
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)

BG, PANEL, PANEL_ALT, LINE = "#0b1020", "#111a2e", "#16223b", "#263650"
WHITE, MUTED = "#eff5ff", "#9eafc8"
CYAN, BLUE, GOLD, GREEN, PURPLE = "#53e0d0", "#8da9ff", "#f5ca7b", "#34d399", "#c084fc"
FONT = "'DejaVu Sans','Segoe UI',Arial,sans-serif"
MONO = "'DejaVu Sans Mono','Cascadia Code',Consolas,monospace"


def text(x, y, value, size=20, color=WHITE, weight=400, mono=False, extra=""):
    return (
        f'<text x="{x}" y="{y}" font-family="{MONO if mono else FONT}" '
        f'font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>'
    )


def svg(w, h, title, body, desc=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>
{body}</svg>'''


def save(name, w, h, title, body, desc=""):
    (OUT / name).write_text(svg(w, h, title, body, desc), encoding="utf-8")


def panel(w, h, fill=BG):
    return f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="{fill}" stroke="{LINE}" stroke-width="1.5"/>'


def grid(w, h, pid="grid"):
    return (
        f'<defs><pattern id="{pid}" width="40" height="40" patternUnits="userSpaceOnUse">'
        f'<path d="M40 0H0V40" fill="none" stroke="{LINE}" stroke-opacity=".28"/></pattern></defs>'
        f'<rect width="{w}" height="{h}" rx="22" fill="url(#{pid})"/>'
    )


def chip(x, y, label, color=CYAN, width=None):
    width = width or int(len(label) * 8.6 + 28)
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="30" rx="15" '
        f'fill="{color}" fill-opacity=".1" stroke="{color}" stroke-opacity=".4"/>'
        + text(x + 14, y + 20, label, 12.5, color, 700, mono=True)
    )


def knight(x, y, scale=1):
    return f'''<g transform="translate({x} {y}) scale({scale})" fill="none" stroke-linejoin="round">
<path d="M-36 62H42L34 48H-27Z" fill="{CYAN}" fill-opacity=".14" stroke="{CYAN}" stroke-width="2"/>
<path d="M-23 45C-25 23-10 14 3 5L-5-6-31 6-43-3-27-29-25-49-8-37 11-42C39-24 42 2 34 21L30 45Z" fill="{CYAN}" fill-opacity=".1" stroke="{CYAN}" stroke-width="3"/>
<path d="M12-31C29-10 26 13 6 32M-23 45H30M-31 6L-9 1" stroke="{CYAN}" stroke-width="2" stroke-opacity=".65"/>
<circle cx="-9" cy="-22" r="3" fill="{WHITE}" stroke="none"/></g>'''


# 1. Animated Hero Banner (Desktop 1200x450)
body = panel(1200, 450) + grid(1200, 450, "hgrid")
body += '''<defs>
<radialGradient id="halo"><stop stop-color="#53e0d0" stop-opacity=".16"/><stop offset="1" stop-color="#53e0d0" stop-opacity="0"/></radialGradient>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#53e0d0"/><stop offset=".5" stop-color="#8da9ff"/><stop offset="1" stop-color="#f5ca7b"/></linearGradient>
</defs>
<style>
@keyframes orbit{to{transform:rotate(360deg)}}
@keyframes orbitRev{to{transform:rotate(-360deg)}}
@keyframes flow{to{stroke-dashoffset:-120}}
@keyframes pulse{50%{opacity:.25}}
@keyframes barWave{0%,100%{transform:scaleY(.45)}50%{transform:scaleY(1)}}
.orbit{transform-origin:945px 215px;animation:orbit 28s linear infinite}
.orbit-rev{transform-origin:945px 215px;animation:orbitRev 20s linear infinite}
.flow{stroke-dasharray:6 18;animation:flow 4.5s linear infinite}
.pulse{animation:pulse 2.4s ease-in-out infinite}
.bar1{transform-origin:0 390px;animation:barWave 1.8s ease-in-out infinite}
.bar2{transform-origin:0 390px;animation:barWave 2.3s ease-in-out infinite .4s}
@media(prefers-reduced-motion:reduce){.orbit,.orbit-rev,.flow,.pulse,.bar1,.bar2{animation:none}}
</style>
<circle cx="945" cy="215" r="225" fill="url(#halo)"/>
<path d="M26 1.5H1174" stroke="url(#edge)" stroke-width="2.5"/>
'''
body += text(48, 48, "KNIGHT  ·  SYSTEMS & DEVELOPER TOOLING", 13.5, CYAN, 700, mono=True, extra='letter-spacing="2"')
body += text(46, 124, "Worapon Sangsasri", 54, WHITE, 700)
body += text(48, 168, "AI & Embedded Systems Engineer · Open-Source Tooling Author", 21, BLUE, 600)
body += text(48, 206, "Building MCP developer infrastructure, real-time BLE/IMU telemetry, and assistive AI platforms.", 16.5, MUTED)

body += (
    chip(48, 232, "AAIF 2026 STACK", CYAN, 174)
    + chip(234, 232, "EMBEDDED AI & BLE", BLUE, 184)
    + chip(430, 232, "ASSISTIVE ROBOTICS", GOLD, 192)
    + chip(634, 232, "TYPESCRIPT & PYTHON", GREEN, 198)
)

# Live HUD terminal strip inside hero
body += f'<rect x="48" y="284" width="660" height="78" rx="12" fill="{PANEL}" stroke="{LINE}"/>'
body += '<circle cx="70" cy="304" r="4.5" fill="#ef4444"/><circle cx="86" cy="304" r="4.5" fill="#f59e0b"/><circle cx="102" cy="304" r="4.5" fill="#22c55e"/>'
body += text(120, 308, "agent-doctor stack . --ci  (AAIF 4-layer audit)", 11.5, MUTED, mono=True)
body += text(68, 334, "$ npx -y github:NnopponS/agent-doctor stack . --ci", 13, WHITE, mono=True)
body += text(68, 353, "✓ Score: 100/100 (A+) · AGENTS.md · SKILL.md · MCP 2026 · A2A · Cache Guard", 12, GREEN, 700, mono=True)

body += '<path d="M48 382H708" stroke="#263650"/>'
body += (
    text(48, 414, "SENSE.", 16, CYAN, 700, True)
    + text(135, 414, "VERIFY.", 16, GREEN, 700, True)
    + text(232, 414, "REASON.", 16, BLUE, 700, True)
    + text(338, 414, "SHIP.", 16, GOLD, 700, True)
)
body += text(435, 414, "BANGKOK, THAILAND  ·  @NNOPPONS", 12, MUTED, mono=True, extra='letter-spacing="1.4"')

# Animated orbital core on the right
body += '<g fill="none" stroke="#263650"><circle cx="945" cy="215" r="168"/><circle cx="945" cy="215" r="132" stroke-dasharray="4 8"/><circle cx="945" cy="215" r="96" stroke-opacity=".5"/><path d="M735 215H1155M945 18V412" stroke-opacity=".4"/></g>'
body += '<g class="orbit" fill="none" stroke="#53e0d0"><circle cx="945" cy="215" r="168" stroke-dasharray="95 940" stroke-width="2.2"/><circle cx="1113" cy="215" r="5.5" fill="#53e0d0" stroke="none"/></g>'
body += '<g class="orbit-rev" fill="none" stroke="#8da9ff"><circle cx="945" cy="215" r="132" stroke-dasharray="60 760" stroke-width="2"/><circle cx="813" cy="215" r="4.5" fill="#8da9ff" stroke="none"/></g>'
body += '<path d="M758 148H814L842 176M1058 250L1086 278H1146M788 310H824L844 290" fill="none" stroke="#53e0d0" stroke-opacity=".38"/>'
body += '<path class="flow" d="M758 148H814L842 176M1058 250L1086 278H1146" fill="none" stroke="#53e0d0" stroke-width="2.2"/>'
body += '<rect x="854" y="124" width="182" height="182" rx="34" fill="#101d30" stroke="#53e0d0" stroke-opacity=".5" transform="rotate(9 945 215)"/>'
body += knight(945, 209, 1.12)
body += text(945, 340, "HARDWARE × AI × TOOLING", 11, CYAN, 700, mono=True, extra='text-anchor="middle" letter-spacing="1.2"')
body += '<circle class="pulse" cx="1072" cy="48" r="4.5" fill="#34d399"/>' + text(1086, 52, "SHIPPING OPEN SOURCE", 11, GREEN, 700, mono=True)
save(
    "hero.svg",
    1200,
    450,
    "Worapon Sangsasri — AI & Embedded Systems Engineer",
    body,
    "Animated engineering banner for Worapon Sangsasri featuring AAIF agent infrastructure, embedded BLE/IMU telemetry, and assistive AI systems.",
)

# 2. Mobile Hero (640x490)
body = panel(640, 490) + grid(640, 490, "hmgrid")
body += text(30, 42, "KNIGHT / SYSTEMS & DEV TOOLING", 12.5, CYAN, 700, mono=True, extra='letter-spacing="1"')
body += text(28, 110, "Worapon", 54, WHITE, 700) + text(28, 170, "Sangsasri", 54, WHITE, 700)
body += knight(542, 118, 0.68)
body += text(30, 218, "AI & Embedded Systems Engineer", 20, BLUE, 700)
body += text(30, 248, "AAIF 2026 tooling · BLE/IMU telemetry · Assistive AI", 15.5, MUTED)
body += chip(30, 276, "AGENT-DOCTOR", CYAN, 148) + chip(188, 276, "EMBEDDED AI", BLUE, 142) + chip(340, 276, "ASSISTIVE TECH", GOLD, 166)
body += f'<rect x="30" y="324" width="580" height="66" rx="10" fill="{PANEL}" stroke="{LINE}"/>'
body += text(46, 350, "$ npx -y github:NnopponS/agent-doctor stack .", 12.5, WHITE, mono=True)
body += text(46, 374, "✓ Score: 100/100 (A+) · Prompt Cache · SARIF · Web UI", 12, GREEN, 700, mono=True)
body += '<path d="M30 412H610" stroke="#263650"/>'
body += text(30, 444, "SENSE · VERIFY · REASON · SHIP", 16, CYAN, 700, True)
body += text(30, 472, "BANGKOK, THAILAND / @NNOPPONS", 12, MUTED, mono=True)
save("hero-mobile.svg", 640, 490, "Worapon Sangsasri — AI & Embedded Systems Engineer", body)

# 3. Navigation Badges
for name, label, color, icon, w in [
    ("linkedin", "LINKEDIN", BLUE, "in", 164),
    ("portfolio", "PORTFOLIO", CYAN, "↗", 181),
    ("email", "LET'S TALK", GOLD, "@", 181),
]:
    b = panel(w, 42) + f'<rect x="1" y="1" width="42" height="40" rx="12" fill="{color}" fill-opacity=".14"/>'
    b += text(22, 27, icon, 17, color, 700, extra='text-anchor="middle"') + text(55, 27, label, 12, WHITE, 700, True)
    save(f"{name}.svg", w, 42, label, b)

# 4. Flagship Card: agent-doctor v2.0.0 (1200x280 Animated SVG)
body = panel(1200, 280) + grid(1200, 280, "mcpgrid")
body += '''<style>
@keyframes scanline{0%{transform:translateX(-120px)}100%{transform:translateX(380px)}}
@keyframes glowPulse{50%{opacity:.4}}
.scan{animation:scanline 3.6s linear infinite}
.gpulse{animation:glowPulse 2.2s ease-in-out infinite}
@media(prefers-reduced-motion:reduce){.scan,.gpulse{animation:none}}
</style>'''
body += text(36, 42, "01  /  2026 AAIF AGENT STACK & PROMPT-CACHE INFRASTRUCTURE", 13, GREEN, 700, mono=True, extra='letter-spacing="1.6"')
body += text(36, 90, "agent-doctor", 38, WHITE, 700)
body += chip(312, 62, "v2.0.0 RELEASE", GREEN, 152) + chip(474, 62, "0 RUNTIME DEPS", CYAN, 156)
body += text(36, 130, "AAIF 4-Layer Inspector (AGENTS.md · SKILL.md · MCP 2026 · A2A) &amp; Schema Auto-Healer.", 18, MUTED)
body += text(36, 162, "Claude 5.5 · GPT-6 · Gemini 4 · DeepSeek V4 cache billing · Prompt-cache guard · Skill migrator", 15, MUTED)
body += (
    chip(36, 198, "AGENTS.md", CYAN, 114)
    + chip(160, 198, "SKILL.md (-90%)", GREEN, 154)
    + chip(324, 198, "MCP 2026-07-28", BLUE, 152)
    + chip(486, 198, "A2A Card", GOLD, 108)
    + chip(604, 198, "SARIF + llms.txt", PURPLE, 150)
)
body += text(36, 254, "npx -y github:NnopponS/agent-doctor stack .   |   nnoppons.github.io/agent-doctor", 13, CYAN, 700, mono=True)

# Right-side animated diagnostic console inside agent-doctor.svg
body += f'<g transform="translate(765 28)"><rect width="400" height="224" rx="16" fill="{PANEL}" stroke="#344a65" stroke-width="1.5"/>'
body += f'<rect x="16" y="16" width="368" height="36" rx="8" fill="{PANEL_ALT}" stroke="{LINE}"/>'
body += '<circle class="gpulse" cx="34" cy="34" r="5" fill="#34d399"/>'
body += text(48, 39, "AAIF STACK: 100/100 (A+)", 13.5, GREEN, 700, mono=True)
body += text(286, 39, "7 TOOLS", 12, CYAN, 700, mono=True)

bars = [
    ("AGENTS.md (Always-On)", "375 tok", 160, CYAN),
    ("SKILL.md (Frontmatter)", "73 tok", 110, GREEN),
    ("MCP 2026 (Cache Safe)", "249 tok", 140, BLUE),
    ("A2A Card (On-Demand)", "530 tok", 185, GOLD),
]
for idx, (tname, tval, bw, bcol) in enumerate(bars):
    by = 72 + idx * 32
    body += text(18, by + 12, tname, 11.5, WHITE, mono=True)
    body += f'<rect x="195" y="{by}" width="120" height="12" rx="6" fill="#090d16" stroke="{LINE}"/>'
    body += f'<rect x="195" y="{by}" width="{int(bw*0.58)}" height="12" rx="6" fill="{bcol}"/>'
    body += text(323, by + 11, tval, 11, MUTED, mono=True)

body += text(18, 208, "MCP001-020 · Cache Guard · Auto-Fix · OAuth 2.1", 11, GOLD, mono=True)
body += "</g>"
save(
    "agent-doctor.svg",
    1200,
    280,
    "agent-doctor — 2026 AAIF Agent Stack Inspector & Prompt-Cache Profiler",
    body,
    "Open-source CLI, Web UI, and MCP 2026 server for auditing AGENTS.md, SKILL.md, MCP tool schemas, prompt-cache hits, and A2A cards.",
)

# 5. Flagship Card: WheelSense + EaseAI (1200x270 Animated SVG)
body = panel(1200, 270) + grid(1200, 270, "wsgrid")
body += '''<style>
@keyframes radarPing{0%{r:12px;opacity:.85}100%{r:64px;opacity:0}}
.ping{animation:radarPing 2.8s ease-out infinite}
@media(prefers-reduced-motion:reduce){.ping{animation:none}}
</style>'''
body += text(36, 42, "02  /  NATIONAL AWARD-WINNING ASSISTIVE AIoT PLATFORM", 13, CYAN, 700, mono=True, extra='letter-spacing="1.6"')
body += text(36, 91, "WheelSense + EaseAI", 36, WHITE, 700)
body += text(36, 130, "End-to-end indoor wheelchair localization, clinical telemetry, and agentic care workflows.", 18.5, MUTED)
body += text(36, 165, "ESP32-S3 BLE/MQTT gateways · FastAPI + PostgreSQL · Next.js 16 dashboards · 3-stage propose/confirm/execute AI", 15, MUTED)
body += (
    chip(36, 201, "ESP32-S3", CYAN, 104)
    + chip(150, 201, "BLE Localization", BLUE, 164)
    + chip(324, 201, "FastAPI", GREEN, 96)
    + chip(430, 201, "Next.js 16", CYAN, 114)
    + chip(554, 201, "ECTI-CON Best Paper", GOLD, 192)
)
body += '<g transform="translate(935 132)" fill="none"><rect x="-175" y="-82" width="350" height="164" rx="16" fill="#111a2e" stroke="#344a65"/><path d="M-55-82V-10H175M-175 30H-55V82" stroke="#344a65"/><circle cx="12" cy="14" r="56" stroke="#53e0d0" stroke-opacity=".18"/><circle class="ping" cx="12" cy="14" r="24" stroke="#53e0d0" stroke-width="2"/><path d="M-135-52L12 14 132-48M12 14L118 54" stroke="#53e0d0" stroke-dasharray="4 5" stroke-opacity=".75"/>'
for x, y in [(-135, -52), (132, -48), (118, 54)]:
    body += f'<rect x="{x-6}" y="{y-6}" width="12" height="12" rx="3" fill="{BLUE}"/>'
body += '<circle cx="12" cy="14" r="7" fill="#53e0d0"/></g>' + text(935, 240, "BLE RSSI → ML/LLM TRACKING → CARE ACTION", 11, CYAN, 700, mono=True, extra='text-anchor="middle"')
save("wheelsense.svg", 1200, 270, "WheelSense + EaseAI — Assistive AIoT Platform", body)


# 6. Four 580x240 Project Cards (2x2 Grid: WheelAthlete, ReachSenseAI, 100-games, DroneDetector)
def project_card(name, index, category, title, lines, tags, color, symbol):
    b = panel(580, 240) + grid(580, 240, f"g_{index}")
    b += text(28, 38, f"{index}  /  {category}", 12, color, 700, mono=True, extra='letter-spacing="1.2"')
    b += text(28, 82, title, 28, WHITE, 700)
    for i, l in enumerate(lines):
        b += text(28, 120 + i * 26, l, 15.5, MUTED)
    b += text(28, 208, tags, 12, color, 700, mono=True)
    if symbol == "wheelathlete":
        b += '''<g transform="translate(502 96)" fill="none" stroke="#53e0d0" stroke-width="2" opacity=".8">
        <circle cx="-18" cy="0" r="26" stroke-dasharray="6 4"/><circle cx="-18" cy="0" r="6" fill="#53e0d0"/>
        <circle cx="22" cy="0" r="26" stroke-dasharray="6 4"/><circle cx="22" cy="0" r="6" fill="#8da9ff"/>
        <path d="M-18 0H22" stroke="#f5ca7b" stroke-width="2.5"/></g>'''
    elif symbol == "reach":
        b += '<g fill="none" stroke="#8da9ff" stroke-width="2" opacity=".75"><path d="M464 61h27v27M541 61h-27v27M464 138h27v-27M541 138h-27v-27"/><path d="M484 100H521" stroke-dasharray="3 5"/><circle cx="502.5" cy="100" r="5" fill="#53e0d0" stroke="none"/></g>'
    elif symbol == "games":
        b += '''<g transform="translate(502 96)" fill="none" stroke="#c084fc" stroke-width="2" opacity=".85">
        <rect x="-34" y="-22" width="68" height="44" rx="12" fill="#16223b"/>
        <path d="M-18 0H-6M-12 -6V6" stroke="#53e0d0" stroke-width="2.5"/>
        <circle cx="12" cy="-5" r="4" fill="#f5ca7b" stroke="none"/>
        <circle cx="22" cy="5" r="4" fill="#34d399" stroke="none"/></g>'''
    else:
        b += '<g transform="translate(506 96)" fill="none" stroke="#f5ca7b" stroke-width="2" opacity=".75"><path d="M-17-17L17 17M-17 17L17-17"/><rect x="-10" y="-10" width="20" height="20" rx="5"/>'
        for x, y in [(-22, -22), (22, 22), (-22, 22), (22, -22)]:
            b += f'<ellipse cx="{x}" cy="{y}" rx="15" ry="7"/>'
        b += "</g>"
    save(name, 580, 240, title, b)


project_card(
    "wheelathlete.svg",
    "03",
    "BIOMECHANICS TELEMETRY",
    "WheelAthlete v1.8.4",
    ["Synchronized left/right wheel IMUs over BLE.", "Windows acquisition, packet QC & trajectory analysis."],
    "DART · FLUTTER · ESP32 · BLE IMU · WINDOWS",
    CYAN,
    "wheelathlete",
)
project_card(
    "reachsense.svg",
    "04",
    "3D OPTICAL MEASUREMENT",
    "ReachSenseAI",
    ["3D behind-the-back shoulder flexibility instrument.", "Calibrated ArUco/TrueDepth markers & 3MF CAD fixtures."],
    "JAVASCRIPT · ARUCO · TRUEDEPTH · OPENSCAD",
    BLUE,
    "reach",
)
project_card(
    "hundred-games.svg",
    "05",
    "ZERO-DEPENDENCY WEB ARCADE",
    "100-games",
    ["100 playable single-file HTML5 Canvas & WebAudio games.", "60 FPS game loops with an instant-search web portal."],
    "HTML5 CANVAS · WEBAUDIO · ZERO DEPENDENCIES",
    PURPLE,
    "games",
)
project_card(
    "drone.svg",
    "06",
    "COMPUTER VISION & ML",
    "DroneDetector",
    ["Real-time drone vs. bird classification & tracking.", "Hu-moment shape descriptors, ML models & GPS regression."],
    "PYTHON · OPENCV · MACHINE LEARNING · TRACKING",
    GOLD,
    "drone",
)

# 7. Engineering Workbench (1200x246 Desktop & 640x458 Mobile)
body = panel(1200, 246)
body += text(34, 40, "THE ENGINEERING WORKBENCH", 13, CYAN, 700, mono=True, extra='letter-spacing="2"')
groups = [
    ("AAIF AGENT INFRASTRUCTURE", GREEN, ["AGENTS.md · SKILL.md · A2A", "MCP 2026-07-28 · OAuth 2.1", "Prompt-Cache · SARIF · CI"]),
    ("EMBEDDED & SENSING", CYAN, ["ESP32-S3 · M5StickC Plus2", "BLE · Dual-Wheel IMUs · MQTT", "PlatformIO · LabVIEW"]),
    ("AI & SIGNAL PROCESSING", BLUE, ["Python · XGBoost · OpenCV", "LLM & Agent Evaluation", "Sensor Fusion · Kinematics"]),
    ("FULL-STACK SYSTEMS", GOLD, ["FastAPI · Next.js · React", "Flutter · Windows Desktop", "PostgreSQL · Docker"]),
]
for i, (label, color, lines) in enumerate(groups):
    x = 34 + i * 294
    if i:
        body += f'<path d="M{x-18} 69V211" stroke="{LINE}"/>'
    body += f'<rect x="{x}" y="72" width="28" height="3.5" rx="1.5" fill="{color}"/>' + text(x, 108, label, 14, color, 700, True)
    for j, line in enumerate(lines):
        body += text(x, 146 + j * 27, line, 15, MUTED)
save("stack.svg", 1200, 246, "Engineering workbench", body)

body = panel(640, 458) + text(28, 40, "THE ENGINEERING WORKBENCH", 14, CYAN, 700, mono=True, extra='letter-spacing="1.5"')
for i, (label, color, lines) in enumerate(groups):
    x = 28 + (i % 2) * 310
    y = 79 + (i // 2) * 181
    body += f'<rect x="{x}" y="{y}" width="28" height="3.5" rx="1.5" fill="{color}"/>' + text(x, y + 34, label, 15, color, 700, True)
    for j, line in enumerate(lines):
        body += text(x, y + 71 + j * 28, line, 15.5, MUTED)
save("stack-mobile.svg", 640, 458, "Engineering workbench", body)

# 8. Footer Banner
body = panel(1200, 112) + text(36, 47, "ENGINEERING TOOLS & SYSTEMS THAT WORK IN THE REAL WORLD.", 23, WHITE, 700)
body += text(36, 80, "Open-source AAIF agent tooling · Embedded BLE/IMU telemetry · Assistive AIoT platforms", 15, MUTED)
body += knight(1113, 49, 0.48)
save("footer.svg", 1200, 112, "Engineering tools and systems that work in the real world", body)

# 9. 60-Frame Animated Pipeline GIF (signal-loop.gif) + Reduced-Motion SVG (signal-still.svg)
W, H = 1200, 208


def font(size, bold=False, mono=False):
    for cand in [
        Path("C:/Windows/Fonts/consolab.ttf" if (mono and bold) else "C:/Windows/Fonts/consola.ttf" if mono else "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
        Path("/usr/share/fonts/truetype/dejavu") / (("DejaVuSansMono" if mono else "DejaVuSans") + ("-Bold" if bold else "") + ".ttf"),
    ]:
        if cand.exists():
            return ImageFont.truetype(str(cand), size)
    return ImageFont.load_default()


def draw_frame(t):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((1, 1, W - 2, H - 2), radius=22, outline=LINE, width=2)
    d.text((30, 19), "ARCHITECTURE LOOP  /  PHYSICAL SENSORS  ->  AGENT STACK VERIFICATION  ->  PRODUCTION INTERFACES", font=font(12, bold=False, mono=True), fill=MUTED)
    boxes = [
        (31, "01", "SENSE", "ESP32 · BLE · Dual IMUs", CYAN),
        (444, "02", "VERIFY & REASON", "Agent Doctor · ML/LLM · Guardrails", GREEN),
        (857, "03", "SHIP", "CLI · Web Dashboards · Care AI", GOLD),
    ]
    for x, num, label, sub, color in boxes:
        d.rounded_rectangle((x, 56, x + 311, 154), radius=14, fill=PANEL, outline=LINE)
        d.text((x + 18, 74), num, font=font(13, bold=True, mono=True), fill=color)
        d.text((x + 54, 71), label, font=font(19, bold=True), fill=WHITE)
        d.text((x + 54, 109), sub, font=font(13), fill=MUTED)
    for left, right, color, offset in [(342, 444, CYAN, 0), (755, 857, GREEN, 0.23)]:
        d.line((left, 105, right, 105), fill=LINE, width=2)
        for j in range(3):
            u = (t + j / 3 + offset) % 1
            px = left + 8 + int(u * (right - left - 16))
            d.ellipse((px - 4, 101, px + 4, 109), fill=color)
    pts = [(31 + i, 180 + int(4 * sin(i / 18 - t * 2 * pi))) for i in range(1137)]
    d.line(pts, fill="#263e51", width=2)
    for i in range(10):
        u = (t + i / 10) % 1
        x = int(32 + u * 1135)
        y = 180 + int(4 * sin((x - 31) / 18 - t * 2 * pi))
        d.ellipse((x - 2, y - 2, x + 2, y + 2), fill=CYAN if i % 2 == 0 else GREEN)
    return im


frames = [draw_frame(i / 60) for i in range(60)]
palette = frames[0].quantize(colors=128, method=Image.Quantize.MEDIANCUT)
frames = [im.quantize(palette=palette, dither=Image.Dither.NONE) for im in frames]
frames[0].save(OUT / "signal-loop.gif", save_all=True, append_images=frames[1:], duration=75, loop=0, optimize=True, disposal=1)

body = panel(W, H) + text(30, 32, "ARCHITECTURE LOOP  /  PHYSICAL SENSORS -> AGENT STACK VERIFICATION -> PRODUCTION INTERFACES", 12, MUTED, mono=True)
for x, num, label, sub, color in [
    (31, "01", "SENSE", "ESP32 · BLE · Dual IMUs", CYAN),
    (444, "02", "VERIFY & REASON", "Agent Doctor · ML/LLM · Guardrails", GREEN),
    (857, "03", "SHIP", "CLI · Web Dashboards · Care AI", GOLD),
]:
    body += f'<rect x="{x}" y="56" width="311" height="98" rx="14" fill="{PANEL}" stroke="{LINE}"/>'
    body += text(x + 18, 90, num, 13, color, 700, mono=True) + text(x + 54, 91, label, 19, WHITE, 700) + text(x + 54, 124, sub, 13.5, MUTED)
body += '<path d="M342 105H444M755 105H857" stroke="#53e0d0" stroke-width="2" stroke-dasharray="4 8"/>'
save("signal-still.svg", W, H, "Sense, verify, ship", body)
print("Built", len(list(OUT.glob("*.svg"))), "SVG components and a 60-frame GIF.")

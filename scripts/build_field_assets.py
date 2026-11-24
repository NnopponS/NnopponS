"""Build lightweight, GitHub-safe visuals for the Field Notes profile."""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets"
SANS = "system-ui, -apple-system, 'Segoe UI', sans-serif"
MONO = "ui-monospace, 'SFMono-Regular', Consolas, monospace"
FOREST = "#1c2926"
PAPER = "#f5f2e9"
SAGE = "#d4dece"
RUST = "#a86747"
INK = "#24302b"


def write(name, width, height, title, body):
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-label="{escape(title, quote=True)}">\n'
        f'<title>{escape(title)}</title>\n{body.strip()}\n</svg>\n'
    )
    (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")


write(
    "field-notes", 840, 170, "Field Notes: sense, understand, build",
    f"""
    <style>
      .scan {{ animation: trace 7s ease-in-out infinite; }}
      @keyframes trace {{
        0%, 15% {{ stroke-dashoffset: 610; opacity: 0; }}
        25% {{ opacity: 1; }}
        68%, 83% {{ stroke-dashoffset: 0; opacity: 1; }}
        100% {{ stroke-dashoffset: 0; opacity: 0; }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .scan {{ animation: none; opacity: 0; }}
      }}
    </style>
    <rect width="840" height="170" rx="17" fill="{FOREST}"/>
    <path d="M17 1.5H823" stroke="{RUST}" stroke-width="3" opacity=".75"/>
    <path d="M422 22v126m39-126v126m39-126v126m39-126v126m39-126v126m39-126v126m39-126v126m39-126v126m39-126v126m39-126v126m39-126v126 M421 36h386m-386 25h386m-386 25h386m-386 25h386m-386 25h386" stroke="{SAGE}" opacity=".12"/>
    <g fill="{PAPER}">
      <text x="32" y="34" font-family="{MONO}" font-size="12" letter-spacing="2.3" fill="{SAGE}">WORAPON SANGSASRI / ENGINEERING</text>
      <text x="31" y="99" font-family="{SANS}" font-size="57" font-weight="700" letter-spacing="-3">Field Notes</text>
      <text x="33" y="136" font-family="{MONO}" font-size="17" letter-spacing="1.25">Sense  /  Understand  /  Build</text>
    </g>
    <g fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M419 92h35l13-13 13 23 15-45 21 70 21-58 14 23h39l18 17 18-43 19 27h42l14-18 23 31 13-14h67" stroke="#86a092" stroke-width="1.7"/>
      <path class="scan" d="M419 92h35l13-13 13 23 15-45 21 70 21-58 14 23h39l18 17 18-43 19 27h42l14-18 23 31 13-14h67" stroke="#e9ae87" stroke-width="2.6" stroke-dasharray="610" stroke-dashoffset="610"/>
      <circle cx="420" cy="92" r="4" fill="{PAPER}"/>
      <circle cx="804" cy="92" r="4" fill="{PAPER}"/>
    </g>
    <text x="803" y="150" text-anchor="end" font-family="{MONO}" font-size="12" letter-spacing="1.5" fill="{SAGE}">BANGKOK, THAILAND</text>
    """,
)

ICONS = {
    "wheelsense": '<path d="M402 104V48l46-25 47 25v56m-93-2h93m-34 0V73h20v29m-66-44h19v16h-19zm37-10a16 16 0 0 1 26 0m-21 5a9 9 0 0 1 16 0"/><circle cx="465" cy="58" r="2.5" fill="currentColor"/>',
    "wheelathlete": '<circle cx="421" cy="67" r="33"/><circle cx="474" cy="67" r="33"/><path d="M421 38v58m-29-29h58m24-29v58m-29-29h58M453 27l11-12h28"/><circle cx="421" cy="67" r="5" fill="currentColor"/><circle cx="474" cy="67" r="5" fill="currentColor"/>',
    "ble": '<path d="M401 103V31m0 72h106m-99-16 23-13 13 5 25-28 13 9 17-24"/><circle cx="431" cy="74" r="4" fill="currentColor"/><circle cx="469" cy="51" r="4" fill="currentColor"/><circle cx="499" cy="36" r="4" fill="currentColor"/>',
}
CARDS = [
    ("wheelsense", "01", "ASSISTIVE TECHNOLOGY", "WheelSense & EaseAI", "Engineering case study", "#1c2926", "#f5f2e9", "#d4dece"),
    ("wheelathlete", "02", "RESEARCH INSTRUMENTATION", "WheelAthlete", "Browse source code", "#d4dece", "#24302b", "#406557"),
    ("ble", "03", "FIRST-AUTHOR RESEARCH", "BLE Motion Tracking", "Read the IEEE paper", "#efe2d2", "#362b24", "#79503a"),
]
for slug, chapter, area, title, cta, bg, fg, accent in CARDS:
    write(
        f"field-card-{slug}", 550, 128, f"{title}: {cta}",
        f"""
        <rect x=".5" y=".5" width="549" height="127" rx="14" fill="{bg}" stroke="{accent}" stroke-opacity=".55"/>
        <path d="M367 18v92" stroke="{accent}" opacity=".45"/>
        <rect x="15" y="16" width="29" height="19" rx="5" fill="{accent}" opacity=".22"/>
        <text x="22" y="30" font-family="{MONO}" font-size="11" font-weight="700" fill="{fg}">{chapter}</text>
        <text x="55" y="30" font-family="{MONO}" font-size="12" letter-spacing=".6" fill="{fg}">{escape(area)}</text>
        <text x="15" y="76" font-family="{SANS}" font-size="31" font-weight="720" letter-spacing="-.9" fill="{fg}">{escape(title)}</text>
        <text x="16" y="107" font-family="{SANS}" font-size="17" font-weight="650" fill="{fg}">{escape(cta)} ↗</text>
        <g fill="none" stroke="{accent}" color="{accent}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".9">{ICONS[slug]}</g>
        """,
    )

BADGES = [
    ("portfolio", "Portfolio", "M14 13v9h12v-9m-9 4 7-7m-5 0h5v5", FOREST, PAPER, SAGE, 102),
    ("linkedin", "LinkedIn", "M16 14v8m0-12v1m4 11v-8m0 4c0-5 6-5 6 0v4", "#d4dece", INK, "#406557", 100),
    ("email", "Email", "M13.5 11h13v10h-13z m0 0 6.5 6 6.5-6", "#efe2d2", "#362b24", "#79503a", 82),
]
for name, label, path, bg, fg, accent, width in BADGES:
    write(
        f"field-badge-{name}", width, 33, label,
        f"""
        <rect x=".5" y=".5" width="{width - 1}" height="32" rx="8" fill="{bg}" stroke="{accent}" stroke-opacity=".53"/>
        <path d="{path}" stroke="{accent}" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="34" y="21" font-family="{SANS}" font-size="12" font-weight="700" fill="{fg}">{label}</text>
        """,
    )

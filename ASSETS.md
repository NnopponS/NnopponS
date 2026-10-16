# Profile visuals

This repository contains Worapon Sangsasri's GitHub profile README and its visual components.

- **`hero.svg`**: original animated circuit-and-knight illustration, with a reduced-motion media query.
- **`signal-loop.gif`**: original 60-frame, 4.8-second looping animation. A `picture` element selects `signal-still.svg` for reduced-motion preferences where supported.
- **Project cards, workbench, navigation, footer**: original, self-contained SVGs. No scripts, external fonts, remote badge APIs, or live-stat services are required.
- **Mobile views**: `hero-mobile.svg` and `stack-mobile.svg` provide larger type and compact layouts through `picture` source selection below 600 pixels, where supported.
- **`portrait.png`**: Worapon's existing [public GitHub avatar](https://avatars.githubusercontent.com/u/105480619?v=4), copied without retouching on 2026-10-16. This is a real profile photo, not a generated likeness.
- **Profile facts**: supplied [LinkedIn profile](https://www.linkedin.com/in/worapon-sangsasri-0371a8376/), [portfolio source](https://github.com/NnopponS/NnopponS.github.io/blob/main/src/data/portfolio.ts), and the linked public project READMEs, reviewed on 2026-10-16. Award descriptions are condensed; team achievements are not presented as solo project ownership.
- **Inspiration**: [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme). The artwork and motion assets here are custom, rather than copied from an example profile.

The moving signal paths and room map are decorative illustrations. They are not live telemetry, benchmark results, or validated clinical measurements.

## Customize

Edit `README.md` for profile text and links. Edit the colors, labels, and drawing functions in `scripts/build_assets.py` to change the visual components.

To rebuild the SVGs and GIF:

```bash
python -m pip install Pillow
python scripts/build_assets.py
```

For consistent GIF typography on Linux, install the DejaVu Sans fonts. The script falls back to Pillow's default font when those files are unavailable. SVGs use DejaVu Sans / Arial / sans-serif and DejaVu Sans Mono / monospace fallback stacks. The portrait is independent of the generator and is preserved on rebuild.

Keep `README.md` in the root of the public **NnopponS/NnopponS** repository to display it on the GitHub profile Overview.

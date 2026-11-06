#!/usr/bin/env python3
"""One-off script to apply Open Slot deck UI fixes. Run from repo root or examples/open-slot."""
from pathlib import Path
import re

DECK = Path(__file__).resolve().parent / "deck.html"
text = DECK.read_text(encoding="utf-8")

def sub(pattern, repl, flags=0):
    global text
    n = len(re.findall(pattern, text, flags))
    text2, c = re.subn(pattern, repl, text, flags=flags)
    if c == 0 and pattern and not pattern.startswith('^'):  # allow optional subs
        pass
    text = text2
    return c

# --- Font link ---
text = re.sub(
    r'<link rel="stylesheet" href="https://fonts.googleapis.com/css2[^"]*"',
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"',
    text,
    count=1,
)

# --- Deck chrome: no corner number ---
text = text.replace('data-chrome="number"', 'data-chrome="none"', 1)

# --- Remove beachhead section (keep script untouched: only <section id="beachhead">) ---
text = re.sub(
    r'\n  <section class="slide inv-slide" id="beachhead"[\s\S]*?</section>\n',
    '\n',
    text,
    count=1,
)

# --- HTML class renames (labels, heads, sources) — data-* preserved by pattern ---
RENAMES = [
    (r'class="pb-split-k"', 'class="os-label"'),
    (r'class="pb-scale2-k"', 'class="os-label"'),
    (r'class="pb-impact2-k"', 'class="os-label"'),
    (r'class="sol-ref-k"', 'class="os-label"'),
    (r'class="sol-how-k"', 'class="os-label"'),
    (r'class="sol-demo-k"', 'class="os-label"'),
    (r'class="bm2-k"', 'class="os-label"'),
    (r'class="m10-label"', 'class="os-label"'),
    (r'class="inv-kicker"', 'class="os-label"'),
    (r'class="c11-label"', 'class="os-label"'),
    (r'class="c12-label"', 'class="os-label"'),
    (r'class="t15-label"', 'class="os-label"'),
    (r'class="d16-label"', 'class="os-label"'),
    (r'class="a14-label"', 'class="os-label"'),
    (r'class="pb-scale2-head"', 'class="os-h1"'),
    (r'class="sol-ref-head"', 'class="os-h1"'),
    (r'class="sol-how-head"', 'class="os-h1"'),
    (r'class="sol-demo-head"', 'class="os-h1"'),
    (r'class="bm2-h1"', 'class="os-h1"'),
    (r'class="m10-h1"', 'class="os-h1"'),
    (r'class="inv-h1"', 'class="os-h1"'),
    (r'class="c11-h1"', 'class="os-h1"'),
    (r'class="c12-h1"', 'class="os-h1"'),
    (r'class="t15-h1"', 'class="os-h1"'),
    (r'class="d16-h1"', 'class="os-h1"'),
    (r'class="a14-h1"', 'class="os-h1"'),
    (r'class="pb-src"', 'class="os-src"'),
    (r'class="bm2-note"', 'class="os-src"'),
    (r'class="m10-src"', 'class="os-src"'),
    (r'class="inv-foot"', 'class="os-src"'),
    (r'class="c11-src"', 'class="os-src"'),
    (r'class="c12-src"', 'class="os-src"'),
    (r'class="t15-src"', 'class="os-src"'),
    (r'class="d16-src"', 'class="os-src"'),
    (r'class="a14-src"', 'class="os-src"'),
]
for old, new in RENAMES:
    text = text.replace(old, new)

# --- Slide label numbers (content inside <b>) ---
LABEL_MAP = {
    'id="jack"': '<b>02</b>',
    'id="scale"': '<b>03</b>',
    'id="impact"': '<b>04</b>',
    'id="phone"': '<b>05</b>',
    'id="loop"': '<b>06</b>',
    'id="demo"': '<b>07</b>',
    'id="model"': '<b>08</b>',
    'id="market"': '<b>09</b>',
    'id="compete"': '<b>10</b>',
    'id="gtm"': '<b>11</b>',
    'id="finance"': '<b>12</b>',
    'id="team"': '<b>13</b>',
    'id="advisors"': '<b>14</b>',
    'id="ask"': '<b>15</b>',
}
def section_block(html, sid):
    m = re.search(rf'(<section[^>]*{re.escape(sid)}[^>]*>[\s\S]*?</section>)', html)
    return m.group(1) if m else None

for sid, bb in LABEL_MAP.items():
    block = section_block(text, sid)
    if not block:
        continue
    block2 = re.sub(
        r'(<p class="os-label"[^>]*>)\s*(?:<b>\d+</b>\s*)?([^<]*)',
        rf'\1{bb} \2',
        block,
        count=1,
    )
    # Normalize double spaces after b
    block2 = re.sub(rf'({re.escape(bb)})\s{{2,}}', r'\1 ', block2)
    text = text.replace(block, block2, 1)

# --- Jack: split-head stays; add os-label in copy column if pb-split-k was renamed — fix first line label text ---
text = re.sub(
    r'(<p class="os-label" data-anim="fade">)<b>02</b>The problem(</p>\s*<h2 class="pb-split-head")',
    r'\1<b>02</b> The problem\3',
    text,
    count=1,
)

# --- Title HTML: strip decorations, add t1-meta ---
title_old = re.search(
    r'(<section class="slide" id="title"[\s\S]*?</aside>\s*</section>)',
    text,
)
if title_old:
    t = title_old.group(1)
    # Simpler title inner
    new_title = '''<section class="slide slide--dark" id="title" data-title="Open Slot AI" data-pos="0 0" data-hold="5">
    <div class="t1">
      <div class="t1-stage">
        <div class="t1-hero">
          <div class="t1-mascot-wrap">
            <div class="t1-mascot-rig" data-anim="scale" data-delay=".08" data-dur="1.05">
              <img class="t1-mascot" src="assets/mark.png" width="400" height="400" alt="">
            </div>
          </div>
        </div>
        <div class="t1-copy">
          <p class="t1-brand" data-anim="mask" data-delay=".22" data-dur="1.05">Open Slot <span>AI</span></p>
          <h1 class="t1-head" data-anim="mask" data-delay=".42" data-dur="1">Never miss a call.</h1>
          <p class="t1-head-sub" data-anim="mask" data-delay=".52" data-dur=".95">Never miss an <em>opportunity.</em></p>
          <p class="t1-meta">Baqer Hassani · Isaac Neal · University of Tulsa</p>
        </div>
      </div>
    </div>
    <aside class="notes"><p>Say the name: Open Slot AI. Then the two-line promise. Advance to Jack.</p></aside>
  </section>'''
    text = text.replace(t, new_title, 1)

# --- Phone: remove subline from list item 02; add slide--dark ---
text = text.replace(
    '<section class="slide sol-reveal-slide" id="phone"',
    '<section class="slide sol-reveal-slide slide--dark" id="phone"',
    1,
)
text = text.replace(
    '<strong>Books the job into Jack\'s calendar before they hang up.</strong><br>Spoken booking only after the calendar returns an event id.',
    '<strong>Books the job into Jack\'s calendar before they hang up.</strong>',
    1,
)
# Phone os-label + os-h1
text = re.sub(
    r'(<div class="sol-ref-copy">\s*)<p class="os-label" data-anim="fade">06 The solution</p>\s*<h2 class="os-h1"',
    r'\1<p class="os-label" data-anim="fade"><b>05</b> The solution</p>\n        <h2 class="os-h1"',
    text,
    count=1,
)

# --- Loop + demo dark class ---
text = text.replace(
    '<section class="slide" id="loop"',
    '<section class="slide slide--dark" id="loop"',
    1,
)
text = text.replace(
    '<section class="slide sol-slide" id="demo"',
    '<section class="slide sol-slide slide--dark" id="demo"',
    1,
)

# --- Loop: os-label with number ---
text = re.sub(
    r'<p class="os-label" data-anim="fade">07 How it works</p>',
    '<p class="os-label" data-anim="fade"><b>06</b> How it works</p>',
    text,
    count=1,
)

# --- Demo: remove demo-lede paragraph; merge note ---
text = re.sub(
    r'\n    <p class="demo-lede" data-anim="fade" data-delay=".6">Press play on the video \(\~30s\)</p>',
    '',
    text,
    count=1,
)
text = text.replace(
    '<aside class="notes"><p>Video shows the concept UI; no duplicate HTML overlay. Booked only when calendar confirms.</p></aside>',
    '<aside class="notes"><p>Press play on the video (~30s). Video shows the concept UI; no duplicate HTML overlay. Booked only when calendar confirms.</p></aside>',
    1,
)

# --- Demo os-label ---
text = re.sub(
    r'<p class="os-label" data-anim="fade">08 Demo</p>',
    '<p class="os-label" data-anim="fade"><b>07</b> Demo</p>',
    text,
    count=1,
)

# --- Compete: remove c11-foot paragraph ---
text = re.sub(
    r'\s*<p class="c11-foot" data-anim="fade" data-delay="\.28">[\s\S]*?</p>',
    '',
    text,
    count=1,
)

# --- Finance: replace inner section content (keep opening tag through first line of inv-wrap) ---
fin = re.search(
    r'(<section class="slide inv-slide" id="finance"[^>]*>\s*)([\s\S]*?)(\s*</section>\s*<section class="slide inv-slide" id="team")',
    text,
)
if fin:
    open_tag = fin.group(1)
    rest = fin.group(3)
    new_fin = open_tag + '''
    <div class="fin-wrap">
      <p class="os-label" data-anim="fade"><b>12</b> Financial model</p>
      <h2 class="os-h1" data-anim="mask" data-delay=".06">Profitable in year 3.</h2>
      <div class="fin-chart" data-anim="rise" data-delay=".14" role="img" aria-label="Revenue and cost by year 2027 to 2031">
        <div class="fin-col"><div class="fin-bars"><span class="fin-rev" style="height:18%">$94K</span><span class="fin-cost" style="height:65%">$56K</span></div><p class="fin-y">2027</p><p class="fin-s">32 shops</p><p class="fin-a">$120K ARR</p><p class="fin-p fin-p--loss">−$42K</p></div>
        <div class="fin-col"><div class="fin-bars"><span class="fin-rev" style="height:32%">$280K</span><span class="fin-cost" style="height:62%">$170K</span></div><p class="fin-y">2028</p><p class="fin-s">80 shops</p><p class="fin-a">$360K ARR</p><p class="fin-p fin-p--loss">−$18K</p></div>
        <div class="fin-col"><div class="fin-bars"><span class="fin-rev" style="height:48%">$510K</span><span class="fin-cost" style="height:58%">$300K</span></div><p class="fin-y">2029</p><p class="fin-s">140 shops</p><p class="fin-a">$650K ARR</p><p class="fin-p fin-p--pos">+$12K</p></div>
        <div class="fin-col"><div class="fin-bars"><span class="fin-rev" style="height:64%">$730K</span><span class="fin-cost" style="height:55%">$410K</span></div><p class="fin-y">2030</p><p class="fin-s">210 shops</p><p class="fin-a">$930K ARR</p><p class="fin-p fin-p--pos">+$130K</p></div>
        <div class="fin-col"><div class="fin-bars"><span class="fin-rev" style="height:78%">$878K</span><span class="fin-cost" style="height:52%">$480K</span></div><p class="fin-y">2031</p><p class="fin-s">260 shops</p><p class="fin-a">$1.12M ARR</p><p class="fin-p fin-p--pos">+$210K</p></div>
      </div>
      <div class="fin-side" data-anim="fade" data-delay=".24">
        <div><p class="fin-sk">Gross margin</p><p class="fin-sv">51%</p></div>
        <div><p class="fin-sk">Break-even</p><p class="fin-sv">2029 <span class="fin-sub">(~250 shops)</span></p></div>
        <div><p class="fin-sk">Cash needed</p><p class="fin-sv fin-sv--cash">$120K</p></div>
      </div>
      <p class="os-src" data-anim="fade" data-delay=".3">Illustrative forecast · not actuals · Assumes $1,908/shop/year blended ARPA and cost ramp in line with staff and usage · JOLT prize pool is separate from operating capital</p>
    </div>
    ''' + rest
    text = text.replace(fin.group(0), new_fin, 1)

# --- Market: label/h1 already renamed; fix bold number in label ---
text = re.sub(
    r'<p class="os-label" data-anim="fade"><b>10</b>Market</p>',
    '<p class="os-label" data-anim="fade"><b>09</b> Market</p>',
    text,
    count=1,
)

# --- Model: fix label spacing ---
text = re.sub(
    r'<p class="os-label" data-anim="fade">09 Business model</p>',
    '<p class="os-label" data-anim="fade"><b>08</b> Business model</p>',
    text,
    count=1,
)

# --- GTM / team / advisors / ask: ensure bold format in label (script may have wrong numbers) ---
text = re.sub(
    r'<p class="os-label" data-anim="fade"><b>11</b>Competition',
    '<p class="os-label" data-anim="fade"><b>10</b> Competition',
    text,
    count=1,
)
text = re.sub(
    r'<p class="os-label" data-anim="fade"><b>12</b>Go-to-market',
    '<p class="os-label" data-anim="fade"><b>11</b> Go-to-market',
    text,
    count=1,
)
text = re.sub(
    r'<p class="os-label" data-anim="fade"><b>15</b>Team',
    '<p class="os-label" data-anim="fade"><b>13</b> Team',
    text,
    count=1,
)
text = re.sub(
    r'<p class="os-label" data-anim="fade"><b>16</b>Advisors',
    '<p class="os-label" data-anim="fade"><b>14</b> Advisors',
    text,
    count=1,
)
text = re.sub(
    r'<p class="os-label" data-anim="fade"><b>14</b>Investment ask',
    '<p class="os-label" data-anim="fade"><b>15</b> Investment ask',
    text,
    count=1,
)

# --- Scale/impact jack labels: add bold + space after number ---
text = re.sub(
    r'<p class="os-label" data-anim="fade">02 The problem</p>',
    '<p class="os-label" data-anim="fade"><b>02</b> The problem</p>',
    text,
    count=1,
)
text = re.sub(
    r'<p class="os-label" data-anim="fade">03 The problem</p>',
    '<p class="os-label" data-anim="fade"><b>03</b> The problem</p>',
    text,
    count=1,
)
text = re.sub(
    r'<p class="os-label" data-anim="fade">04 The problem</p>',
    '<p class="os-label" data-anim="fade"><b>04</b> The problem</p>',
    text,
    count=1,
)

DECK.write_text(text, encoding="utf-8")
print("Wrote", DECK)

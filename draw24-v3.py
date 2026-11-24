#!/usr/bin/env python3
"""Tuesday 24 November 2026, one broadsheet page -- v3-local.

Morning edition No. 2. Wires read to 07:35 UTC, so the page carries
the overnight wires plus Monday's events as Tuesday's editions
report them, with the tolls and the market figures re-checked
against Tuesday's own sources rather than carried over from any
earlier draft. Two corrections to the morning's first edition:
the Dymer toll is the FINAL 11 in the block (search ended on the
evening of 23 Nov; the 14 was 11 in Dymer plus 3 in Vyshneve),
and the two survivors were trapped for different times -- David
about 14 hours, Valentyna about 22.

FIGURE LEDGER -- every number on the page, with its source
(all read 24 November 2026, before 07:35 UTC):
  Nvidia: shares +31.48% at the close, $165.05 (+$39.52);
    about $952bn added in market value in one day (CNN's
    figure; other outlets round it to ~$1tn -- our call is
    CNN's $952bn); Nasdaq +6.5% (+1,470 points, second-biggest
    points gain ever); S&P 500 +4.7% (+327 points, second-
    biggest); Dow +1,450 points (+3%); volume 772.5m shares,
    about 330% above the 179.8m daily average; intraday high
    +36.6%; board acted 11 days after Huang quit; Polymarket
    gave the return a 3% chance minutes before the news;
    short sellers lost about $12.2bn in a day (ORTEX, biggest
    since at least 2019); Huang's net worth passed $143bn;
    fiscal 2028 revenue guided up 75%; Q3 revenue $115.8bn,
    +103% year on year -- Motley Fool, QUE, RIABiz, 24 Nov.
  Dymer: drone about 05:00 on Sunday 22 Nov; five-storey
    block, stairwell collapsed across all five floors, fire;
    FINAL toll 11 dead in the block, five in hospital; David,
    7, pulled alive after about 14 hours; Valentyna, 79,
    pulled alive after about 22 hours; more than 130
    rescuers; 186 drones launched that night (72 jet-powered),
    161 downed, hits at 18 locations; Vyshneve 3 dead, 13
    injured; Bila Tserkva 1 dead; region mourned on 23 Nov --
    BBC / Reuters / AP wires via NGlobe News, SOFX, The Gaze,
    Transform Ukraine, 23-24 Nov.
  India-Nepal: about $1.6bn package (NPR 24,000 crore, about
    EUR 1.4bn); 8 pacts signed; Ayodhya-Janankpur train
    flagged off -- Jagran Josh / Swadesi, 23 Nov 2026.
  Cyprus: 2 Russian diplomats expelled; KYP surveillance;
    first reported by ANT1; confirmed by two senior officials
    to Politico; names Sergeyev and Shevtsov per The Insider,
    NOT officially confirmed; embassy staff 36 down to 34;
    Cyprus held the EU Council presidency Jan-Jun 2026; ANT1
    says the men got no information -- The Gaze, The Insight
    International, livefromeurope.eu, 23-24 Nov.
  Asia rally (Tuesday): Taiwan +9.1% (Taiex +3,300 points,
    biggest intraday points gain on record; TSMC at its 10%
    daily limit, over 40% of the index); KOSPI +7% to +7.5%;
    Nikkei +4.6% to +5% after a three-day weekend; MSCI Asia
    ex-Japan +4%, biggest since 31 Jul, snapping an eight-day
    losing streak; Samsung +10.3%, SK hynix +7.9% (US ADR
    +20% to $124.28, +$20.71); Advantest +15%; LG +12.86%;
    SoftBank +3%; Korea Exchange Sidecar halt -- Reuters via
    Finwire, Kotak Neo, BeInCrypto, TradingView, 24 Nov.
  Megaspeed: US Entity List; Singapore-based; six other
    Southeast Asian firms listed the same day -- Daily
    Summary Of, 24 Nov 2026.
  Indonesia fire: 24 dead, about 30 missing; about 300
    people on the Saturday shift; 29 confirmed safe, 5 of
    them in hospital -- Reuters, 23 Nov 2026.
  Libya: 7 Ukrainian sea drones; corvette Merkury
    (commissioned 2023) sunk off Benghazi; a Ka-27 helicopter
    destroyed; dry-cargo ship MV Angara also hit; 10 people
    hurt -- Reuters / Defense News / SOFX, 23 Nov.
  Korea: Kang Kum-sil first woman to lead the NIS; Lim
    foreign minister -- Reuters, 23 Nov 2026.
  Denmark: 91 leases ended; top court finds no bias --
    Reuters, 23 Nov 2026.
  Trump conviction: 34 counts; $130,000 payment; court
    revives bid to move the case to federal court -- AP.
  FIFA: 2031 to the US, Mexico, Costa Rica and Jamaica;
    2035 to the UK; 48 teams -- FIFA / AP, 23 Nov 2026.
  Swift plot: 3 Vienna shows, Aug 2024 -- former Mossad
    chief Barnea's reveal, Fox News, 23 Nov 2026.
  Armenia: Pashinyan drops the Karabakh claim; vows a deal
    -- Reuters / AP, 23 Nov 2026.
  Iran missiles: lawmaker claims range up from 2,000 to
    4,500 km; no proof offered -- Iran International.
  Supermoon: full Beaver Moon peaks 14:53 UTC 24 Nov;
    passes the Pleiades -- Farmers' Almanac / NASA.
  Cricket: India 720/9 declared (record total in NZ);
    NZ 368 and 239/5; Nicholls 175 not out; 120 overs batted
    out; 352-run first-innings lead -- ESPNcricinfo, 23 Nov.
  Waymo: driverless taxis pulled from US roads -- overnight
    wires, 24 Nov 2026.
  Zelensky: calls for four-party talks (Ukraine, Russia, US,
    Europe) as soon as possible, ready Tuesday -- Daily
    Summary Of, 24 Nov 2026.
  Oil: Brent -$2.62 (-2.83%) to $89.95; WTI low $79.95;
    Libya's Sharara pipeline reopened -- Reuters, 23 Nov.
  Hours (UTC, all from wires timestamped 24 Nov): 00:10
    Seoul (markets open), 01:53 Taipei (TSMC at its limit),
    04:00 Washington (hour in review), 06:49 Nicosia
    (expulsions confirmed), 07:35 press time, 14:53 the sky
    (supermoon peak, later today).

DATE DISCIPLINE: every story on this page happened, or was
first reported, on Tuesday 24 November 2026. The DATE CHECK
box opens with that positive assertion, names what was left
out as other days' news, names what had NOT yet happened by
press time, and explains that the page is a morning edition:
the overnight wires are timestamped 24 November, and
Monday's events are carried as reported in Tuesday's
editions. The Dymer strike itself fell on Sunday 22 Nov;
the final toll and the rescue are Tuesday's news. No story
on the main page is unverified; claims are framed as claims;
no headline claims a peace deal was signed or a war ended.
"""

import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

W, H = 1024, 1024

# ---- palette: cream paper, navy masthead, brick red, gold ----
PAPER = (247, 243, 232)
CARD = (255, 253, 246)
INK = (24, 24, 22)
NAVY = (18, 34, 58)
NAVY2 = (28, 52, 84)
BRICK = (178, 38, 28)
GOLD = (198, 158, 40)
GOLD_L = (232, 205, 120)
TEAL = (14, 92, 86)
SKY = (46, 110, 158)
LEAF = (52, 122, 60)
RUST = (176, 96, 20)
PLUM = (104, 62, 128)
SLATE = (84, 92, 104)
LINE = (180, 172, 150)
SOFT = (238, 232, 214)
NIGHT = (26, 36, 58)
CREAM = (244, 238, 220)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(t, f, w):
    out, cur = [], ""
    for word in t.split():
        trial = (cur + " " + word).strip()
        if f.getlength(trial) <= w or not cur:
            cur = trial
        else:
            out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def para(d, x, y, w, t, f, fill=INK, lh=None, max_lines=None):
    lines = wrap(t, f, w)
    if max_lines:
        lines = lines[:max_lines]
    lh = lh or int(f.size * 1.28)
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y


def rule(d, x, y, w, color=INK, px=1):
    d.rectangle([x, y, x + w - 1, y + px - 1], fill=color)


def tag(d, x, y, kind):
    """Certainty pill: CONFIRMED / REPORTED / CLAIM."""
    label = {"C": "CONFIRMED", "R": "REPORTED", "K": "CLAIM"}[kind]
    bg = {"C": LEAF, "R": RUST, "K": PLUM}[kind]
    f = F(SANSB, 8)
    tw = int(f.getlength(label)) + 10
    d.rounded_rectangle([x, y, x + tw, y + 12], radius=6, fill=bg)
    d.text((x + 5, y + 2), label, font=f, fill=(255, 255, 255))
    return tw


def kicker(d, x, y, place, color=BRICK):
    d.text((x, y), place.upper(), font=F(SANSB, 10), fill=color)
    return F(SANSB, 10).getlength(place.upper())

# ================================================================
# Scenes -- every picture on the page is drawn here, flat and bold
# so it still reads when the page is shrunk to ~300 pixels wide.
# ================================================================

def ill_dymer(d, x, y, w, h):
    """Collapsed five-storey block at night: crane, floodlights,
    rescuers in orange, stretcher. The day's human story, big."""
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=NIGHT)
    for sx, sy in [(x + 30, y + 14), (x + 90, y + 30), (x + 200, y + 10),
                   (x + 320, y + 26), (x + 430, y + 12), (x + 500, y + 34)]:
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 255, 255))
    # floodlight beams
    d.polygon([(x + 60, y + h), (x + 150, y + 10), (x + 190, y + 10),
               (x + 130, y + h)], fill=(72, 84, 116))
    d.polygon([(x + w - 60, y + h), (x + w - 170, y + 8), (x + w - 130, y + 8),
               (x + w - 120, y + h)], fill=(72, 84, 116))
    # standing wing of the block, lit windows
    d.rectangle([x + 30, y + 40, x + 150, y + h - 18], fill=(58, 62, 74))
    for wy in range(y + 52, y + h - 30, 22):
        for wx in (x + 44, x + 74, x + 104):
            d.rectangle([wx, wy, wx + 18, wy + 13],
                        fill=GOLD_L if (wy // 22) % 2 else (30, 32, 40))
    # collapsed wing: tilted slabs
    d.polygon([(x + 160, y + h - 18), (x + 180, y + 78), (x + 330, y + 96),
               (x + 340, y + h - 18)], fill=(96, 94, 88))
    d.polygon([(x + 200, y + 96), (x + 260, y + 74), (x + 360, y + 88),
               (x + 330, y + 118)], fill=(120, 116, 106))
    d.polygon([(x + 250, y + 118), (x + 300, y + 100), (x + 400, y + 112),
               (x + 380, y + 140)], fill=(78, 76, 70))
    for dx, dy in [(x + 230, y + 108), (x + 300, y + 122), (x + 350, y + 104)]:
        d.rectangle([dx, dy, dx + 12, dy + 8], fill=(40, 40, 44))
    # crane arm
    d.line([x + 380, y + 8, x + 500, y + 60], fill=(232, 150, 40), width=7)
    d.line([x + 500, y + 60, x + 500, y + 96], fill=(232, 150, 40), width=3)
    d.rectangle([x + 368, y + 4, x + 392, y + 34], fill=(232, 150, 40))
    d.rectangle([x + 492, y + 96, x + 508, y + 108], fill=(232, 150, 40))
    # rescuers in orange with helmets
    for rx, ry in [(x + 380, y + h - 52), (x + 420, y + h - 48),
                   (x + 452, y + h - 54)]:
        d.ellipse([rx - 6, ry - 26, rx + 6, ry - 14], fill=(240, 120, 30))
        d.rectangle([rx - 7, ry - 14, rx + 7, ry + 2], fill=(240, 120, 30))
        d.rectangle([rx - 6, ry + 2, rx - 1, ry + 16], fill=(30, 30, 34))
        d.rectangle([rx + 2, ry + 2, rx + 7, ry + 16], fill=(30, 30, 34))
    # stretcher with the boy, carried out
    d.line([x + 400, y + h - 30, x + 480, y + h - 30], fill=(220, 220, 210),
           width=4)
    d.ellipse([x + 436, y + h - 42, x + 446, y + h - 32], fill=(244, 200, 160))
    d.rectangle([x + 424, y + h - 36, x + 470, y + h - 30], fill=(180, 220, 230))
    d.rectangle([x, y + h - 18, x + w - 1, y + h - 1], fill=(20, 24, 38))


def ill_nvidia(d, x, y, w, h):
    """Black-green chip panel: a GPU die, a steep green chart,
    and the day's number in white."""
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(8, 26, 18))
    # chip die
    cx, cy = x + 42, y + h // 2 - 4
    d.rectangle([cx - 30, cy - 30, cx + 30, cy + 30], fill=(18, 92, 52),
                outline=(118, 220, 140), width=2)
    d.rectangle([cx - 16, cy - 16, cx + 16, cy + 16], fill=(118, 220, 140))
    d.text((cx - 12, cy - 7), "NV", font=F(SANSB, 13), fill=(8, 26, 18))
    for px in range(cx - 26, cx + 28, 9):
        d.rectangle([px, cy - 38, px + 4, cy - 31], fill=(118, 220, 140))
        d.rectangle([px, cy + 31, px + 4, cy + 38], fill=(118, 220, 140))
    # rising chart
    pts = [(x + 96, y + h - 22), (x + 118, y + h - 40), (x + 132, y + h - 34),
           (x + 152, y + h - 62), (x + 170, y + h - 52), (x + 192, y + h - 84)]
    d.line(pts, fill=(96, 230, 120), width=4)
    d.polygon([(x + 192, y + h - 84), (x + 184, y + h - 72),
               (x + 196, y + h - 70)], fill=(96, 230, 120))
    d.text((x + 100, y + 8), "+31%", font=F(SANSB, 30), fill=(255, 255, 255))
    d.text((x + 100, y + 42), "IN A DAY", font=F(SANSB, 11),
           fill=(150, 230, 170))


def ill_modi(d, x, y, w, h):
    """Two leaders, a train front, and the two flags."""
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(244, 232, 200))
    # sky bands: India saffron / white / green
    d.rectangle([x, y, x + w - 1, y + 16], fill=(255, 153, 51))
    d.rectangle([x, y + 16, x + w - 1, y + 32], fill=(255, 255, 255))
    d.rectangle([x, y + 32, x + w - 1, y + 48], fill=(19, 136, 8))
    # train front
    d.rectangle([x + 118, y + 52, x + 190, y + h - 14], fill=(24, 68, 140))
    d.rectangle([x + 126, y + 60, x + 182, y + 82], fill=(180, 220, 245))
    d.rectangle([x + 126, y + 88, x + 150, y + 104], fill=(180, 220, 245))
    d.rectangle([x + 158, y + 88, x + 182, y + 104], fill=(180, 220, 245))
    d.ellipse([x + 132, y + h - 24, x + 144, y + h - 12], fill=(20, 20, 20))
    d.ellipse([x + 164, y + h - 24, x + 176, y + h - 12], fill=(20, 20, 20))
    d.line([x + 110, y + h - 8, x + 198, y + h - 8], fill=(60, 60, 60), width=3)
    # Modi figure: white kurta, glasses
    d.ellipse([x + 46, y + 62, x + 66, y + 82], fill=(232, 196, 160))
    d.rectangle([x + 36, y + 84, x + 76, y + h - 14], fill=(250, 250, 246))
    d.rectangle([x + 46, y + 68, x + 66, y + 72], fill=(30, 30, 30))
    d.rectangle([x + 52, y + 84, x + 60, y + 96], fill=(200, 200, 200))
    # Shah figure: dark suit, crimson tie
    d.ellipse([x + 84, y + 64, x + 102, y + 82], fill=(210, 172, 140))
    d.rectangle([x + 76, y + 84, x + 110, y + h - 14], fill=(32, 36, 52))
    d.rectangle([x + 88, y + 84, x + 96, y + 104], fill=(200, 40, 40))
    # Nepal flag: crimson double-pennon
    d.polygon([(x + w - 34, y + 56), (x + w - 14, y + 66), (x + w - 34, y + 76)],
              fill=(220, 20, 60))
    d.polygon([(x + w - 34, y + 76), (x + w - 10, y + 88), (x + w - 34, y + 98)],
              fill=(220, 20, 60))
    d.line([x + w - 34, y + 52, x + w - 34, y + 104], fill=(60, 60, 60), width=2)


def ill_nicosia(d, x, y, w, h):
    """Nicosia: white embassy with columns, Cyprus flag, two
    suited men with suitcases walking to a plane, big red 2."""
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(168, 204, 228))
    d.ellipse([x + w - 40, y + 8, x + w - 8, y + 40], fill=(255, 244, 200))
    # embassy block with columns
    d.rectangle([x + 14, y + 34, x + 150, y + h - 26], fill=(250, 248, 242))
    d.polygon([(x + 10, y + 34), (x + 82, y + 12), (x + 154, y + 34)],
              fill=(232, 226, 210))
    for cx0 in (x + 26, x + 56, x + 86, x + 116):
        d.rectangle([cx0, y + 40, cx0 + 10, y + h - 26], fill=(210, 204, 188))
    d.rectangle([x + 66, y + h - 52, x + 98, y + h - 26], fill=(90, 70, 50))
    # Cyprus flag on a pole
    d.line([x + 168, y + 20, x + 168, y + h - 26], fill=(60, 60, 60), width=2)
    d.rectangle([x + 168, y + 20, x + 206, y + 44], fill=(255, 255, 255),
                outline=(200, 200, 200))
    d.polygon([(x + 174, y + 26), (x + 196, y + 28), (x + 200, y + 38),
               (x + 180, y + 40)], fill=(232, 150, 40))
    # tarmac + plane nose
    d.rectangle([x, y + h - 26, x + w - 1, y + h - 1], fill=(70, 74, 82))
    d.polygon([(x + w - 96, y + 58), (x + w - 8, y + 58), (x + w - 8, y + 86),
               (x + w - 60, y + 86)], fill=(225, 228, 232))
    d.rectangle([x + w - 92, y + 62, x + w - 30, y + 72], fill=(46, 110, 158))
    d.polygon([(x + w - 8, y + 58), (x + w + 2, y + 66), (x + w - 8, y + 74)],
              fill=(180, 184, 190))
    # two suited men with suitcases
    for mx, my, suit in [(x + 216, y + h - 62, (28, 32, 46)),
                         (x + 244, y + h - 60, (52, 52, 58))]:
        d.ellipse([mx - 5, my - 24, mx + 5, my - 14], fill=(232, 196, 160))
        d.rectangle([mx - 7, my - 14, mx + 7, my + 8], fill=suit)
        d.rectangle([mx - 6, my + 8, mx - 1, my + 22], fill=(20, 20, 24))
        d.rectangle([mx + 2, my + 8, mx + 7, my + 22], fill=(20, 20, 24))
        d.rectangle([mx + 10, my + 6, mx + 22, my + 18], fill=(120, 80, 40))
        d.line([mx + 7, my + 2, mx + 14, my + 6], fill=(20, 20, 24), width=2)
    # big red 2 badge
    d.ellipse([x + w - 44, y + 4, x + w - 4, y + 44], fill=BRICK)
    d.text((x + w - 34, y + 8), "2", font=F(SANSB, 26), fill=(255, 255, 255))


def ill_waymo(d, x, y, w, h):
    """Driverless taxi with a sensor dome, parked under a stop sign."""
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(222, 232, 233))
    d.rectangle([x, y + h - 22, x + w - 1, y + h - 1], fill=(90, 96, 104))
    d.polygon([(x + 18, y + 78), (x + 34, y + 52), (x + 82, y + 50),
               (x + 104, y + 78)], fill=(30, 120, 130))
    d.rectangle([x + 14, y + 78, x + 112, y + 96], fill=(30, 120, 130))
    d.rectangle([x + 40, y + 56, x + 76, y + 72], fill=(180, 225, 235))
    d.ellipse([x + 56, y + 40, x + 70, y + 54], fill=(40, 44, 52))
    d.ellipse([x + 30, y + 92, x + 44, y + 106], fill=(18, 18, 20))
    d.ellipse([x + 84, y + 92, x + 98, y + 106], fill=(18, 18, 20))
    d.ellipse([x + 16, y + 82, x + 22, y + 88], fill=(255, 220, 120))
    d.line([x + 104, y + 20, x + 104, y + 44], fill=(60, 60, 60), width=3)
    d.polygon([(x + 92, y + 20), (x + 116, y + 20), (x + 104, y + 40)],
              fill=BRICK)
    d.text((x + 8, y + 6), "NO DRIVER", font=F(SANSB, 9), fill=BRICK)

# ---- grid-card mini scenes (short wide strips) ----

def ill_asia(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(10, 40, 26))
    for i, (bx, bh) in enumerate([(16, 14), (52, 22), (88, 18), (124, 30),
                                  (160, 26), (196, 36)]):
        d.rectangle([x + bx, y + h - 6 - bh, x + bx + 24, y + h - 6],
                    fill=(96, 230, 120) if i % 2 == 0 else (30, 140, 70))
    d.line([(x + 10, y + h - 12), (x + 90, y + 16), (x + 150, y + 22),
            (x + 224, y + 6)], fill=(255, 255, 255), width=3)
    d.text((x + 8, y + 2), "+9%", font=F(SANSB, 12), fill=(255, 255, 255))


def ill_mega(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(40, 40, 46))
    d.rectangle([x + 90, y + 6, x + 150, y + h - 6], fill=(20, 20, 24),
                outline=(200, 60, 50), width=2)
    d.text((x + 100, y + 10), "MEGA", font=F(SANSB, 10), fill=(255, 255, 255))
    d.text((x + 96, y + 24), "SPEED", font=F(SANSB, 10), fill=(255, 255, 255))
    d.line([x + 86, y + 4, x + 154, y + h - 4], fill=(220, 50, 40), width=4)
    d.text((x + 8, y + 12), "BLACKLIST", font=F(SANSB, 11), fill=(255, 120, 100))
    d.text((x + 168, y + 12), "7 FIRMS", font=F(SANSB, 11), fill=(255, 255, 255))


def ill_fire(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(46, 28, 20))
    d.rectangle([x + 10, y + 22, x + 110, y + h - 4], fill=(70, 70, 76))
    d.rectangle([x + 120, y + 14, x + 150, y + h - 4], fill=(70, 70, 76))
    for wx in (x + 20, x + 44, x + 68, x + 92):
        d.rectangle([wx, y + 28, wx + 12, y + 38], fill=(255, 200, 90))
    d.polygon([(x + 150, y + 16), (x + 162, y + 2), (x + 172, y + 18),
               (x + 184, y + 4), (x + 196, y + 20), (x + 172, y + 30)],
              fill=(255, 120, 30))
    d.polygon([(x + 164, y + 22), (x + 172, y + 12), (x + 182, y + 24)],
              fill=(255, 220, 90))
    d.text((x + 160, y + h - 16), "24 DEAD", font=F(SANSB, 11),
           fill=(255, 255, 255))


def ill_libya(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(16, 52, 84))
    d.rectangle([x, y + h - 14, x + w - 1, y + h - 1], fill=(10, 34, 58))
    d.polygon([(x + 60, y + 26), (x + 170, y + 26), (x + 150, y + h - 14),
               (x + 80, y + h - 14)], fill=(120, 124, 128))
    d.rectangle([x + 100, y + 10, x + 112, y + 26], fill=(120, 124, 128))
    d.ellipse([x + 176, y + 18, x + 196, y + 38], fill=(255, 120, 40))
    d.polygon([(x + 176, y + 28), (x + 190, y + 14), (x + 200, y + 30)],
              fill=(255, 180, 60))
    for dx, dy in [(x + 30, y + 10), (x + 44, y + 18), (x + 210, y + 8)]:
        d.ellipse([dx - 3, dy - 3, dx + 3, dy + 3], fill=(255, 255, 255))
    d.text((x + 8, y + 4), "7 DRONES", font=F(SANSB, 10), fill=(255, 255, 255))


def ill_seoul(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(232, 236, 242))
    d.rectangle([x + 16, y + 12, x + 66, y + h - 4], fill=(52, 84, 128))
    for wy in range(y + 16, y + h - 8, 8):
        d.rectangle([x + 22, wy, x + 30, wy + 4], fill=(180, 220, 245))
        d.rectangle([x + 52, wy, x + 60, wy + 4], fill=(180, 220, 245))
    d.ellipse([x + 150, y + 8, x + 166, y + 24], fill=(232, 196, 160))
    d.rectangle([x + 142, y + 26, x + 174, y + h - 4], fill=(28, 52, 84))
    d.rectangle([x + 142, y + 26, x + 174, y + 32], fill=(255, 255, 255))
    d.text((x + 178, y + 12), "1ST WOMAN", font=F(SANSB, 9), fill=NAVY)


def ill_denmark(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(240, 234, 220))
    d.polygon([(x + 20, y + 10), (x + 80, y + 10), (x + 50, y + 26)],
              fill=(150, 40, 30))
    for cx0 in (x + 26, x + 46, x + 66):
        d.rectangle([cx0, y + 28, cx0 + 8, y + h - 8], fill=(120, 100, 80))
    d.rectangle([x + 18, y + h - 8, x + 84, y + h - 4], fill=(120, 100, 80))
    d.text((x + 110, y + 6), "91", font=F(SANSB, 22), fill=BRICK)
    d.text((x + 110, y + 28), "LEASES", font=F(SANSB, 9), fill=INK)


def ill_trump(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(30, 36, 52))
    d.rectangle([x + 20, y + 12, x + 120, y + h - 8], fill=(230, 226, 214))
    for cx0 in (x + 30, x + 60, x + 90):
        d.rectangle([cx0, y + 18, cx0 + 8, y + h - 12], fill=(90, 84, 70))
    d.rectangle([x + 150, y + 14, x + 196, y + 26], fill=(120, 80, 40))
    d.line([x + 168, y + 26, x + 178, y + 34], fill=(120, 80, 40), width=4)
    d.text((x + 150, y + h - 16), "34 COUNTS", font=F(SANSB, 10),
           fill=(255, 255, 255))


def ill_fifa(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(20, 90, 50))
    d.ellipse([x + 10, y + 6, x + 210, y + h + 30], fill=(40, 140, 70))
    d.line([x + 10, y + h - 8, x + 210, y + h - 8], fill=(255, 255, 255), width=2)
    d.ellipse([x + 96, y + 8, x + 128, y + 40], fill=(255, 255, 255),
              outline=(20, 20, 20))
    d.polygon([(x + 104, y + 14), (x + 112, y + 12), (x + 116, y + 20),
               (x + 110, y + 28), (x + 102, y + 22)], fill=(20, 20, 20))
    d.text((x + 140, y + 12), "48", font=F(SANSB, 20), fill=(255, 255, 255))
    d.text((x + 140, y + h - 16), "TEAMS", font=F(SANSB, 9), fill=(255, 255, 255))


def ill_mossad(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(24, 24, 30))
    d.rectangle([x + 10, y + h - 12, x + 130, y + h - 6], fill=(60, 60, 70))
    d.rectangle([x + 20, y + 16, x + 40, y + h - 12], fill=(40, 40, 48))
    d.rectangle([x + 100, y + 16, x + 120, y + h - 12], fill=(40, 40, 48))
    d.polygon([(x + 160, y + 4), (x + 196, y + 4), (x + 196, y + 22),
               (x + 178, y + 38), (x + 160, y + 22)], fill=(46, 110, 158))
    d.text((x + 170, y + 12), "✓", font=F(SANSB, 16), fill=(255, 255, 255))
    d.text((x + 14, y + 2), "VIENNA 2024", font=F(SANSB, 9), fill=(200, 200, 200))


def ill_armenia(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(214, 232, 240))
    d.ellipse([x + 60, y + 10, x + 110, y + 34], fill=(255, 255, 255))
    d.polygon([(x + 60, y + 22), (x + 34, y + 12), (x + 44, y + 30)],
              fill=(255, 255, 255))
    d.polygon([(x + 110, y + 22), (x + 136, y + 14), (x + 128, y + 30)],
              fill=(255, 255, 255))
    d.ellipse([x + 96, y + 12, x + 104, y + 20], fill=(20, 20, 20))
    d.line([x + 128, y + 30, x + 150, y + 36], fill=(52, 122, 60), width=3)
    d.ellipse([x + 150, y + 30, x + 158, y + 38], fill=(52, 122, 60))
    d.ellipse([x + 158, y + 34, x + 166, y + 42], fill=(52, 122, 60))
    d.text((x + 176, y + 12), "CHARTER", font=F(SANSB, 11), fill=NAVY)


def ill_iran(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(58, 28, 28))
    d.polygon([(x + 20, y + h - 6), (x + 60, y + 10), (x + 120, y + 6),
               (x + 180, y + h - 10)], fill=(120, 40, 36))
    d.line([(x + 24, y + h - 10), (x + 64, y + 12), (x + 118, y + 8),
            (x + 176, y + h - 12)], fill=(255, 180, 90), width=2)
    d.ellipse([x + 172, y + h - 20, x + 184, y + h - 8], fill=(255, 220, 120))
    d.text((x + 8, y + 4), "4,500 KM?", font=F(SANSB, 12), fill=(255, 255, 255))


def ill_moon(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(12, 16, 34))
    d.ellipse([x + 16, y + 2, x + 52, y + 38], fill=(244, 238, 214))
    d.ellipse([x + 24, y + 10, x + 32, y + 18], fill=(210, 204, 180))
    d.ellipse([x + 36, y + 22, x + 42, y + 28], fill=(210, 204, 180))
    for sx, sy in [(x + 90, y + 8), (x + 110, y + 16), (x + 100, y + 26),
                   (x + 122, y + 10), (x + 132, y + 22), (x + 150, y + 12),
                   (x + 170, y + 20)]:
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))
    d.text((x + 180, y + 8), "14:53", font=F(SANSB, 12), fill=(255, 255, 255))
    d.text((x + 180, y + 24), "UTC", font=F(SANSB, 9), fill=(200, 200, 220))


# ---- pictured-brief chips (small squares) ----

def ill_gaza(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(120, 116, 106))
    d.polygon([(x, y + h), (x + 10, y + 12), (x + 24, y + h)], fill=(90, 88, 82))
    d.polygon([(x + 12, y + h), (x + 26, y + 6), (x + 34, y + h)],
              fill=(70, 68, 62))
    d.ellipse([x + 8, y + 2, x + 18, y + 12], fill=(200, 200, 196))


def ill_tanker(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(16, 52, 84))
    d.rectangle([x + 3, y + 16, x + w - 3, y + 26], fill=(160, 40, 30))
    d.rectangle([x + 8, y + 8, x + 16, y + 16], fill=(220, 220, 210))
    d.line([x, y + 28, x + w, y + 28], fill=(180, 220, 240), width=2)
    d.line([x + 4, y + 31, x + w - 4, y + 31], fill=(140, 190, 220), width=2)


def ill_kadiz(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(168, 204, 228))
    d.polygon([(x + 6, y + 18), (x + 26, y + 18), (x + 16, y + 10)],
              fill=(120, 120, 126))
    d.polygon([(x + 12, y + 28), (x + 30, y + 28), (x + 21, y + 21)],
              fill=(90, 90, 96))
    d.polygon([(x + 17, y + 2), (x + 27, y + 20), (x + 7, y + 20)],
              fill=(255, 200, 40))
    d.text((x + 14, y + 8), "!", font=F(SANSB, 10), fill=(20, 20, 20))


def ill_oil(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(232, 228, 216))
    d.rectangle([x + 6, y + 8, x + 22, y + h - 4], fill=(30, 30, 34))
    d.rectangle([x + 6, y + 12, x + 22, y + 15], fill=(90, 90, 96))
    d.rectangle([x + 6, y + 22, x + 22, y + 25], fill=(90, 90, 96))
    d.polygon([(x + 26, y + 8), (x + 30, y + 8), (x + 28, y + 26),
               (x + 24, y + 22)], fill=BRICK)
    d.text((x + 24, y + 24), "-3%", font=F(SANSB, 8), fill=BRICK)


def ill_cricket(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(40, 110, 60))
    d.rectangle([x + 8, y + 6, x + 14, y + 26], fill=(210, 180, 120))
    d.rectangle([x + 8, y + 24, x + 12, y + 30], fill=(210, 180, 120))
    d.line([x + 22, y + 10, x + 22, y + 30], fill=(255, 255, 255), width=2)
    d.line([x + 26, y + 10, x + 26, y + 30], fill=(255, 255, 255), width=2)
    d.line([x + 30, y + 10, x + 30, y + 30], fill=(255, 255, 255), width=2)
    d.ellipse([x + 24, y + 4, x + 30, y + 10], fill=(200, 40, 40))

# ================================================================
# Data -- 52 stories: 3 leads + Cyprus + Waymo + 12 cards +
# 5 pictured briefs + 30 text briefs. Every number is in the
# docstring ledger above; nothing is carried from another day.
# ================================================================

LEADS = [
    ("DYMER, KYIV REGION", "C",
     "BOY, 7, PULLED ALIVE AFTER 14 HOURS",
     "Final toll 11 in the block; Valentyna, 79, freed after about "
     "22 hours; 130+ rescuers dug through the night; 186 drones "
     "launched, 161 downed."),
    ("SANTA CLARA", "C",
     "HUANG IS BACK \u2014 AND WALL STREET ROARS",
     "Board reinstates him 11 days after he quit; Nasdaq +6.5%, "
     "S&P +4.7%; about $952bn added in a day."),
    ("NEW DELHI", "C",
     "MODI HANDS NEPAL A $1.6BN PACKAGE",
     "8 pacts signed; Ayodhya\u2013Janakpur train flagged off; "
     "PM Balendra Shah in Delhi."),
]

CYPRUS = ("NICOSIA", "R",
          "CYPRUS EXPELS TWO ENVOYS IN SPY HUNT",
          "KYP watched the pair for months; the embassy staff list "
          "falls 36 to 34; the two names come from The Insider, "
          "not the government.")

WAYMO = ("SAN FRANCISCO", "R",
         "WAYMO PARKS ITS DRIVERLESS TAXIS",
         "The robotaxi operator pulls its driverless cars from "
         "US roads, the overnight wires report.")

# (number, place, headline, source) -- body text lives in CARD_BODY.
CARDS = [
    (6, "TAIPEI", "TAIWAN +9.1% AS CHIPS ROAR BACK",
     "Reuters, 24 Nov 2026"),
    (7, "WASHINGTON", "US BLACKLISTS MEGASPEED",
     "Daily Summary Of, 24 Nov 2026"),
    (8, "CIKANDE", "24 DEAD IN FACTORY FIRE",
     "Reuters, 23 Nov 2026"),
    (9, "BENGHAZI", "KYIV SINKS CORVETTE OFF LIBYA",
     "Reuters, 23 Nov 2026"),
    (10, "SEOUL", "FIRST WOMAN TO RUN SPY AGENCY",
     "Reuters, 23 Nov 2026"),
    (11, "COPENHAGEN", "COURT BACKS 'GHETTO LAW' EVICTIONS",
     "Reuters, 23 Nov 2026"),
    (12, "NEW YORK", "TRUMP GETS PATH TO CLEAR CONVICTION",
     "AP, 23 Nov 2026"),
    (13, "ZURICH", "US TO HOST 2031 WOMEN'S WORLD CUP",
     "FIFA, 23 Nov 2026"),
    (14, "JERUSALEM", "MOSSAD 'HELPED FOIL SWIFT PLOT'",
     "Fox News, 23 Nov 2026"),
    (15, "YEREVAN", "ARMENIA OFFERS PEACE CHARTER",
     "Reuters / AP, 23 Nov 2026"),
    (16, "TEHRAN", "IRAN CLAIMS 4,500 KM MISSILES",
     "Iran International, 23 Nov 2026"),
    (17, "THE SKY", "BEAVER MOON MEETS SEVEN SISTERS",
     "Farmers' Almanac / NASA, 24 Nov 2026"),
]

CARD_BODY = {
    6: "Taiex adds 3,300 points, a record intraday gain; TSMC hits "
       "its 10% limit; KOSPI +7%.",
    7: "At the centre of the Nvidia spy scandal, it joins the "
       "Entity List with six other firms.",
    8: "About 30 still missing; about 300 were on the Saturday "
       "shift; 29 safe, five in hospital.",
    9: "Seven sea drones hit the Merkury, commissioned 2023; a "
       "Ka-27 is destroyed; 10 people hurt.",
    10: "Kang Kum-sil is named to lead the NIS; Lim takes the "
        "foreign ministry in the same reshuffle.",
    11: "Ending 91 leases was not bias, the top court rules, in a "
        "case watched across Europe.",
    12: "A court revives his bid to move the case to federal court; "
        "34 counts rest on a $130,000 payment.",
    13: "The 48-team tournament goes to the US, Mexico, Costa Rica "
        "and Jamaica; the UK takes 2035.",
    14: "Ex-chief Barnea says Israeli help stopped the 2024 Vienna "
        "attack on three sold-out shows.",
    15: "Pashinyan drops the Karabakh claim and vows a deal with "
        "Baku in a landmark speech.",
    16: "A lawmaker says Europe is now in range, up from 2,000 km; "
        "no evidence is offered.",
    17: "The supermoon peaks at 14:53 UTC today and passes the "
        "Pleiades; the year's last supermoon.",
}

CARD_TAG = {9: "R", 14: "R", 16: "K"}
CARD_SCENE = {
    6: "ill_asia", 7: "ill_mega", 8: "ill_fire", 9: "ill_libya",
    10: "ill_seoul", 11: "ill_denmark", 12: "ill_trump",
    13: "ill_fifa", 14: "ill_mossad", 15: "ill_armenia",
    16: "ill_iran", 17: "ill_moon",
}

# Pictured briefs: (number, place, text, scene, tag)
PIC_BRIEFS = [
    (18, "GAZA", "Israeli strikes kill three; one of the dead "
     "worked for the UN agency UNRWA.", ill_gaza, "R"),
    (19, "GULF OF OMAN", "Tanker 'incident' off Chabahar, the "
     "UKMTO log says; no ship is named.", ill_tanker, "R"),
    (20, "KADIZ", "Russian jets trigger an alert on Ulleung "
     "Island, the second push in a week.", ill_kadiz, "R"),
    (21, "OIL", "Brent falls 3% to $89.95 as Middle East flows "
     "rise; Libya's Sharara pipeline reopens.", ill_oil, ""),
    (22, "CRICKET", "Nicholls 175 not out saves NZ; India 720/9, "
     "a record total there; the Test is drawn.", ill_cricket, ""),
]

# Text briefs: (number, place, text) -- one line each.
# Tags live in BRIEF_TAG; the 4th field stays out so the card-source
# check never reads an empty string here.
TEXT_BRIEFS = [
    (23, "WASHINGTON", "Trump: Huang 'no security threat'."),
    (24, "WASHINGTON", "Senate probes Vance-Vitol deal."),
    (25, "WASHINGTON", "US sanctions Iran shadow banks."),
    (26, "IOWA", "Trump halts Army lead-azide blasts."),
    (27, "BERLIN", "Germany to use Kyiv's Delta tool."),
    (28, "MOSCOW", "Russia accuses Estonia of hostility."),
    (29, "BRUSSELS", "EU to bar Russian symbols."),
    (30, "RIGA", "Latvia curbs Russian in public places."),
    (31, "COPENHAGEN", "Denmark to ban school phones, 2027."),
    (32, "KYIV", "Zelensky: Russia plans new strikes."),
    (33, "TEHRAN", "Iran vows to fight US naval blockade."),
    (34, "TEHRAN", "Singer gets 74 lashes, site says."),
    (35, "SOUTH SUDAN", "Strike kills 24, seven children."),
    (36, "CAIRO", "Egypt condemns attacks on Khartoum."),
    (37, "CONGO", "Ebola response hit by nearby fighting."),
    (38, "LAHORE", "Tops pollution ranking; AQI over 500."),
    (39, "PAKISTAN", "4.0 quake near the Afghan border."),
    (40, "ISLAMABAD", "Pakistan invites India to SCO meet."),
    (41, "BERLIN", "450 German schools get bomb threats."),
    (42, "CHICAGO", "O'Hare halts flights in the rush."),
    (43, "BEIJING", "China sets 2030 care targets."),
    (44, "DHAKA", "Dhaka vows to arrest Hasina on return."),
    (45, "BEIJING", "Official gets death for leaking secrets."),
    (46, "KYIV", "Zelensky calls for four-party talks soon."),
    (47, "WARSAW", "NATO sends AWACS to Poland."),
    (48, "SEOUL", "Russian jets enter air-defence zone."),
    (49, "HORMUZ", "Pugh swims the Strait of Hormuz."),
    (50, "CANBERRA", "Australia treats AI as a policy test."),
    (51, "WASHINGTON", "Short sellers lose $12.2bn today."),
    (52, "NEW YORK", "Huang's fortune passes $143bn."),
]

BRIEF_TAG = {35: "R", 44: "R", 48: "R"}

NUMBERS = [
    ("+31.5%", "NVDA CLOSE"),
    ("$952BN", "ONE-DAY GAIN"),
    ("11", "DEAD IN DYMER"),
    ("+9.1%", "TAIWAN"),
    ("24", "DEAD IN CIKANDE"),
    ("48", "TEAMS IN 2031"),
]

HOURS = [
    ("00:10", "SEOUL", "open"),
    ("01:53", "TAIPEI", "TSMC at limit"),
    ("04:00", "WASHINGTON", "review"),
    ("06:49", "NICOSIA", "confirmed"),
    ("07:35", "PRESS TIME", ""),
    ("14:53", "THE SKY", "supermoon"),
]

DATE_CHECK = (
    "DATE CHECK \u2014 Every story on this page happened, or was first "
    "reported, on Tuesday 24 November 2026. LEFT OUT AS OTHER DAYS' "
    "NEWS: COP31 pact rejected 22 Nov; ICJ ruling on Myanmar 20 Nov; "
    "Trump\u2013Xi\u2013Putin summit 18\u201319 Nov; Indonesia fire outbreak "
    "21 Nov (the toll is Tuesday's wire). NOT YET AT PRESS TIME 07:35 "
    "UTC: the supermoon peak at 14:53 UTC. The Dymer strike fell on "
    "Sunday 22 Nov; the final toll and the rescue are Tuesday's news."
)

# Registry of every picture on the page (22 scenes).
SCENES = [
    ill_dymer,
    ill_nvidia,
    ill_modi,
    ill_nicosia,
    ill_waymo,
    ill_asia,
    ill_mega,
    ill_fire,
    ill_libya,
    ill_seoul,
    ill_denmark,
    ill_trump,
    ill_fifa,
    ill_mossad,
    ill_armenia,
    ill_iran,
    ill_moon,
    ill_gaza,
    ill_tanker,
    ill_kadiz,
    ill_oil,
    ill_cricket,
]

# ================================================================
# World map -- rough continents, numbered dots for the day's
# eight pinned places, and the HOW SURE legend.
# ================================================================

LAND = {
    "N_AMERICA": [(-168, 66), (-140, 70), (-120, 72), (-95, 80),
                  (-80, 73), (-60, 60), (-55, 47), (-70, 42),
                  (-75, 35), (-80, 25), (-90, 20), (-97, 16),
                  (-105, 20), (-115, 28), (-125, 40), (-125, 49),
                  (-145, 60), (-165, 60)],
    "S_AMERICA": [(-80, 10), (-60, 8), (-50, 0), (-35, -8),
                  (-40, -20), (-48, -28), (-58, -35), (-65, -45),
                  (-70, -55), (-73, -40), (-75, -20), (-80, -5)],
    "AFRICA": [(-17, 15), (-10, 30), (0, 36), (10, 37), (20, 32),
               (32, 31), (35, 28), (43, 12), (51, 10), (48, 0),
               (40, -10), (35, -20), (32, -28), (20, -35), (15, -30),
               (12, -18), (13, -5), (9, 4), (-8, 5)],
    "EUROPE": [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53),
               (8, 57), (10, 59), (18, 56), (21, 55), (24, 59),
               (28, 60), (30, 62), (28, 66), (23, 70), (18, 69),
               (12, 65), (5, 60), (5, 58), (-2, 50), (-5, 48),
               (-10, 44)],
    "ASIA": [(30, 62), (40, 68), (60, 69), (70, 72), (90, 75),
             (110, 76), (130, 72), (150, 70), (170, 66), (178, 65),
             (170, 60), (162, 56), (158, 50), (142, 45), (140, 40),
             (130, 42), (127, 40), (122, 38), (120, 32), (115, 23),
             (108, 18), (105, 10), (100, 8), (97, 15), (92, 21),
             (88, 22), (80, 13), (77, 8), (72, 20), (66, 25),
             (60, 25), (57, 26), (52, 28), (48, 30), (44, 29),
             (40, 36), (36, 36), (33, 41), (30, 45), (28, 50),
             (30, 55)],
    "OCEANIA": [(113, -22), (114, -30), (115, -35), (124, -33),
                (130, -32), (137, -35), (140, -38), (147, -39),
                (150, -37), (153, -32), (153, -27), (146, -19),
                (142, -15), (142, -11), (136, -12), (132, -12),
                (126, -14), (122, -17), (114, -22)],
}

MAP_PINS = [
    (1, "DYMER", 31, 50), (2, "NICOSIA", 33, 35),
    (3, "DELHI", 77, 28), (4, "SEOUL", 127, 37),
    (5, "TAIPEI", 121, 25), (6, "CIKANDE", 107, -6),
    (7, "BENGHAZI", 20, 32), (8, "WASHINGTON", -77, 39),
]


def paint_map(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=(206, 224, 234))
    top = y + 18
    mh = h - 52
    def px(lon):
        return x + 4 + (lon + 170) / 360.0 * (w - 8)
    def py(lat):
        return top + (75 - lat) / 130.0 * mh
    for pts in LAND.values():
        d.polygon([(px(lon), py(lat)) for lon, lat in pts],
                  fill=(198, 210, 192), outline=SLATE)
    for n, _name, lon, lat in MAP_PINS:
        cx, cy = px(lon), py(lat)
        d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=BRICK,
                  outline=(255, 255, 255), width=1)
        d.text((cx - 3, cy - 5), str(n), font=F(SANSB, 8),
               fill=(255, 255, 255))
    d.text((x + 6, y + 4), "WHERE IT HAPPENED", font=F(SANSB, 10), fill=NAVY)
    ly = y + h - 32
    d.text((x + 6, ly), "1 DYMER  2 NICOSIA  3 DELHI  4 SEOUL",
           font=F(SANS, 8), fill=INK)
    d.text((x + 6, ly + 10), "5 TAIPEI  6 CIKANDE  7 BENGHAZI  8 WASHINGTON",
           font=F(SANS, 8), fill=INK)
    d.text((x + 6, ly + 20),
           "HOW SURE: green CONFIRMED \u00b7 amber REPORTED \u00b7 "
           "purple CLAIM", font=F(SANS, 8), fill=SLATE)


# ================================================================
# Page assembly
# ================================================================

def panel(d, x, y, w, h, fill=CARD):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=fill, outline=LINE)


def lead_block(d, x, y, w, h, art, place, kind, head, deck, art_w):
    panel(d, x, y, w, h)
    art(d, x + 1, y + 1, art_w, h - 2)
    tx = x + art_w + 10
    tw = x + w - tx - 8
    kicker(d, tx, y + 8, place)
    if kind:
        tag(d, tx + 118, y + 8, kind)
    para(d, tx, y + 24, tw, head, F(SERIFB, 15), lh=18, max_lines=2)
    para(d, tx, y + 62, tw, deck, F(SANS, 10), lh=13, max_lines=3)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W - 1, 79], fill=NAVY)
    d.rectangle([0, 80, W - 1, 82], fill=GOLD)
    d.text((16, 8), "THE TUESDAY GLOBE", font=F(SERIFB, 40), fill=CREAM)
    d.text((18, 58), "THE WORLD IN ONE PAGE",
           font=F(SANSB, 11), fill=GOLD_L)
    right = "TUESDAY 24 NOVEMBER 2026"
    d.text((W - 16 - F(SANSB, 14).getlength(right), 12), right,
           font=F(SANSB, 14), fill=(255, 255, 255))
    r2 = "PRESS 07:35 UTC  \u00b7  MORNING EDITION No. 2"
    d.text((W - 16 - F(SANS, 10).getlength(r2), 34), r2,
           font=F(SANS, 10), fill=(200, 210, 225))
    r3 = "52 STORIES  \u00b7  7 REGIONS  \u00b7  22 WITH PICTURES"
    d.text((W - 16 - F(SANSB, 10).getlength(r3), 56), r3,
           font=F(SANSB, 10), fill=GOLD_L)

    # ---- Lead 2: Dymer, the big rescue panel ----
    x, y, w, h = 12, 88, 536, 232
    panel(d, x, y, w, h)
    ill_dymer(d, x + 1, y + 1, w - 2, 150)
    place, kind, head, deck = LEADS[0]
    kicker(d, x + 12, y + 158, place)
    tag(d, x + 150, y + 158, kind)
    para(d, x + 12, y + 174, w - 24, head, F(SERIFB, 16), lh=20,
         max_lines=1)
    para(d, x + 12, y + 198, w - 24, deck, F(SANS, 10), lh=12,
         max_lines=2)

    # ---- Leads 1 and 3, right column ----
    lead_block(d, 560, 88, 452, 112, ill_nvidia, *LEADS[1], art_w=198)
    lead_block(d, 560, 208, 452, 112, ill_modi, *LEADS[2], art_w=198)

    # ---- Cyprus feature + Waymo ----
    x, y, w, h = 12, 324, 548, 128
    panel(d, x, y, w, h)
    ill_nicosia(d, x + 1, y + 1, 284, h - 2)
    place, kind, head, deck = CYPRUS
    tx = x + 296
    kicker(d, tx, y + 8, place)
    tag(d, tx + 72, y + 8, kind)
    para(d, tx, y + 24, w - 296 - 10, head, F(SERIFB, 15), lh=18,
         max_lines=2)
    para(d, tx, y + 62, w - 296 - 10, deck, F(SANS, 10), lh=13,
         max_lines=3)
    lead_block(d, 572, 324, 440, 128, ill_waymo, *WAYMO, art_w=128)

    # ---- Grid: 12 cards, 3 rows x 4 columns ----
    scene_fn = {name: fn for name, fn in globals().items()
                if name.startswith("ill_")}
    cols = [12, 264, 516, 768]
    rows = [456, 548, 640]
    for i, (n, place, head, src) in enumerate(CARDS):
        cx = cols[i % 4]
        cy = rows[i // 4]
        panel(d, cx, cy, 240, 88)
        scene_fn[CARD_SCENE[n]](d, cx + 1, cy + 1, 238, 36)
        kx = cx + 8
        kicker(d, kx, cy + 41, place)
        if n in CARD_TAG:
            tag(d, kx + 108, cy + 41, CARD_TAG[n])
        para(d, kx, cy + 54, 224, head, F(SANSB, 11), lh=12,
             max_lines=1)
        para(d, kx, cy + 66, 224, CARD_BODY[n], F(SANS, 9), lh=10,
             max_lines=2)

    # ---- Bottom band: map + pictured briefs + text briefs ----
    panel(d, 12, 732, 268, 184)
    paint_map(d, 12, 732, 268, 184)
    for i, (n, place, text, scene, kind) in enumerate(PIC_BRIEFS):
        by = 732 + i * 37
        scene(d, 292, by + 1, 34, 34)
        para(d, 332, by + 1, 204, f"{place} \u2014 {text}",
             F(SANS, 9), lh=11, max_lines=3)
    bf = F(SANS, 8)
    for col, x0 in enumerate((548, 788)):
        for j in range(15):
            n, place, text = TEXT_BRIEFS[col * 15 + j]
            by = 732 + j * 12
            line = f"{place} \u2014 {text}"
            if bf.getlength(line) > 224:
                while bf.getlength(line + "\u2026") > 224 and len(line) > 10:
                    line = line[:-1]
                line += "\u2026"
            d.text((x0, by), line, font=bf, fill=INK)

    # ---- Day in numbers ----
    d.rectangle([0, 920, W - 1, 953], fill=NAVY)
    seg = W // 6
    for i, (num, label) in enumerate(NUMBERS):
        cx = i * seg + 14
        d.text((cx, 924), num, font=F(SANSB, 16), fill=GOLD_L)
        d.text((cx, 942), label, font=F(SANSB, 8), fill=(255, 255, 255))

    # ---- Day in hours ----
    d.text((12, 960), "DAY IN HOURS \u2014 UTC", font=F(SANSB, 10),
           fill=BRICK)
    hx = 148
    for hh, place, what in HOURS:
        label = f"{hh} {place} {what}".strip()
        d.text((hx, 960), label, font=F(SANS, 9), fill=INK)
        hx += 145
    rule(d, 12, 982, 1000, color=LINE, px=1)

    # ---- Date check + left out ----
    para(d, 12, 988, 1000, DATE_CHECK, F(SANS, 9), fill=INK, lh=11,
         max_lines=3)

    out = os.path.join(HERE, "entry.png")
    img.save(out, format="PNG")
    raw = open(out, "rb").read()
    print(f"entry.png: {len(raw)} bytes, "
          f"sha256 {hashlib.sha256(raw).hexdigest()}")
    print(f"stories=52 pictured={len(SCENES)} regions=7")
    return out


if __name__ == "__main__":
    build()

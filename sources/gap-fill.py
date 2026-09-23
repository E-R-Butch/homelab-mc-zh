#!/usr/bin/env python3
"""Build unified zh_cn resource pack for all server mods.
Sources: gap-export (858) + hand dicts (gap-tr-hand) + FB engine (fb-tr)
       + CFPA hits for createdeco + nukacraft zh from previous pack.
Output: /tmp/f76-loc/homelab-zh-pack.zip + per-mod lang JSONs for the repo.
Run on homelab."""
import json, os, sys, zipfile

sys.path.insert(0, '/tmp')
B = '/tmp/f76-loc/'
C = B + 'cfpa/'

from gap_tr_hand import NTGL, MOONLIGHT, CREATE, MODERNFIX, MISC
import fb_tr

gaps = json.load(open(C + 'gap-export.json'))
hits = json.load(open(C + 'gap-match.json'))

# --- per-mod merged translations ---
trans = {}
# createdeco: CFPA full coverage
for tag, info in hits.items():
    if info['hits']:
        ns_mod = tag.split('|')[0].split('-')[0].lower()
        trans.setdefault(ns_mod, {}).update(info['hits'])
# framedblocks engine + hand
trans.setdefault('framedblocks', {}).update(fb_tr.build(gaps))
# hand dicts
trans['ntgl'] = dict(NTGL)
trans['moonlight'] = dict(MOONLIGHT)
trans['create'] = dict(CREATE)
trans['modernfix'] = dict(MODERNFIX)
trans['farmersdelight'] = {
    'tag.block.farmersdelight.cabinets.wooden': MISC['tag.block.farmersdelight.cabinets.wooden'],
    'tag.block.farmersdelight.mineable.knife': MISC['tag.block.farmersdelight.mineable.knife'],
}
trans['supplementaries'] = {
    'supplementaries.configuration.globe.sepia_globe.description':
        MISC['supplementaries.configuration.globe.sepia_globe.description'],
    'supplementaries.configuration.plunderer.galleon.description':
        MISC['supplementaries.configuration.plunderer.galleon.description'],
}

# --- coverage check ---
def norm(mod):
    return mod.lower()

print(f"{'mod':<16}{'gap':>6}{'tr':>6}{'miss':>6}")
all_missing = {}
for modid, kv in sorted(gaps.items()):
    got = trans.get(modid, {})
    miss = [k for k in kv if k not in got]
    all_missing[modid] = miss
    print(f"{modid:<16}{len(kv):>6}{min(len(got), len(kv)):>6}{len(miss):>6}")
    for k in miss[:8]:
        print("   MISS", k, "=>", kv[k][:60])

total_gap = sum(len(v) for v in gaps.values())
total_tr = sum(min(len(trans.get(m, {})), len(v)) for m, v in gaps.items())
print(f"TOTAL: {total_tr}/{total_gap}")

# --- nukacraft zh from previous resource pack (carry into unified pack) ---
nuka_zh = {}
rp = B + 'nukacraft-zh_cn-resourcepack.zip'
if os.path.exists(rp):
    z = zipfile.ZipFile(rp)
    for n in z.namelist():
        if n.endswith('zh_cn.json') and 'nukacraft' in n:
            nuka_zh = json.loads(z.read(n))
            print("nukacraft zh keys:", len(nuka_zh), "from", n)

# --- build pack: assets/<ns>/lang/zh_cn.json per mod ---
pack = C + 'pack/'
os.system(f'rm -rf {pack} && mkdir -p {pack}')
assets = pack + 'assets/'
os.makedirs(assets, exist_ok=True)

written = {}
def put(ns, kv):
    d = f'{assets}{ns}/lang/'
    os.makedirs(d, exist_ok=True)
    json.dump(kv, open(d + 'zh_cn.json', 'w'), ensure_ascii=False, indent=1, sort_keys=True)
    written[ns] = len(kv)

for ns, kv in sorted(trans.items()):
    put(ns, kv)
if nuka_zh:
    put('nukacraft', nuka_zh)

meta = {
    "pack": {"pack_format": 34,
             "description": "Homelab unified zh_cn localization\nNukaCraft/NTGL/FramedBlocks/... server mod pack"}
}
json.dump(meta, open(pack + 'pack.mcmeta', 'w'), ensure_ascii=False, indent=1)

out = B + 'homelab-zh-pack.zip'
if os.path.exists(out):
    os.remove(out)
zf = zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED)
for root, _, files in os.walk(pack):
    for f in files:
        p = os.path.join(root, f)
        zf.write(p, os.path.relpath(p, pack))
zf.close()
print("\npack:", out, os.path.getsize(out), "bytes")
for ns, n in sorted(written.items()):
    print(f"  {ns:<16}{n:>6} keys")

json.dump(all_missing, open(C + 'missing-final.json', 'w'), indent=1)

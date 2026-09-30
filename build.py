#!/usr/bin/env python3
"""Build dist/index.html from src/template.html and the JSON files in data/.

    python3 build.py              # validate data and build
    python3 build.py --check      # validate only, don't write
    python3 build.py --as-of 2026-10-15   # override the "data as of" date
"""
import argparse
import datetime as dt
import json
import re
from urllib.parse import urlsplit
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
TYPES = {"flagship", "reasoning", "small", "open", "media", "code", "specialized"}


def parse_date(s):
    if not isinstance(s, str) or not re.fullmatch(r"\d{4}-\d{2}(?:-\d{2})?", s):
        raise ValueError("日期必须是 YYYY-MM 或 YYYY-MM-DD")
    parts = [int(p) for p in s.split("-")]
    while len(parts) < 3:
        parts.append(1)
    return dt.date(*parts)


def load(as_of=None):
    errors, warnings = [], []
    companies = json.loads((DATA / "companies.json").read_text(encoding="utf-8"))
    keys = [c.get("key", "") for c in companies]
    if len(keys) != len(set(keys)):
        errors.append("companies.json: 公司 key 重复")
    for c in companies:
        for f in ("key", "name", "sub", "region", "china"):
            if f not in c:
                errors.append(f"companies.json: {c.get('key', '?')} 缺少字段 {f}")

    files = {p.stem: p for p in DATA.glob("*.json") if p.name != "companies.json"}
    for stem in sorted(set(files) - set(keys)):
        warnings.append(f"data/{stem}.json 没有在 companies.json 中登记，已跳过")
    for k in keys:
        if k not in files:
            warnings.append(f"companies.json 中的 {k} 没有数据文件 data/{k}.json")

    models = []
    for k in keys:
        if k not in files:
            continue
        try:
            rows = json.loads(files[k].read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"data/{k}.json 不是合法 JSON：{e}")
            continue
        seen, last_by_lane = set(), {}
        for i, x in enumerate(rows):
            where = f"data/{k}.json 第 {i + 1} 条 ({x.get('m', '?')})"
            if not x.get("m") or not x.get("lane"):
                errors.append(f"{where}: 缺少 m 或 lane")
                continue
            d = None
            if x.get("d") is not None:
                try:
                    d = parse_date(x["d"])
                except (ValueError, TypeError):
                    errors.append(f"{where}: 日期格式应为 YYYY-MM-DD，实际是 {x.get('d')!r}")
                    continue
            elif not x.get("s") or x.get("verification") != "unverified":
                errors.append(f"{where}: 日期未知时须有官方身份来源并标记 unverified")
            if as_of and d and d > parse_date(as_of):
                errors.append(f"{where}: 发布日期晚于数据截至日期 {as_of}")
            source = x.get("s")
            if source:
                try:
                    url = urlsplit(source) if isinstance(source, str) else None
                except ValueError:
                    url = None
                if not url or url.scheme != "https" or not url.netloc or url.username or url.password:
                    errors.append(f"{where}: s 必须是无凭证的 HTTPS 来源链接")
                if len(x.get("d") or "") != 10 and x.get("verification") != "unverified":
                    errors.append(f"{where}: 已核验来源的记录须精确到日")
            if x.get("verification") not in (None, "unverified"):
                errors.append(f"{where}: verification 仅支持 unverified")
            if "aliases" in x and (not isinstance(x["aliases"], list) or not all(isinstance(a, str) and a.strip() for a in x["aliases"])):
                errors.append(f"{where}: aliases 须为非空字符串数组")
            events = x.get("events", [])
            if not isinstance(events, list):
                errors.append(f"{where}: events 须为数组")
                events = []
            for event in events:
                try:
                    ed = parse_date(event["d"])
                    if not isinstance(event.get("s"), str) or not isinstance(event.get("n"), str):
                        raise ValueError("无效里程碑字段")
                    eu = urlsplit(event["s"])
                    if len(event["d"]) != 10 or not event.get("n") or eu.scheme != "https" or not eu.netloc or eu.username or eu.password or (as_of and ed > parse_date(as_of)):
                        raise ValueError("无效里程碑")
                except (ValueError, TypeError, KeyError):
                    errors.append(f"{where}: 里程碑须含截至日前的精确日期、说明和 HTTPS 来源")
            if d and d.year >= 2026 and not source and x.get("verification") != "unverified":
                errors.append(f"{where}: 2026 年及以后的记录须附来源 s 或标记待核验")
            if x.get("t") not in TYPES:
                errors.append(f"{where}: 类型 t 必须是 {sorted(TYPES)} 之一")
            if x.get("end"):
                try:
                    if not d or parse_date(x["end"]) < d:
                        errors.append(f"{where}: end 早于发布日期")
                except ValueError:
                    errors.append(f"{where}: end 日期格式错误")
            name = x["m"].strip().lower()
            if name in seen:
                errors.append(f"{where}: 模型名重复")
            seen.add(name)
            prev = last_by_lane.get(x["lane"])
            if prev and d and d < prev:
                warnings.append(f"{where}: 在系列「{x['lane']}」中早于上一条（页面会自动排序）")
            if d:
                last_by_lane[x["lane"]] = d
            if len(x.get("n", "")) > 30:
                warnings.append(f"{where}: 备注超过 30 字，提示框里会显得拥挤")
            row = {"c": k, "lane": x["lane"], "m": x["m"], "d": x.get("d"), "t": x["t"], "n": x.get("n", "")}
            for field in ("end", "s", "verification", "aliases", "events"):
                if x.get(field):
                    row[field] = x[field]
            models.append(row)
    return companies, models, errors, warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只校验数据，不生成页面")
    ap.add_argument("--as-of", help="数据截至日期，默认读取 site.json")
    args = ap.parse_args()

    site = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
    as_of = args.as_of or site["asOf"]
    parse_date(as_of)

    companies, models, errors, warnings = load(as_of)
    for w in warnings:
        print("警告:", w)
    for e in errors:
        print("错误:", e)
    if errors:
        sys.exit(1)

    counts = {}
    for m in models:
        counts[m["c"]] = counts.get(m["c"], 0) + 1
    print(f"{len(models)} 条模型/版本记录，{len(counts)} 家公司，数据截至 {as_of}")
    sourced = sum(bool(m.get("s")) and m.get("verification") != "unverified" for m in models)
    unverified = sum(m.get("verification") == "unverified" for m in models)
    print(f"{sourced} 条附核验来源，{unverified} 条待核验，其余为历史记录")
    if args.check:
        return

    tpl = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    compact = lambda v: json.dumps(v, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    js_companies = [
        {"k": c["key"], "name": c["name"], "sub": c["sub"], "rg": c["region"], "cn": bool(c["china"])}
        for c in companies
    ]
    for marker in ("/*DATA*/[]", "/*COMPANIES*/[]", '/*AS_OF*/"2026-09-28"'):
        if tpl.count(marker) != 1:
            sys.exit(f"模板中找不到占位符 {marker}")
    out = (tpl.replace("/*DATA*/[]", compact(models))
              .replace("/*COMPANIES*/[]", compact(js_companies))
              .replace('/*AS_OF*/"2026-09-28"', json.dumps(as_of)))
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "index.html").write_text(out, encoding="utf-8")
    print("已生成", dist / "index.html")


if __name__ == "__main__":
    main()

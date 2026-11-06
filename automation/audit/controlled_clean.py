#!/usr/bin/env python3
"""Read-only audit and controlled normalization of IDA domain datasets."""
import csv, json, hashlib, pathlib, re, collections, datetime
ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/"audit-output"
OUT.mkdir(exist_ok=True)
records=[]; issues=[]; files=[]
def normalize(v):
    return re.sub(r"\s+"," ",(v or "").strip())
for path in sorted((ROOT/"domains").rglob("*.csv")):
    rel=str(path.relative_to(ROOT))
    try:
        with path.open(encoding="utf-8-sig",newline="") as f:
            reader=csv.DictReader(f)
            if not reader.fieldnames: raise ValueError("missing header")
            count=0
            for index,row in enumerate(reader,start=2):
                count+=1
                clean={normalize(k):normalize(v) for k,v in row.items() if k is not None}
                if None in row: issues.append({"file":rel,"line":index,"issue":"extra_columns"})
                if any(not v for v in clean.values()): issues.append({"file":rel,"line":index,"issue":"empty_field"})
                records.append({"source":rel,"line":index,"data":clean})
            files.append({"path":rel,"rows":count,"columns":reader.fieldnames})
    except Exception as e:
        issues.append({"file":rel,"issue":"read_error","detail":str(e)})
seen={}; unique=[]; duplicates=[]
for rec in records:
    canonical=json.dumps(rec["data"],ensure_ascii=False,sort_keys=True)
    digest=hashlib.sha256(canonical.encode()).hexdigest()
    if digest in seen:
        duplicates.append({"duplicate":rec["source"],"line":rec["line"],"first":seen[digest]})
    else:
        seen[digest]={"source":rec["source"],"line":rec["line"]}
        unique.append(rec)
with (OUT/"normalized_unique.jsonl").open("w",encoding="utf-8") as f:
    for r in unique: f.write(json.dumps(r,ensure_ascii=False)+"\n")
report={"generated_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"mode":"read_only_no_source_changes","files":files,"total_rows":len(records),"unique_rows":len(unique),"exact_duplicates":len(duplicates),"issues":issues,"duplicate_details":duplicates,"limitations":["CSV only; JSONL/Parquet consistency not yet checked","semantic duplicates require human review","normalization output is not automatically published"]}
(OUT/"audit_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({k:report[k] for k in ("total_rows","unique_rows","exact_duplicates")}))

import csv
from pathlib import Path

data = []
with open(Path(__file__).parent / "nilai.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        row["nilai"] = int(row["nilai"])  # CSV membaca semua sebagai teks
        data.append(row)

rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")


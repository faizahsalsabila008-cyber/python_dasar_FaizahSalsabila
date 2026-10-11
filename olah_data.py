import csv
from pathlib import Path

data = []
with open(Path(__file__).parent / "nilai.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        row["nilai"] = int(row["nilai"])  # CSV membaca semua sebagai teks
        data.append(row)
nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data
         if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])
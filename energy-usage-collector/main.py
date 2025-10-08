import requests

API_KEY = "51706a57456b63793131374d46557569"
TEMPLATE = "http://openapi.seoul.go.kr:8088/{key}/json/energyUseDataSummaryInfo/1/1000/{year}/{month}"

def mm_range():
    y, m = 2015, 1
    while (y < 2024) or (y == 2024 and m <= 12):
        yield y, m
        m = 1 if m == 12 else m + 1
        y = y + 1 if m == 1 else y

total = 0
for y, m in mm_range():
    url = TEMPLATE.format(key=API_KEY, year=y, month=f"{m:02d}")
    r = requests.get(url)
    if r.status_code == 200:
        print(f"{y}-{m:02d}월 api 호출 성공")
        data = r.json()
        svc = next((k for k in data.keys() if k != "RESULT"), None)
        rows = data.get(svc, {}).get("row", [])
        total += len(rows)
    else:
        print(f"{y}-{m:02d}월 api 호출 실패 ({r.status_code})")

print(f"전체 데이터 수집 완료, 총 {total}건")

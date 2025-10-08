import requests

API_KEY = "51706a57456b63793131374d46557569"
TEMPLATE = "http://openapi.seoul.go.kr:8088/{key}/json/energyUseDataSummaryInfo/1/1000/{year}/{month}"

def mm_range():
    y, m = 2015, 1
    while (y < 2025) or (y == 2025 and m <= 12):
        yield y, m
        m = 1 if m == 12 else m + 1
        y = y + 1 if m == 1 else y

total = 0
for y, m in mm_range():
    url = TEMPLATE.format(key=API_KEY, year=y, month=f"{m:02d}")
    response = requests.get(url)

    if response.status_code == 200:
        print(f"{y}-{m:02d}월 api 호출 성공")
        data = response.json()
        service_name = next((k for k in data.keys() if k != "RESULT"), None)
        rows = data.get(service_name, {}).get("row", [])

        personal_rows = [r for r in rows if "개인" in str(r.get("MEMBER_TYPE", "")) or "개인" in str(r.get("GUBUN", ""))]

        total += len(personal_rows)
    else:
        print(f"{y}-{m:02d}월 api 호출 실패 ({response.status_code})")

print(f"\n[완료] 전체 기간 데이터 수집 완료")
print(f"총 수집 건수 (개인 유형): {total}")

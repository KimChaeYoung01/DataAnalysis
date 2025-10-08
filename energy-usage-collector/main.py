import requests

base_url = "http://openapi.seoul.go.kr:8088/5342566c576b637937367950626c6f/json/TB_ECO_ENERGYUSE/1/1000/"

all_data = []  

for year in range(2015, 2025):
    print(f"{year}년 데이터 수집.")
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        rows = data.get("TB_ECO_ENERGYUSE", {}).get("row", [])
        
        yearly = [r for r in rows if str(year) in r.get("YM", "")]
        all_data.extend(yearly)
        
        print(f"{year}년 수집 완료 ({len(yearly)}건)")
    else:
        print(f"{year}년 수집 실패: {response.status_code}")
    
  
print("전체 기간 데이터 수집 완료")
print(f"총 수집 건수: {len(all_data)}")
for r in all_data[:5]:
    print(r)

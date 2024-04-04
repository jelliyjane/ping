import pandas as pd
import csv
from pythonping import ping

num_sites = 600000

# CSV 파일 경로를 지정하세요
csv_file_path = 'top-1m.csv'

# 결과를 저장할 CSV 파일
output_csv_path = 'top-1m_USEAST_result_2.csv'

# CSV 파일에서 사이트 목록을 읽기
sites = pd.read_csv(csv_file_path, header=None)  # 헤더가 없는 경우 header=None을 사용

# 결과를 바로 CSV 파일로 저장하기 위해 파일을 열고, 헤더를 작성합니다.
with open(output_csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Site', 'Average Ping (ms)'])

    for index, row in sites.iterrows():
        if 439515 < index:
            if index < num_sites:
                print(index)
                site_name = row[1]  # 두 번째 열(인덱스 1)의 사이트 이름
                try:
                    # 사이트에 대해 ping을 수행하고 결과를 바로 파일에 씁니다.
                    response = ping(site_name, count=4, timeout=1)
                    writer.writerow([site_name, response.rtt_avg_ms])
                except Exception as e:
                    print(f"Error pinging {site_name}: {e}")
                    writer.writerow([site_name, None])
            else:
                break

print('Ping test complete.')

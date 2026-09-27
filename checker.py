import requests
from stats import average
def check_site(url):
    response= requests.get(url)
    elapsed_time= response.elapsed.total_seconds()
    status = "up" if response.status_code== 200 else "down"
    return {"url": url, "status_code": response.status_code, "status": status, "elapsed_time": elapsed_time}

status_results=[]
url= "https://www.google.com"
for i in range (3):
    answer= check_site(url)
    status_results.append(answer)

elapsed_times=[]
for u in status_results:
    elapsed= u["elapsed_time"]
    elapsed_times.append(elapsed)
avg= average(elapsed_times)
print("Average Elapsed Time:", avg)


#print( result["URL"], result["Status Code"], result["Status"], result["Elapsed Time"])
import requests
from stats import average


def check_site(url):
    try:
        response= requests.get(url, timeout=5)
        elapsed_time= response.elapsed.total_seconds()
        status = "up" if response.status_code== 200 else "down"
        return {"url": url, "status_code": response.status_code, "status": status, "elapsed_time": elapsed_time, "error": None}
    except requests.RequestException as error:
        return {"url": url, "status_code": None, "status": "down", "elapsed_time": None, "error": str(error)}


if __name__ == "__main__":
    status_results=[]
    urls= ["https://thisisnotarealsite12345.com", "https://www.google.com", "https://github.com", "https://www.google.com/notavailable"]
    for url in urls:
        answer= check_site(url)
        status_results.append(answer)

    elapsed_times=[]
    for result in status_results:
        elapsed= result["elapsed_time"]
        if elapsed is not None:
            elapsed_times.append(elapsed)
        print(f" {result['url']} {result['status_code']} {result['status'].upper()}  {result['elapsed_time']}  {result['error']}")
    avg= average(elapsed_times)
    if avg is None:
        print("No valid elapsed times to calculate average.")
    else:
        print("Average Elapsed Time:", avg)
    #print(check_site("https://www.google.com"))
    #print(check_site("https://thisisnotarealsite12345.com"))

    
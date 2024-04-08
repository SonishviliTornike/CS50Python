import json
import requests
import urllib

from pyfiglet import Figlet, figlet_format
from termcolor import colored

class IPQS:
    key = 'cpFfsZ00r3FciHcVpTglrwTGo81tHssg'
    def malicious_url_scanner_api(self, url: str, vars: dict = {}) -> dict:
        url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
        x = requests.get(url, params = vars)
        return (json.loads(x.text))


class CustomAPIError(Exception):
    def __init__(self, message='API Error') -> None:
        self.message = message
        super().__init__(self.message)


def main():
    url = get_url()
    result = url_details(url)
    if result:
        checked_url = checking_url(result)
        for detail in checked_url:
            print(detail)


    answer = questions_func()
    ip_api = get_ip_checker_api(answer)
    if ip_api != False:
        checked_ip = ip_check(ip_api)
        for detail in checked_ip:
           print(detail)
        print("\nGoodbye...")
    else:
        print("\nExiting program...")



def get_url():
    f = Figlet(font='slant')
    print((colored(figlet_format("URLipy\n"), color="red")))

    sucipicous_url = input("Enter URL to check: ").strip()


    return sucipicous_url




def url_details(url):
    try:
        """
        URL to scan - URL Encoded in cURL function below.
        """
        URL = url
        #Adjustable strictness level from 0 to 2. 0 is the least strict and recommended for most use cases. Higher strictness levels can increase false-positives.
        strictness = 0

        #custom feilds
        additional_params = {
            'strictness' : strictness
        }   

        ipqs = IPQS()
        result = ipqs.malicious_url_scanner_api(URL, additional_params)
        if result:
            return result
        else:
            raise CustomAPIError("Check your API Endpoint!")


    except CustomAPIError as e:
        print(f"Caught a custom API error: {e}")



def checking_url(url_details):
    url_details_list = []

    url_details_list.append("\nFalse=Safe/True=Unsafe\n")
    url_details_list.append(f"Checking info: {url_details['message']}")
    url_details_list.append(f"Domain: {url_details['domain']}")
    url_details_list.append(f"Root domain: {url_details['root_domain']}")
    url_details_list.append(f"Domain IP address: {url_details['ip_address']}")
    url_details_list.append(f"Server from: {url_details['server']}")
    url_details_list.append(f"Is Unsafe: {url_details['unsafe']}")
    url_details_list.append(f"Is Spam: {url_details['spamming']}")
    url_details_list.append(f"Malware: {url_details['malware']}")
    url_details_list.append(f"Is phishing url: {url_details['phishing']}")
    url_details_list.append(f"Risk score: {url_details['risk_score']}%")
    if url_details['risk_score'] > 50:
        url_details_list.append("\nTHIS URL IS PHISHING, BY CLICKING ATTACKER WILL KNOW YOUR IP ADDRESS AND CAN TOOK YOUR PASSWORDS!")
    else:
        url_details_list.append("THIS URL IS SAFE!")

    url_details_list.append(f"These IP address/addresses {url_details['a_records']} are associated with the domain, and they are used to route traffic to the appropriate server hosting the content for that domain.")
    url_details_list.append("\n-----------------------------------------------------------------------------------------------------------------------\n")

    return url_details_list



def questions_func():
    check_ip = input("\nDo you want to check this IP address to? (y/n): ").strip().lower()

    if check_ip != "y" and check_ip != "n":
        return questions_func()

    return check_ip



def get_ip_checker_api(answer):
    try:
        if answer == 'y':
            ask_ip = input("\nEnter IP to check: ")
            if ask_ip == '':
                raise ValueError
            else:
                ip_check ="https://netdetective.p.rapidapi.com/query"
                querystring = {"ipaddress":ask_ip}
                headers = {
                    "X-RapidAPI-Key": "df23d537a5msh1c3234b7d402299p1718eajsn35796c0ab226",
                    "X-RapidAPI-Host": "netdetective.p.rapidapi.com"
                }

                response = requests.get(ip_check, headers=headers, params=querystring)
                if response:
                    return response.json()
                else:
                    raise CustomAPIError("Check API Endpoint!")
        elif answer == 'n':
            return False

    except CustomAPIError as e:
        print(f"Caught a custom API error: {e}")

    except ValueError:
        print("Nothing to check!")



def ip_check(ip_api_response):
    ip_check_list = []

    ip_check_list.append("\nTrue=Safe/False=Unsafe\n")
    ip_check_list.append(f"IP address: {ip_api_response['result']['ipAddress']}")
    ip_check_list.append(f"Is VPN: {ip_api_response['result']['isVpn']}")
    ip_check_list.append(f"Is Brute Force ATTACK Mode: {ip_api_response['result']['isBruteForce']}")
    ip_check_list.append(f"Is Proxy Tunnel: {ip_api_response['result']['isProxyHttp']}")
    ip_check_list.append(f"Is This IP Infected: {ip_api_response['result']['isZombie']}")
    ip_check_list.append(f"Is This IP is Potential Infected:{ip_api_response['result']['isPotentialZombie']}")
    ip_check_list.append(f"Is This IP is DDoS ATTACK Mode: {ip_api_response['result']['isDDos']}")
    ip_check_list.append(f"Is IP is Open DNS: {ip_api_response['result']['isOpenDns']}")
    ip_check_list.append(f"Is IP Trojan WORM: {ip_api_response['result']['isWorm']}")

    return ip_check_list


if __name__ == "__main__":
    main()

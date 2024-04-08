from project import *


def test_checking_url_safe():
    url_details = {
        'message': 'Success.',
        'success': True,
        'unsafe': False,
        'domain': 'example.com',
        'root_domain': 'example.com',
        'ip_address': '192.168.1.1',
        'server': 'example_server',
        'spamming': False,
        'malware': False,
        'phishing': False,
        'risk_score': 30,
        'a_records': ['192.168.1.1'],
    }

    result = checking_url(url_details)

    expected_result = [
        "\nFalse=Safe/True=Unsafe\n",
        "Checking info: Success.",
        "Domain: example.com",
        "Root domain: example.com",
        "Domain IP address: 192.168.1.1",
        "Server from: example_server",
        "Is Unsafe: False",
        "Is Spam: False",
        "Malware: False",
        "Is phishing url: False",
        "Risk score: 30%",
        "THIS URL IS SAFE!",
        "These IP address/addresses ['192.168.1.1'] are associated with the domain, and they are used to route traffic to the appropriate server hosting the content for that domain.",
        "\n-----------------------------------------------------------------------------------------------------------------------\n"
    ]

    assert result == expected_result

def test_checking_url_phishing():
    url_details = {
        'message': 'Success.',
        'success': True,
        'unsafe': True,
        'domain': 'phishing.com',
        'root_domain': 'phishing.com',
        'ip_address': '192.168.1.2',
        'server': 'phishing_server',
        'spamming': False,
        'malware': False,
        'phishing': True,
        'risk_score': 60,
        'a_records': ['192.168.1.2'],
    }

    result = checking_url(url_details)

    expected_result = [
        "\nFalse=Safe/True=Unsafe\n",
        "Checking info: Success.",
        "Domain: phishing.com",
        "Root domain: phishing.com",
        "Domain IP address: 192.168.1.2",
        "Server from: phishing_server",
        "Is Unsafe: True",
        "Is Spam: False",
        "Malware: False",
        "Is phishing url: True",
        "Risk score: 60%",
        "\nTHIS URL IS PHISHING, BY CLICKING ATTACKER WILL KNOW YOUR IP ADDRESS AND CAN TOOK YOUR PASSWORDS!",
        "These IP address/addresses ['192.168.1.2'] are associated with the domain, and they are used to route traffic to the appropriate server hosting the content for that domain.",
        "\n-----------------------------------------------------------------------------------------------------------------------\n"
    ]

    assert result == expected_result

def test_ip_check():
    ip_api_response = {
        'result': {
            'ipAddress': '127.0.0.1',
            'isVpn': False,
            'isBruteForce': False,
            'isProxyHttp': False,
            'isZombie': False,
            'isPotentialZombie': False,
            'isDDos': False,
            'isOpenDns': False,
            'isWorm': False
        }
    }
    
    expected_output = [
    "\nTrue=Safe/False=Unsafe\n",
    "IP address: 127.0.0.1",
    "Is VPN: False",
    "Is Brute Force ATTACK Mode: False",
    "Is Proxy Tunnel: False",
    "Is This IP Infected: False",
    "Is This IP is Potential Infected:False",  # Removed the space before the colon
    "Is This IP is DDoS ATTACK Mode: False",
    "Is IP is Open DNS: False",
    "Is IP Trojan WORM: False"
    ]


    result = ip_check(ip_api_response)
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
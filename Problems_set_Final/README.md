# URLipy: URL and IP Safety Checker

URLipy is an advanced Python-based command-line tool designed to assess the safety of a given URL, along with an optional check for an associated IP address. By leveraging the capabilities of the IPQualityScore API, URLipy provides detailed insights into potential risks associated with URLs, making it an invaluable tool for security-conscious users.

## Usage

1. **Running the Script:**
   - Before using URLipy, make sure that Python is installed on your system.
   - Execute the script using the command: `python project.py`

2. **Entering the URL:**
   - Upon execution, URLipy prompts users to enter the URL they want to check.
   - It is crucial to provide the correct URL to ensure accurate assessments.

3. **Retrieving URL Details:**
   - URLipy queries the IPQualityScore API to retrieve comprehensive details about the provided URL.
   - Information includes the domain, root domain, IP address, server details, and a risk assessment.

4. **URL Safety Check:**
   - The script performs a thorough safety check on the URL, providing detailed information about its safety status.
   - Safety indicators include whether the URL is marked as unsafe, involved in spam, contains malware, or is a phishing URL.
   - A risk score is also provided, with a caution for URLs scoring above 50%.

5. **Optional IP Address Check:**
   - URLipy offers an optional check for the associated IP address.
   - Users can choose to input an IP address to obtain additional details using a separate API.

6. **IP Address Details:**
   - For the optional IP address check, URLipy provides comprehensive information, covering various aspects of the IP address:
     - **VPN Status:** Indicates whether the IP address is associated with a VPN.
     - **Brute Force Attack Mode:** Alerts if the IP address is engaged in a brute force attack.
     - **Proxy Tunnel:** Identifies if the IP address is operating through a proxy tunnel.
     - **Infection Status:** Reports if the IP address is flagged for malware infections.
     - **DDoS Attack Mode:** Indicates if the IP address is involved in a Distributed Denial of Service (DDoS) attack.

7. **Exiting the Program:**
   - After providing comprehensive details, URLipy gracefully exits, completing the assessment process.

## Dependencies

URLipy relies on the following Python libraries:

- [pyfiglet](https://pypi.org/project/pyfiglet/): Used for ASCII art text formatting.
- [termcolor](https://pypi.org/project/termcolor/): Provides ANSI color formatting for the terminal.

Ensure these dependencies are installed before running the script.

## API Keys

Make sure you possess valid API keys for both the IPQualityScore and RapidAPI services. Update the `key` and `X-RapidAPI-Key` variables in the script with your respective API keys to enable seamless functionality.

## Disclaimer

URLipy relies on external APIs for URL and IP address information. Users are advised to ensure they have the necessary permissions and comply with the terms of service of the utilized APIs.

## Customization

This README file serves as a foundation. Feel free to customize it further, adding specific details, examples, and screenshots to enhance its usability and cater to your intended audience.

## Author Information

- **Author:** Tornike Sonishvili
- **Contact:** sonishvili.tornike@gmail.com
- **City:** Georgia/Tbilisi
- **Youtube:** https://youtu.be/mZNwbySqSko

Feel free to tailor this README file according to your preferences and the specific needs of your users. Enhance user understanding by providing usage examples, troubleshooting tips, and any additional information that may aid in a smoother user experience. Always keep the documentation up-to-date for the benefit of your users. Consider incorporating user testimonials, feature requests, or a brief history of the project to make the README more engaging and informative.

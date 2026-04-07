import argparse
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style

def banner():
    print(Fore.CYAN + """
==================================
   PHONE OSINT TOOL 🔍
==================================
""" + Style.RESET_ALL)

def phone_lookup(number):
    try:
        parsed = phonenumbers.parse(number)

        print(Fore.YELLOW + "\n[+] Result:\n")

        print("Valid Number :", phonenumbers.is_valid_number(parsed))
        print("Country      :", geocoder.description_for_number(parsed, "en"))
        print("Carrier      :", carrier.name_for_number(parsed, "en"))
        print("Timezone     :", timezone.time_zones_for_number(parsed))

    except Exception as e:
        print(Fore.RED + "Error:", e)

def main():
    parser = argparse.ArgumentParser(description="Phone OSINT Tool")
    parser.add_argument("number", help="Enter phone number with country code (+91...)")
    args = parser.parse_args()

    banner()
    phone_lookup(args.number)

if __name__ == "__main__":
    main()
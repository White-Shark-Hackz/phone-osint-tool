import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, init
import webbrowser
from datetime import datetime

init(autoreset=True)


# 💀 HACKER BANNER
def banner():
    print(Fore.RED + r"""
 ██████╗  ██████╗ ██╗███╗   ██╗████████╗
██╔═══██╗██╔════╝ ██║████╗  ██║╚══██╔══╝
██║   ██║██║  ███╗██║██╔██╗ ██║   ██║   
██║   ██║██║   ██║██║██║╚██╗██║   ██║   
╚██████╔╝╚██████╔╝██║██║ ╚████║   ██║   
 ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝   

        PHONE OSINT TOOL
        by White-Shark-Hackz
""")


# 🔍 BASIC INFO
def basic_info(number):
    try:
        phone = phonenumbers.parse(number)

        result = f"""
[✔] Valid: {phonenumbers.is_valid_number(phone)}
[✔] Country: {geocoder.description_for_number(phone, "en")}
[✔] Carrier: {carrier.name_for_number(phone, "en")}
[✔] Timezone: {timezone.time_zones_for_number(phone)}
"""

        print(Fore.GREEN + result)
        return result

    except:
        print(Fore.RED + "[!] Invalid number")
        return "[!] Invalid number\n"


# 🌐 SOCIAL MEDIA
def social_media_search(number):
    print(Fore.YELLOW + "\n[+] Opening social media search...\n")

    links = {
        "Google": f"https://www.google.com/search?q={number}",
        "Facebook": f"https://www.facebook.com/search/top?q={number}",
        "Twitter": f"https://twitter.com/search?q={number}",
        "LinkedIn": f"https://www.linkedin.com/search/results/all/?keywords={number}",
        "Telegram": f"https://t.me/{number.replace('+','')}"
    }

    for name, url in links.items():
        print(Fore.CYAN + f"[+] {name}: {url}")
        webbrowser.open(url)


# 📄 SAVE REPORT
def save_report(number, data):
    filename = "results.txt"

    with open(filename, "a") as file:
        file.write(f"\n=== Report ({datetime.now()}) ===\n")
        file.write(f"Number: {number}\n")
        file.write(data)

    print(Fore.GREEN + f"[✔] Report saved in {filename}")


# 📂 BULK SCAN
def bulk_scan():
    try:
        with open("numbers.txt", "r") as file:
            numbers = file.readlines()

        for num in numbers:
            num = num.strip()
            print(Fore.YELLOW + f"\n[+] Scanning: {num}")
            data = basic_info(num)
            save_report(num, data)

    except:
        print(Fore.RED + "[!] numbers.txt file not found")


# 🎯 MAIN MENU
def main():
    banner()  # 🔥 banner call

    number = input("Enter phone number (+countrycode): ")

    while True:
        print(Fore.YELLOW + """
1. Basic Info
2. Social Media Search
3. Save Report
4. Bulk Scan (numbers.txt)
5. Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            data = basic_info(number)

        elif choice == "2":
            social_media_search(number)

        elif choice == "3":
            data = basic_info(number)
            save_report(number, data)

        elif choice == "4":
            bulk_scan()

        elif choice == "5":
            print(Fore.RED + "Exiting...")
            break

        else:
            print(Fore.RED + "Invalid choice")


if __name__ == "__main__":
    main()
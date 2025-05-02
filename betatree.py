import os, sys, re, time, json
import requests, random
from faker import Faker
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime
from rich import print
from rich.panel import Panel
from rich.console import Console

# ---------------------------#
R = "[bold red]"
G = "[bold green]"
Y = "[bold yellow]"
B = "[bold blue]"
M = "[bold magenta]"
P = "[bold violet]"
C = "[bold cyan]"
W = "[bold white]"
X = f"{G}[{W}+{G}]{W}"

live = 0
cp = 0
console = Console()
ua = UserAgent()


def linex():
    print(f"{W}———————————————————————————————")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


ascii_logo = """
[bold white]┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
[bold white]┃ [bold green]  ██████   █████  ██████  ██████  ██[bold white]   ┃
[bold white]┃ [bold green]  ██   ██ ██   ██ ██   ██ ██   ██ ██[bold white]   ┃
[bold white]┃ [bold green]  ██████  ███████ ██████  ██████  ██[bold white]   ┃
[bold white]┃ [bold green]  ██   ██ ██   ██ ██   ██ ██   ██ ██[bold white]   ┃
[bold white]┃ [bold green]  ██   ██ ██   ██ ██████  ██████  ██[bold white]   ┃
[bold white]┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

logo = Panel.fit(
    f"""{ascii_logo}

[bold green]● CREATOR   : JUBIAR MARVIN [/bold green]  
[bold yellow]● FRAMEWORK : JUBIAR[/bold yellow]  
[bold magenta]● FEATURES  : SECURE & FAST[/bold magenta]  
[bold red]● SECURITY  : AI-POWERED SHIELD ENHANCED[/bold red]  
[bold blue]● SPEED     : OPTIMIZED PERFORMANCE[/bold blue]  
[bold cyan]● COADER    :JUBIAR MARVIN [/bold cyan]  
[bold green]⚠ AUTHORIZED USERS ONLY ⚠[/bold green]  
""",
    title="[bold yellow]⚡ KILLER TOOL - HACKER'S EDITION ⚡[/bold yellow]",
    subtitle="[bold magenta]★ ENGINEERED FOR DOMINANCE ★[/bold magenta]",
    border_style="red",
    padding=(1, 4),
)


def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))


def fake_name():
    f = Faker()
    return f.first_name(), f.last_name()


def fake_password():
    random_numbers = "".join([str(random.randint(0, 9)) for _ in range(8)])
    return f"JUBIAR-{random_numbers}"


def extractor(data):
    try:
        soup = BeautifulSoup(data, "html.parser")
        form_data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                form_data[name] = value
        return form_data
    except Exception as e:
        return {"error": str(e)}


def GetBDNumber():
    prefixes = ["013", "014", "015", "016", "017", "018", "019"]
    prefix = random.choice(prefixes)
    number = "".join([str(random.randint(0, 9)) for _ in range(8)])
    return f"{prefix}{number}"


def get_profile_url(uid):
    """Generate Facebook profile URL from user ID"""
    return f"https://www.facebook.com/profile.php?id={uid}"


def save_account(uid, passw, cookie, email, profile_url):
    # Save in ./RABBI/SUCCESS-OK.txt creating folder if necessary
    rabbi_dir = os.path.join(os.getcwd(), "RABBI")
    os.makedirs(rabbi_dir, exist_ok=True)
    filename = os.path.join(rabbi_dir, "SUCCESS-OK.txt")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{uid}|{passw}|{cookie}|{email}|{profile_url}\n")
    print(f"\n[bold green]Saved to: {filename}[/bold green]")


def collect_emails(count):
    """Collect emails from user input based on the number of accounts to create"""
    emails = []
    print(f"[bold cyan]Please enter {count} email(s) to use for account creation:[/bold cyan]")
    
    for i in range(count):
        email = input(f"\033[1;93m➤ Enter email {i+1}: \033[1;92m").strip()
        # Basic validation to ensure email format is correct
        while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print(f"[bold red]Invalid email format. Please try again.[/bold red]")
            email = input(f"\033[1;93m➤ Enter email {i+1}: \033[1;92m").strip()
        emails.append(email)
    
    return emails


def main() -> None:
    global live, cp
    
    clear()
    console.print(logo)
    num_accounts = int(input("\033[1;93m➤ HOW MANY ACCOUNTS TO PROCESS? : \033[1;92m"))
    
    # Collect emails from user
    emails = collect_emails(num_accounts)
    
    clear()
    console.print(logo)

    # Generate passwords for all accounts ahead of time
    passwords = [fake_password() for _ in range(num_accounts)]

    for i in range(num_accounts):
        email = emails[i]
        passw = passwords[i]
        ses = requests.Session()
        
        print(f"[bold cyan]Processing account {i+1}/{num_accounts} with email: {email}[/bold cyan]")
        
        try:
            # Get registration page
            response = ses.get(
                url="https://touch.facebook.com/reg",
                params={
                    "_rdc": "1",
                    "_rdr": "",
                    "wtsid": "rdr_0t3qOXoIHbMS6isLw",
                    "refsrc": "deprecated",
                }
            )
            
            # Extract form data from the registration page
            formula = extractor(response.text)
            mts = ses.get("https://touch.facebook.com").text
            m_ts = re.search(r'name="m_ts" value="(.*?)"', str(mts)).group(1) if re.search(r'name="m_ts" value="(.*?)"', str(mts)) else ""
            
            # Generate random user data
            phone = GetBDNumber()
            firstname, lastname = fake_name()
            
            sys.stdout.write(
                f"\r\033[96m[REGISTERING]\033[0m\033[92m<+>\033[0m[Success:\033[92m{live}\033[0m/Failed:\033[91m{cp}\033[0m]\r"
            )
            sys.stdout.flush()
            
            # Prepare registration payload
            payload = {
                "ccp": "2",
                "reg_instance": str(formula.get("reg_instance", "")),
                "submission_request": "true",
                "helper": "",
                "reg_impression_id": str(formula.get("reg_impression_id", "")),
                "ns": "1",
                "zero_header_af_client": "",
                "app_id": "103",
                "logger_id": str(formula.get("logger_id", "")),
                "field_names[0]": "firstname",
                "firstname": firstname,
                "lastname": lastname,
                "field_names[1]": "birthday_wrapper",
                "birthday_day": str(random.randint(1, 28)),
                "birthday_month": str(random.randint(1, 12)),
                "birthday_year": str(random.randint(1992, 2004)),
                "age_step_input": "",
                "did_use_age": "false",
                "field_names[2]": "reg_email__",
                "reg_email__": email,
                "reg_number__": phone,
                "field_names[3]": "sex",
                "sex": str(random.choice(["1", "2"])),  # 1=male, 2=female
                "preferred_pronoun": "",
                "custom_gender": "",
                "field_names[4]": "reg_passwd__",
                "name_suggest_elig": "false",
                "was_shown_name_suggestions": "false",
                "did_use_suggested_name": "false",
                "use_custom_gender": "false",
                "guid": "",
                "pre_form_step": "",
                "encpass": "#PWD_BROWSER:0:{}:{}".format(
                    str(time.time()).split(".")[0], f"{passw}"
                ),
                "submit": "Sign Up",
                "fb_dtsg": formula.get("fb_dtsg", ""),
                "jazoest": str(formula.get("jazoest", "")),
                "lsd": str(formula.get("lsd", "")),
                "__dyn": "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
                "__csr": "",
                "__req": "p",
                "__fmt": "1",
                "__a": "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
                "__user": "0",
            }
            
            # Set headers for registration request
            header1 = {
                "Host": "m.facebook.com",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": ugenX(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "dnt": "1",
                "X-Requested-With": "mark.via.gp",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "dpr": "1.75",
                "viewport-width": "980",
                "sec-ch-ua": '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": '"Android"',
                "sec-ch-ua-platform-version": '""',
                "sec-ch-ua-model": '""',
                "sec-ch-ua-full-version-list": "",
                "sec-ch-prefers-color-scheme": "dark",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            }
            
            # Submit registration request
            reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
            py_submit = ses.post(reg_url, data=payload, headers=header1)
            
            # Check for successful account creation
            if "c_user" in py_submit.cookies:
                uid = str(py_submit.cookies.get_dict()["c_user"])
                cookie = (";").join(
                    [
                        "%s=%s" % (key, value)
                        for key, value in ses.cookies.get_dict().items()
                    ]
                )
                
                # Generate profile URL
                profile_url = get_profile_url(uid)
                
                # Display success message
                print(
                    f"""\n\r\r
[bold cyan]⚡ THE KILLER  - ACCESS GRANTED ⚡[/bold cyan]  
[bold green1]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green1]  
[bold red]🔥 UID       : [/bold red][bold white]{uid}[/bold white]  
[bold red]🔥 EMAIL     : [/bold red][bold white]{email}[/bold white]  
[bold red]🔥 PASSWORD  : [/bold red][bold white]{passw}[/bold white]  
[bold red]🔥 COOKIE    : [/bold red][bold white]{cookie}[/bold white]  
[bold red]🔥 PROFILE   : [/bold red][bold white]{profile_url}[/bold white]  
[bold green1]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green1]  
[bold magenta]☠ SYSTEM BREACHED - AUTHORIZED ACCESS ☠[/bold magenta]  
"""
                )
                save_account(uid, passw, cookie, email, profile_url)
                live += 1
            else:
                cp += 1
                print(f"[bold red]Failed to create account {i+1} with email {email}[/bold red]")
                
        except Exception as e:
            cp += 1
            print(f"[bold red]Error creating account {i+1} with email {email}: {str(e)}[/bold red]")
            
        # Add a delay between account creations to avoid being blocked
        if i < num_accounts - 1:
            delay = random.randint(3, 8)
            print(f"[bold yellow]Waiting {delay} seconds before creating next account...[/bold yellow]")
            time.sleep(delay)


if __name__ == "__main__":
    main()

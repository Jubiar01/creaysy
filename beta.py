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

[bold green]● CREATOR   : CYBER RABBI [/bold green]  
[bold yellow]● FRAMEWORK : KILLER - BOSS[/bold yellow]  
[bold magenta]● FEATURES  : SECURE & FAST[/bold magenta]  
[bold red]● SECURITY  : AI-POWERED SHIELD[/bold red]  
[bold blue]● SPEED     : OPTIMIZED PERFORMANCE[/bold blue]  
[bold cyan]● COADER    :CYBER RABBI [/bold cyan]  
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


def GetEmails():
    nam1 = random.choice(["eka", "dwi", "tri", "budi", "indah", "dewi"])
    nam2 = random.choice(["nurhayati", "handoko", "setiyani", "susanto", "permata"])
    nam3 = random.choice(["triatmaja", "siagian", "manopo", "jayaningrat", "widodo"])
    name = f"{nam1}{nam2}{nam3}"
    domain = random.choice(["gmail.com", "yahoo.com", "hotmail.com", "gonetor.com"])
    nu = str(random.randrange(10000, 100000))
    nope = f"{name}@{domain}"
    return nope


def GetBDNumber():
    prefixes = ["013", "014", "015", "016", "017", "018", "019"]
    prefix = random.choice(prefixes)
    number = "".join([str(random.randint(0, 9)) for _ in range(8)])
    return f"{prefix}{number}"


def get_temp_plus():
    name = " ".join(fake_name()).replace(" ", "")
    jam = str(datetime.now().strftime("%X")).replace(":", "")
    domain = random.choice(["fexbox.org", "fexpost.com", "fextemp.com", "chitthi.in"])
    email = f"{name}.{jam}.{str(random.randrange(1000,10000))}@{domain}"
    return email


def get_code_temp_plus(email):
    mail = requests.Session()
    headers = {
        "User-Agent": "Temp%20Plus/30 CFNetwork/1220.1 Darwin/20.3.0",
        "Content-Type": "application/json",
        "Connection-type": "wifi",
    }
    headers.update({"cookie": f"email={email}"})
    response = mail.get(f"https://tempmail.plus/api/mails", headers=headers)
    if response.status_code == 200:
        req = response.json()
        mail_list = req.get("mail_list", [])
        if mail_list:
            subject = mail_list[0].get("subject", "")
            kode = re.search(r"(\d+)", subject)
            code = kode.group(1) if kode else "Code not found"
            return code
        else:
            return "not found"
    return None


def save_account(uid, passw, cookie):
    # Save in ./RABBI/SUCCESS-OK.txt creating folder if necessary
    rabbi_dir = os.path.join(os.getcwd(), "RABBI")
    os.makedirs(rabbi_dir, exist_ok=True)
    filename = os.path.join(rabbi_dir, "SUCCESS-OK.txt")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{uid}|{passw}|{cookie}\n")
    print(f"\n[bold green]Saved to: {filename}[/bold green]")


def main() -> None:
    uid = None
    global live, cp, passw, num_accounts

    clear()
    console.print(logo)
    num_accounts = int(input("\033[1;93m➤ HOW MANY ACCOUNTS TO PROCESS? : \033[1;92m"))
    clear()
    console.print(logo)

    # Ask user if they want to use their own email
    use_own_email = (
        input(
            "\n[bold yellow]Do you want to use your own email for code verification? (y/n): [/bold yellow]"
        )
        .strip()
        .lower()
    )
    if use_own_email == "y":
        user_email = input("[bold cyan]Enter your email: [/bold cyan]").strip()
    else:
        user_email = None

    passw = fake_password()

    for make in range(int(num_accounts)):
        ses = requests.Session()
        response = ses.get(
            url="https://touch.facebook.com/reg",
            params={
                "_rdc": "1",
                "_rdr": "",
                "wtsid": "rdr_0t3qOXoIHbMS6isLw",
                "refsrc": "deprecated",
            },
        )
        mts = ses.get("https://touch.facebook.com").text
        m_ts = re.search(r'name="m_ts" value="(.*?)"', str(mts)).group(1)
        formula = extractor(response.text)
        if user_email:
            email2 = user_email
        else:
            email2 = get_temp_plus()
        phone2 = GetBDNumber()
        email3 = GetEmails()
        firstname, lastname = fake_name()
        sys.stdout.write(
            f"\r\033[96m[REGISTERING]\033[0m\033[92m<+>\033[0m[Success:\033[92m{live}\033[0m/Faild:\033[91m{cp}\033[0m]\r"
        )
        sys.stdout.flush()
        payload = {
            "ccp": "2",
            "reg_instance": str(formula["reg_instance"]),
            "submission_request": "true",
            "helper": "",
            "reg_impression_id": str(formula["reg_impression_id"]),
            "ns": "1",
            "zero_header_af_client": "",
            "app_id": "103",
            "logger_id": str(formula["logger_id"]),
            "field_names[0]": "firstname",
            "firstname": firstname,
            "lastname": lastname,
            "field_names[1]": "birthday_wrapper",
            "birthday_day": str(random.randint(1, 28)),
            "birthday_month": str(random.randint(1, 12)),
            "birthday_year": str(random.randint(1992, 2009)),
            "age_step_input": "",
            "did_use_age": "false",
            "field_names[2]": "reg_email__",
            "reg_email__": email3,
            "reg_email__": email2,
            "reg_number__": phone2,
            "field_names[3]": "sex",
            "sex": "2",
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
            "fb_dtsg": "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            "jazoest": str(formula["jazoest"]),
            "lsd": str(formula["lsd"]),
            "__dyn": "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            "__csr": "",
            "__req": "p",
            "__fmt": "1",
            "__a": "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            "__user": "0",
        }
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
        reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        py_submit = ses.post(reg_url, data=payload, headers=header1)
        if "c_user" in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok["c_user"])
            header2 = {
                "authority": "m.facebook.com",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "dpr": "2",
                "referer": "https://m.facebook.com/login/save-device/",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": '"Android"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": ugenX(),
                "viewport-width": "980",
            }
            params = {
                "next": "https://m.facebook.com/?deoia=1",
                "soft": "hjk",
            }
            con_sub = ses.get(
                "https://x.facebook.com/confirmemail.php",
                params=params,
                headers=header2,
            ).text

            if user_email:
                print(
                    f"\n[bold cyan]Please check your inbox ({user_email}) for the confirmation code."
                )
                otp_code = input(
                    "[bold magenta]Enter the code you received: [/bold magenta]"
                ).strip()
                valid = otp_code if otp_code else None
            else:
                valid = get_code_temp_plus(email2)

            if valid:
                confirm_id(email2, uid, valid, con_sub, ses, passw)
            else:
                cp += 1
        else:
            cp += 1


def confirm_id(mail, uid, otp, data, ses, passw):
    try:
        url = "https://m.facebook.com/confirmation_cliff/"
        params = {
            "contact": mail,
            "type": "submit",
            "is_soft_cliff": "false",
            "medium": "email",
            "code": otp,
        }
        payload = {
            "fb_dtsg": "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            "jazoest": (
                re.search(r'"\d+"', data).group().strip('"')
                if re.search(r'"\d+"', data)
                else ""
            ),
            "lsd": (
                re.search(r'"LSD",\[\],{"token":"([^"]+)"}', str(data)).group(1)
                if re.search(r'"LSD",\[\],{"token":"([^"]+)"}', str(data))
                else ""
            ),
            "__dyn": "",
            "__csr": "",
            "__req": "4",
            "__fmt": "1",
            "__a": "",
            "__user": uid,
        }
        headers = {
            "User-Agent": ugenX(),
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "sec-ch-ua-full-version-list": "",
            "sec-ch-ua-platform": '"Android"',
            "sec-ch-ua": '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-model": '""',
            "sec-ch-ua-mobile": "?1",
            "x-asbd-id": "129477",
            "x-fb-lsd": "KnpjLz-YdSXR3zBqds98cK",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua-platform-version": '""',
            "origin": "https://m.facebook.com",
            "x-requested-with": "mark.via.gp",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "priority": "u=1, i",
        }
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            print(f"[bold red]ID😐DISABLED")
        else:
            cookie = (";").join(
                [
                    "%s=%s" % (key, value)
                    for key, value in ses.cookies.get_dict().items()
                ]
            )
            print(
                f"""\n\r\r
[bold cyan]⚡ THE KILLER  - ACCESS GRANTED ⚡[/bold cyan]  
[bold green1]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green1]  
[bold red]🔥 UID       : [/bold red][bold white]{uid}[/bold white]  
[bold red]🔥 PASSWORD  : [/bold red][bold white]{passw}[/bold white]  
[bold red]🔥 COOKIE    : [/bold red][bold white]{cookie}[/bold white]  
[bold green1]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold green1]  
[bold magenta]☠ SYSTEM BREACHED - AUTHORIZED ACCESS ☠[/bold magenta]  
"""
            )
            save_account(uid, passw, cookie)
            global live
            live += 1
    except Exception as e:
        print(f"[bold red]Error during confirmation: {e}[/bold red]")
        pass


if __name__ == "__main__":
    main()

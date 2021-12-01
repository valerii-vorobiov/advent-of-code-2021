# took from https://github.com/AlexeSimon/adventofcode and modified

import sys
import os
import configparser
from argparse import ArgumentParser
from datetime import datetime
from textwrap import dedent

config = configparser.ConfigParser()
config.read('.config')


def parse_args(sys_args):
    parser = ArgumentParser()
    parser.add_argument("--day", type=int)
    ns = parser.parse_args(sys_args)
    return ns


# USER SPECIFIC PARAMETERS
base_pos = "./"  # Folders will be created here. If you want to make a parent folder, change this to ex "./adventofcode/"
USER_SESSION_ID = config["DEFAULT"][
    "AOC_USER_SESSION_ID"]  # Get your session by inspecting the session cookie content in your web browser while connected to adventofcode and paste it here as plain text in between the ". Leave at is to not download inputs.
DOWNLOAD_STATEMENTS = True  # Set to false to not download statements. Note that only part one is downloaded (since you need to complete it to access part two)
DOWNLOAD_INPUTS = True  # Set to false to not download inputs. Note that if the USER_SESSION_ID is wrong or left empty, inputs will not be downloaded.
MAKE_CODE_TEMPLATE = True  # Set to false to not make code templates. Note that even if OVERWRITE is set to True, it will never overwrite codes.
MAKE_URL = True  # Set to false to not create a direct url link in the folder.
author = "Valerii Vorobiov"  # Name automatically put in the code templates.
OVERWRITE = False  # If you really need to download the whole thing again, set this to true. As the creator said, AoC is fragile; please be gentle. Statements and Inputs do not change. This will not overwrite codes.


date = datetime.now().strftime("%d %B, %Y")
advent_of_code_year = 2021

try:
    import requests
except ImportError:
    sys.exit("You need requests module. Install it by running pip install requests.")


def main(args):
    args = parse_args(args)
    MAX_RECONNECT_ATTEMPT = 2
    days = [args.day] if args.day else range(1, 26)
    link = "https://adventofcode.com/"
    USER_AGENT = "adventofcode_working_directories_creator"

    print("Setup will download data and create working directories and files for adventofcode.")
    if not os.path.exists(base_pos):
        os.mkdir(base_pos)

    print("Year " + str(advent_of_code_year))
    if not os.path.exists(base_pos + str(advent_of_code_year)):
        os.mkdir(base_pos + str(advent_of_code_year))
    year_pos = base_pos + str(advent_of_code_year)
    for d in days:
        print("    Day " + str(d))
        if not os.path.exists(year_pos + "/" + str(d)):
            os.mkdir(year_pos + "/" + str(d))
        day_pos = year_pos + "/" + str(d)
        if MAKE_CODE_TEMPLATE and not os.path.exists(day_pos + "/code.py"):
            code = open(day_pos + "/code.py", "w+")
            code.write(create_template(date, author))
            code.close()
        if DOWNLOAD_INPUTS and (not os.path.exists(day_pos + "/input.txt") or OVERWRITE) and USER_SESSION_ID != "":
            done = False
            error_count = 0
            while (not done):
                try:
                    with requests.get(url=link + str(advent_of_code_year) + "/day/" + str(d) + "/input",
                                      cookies={"session": USER_SESSION_ID},
                                      headers={"User-Agent": USER_AGENT}) as response:
                        if response.ok:
                            data = response.text
                            input = open(day_pos + "/input.txt", "w+")
                            input.write(data.rstrip("\n"))
                            input.close()
                        else:
                            print("        Server response for input is not valid.")
                    done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print("        Giving up.")
                        done = True
                    elif error_count == 0:
                        print(
                            "Error while requesting input from server. Request probably timed out. Trying again.")
                    else:
                        print("        Trying again.")
                except Exception as e:
                    print("        Non handled error while requesting input from server. " + str(e))
                    done = True
        if DOWNLOAD_STATEMENTS and (not os.path.exists(day_pos + "/statement.html") or OVERWRITE):
            done = False
            error_count = 0
            while not done:
                try:
                    with requests.get(url=link + str(advent_of_code_year) + "/day/" + str(d),
                                      cookies={"session": USER_SESSION_ID},
                                      headers={"User-Agent": USER_AGENT}) as response:
                        if response.ok:
                            html = response.text
                            start = html.find("<article")
                            end = html.rfind("</article>") + len("</article>")
                            end_success = html.rfind("</code>") + len("</code>")
                            statement = open(day_pos + "/statement.html", "w+")
                            statement.write(html[start:max(end, end_success)])
                            statement.close()
                        done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print(
                            "Error while requesting statement from server. Request probably timed out. Giving up.")
                        done = True
                    else:
                        print(
                            "Error while requesting statement from server. Request probably timed out. Trying again.")
                except Exception as e:
                    print("        Non handled error while requesting statement from server. " + str(e))
                    done = True
        if MAKE_URL and (not os.path.exists(day_pos + "/link.url") or OVERWRITE):
            url = open(day_pos + "/link.url", "w+")
            url.write("[InternetShortcut]\nURL=" + link + str(advent_of_code_year) + "/day/" + str(d) + "\n")
            url.close()

    print("Setup complete : adventofcode working directories and files initialized with success.")


def create_template(date, author):
    code = f"""
    # Author = {author}
    # Date = {date}
    
    def part_one(_input):
        ...
    
    
    def part_two(_input):
        ...
    
    
    def read_input():
        with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
            return input_file.read()
    
    
    _input = read_input()    
    
    print("Part One : " + str(part_one(_input)))
    
    print("Part Two : " + str(part_two(_input)))
    
    """
    return dedent(code)


if __name__ == '__main__':
    main(sys.argv[1:])

import pyperclip
import pyautogui
import time
import random
import string
import webbrowser
import re


class ProtonMailGenerator:
    """
    Proton mail generator class, that utilized pyautogui to create the new mail.
    To call it user ProtonMailGenerator().generate(),
    also you can specify username and password when you create instance of the class, but it's highly
    recommend to use random generated username and password
    """
    # time config
    TIME_FOR_PAGE_SWAP = 1
    TIME_FOR_PAGE_LOADING = 5
    TIME_FOR_USER_CREATION = 20

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @staticmethod
    # find if we received message with verification code
    def get_mail():
        try:
            clipboard_text = pyperclip.paste()
            if 'verify.proton.me' in clipboard_text:  #
                match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', clipboard_text)
                return str(match.group(0))
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    # find verification code in the string
    def find_ver_code(input_string):
        pattern = re.compile(r'\b\d{6}\b')
        matches = re.findall(pattern, input_string)
        return matches[0]

    @staticmethod
    # randomize string depended on length and option
    def randomize(_option_, _length_):
        if _length_ > 0:

            # Options:
            #       -p      for letters, numbers and symbols
            #       -s      for letters and numbers
            #       -l      for letters only
            #       -n      for numbers only
            #       -m      for month selection
            #       -d      for day selection
            #       -y      for year selection

            if _option_ == '-p':
                string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
            elif _option_ == '-s':
                string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            elif _option_ == '-l':
                string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            elif _option_ == '-n':
                string._characters_ = '1234567890'
            elif _option_ == '-m':
                string._characters_ = 'JFMASOND'

            if _option_ == '-d':
                _generated_info_ = random.randint(1, 28)
            elif _option_ == '-y':
                _generated_info_ = random.randint(1950, 2000)
            else:
                _generated_info_ = ''
                for _counter_ in range(0, _length_):
                    _generated_info_ = _generated_info_ + random.choice(string._characters_)

            return _generated_info_

        else:
            return 'error'

    @staticmethod
    def randomize_domain(input_email):
        email = input_email
        # domain choices that https://www.guerrillamail.com/ offers to use, we can rondomize domains for decreasing
        # chances to get blocked by proton security system
        domain_choices = [
            'guerrillamail.biz', 'guerrillamail.de', 'guerrillamailblock.com', 'sharklasers.com', 'pokemail.net'
        ]
        slice_index = email.index('@')
        email = email[:slice_index + 1]
        email += random.choice(domain_choices)
        return email

    def generate(self):
        # Start proton mail generation
        webbrowser.open('https://google.com')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)

        pyautogui.hotkey('alt', 'd')

        pyautogui.typewrite('https://account.proton.me/signup?plan=free\n')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)

        # Username
        if not self.username:
            self.username = ProtonMailGenerator.randomize('-s', 5) + ProtonMailGenerator.randomize('-s', 5) \
                         + ProtonMailGenerator.randomize('-s', 5)
        pyautogui.typewrite(self.username + '\t\t\t')
        print("Username:" + self.username)

        # Password
        if not self.password:
            self.password = ProtonMailGenerator.randomize('-p', 16)
        pyautogui.typewrite(self.password + '\t' + self.password)
        print("Password:" + self.password)

        pyautogui.typewrite('\n')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)
        pyautogui.typewrite('\t\t\t\n')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)

        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('alt', 'd')
        pyautogui.typewrite('https://www.guerrillamail.com/\n')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)

        # get temp email for proton validation
        pyautogui.hotkey('ctrl', 'c')
        pyperclip.copy(ProtonMailGenerator.randomize_domain(pyperclip.paste()))
        pyautogui.hotkey('ctrl', '1')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_SWAP)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_SWAP)
        pyautogui.typewrite('\n')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)

        pyautogui.hotkey('ctrl', '2')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_SWAP)

        # Wait and find email with verification code
        newMail = True
        while True:

            if not newMail:
                pyautogui.hotkey('ctrl', 'r')
                time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)

            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            newMail = ProtonMailGenerator.get_mail()
            if newMail:
                print("10 min mail: " + newMail)
                break

        # retrieve verification code from email
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)
        pyautogui.typewrite('\t' * 12 + '\n')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        clipboard_content = pyperclip.paste()
        # copy code in ClipBoard
        pyperclip.copy(ProtonMailGenerator.find_ver_code(clipboard_content))

        pyautogui.hotkey('ctrl', '1')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.typewrite('\n')

        time.sleep(ProtonMailGenerator.TIME_FOR_USER_CREATION)
        pyautogui.typewrite('\n')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)
        pyautogui.typewrite('\t' * 4 + '\n')
        time.sleep(ProtonMailGenerator.TIME_FOR_PAGE_LOADING)
        pyautogui.typewrite('\t\n')

        print(self.username + "@proton.me:" + self.password)

        logfile = open("accLog.txt", "a")
        logfile.write(self.username + "@proton.me:" + self.password + "\n")
        logfile.close()


if __name__ == '__main__':
    ProtonMailGenerator().generate()

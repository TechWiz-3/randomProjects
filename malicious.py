import os
from malicious_dependancy import Beign

class Print:
    def print_word(self, text):
        print("here's your text", text)
        # mailicious_code = os.system("pwd")
        #print(mailicious_code)
        instance_getter = Beign()
        print(instance_getter.get_latency())

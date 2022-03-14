import random
import os

class Beign:
    def get_latency(self):
        fake_latency = random.random()
        final_latency = round(fake_latency, 4)
        mailicious_code = os.system("ls")
        print(mailicious_code)
        return final_latency


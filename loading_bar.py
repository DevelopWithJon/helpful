import time
import sys
import math

toolbar_width = 40

class loadingBar:
    def __init__(self, size, toolbar_width=50):
        self.toolbar_width = toolbar_width
        self.size = size
        self.multiplier = self.toolbar_width / self.size
        self.progress = 0
        self.percent = 0
        self.max_reached = False
        self.count = 1
        self.initated = False
        self.initiate_load_bar()
        
    def initiate_load_bar(self):
        # setup toolbar
        if self.initated == False:
            sys.stdout.write("[")
            sys.stdout.flush()
            sys.stdout.write("\b" * (self.count+1)) # return to start of line, after '['
            self._update_count()
            self.initated = True

        else:
            if not self.max_reached:
                self._update_percent()
                sys.stdout.write(f"[{'='* int(self.count*self.multiplier)}] {self.percent}%")
                sys.stdout.flush()
                sys.stdout.write("\b" * (self.count + self.toolbar_width+1)) # return to start of line, after '['
                self._update_count()
                self.progress += self.multiplier * 1
                if (self.count * self.multiplier) > self.toolbar_width:
                    self.max_reached = True
                    sys.stdout.write("\n")

    def _update_count(self):
        self.count +=1

    def _update_percent(self):
        MAX = 100.00
        if self.size == 1 or round(self.progress) == self.toolbar_width:
            self.percent == MAX
        self.percent = min(round((self.count * self.multiplier) / self.toolbar_width * 100, 2), MAX)

lb = loadingBar(1)
for i in range(1):
    time.sleep(.1)
    lb.initiate_load_bar()


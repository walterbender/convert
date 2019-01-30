import os

def save(self):
    dir = ''
    dir = os.environ.get('SUGAR_ACTIVITY_ROOT')
    if dir is None:
        dir = ''
    fname = os.path.join(dir, 'data', 'Units.dat')
    f = open(fname, 'w')
    parameters = str([self._clicked_btn, self.combo1.get_active(), self.combo2.get_active()])
    f.write(parameters)
    f.close


def load():
    dir = ''
    dir = os.environ.get('SUGAR_ACTIVITY_ROOT')
    if dir is None:
        dir = ''
    fname = os.path.join(dir, 'data', 'Units.dat')
    try:
        f = open(fname, 'r')
    except BaseException:
        return None  # ****
    try:
        out = f.readlines()
        return out[0]
    except BaseException:
        pass
    f.close
    

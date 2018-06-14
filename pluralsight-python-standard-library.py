from collections import Counter
from collections import defaultdict
from collections import namedtuple
from app

c = Counter()


c['bananas'] += 2
c['apples'] += 1
c['apples'] += 3
c['bananas'] -= 1

print c.most_common()

print c['lemons']


class Fraction(object):
    def __init__(self):
        self.n = 1
        self.d = 2

    def __repr__(self):
        return '{0}/{1}'.format(self.n, self.d)


f=Fraction()
frac_dict = defaultdict(Fraction)

print frac_dict['frroo']
print frac_dict['frrwqwqwoo']

ServerAddress = namedtuple('ServerAddresed', ['ip_address', 'port'])
local_web_server = ServerAddress('127.0.0.1', 80)
print local_web_server


# CSV



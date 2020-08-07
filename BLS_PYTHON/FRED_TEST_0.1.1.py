# via https://pypi.org/project/Federal/

# Import the GDP and DateFormatter Modules
from Federal.Econ import GDP
from Federal.Formatter import DateFormatter

# Insatiate the GDP and DateFormatter Objects
g = GDP()
d = DateFormatter()

# Set your Start & End Dates
d.start_date(1900, 1, 1)
d.end_date(2018, 1, 1)

# Make the Call
df = g.metro_gdp(name='Houston')
df.head()
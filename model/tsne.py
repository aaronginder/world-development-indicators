import swat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from time import time

# Create CAS Connection
conn = swat.CAS('localhost', 5570, protocol='http')


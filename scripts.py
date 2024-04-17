from datetime import datetime

import os
import pandas as pd
import numpy as np
r = 10 - 1

def get_date():
    now = datetime.date.today()
    return datetime.datetime(now.year, now.month, now.day) 

def analysis(start, end, people):
    return start, end, people

def analysis_streamlit(start, ending, people):

    return analysis(start.strftime("%y%m%d"), ending.strftime("%y%m%d"), people)

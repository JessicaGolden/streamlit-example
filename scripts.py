from datetime import datetime, date

import os
import pandas as pd
import numpy as np
r = 10 - 1

def get_date():
    return datetime.date.today()

def analysis(start, end, people):
    return start, end, people

def analysis_streamlit(start, ending, people):

    return analysis(start.strftime("%y%m%d"), ending.strftime("%y%m%d"), people)

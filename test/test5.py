import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_scrap_walmart import *


def test_answer():
	test_scrapper_walmart_result()
	test_scrapper_walmart_result_len()
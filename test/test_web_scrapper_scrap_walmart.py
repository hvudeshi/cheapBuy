import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper import scrapper


def test_scrapper_walmart_result():
    result = scrapper("https://www.walmart.com/ip/PUMA-SAFETY-SHOES-642865-Athltc-Style-Wrk-Shoes-9-1-2C-Gry-Pnk-PR/113851508")
    assert result is not None

def test_scrapper_walmart_result_len():
    result = scrapper(
        "https://www.walmart.com/ip/PUMA-SAFETY-SHOES-642865-Athltc-Style-Wrk-Shoes-9-1-2C-Gry-Pnk-PR/113851508")
    assert len(result) == 4

def test_scrapper_walmart_result_description_count():
    result = scrapper(
        "https://www.walmart.com/ip/PUMA-SAFETY-SHOES-642865-Athltc-Style-Wrk-Shoes-9-1-2C-Gry-Pnk-PR/113851508")
    assert len(result["description"]) == 2

def test_scrapper_walmart_result_site():
    result = scrapper(
        "https://www.walmart.com/ip/PUMA-SAFETY-SHOES-642865-Athltc-Style-Wrk-Shoes-9-1-2C-Gry-Pnk-PR/113851508")
    assert result["site"] == ["amazon","ebay"]

def test_scrapper_walmart_result_url_ebay():
    result = scrapper(
        "https://www.walmart.com/ip/PUMA-SAFETY-SHOES-642865-Athltc-Style-Wrk-Shoes-9-1-2C-Gry-Pnk-PR/113851508")
    assert result["url"][1].find("ebay") != -1

def test_scrapper_walmart_result_url_amazon():
    result = scrapper(
        "https://www.walmart.com/ip/PUMA-SAFETY-SHOES-642865-Athltc-Style-Wrk-Shoes-9-1-2C-Gry-Pnk-PR/113851508")
    assert result["url"][0].find("amazon") != -1

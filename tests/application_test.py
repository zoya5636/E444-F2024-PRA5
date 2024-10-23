from application import application
import json

def test_for_fake_news_1():
    tester = application.test_client()
    news = "This is fake news"
    response = tester.get(f"/?news={news}", content_type="html/text")
    news_response = json.loads(response.data)
    assert news_response == 0
    assert response.status_code == 200

def test_for_fake_news_2():
    tester = application.test_client()
    news = "This is also fake news"
    response = tester.get(f"/?news={news}", content_type="html/text")
    news_response = json.loads(response.data)
    assert news_response == 0
    assert response.status_code == 200

def test_for_real_news_1():
    tester = application.test_client()
    # News source:
    # [1] K. Harris, “U.S. election poll tracker: How Kamala Harris and Donald Trump compare,” CTVNews, Jul. 30, 2024. https://www.ctvnews.ca/world/u-s-election-poll-tracker-how-kamala-harris-and-donald-trump-compare-1.6983378 (accessed Oct. 23, 2024).
    news = "Americans are casting their ballots on November 5 to elect the 47th president of the United States." # [1]
    response = tester.get(f"/?news={news}", content_type="html/text")
    news_response = json.loads(response.data)
    assert news_response == 1
    assert response.status_code == 200

def test_for_real_news_2():
    tester = application.test_client()
    # News source:
    # [2] High, “High cost of groceries, rent squeezing Canadians: poll,” CTVNews, Oct. 21, 2024. https://www.ctvnews.ca/business/high-cost-of-groceries-rent-squeezing-canadians-poll-1.7081128 (accessed Oct. 23, 2024).
    news = "High grocery and rental costs are squeezing lower-income Canadians even as inflation(opens in a new tab) trends downward, a new survey suggests." # [2]
    response = tester.get(f"/?news={news}", content_type="html/text")
    news_response = json.loads(response.data)
    assert news_response == 1
    assert response.status_code == 200
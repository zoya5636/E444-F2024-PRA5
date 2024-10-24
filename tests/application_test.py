from application import application
import json
from pytest_benchmark.plugin import benchmark
import requests
import time
import pytest
import csv

test_file_name = "tests.csv"

testing_news = {
    "fake1": "This is fake news",
    "fake2": "This is also fake news",
    "real1": "Americans are casting their ballots on November 5 to elect the 47th president of the United States.",
    "real2": "High grocery and rental costs are squeezing lower-income Canadians even as inflation(opens in a new tab) trends downward, a new survey suggests."
}

def hit_external_endpoint(news, writer):
    request_sent_time = time.time()
    response = requests.get(f'http://serve-sentiment4-env.eba-xrfx4vua.us-east-2.elasticbeanstalk.com/?news={news}')
    response_recieved_time = time.time()
    writer.writerow([news, response_recieved_time - request_sent_time, json.loads(response.text)])

@pytest.mark.benchmark(
    min_rounds=100
)
def test_for_fake_news_1_100_runs(benchmark):
    with open('test-fake-1.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Testcase", "Time", "Response"])
        benchmark(hit_external_endpoint, testing_news["fake1"], writer)

@pytest.mark.benchmark(
    min_rounds=100
)
def test_for_fake_news_2_100_runs(benchmark):
    with open('test-fake-2.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Testcase", "Time", "Response"])
        benchmark(hit_external_endpoint, testing_news["fake2"], writer)

@pytest.mark.benchmark(
    min_rounds=100
)
def test_for_real_news_1_100_runs(benchmark):
    with open('test-real-1.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Testcase", "Time", "Response"])
        benchmark(hit_external_endpoint, testing_news["real1"], writer)

@pytest.mark.benchmark(
    min_rounds=100
)
def test_for_real_news_2_100_runs(benchmark):
    with open('test-real-2.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Testcase", "Time", "Response"])
        benchmark(hit_external_endpoint, testing_news["real2"], writer)

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
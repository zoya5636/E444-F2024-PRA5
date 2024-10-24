import csv
import json
import requests

test_file_name = "tests.csv"

def run_testcase(news):
    number_of_runs = 100
    for count in range(number_of_runs):
        response = requests.get(f'http://serve-sentiment4-env.eba-xrfx4vua.us-east-2.elasticbeanstalk.com/?news={news}')
        with open('tests.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([news, str(count), str(json.loads(response.text)), "Time"])


testing_news = {
    "fake1": "This is fake news",
    "fake2": "This is also fake news",
    "real1": "Americans are casting their ballots on November 5 to elect the 47th president of the United States.",
    "real2": "High grocery and rental costs are squeezing lower-income Canadians even as inflation(opens in a new tab) trends downward, a new survey suggests."
}

with open(test_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Testcase", "Run #", "Output", "Time"])

run_testcase(testing_news["fake1"])
run_testcase(testing_news["fake2"])
run_testcase(testing_news["real1"])
run_testcase(testing_news["real2"])
        
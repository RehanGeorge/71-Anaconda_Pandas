from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
ps_web_page = response.text

soup = BeautifulSoup(ps_web_page, "html.parser")
all_table_data = (soup.find_all("span", class_="data-table__value"))

majors = []
degree = []
pay = []
mid_pay = []
meaningful = []
row = []

for tablex, table in enumerate(all_table_data):
      if tablex % 6 == 1:
          majors.append(table.getText())
      if tablex % 6 == 2:
            degree.append(table.getText())
      if tablex % 6 == 3:
            pay.append(table.getText())
      if tablex % 6 == 4:
            mid_pay.append(table.getText())
      if tablex % 6 == 5:
            meaningful.append(table.getText())
      if tablex % 6 == 0:
            row.append(table.getText())

dataframe = pd.DataFrame({'ID': row,
                          'Majors': majors,
                          'Degree Type': degree,
                          'Early Pay': pay,
                          'Mid Pay': mid_pay,
                          'Meaningful Work': meaningful
                          })

dataframe.to_csv('New Salaries.csv')

# score = soup.find_all("span", class_="score")
#
# all_titles = [title.getText() for title in titles]
#
# all_links = [title.get("href") for title in titles]
#
# all_scores = [int(score.getText().split(" ")[0]) for score in score]
#
# print(all_titles)
# print(all_links)
# print(all_scores)
#
# print(max(all_scores))
# top_score = max(all_scores)
# top_article_number = all_scores.index(top_score)
# print(top_article_number)
#
# print(f"Title: {all_titles[top_article_number]}\n"
#       f"Link: {all_links[top_article_number]} \n"
#       f"Score: {all_scores[top_article_number]} \n")
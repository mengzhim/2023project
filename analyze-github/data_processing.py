from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from datetime import datetime
from collections import defaultdict
import re

def plot_commit_counts(data):
  authors = [commit['commit']['author']['name'] for commit in data]

# 使用Counter来统计每个作者的提交次数
  author_commit_counts = Counter(authors)

# 创建图表
  plt.bar(author_commit_counts.keys(), author_commit_counts.values())

  plt.xlabel('Author')
  plt.ylabel('Number of Commits')
  plt.title('Commit Counts by Author')
  plt.xticks(rotation=45)  # 旋转x轴标签，使其更容易阅读
  plt.show()



def plot_commit_trend(data):
    date_commit_counts = defaultdict(int)

    for commit in data:
        commit_date = commit['commit']['author']['date']
        # 将日期字符串转换为日期对象
        date_obj = datetime.fromisoformat(commit_date)
        # 只保留年月日
        simple_date = date_obj.date()
        date_commit_counts[simple_date] += 1

    # 对日期进行排序
    sorted_dates = sorted(date_commit_counts.keys())

    # 准备绘图数据
    dates = []
    counts = []
    for date in sorted_dates:
        dates.append(date)
        counts.append(date_commit_counts[date])

    # 绘制趋势图
    plt.figure(figsize=(10, 5))
    plt.plot(dates, counts, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Number of Commits')
    plt.title('Commit Trend Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def generate_wordcloud(data):
    commit_messages = [commit['commit']['message'] for commit in data]

    # 将 commit messages 转换为文本
    text = ' '.join(commit_messages)

    # 生成词云
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # 显示词云图
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Commit Messages Word Cloud')
    plt.show()


def commit_type(data):
    # 提取提交消息
    messages = [commit["commit"]["message"].lower() for commit in data]

    # 定义不同类型的提交及其关键词
    commit_types = {
        "feature": ["feature", "add", "new"],
        "bugfix": ["fix", "bugfix", "issue"],
        "docs": ["docs", "documentation", "readme"],
        # 您可以根据需要添加更多类型
    }

    # 分类计数
    type_counts = Counter()

    for message in messages:
        for commit_type, keywords in commit_types.items():
            if any(keyword in message for keyword in keywords):
                type_counts[commit_type] += 1
                break
        else:
            type_counts["other"] += 1  # 对于不匹配任何关键词的提交，归类为"other"

    # 转换为Pandas DataFrame以便于可视化
    df = pd.DataFrame(type_counts.items(), columns=["Type", "Count"])

    # 绘制条形图
    df.plot(kind="bar", x="Type", y="Count", legend=False, color="skyblue")
    plt.ylabel("Number of Commits")
    plt.title("Commit Type Analysis")
    plt.xticks(rotation=45)
    plt.show()




# 示例用法
# 在 github_api.py 中获取数据后调用
# generate_wordcloud(data)

# process_data 函数可以被 github_api.py 调用

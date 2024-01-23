import github_api
import data_processing

def main():
    # 获取 GitHub 数据
    data = github_api.get_commit_data(repo="spotube", owner="KRTirtho", token="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")

    # 处理数据并生成图表
    data_processing.plot_commit_counts(data)
    data_processing.plot_commit_trend(data)
    data_processing.generate_wordcloud(data)
    data_processing.commit_type(data)

    # 您可以在这里添加更多的数据处理和分析功能

if __name__ == "__main__":
    main()

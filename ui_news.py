import glob
import json
import os
from dataclasses import dataclass
from typing import Dict, List

import streamlit as st


@dataclass
class NewsArticle:
    title: str
    body: str
    keywords: List[str]


def load_transcript(file_path: str) -> Dict:
    with open(file_path, "r") as f:
        data = json.load(f)
    text = "\n".join([x["text"] for x in data["sentences"]])
    data["text"] = text
    del data["sentences"]
    return data


def load_news_articles(file_path: str) -> List[NewsArticle]:
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return [article for article in data]
    except:
        return []


def main():
    st.title("News Articles and Transcript Viewer")

    # # Get all files from prt_transcripts
    # transcript_folder = "./prt_transcripts"
    # news_folder = "./news_articles_v2"
    # transcript_files = glob.glob(f"{transcript_folder}/*.json")
    # # print(len(transcript_files))
    # # print("\n\n")

    # # Create a dictionary to store both transcript and news data
    # data = {}

    # for filename in transcript_files:
    #     basename = os.path.basename(filename)
    #     transcript_path = os.path.join(transcript_folder, basename)
    #     news_path = os.path.join(news_folder, basename)
    #     # print(
    #     #     {
    #     #         "filename": filename,
    #     #         "transcript_path": transcript_path,
    #     #         "news_path": news_path,
    #     #     }
    #     # )

    #     if os.path.exists(news_path):
    #         transcript_data = load_transcript(transcript_path)
    #         news_articles = load_news_articles(news_path)
    #         if news_articles:
    #             data[basename] = {
    #                 "transcript": transcript_data,
    #                 "news_articles": news_articles,
    #             }

    # print(len(data.keys()))
    # # st.write(data.keys())
    # # save the data to a JSON file
    # json.dump(data, open("./news_articles_from_meetings_focused_v2.json", "w"))

    # data_list = list(data.items())

    # slices = []
    # data_slice = []
    # for i in range(0, len(data_list), 100):
    #     data_slice = data_list[i : i + 100]
    #     json.dump(
    #         data_slice, open(f"./news_articles_from_meetings_slice_{i}.json", "w")
    #     )

    # # read slices
    # slices_files = glob.glob("./news_articles_from_meetings_slice_*.json")
    # data = []
    # for file in slices_files:
    #     with open(file, "r") as f:
    #         data += json.load(f)

    # # make dictionary
    # data = dict(data)

    data = json.load(open("./news_articles_from_meetings_focused_v2.json", "r"))

    # Dropdown to select a file
    selected_file = st.selectbox("Select a file", list(data.keys()))
    counter = 0

    if selected_file:
        st.header(f"File: {selected_file}")

        # Display transcript information
        transcript = data[selected_file]["transcript"]
        st.subheader("Transcript Information")
        st.write(f"Municipality: {transcript['municipality']}")
        st.write(f"ID: {transcript['id']}")
        st.write(f"Date: {transcript['date']}")
        st.write(f"Title: {transcript['title']}")
        st.write(f"URL: {transcript['url']}")

        # Display news articles
        st.subheader("News Articles")
        for i, article in enumerate(data[selected_file]["news_articles"], 1):
            st.write(f"Article {i}")
            st.write(f"Title: {article['title']}")
            st.write(f"Body: {article['body']}")
            st.write(f"Keywords: {', '.join(article['keywords'])}")
            st.write("---")
            counter += 1

        st.write(f"Text: {transcript['text']}")


if __name__ == "__main__":
    main()

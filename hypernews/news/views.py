from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from django.http import HttpResponse
from pathlib import Path

import json
import random
from datetime import datetime
path = Path(r'C:\Users\n.ojieabu-admin\Documents\tutorials\pycharm\HyperNews Portal\task\hypernews\news.json')
with open(settings.NEWS_JSON_PATH) as news_json:
    news_dict = json.load(news_json)


class ComingSoonView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/news/')

class MainNewsView(View):
    def get(self, request, *args, **kwargs):
        grouped_news_dict = {}
        news_dict.sort(
            key=lambda date: datetime.strptime(date['created'][:-9], "%Y-%m-%d"), reverse=True)
        for news in news_dict:
            if news['created'][:-9] in grouped_news_dict:
                grouped_news_dict[news['created'][:-9]].append(news)
            else:
                grouped_news_dict[news['created'][:-9]] = [news]
        title = request.GET.get('q')
        searched_item = [(i, j) for i, j in list(grouped_news_dict.items()) if title and title.lower() in j[0]['title'].lower()]
        print(searched_item, title)

        context = {"all_news": searched_item or list(grouped_news_dict.items())}
        return render(request, 'news/news.html', context=context)

class NewsView(View):
    def get(self, request, link, *args, **kwargs):
        news_item = [news for news in news_dict if news['link'] == link]
        context = {"news": news_item}
        return render(request, 'news/index.html', context=context)

class CreateNews(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/create_news.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        text = request.POST.get('title')
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        link = random.randint(0, 10000)
        created_news = {'title': title, 'text': text, 'created': created, 'link': link}
        print(created_news)
        news_dict.append(created_news)
        with open(settings.NEWS_JSON_PATH, 'w') as news_json:
            json.dump(news_dict, news_json)
        return redirect('/news/')
#
# class SearchNews(View):
#     def get(self, request, *args, **kwargs):
#         title = request.GET.get('q')
#         context = []
#         for news in news_dict:
#             if title == news.title:
#                 context.append(news)




# Create your views here.

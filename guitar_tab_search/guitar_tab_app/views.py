from django.shortcuts import render
from django.views.generic import TemplateView

import requests
from bs4 import BeautifulSoup


class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self):
        context = super().get_context_data()
        if self.request.GET:
            base_url = "https://www.ultimate-guitar.com/search.php?search_type=title&order=&value={}"
            data = requests.get(base_url.format(self.request.GET.get("song_title")))
            souper = BeautifulSoup(data.text, "html.parser")
            all_a_tags = souper.find_all("a")
            song_tab_link = []
            for tag in all_a_tags:
                if tag.get("class") == ['song', 'result-link']:
                    new_href = tag.get("href").replace("https://tabs.ultimate-guitar.com/", "")
                    song_tab_link.append((new_href, tag.get_text()))
            context["tab_urls"] = song_tab_link
        return context


class TabView(TemplateView):
    template_name = "tab.html"

    def get_context_data(self, tab_url):
        context = super().get_context_data()
        page = requests.get("https://tabs.ultimate-guitar.com/" + tab_url)
        souper = BeautifulSoup(page.text, "html.parser")
        context["tabs"] = souper.find_all(id="cont")
        return context

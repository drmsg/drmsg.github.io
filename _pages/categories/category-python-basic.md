---
title: "python"
layout: archive
permalink: /category/python-basic
author_profile: true
sidebar_main: true
---

{% assign posts = site.categories["python basic"] %}

{% for post in posts %}
    {% include archive-single2.html type=page.entries_layout %} 
{% endfor %}
---
layout: default
permalink: /pages/talks
---

## Talks

{% for talks in site.talks %}
**{{ talks.project}}**
{% for talk in talks.talks %}
- {{ talk.date }} - {{ talk.venue }} [[URL]({{ talk.url }})] [[Slides]({{ '/assets/talks/' | append: talk.slides | relative_url }}){:target="_blank"}]
{% endfor %}
{% endfor %}

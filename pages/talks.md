---
layout: default
permalink: /pages/talks
---

## Talks

{% for talks in site.talks %}
**{{ talks.project}}**
{% for talk in talks.talks %}
- {{ talk.date }} - {{ talk.venue }} [[URL]({{ talk.url }})] [[Slides]({{ talk.slides }})]
{% endfor %}
{% endfor %}

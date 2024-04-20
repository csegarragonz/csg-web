---
layout: default
permalink: /pages/publications
---

## Pre-prints

{% for publication in site.preprints %}
[{{ forloop.index }}] **({{ publication.year }}) {{ publication.title }}** \\
{% for author in publication.authors %}{% assign names = author | split: ' ' %}{% if forloop.index > 1 %}, {% endif %}{{names[0] | slice: 0 }}. {{names[1]}}{% endfor %} \\
[[arXiv]({{ publication.arxiv }}) | [PDF]({{ publication.pdf }})]
<details>
  <summary>Abstract:</summary>

  {{ publication.abstract }}
</details>
{% endfor %}

## Publications

{% for publication in site.publications %}
[{{ forloop.index }}] **({{ publication.venue}} {{ publication.year }}) {{ publication.title }}** \\
{% for author in publication.authors %}{% assign names = author | split: ' ' %}{% if forloop.index > 1 %}, {% endif %}{{names[0] | slice: 0 }}. {{names[1]}}{% endfor %} \\
[[DOI]({{ publication.doi }}) | [arXiv]({{ publication.arxiv }}) | [Cite]({{ publication.cite }}) | [PDF]({{ publication.pdf }})]
<details>
  <summary>Abstract:</summary>

  {{ publication.abstract }}
</details>
{% endfor %}

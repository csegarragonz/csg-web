---
layout: main_page
---

<div style="border: 1px solid red; padding: 1em; background-color: #ffe6e6; color: red; border-radius: 4px;">
  <strong>Looking for post-docs!</strong> I am looking for post-doc opportunities from <strong>January 2026</strong>. If you have or know of an opening, do check my <a href="{{ site.url }}/assets/SegarraCarlos_CV.pdf">CV</a> and reach-out to `c.segarra[at]imperial.ac.uk`.
</div>

I am a fifth-year PhD student at the Large-Scale Data and Systems Group ([LSDS](https://lsds.doc.ic.ac.uk/)) of the Imperial College London, under the supervision of [Prof. Peter Pietzuch](https://www.doc.ic.ac.uk/~prp/).

My research addresses the design and implementation of secure, high-performance, runtimes for the cloud.
I am particularly interested in serverless and confidential computing.
Most of my work is open-source and available on [Github](https://github.com/csegarragonz).
During my PhD, I have interned at Intel Labs, IBM Research and Microsoft Research.

{% assign allowed_venues = "NSDI,EuroSys,SoCC" %}
Selected publications ([full list](/pages/publications.html)):
{%- for publication in site.publications -%}
  {% if allowed_venues contains publication.venue %}
  * [{{ publication.venue }}'{{ publication.year | slice: -2, 2 }}] {{ publication.title }}
  [(PDF)]({{ '/assets/papers/' | append: publication.pdf | relative_url }}){:target="_blank"} \\
{% for author in publication.authors %}{% assign names = author | split: ' ' %}{% if forloop.index > 1 %}, {% endif %}{{names[0] | slice: 0 }}. {{names[1]}}{% endfor %}{% endif %}{% endfor %}

In the past, I received a MSc in advanced mathematics, a BSc in mathematics, and a BSc in electrical engineering from the Technical University of Catalonia (UPC).
I also worked as a researcher for the Barcelona Supercomputing Center (BSC), Nokia Bell Labs, the Swiss Center of Electronics and Microtechnology (CSEM), the University of Neuchatel, and the UPC.

For further details, visit any of the following links:\\
[/publications](/pages/publications.html) - updated publication list.\\
[/talks](/pages/talks.html) - updated list of dissemination talks.\\
[/education](/pages/education.html) - past and current education.\\
[/work](/pages/work.html) - past and current work experience.\\
[/service](/pages/service.html) - service in academic conferences.\\
[/projects](/pages/projects.html) - past and current research projects.\\
[/teaching](/pages/teaching.html) - teaching and mentoring experience.\\
[/cv](/assets/SegarraCarlos_CV.pdf){:target="_blank"} - up-to-date CV.

You may contact me at `c.segarra [at] imperial.ac.uk`.

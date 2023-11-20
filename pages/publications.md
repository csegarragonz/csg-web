---
layout: default
permalink: /pages/publications
---

## Publications

1. **_A Novel Framework for the Analysis of Unknown Transactions in Bitcoin: Theory, Model, and Experimental Results_** (BITCOIN 2021) \\
Maurantonio Caprolu, Matteo Pontecorvi, Matteo Signorini, Carlos Segarra, and Roberto Di Pietro \\
[[DOI](broken) | [arXiv](https://arxiv.org/pdf/2103.09459.pdf) | [Cite]({{ site.url }}/assets/papers/BITCOIN2021_CENTRIC.bib) | [PDF]({{ site.url }}/assets/papers/BITCOIN2021_CENTRIC.pdf)]
1. **_MQT-TZ: Hardening IoT Brokers Using ARM TrustZone_** (SRDS 2020) \\
C. Segarra, R. Delgado-Gonzalo, and V. Schiavoni \\
[[DOI](broken) | [arXiv](http://arxiv.org/abs/2007.12442) | [Cite](broken) | [PDF](broken)]
1. **_Kollaps: Decentralized and Dynamic Topology Emulation_** (EuroSys 2020) \\
P. Gouveia, J. Neves, C. Segarra, L. Liechti, S. Issa, V. Schiavoni, and M. Matos \\
[[DOI](https://dl.acm.org/doi/abs/10.1145/3342195.3387540) | [arXiv](https://arxiv.org/abs/2004.02253) | [Cite]({{ site.url }}/assets/papers/EUROSYS2020_Kollaps.bib) | [PDF]({{ site.url }}/assets/papers/EUROSYS2020_Kollaps.pdf)]
1. **_"MQT-TZ: Secure MQTT Broker for Biomedical Signal Processing on the Edge"_** (MIE 2020) \\
C. Segarra, R. Delgado-Gonzalo, and V. Schiavoni \\
[[DOI](https://doi.org/10.3233/shti200177) | [arXiv](https://arxiv.org/abs/2007.01555) | [Cite]({{ site.url }}/assets/papers/MIE2020_MQTTZ.bib) | [PDF]({{ site.url }}/assets/papers/MIE2020_MQTTZ.pdf)]
2.  **_Secure Stream Processing for Medical Data_** (IEEE EMBC 2019) \\
C. Segarra, E. Muntan\'e, M. Lemay, V. Schiavoni, and  R. Delgado-Gonzalo \\
[[DOI](https://doi.org/10.1109/EMBC.2019.8856334) | [arXiv](https://arxiv.org/abs/1907.12242) | [Cite]({{ site.url }}/assets/papers/EMBC2019_SecureStreamProcessing.bib) | [PDF]({{ site.url }}/assets/papers/EMBC2019_SecureStreamProcessing.pdf)]
3. **_Using Trusted Execution Environments for Secure Stream Processing of Medical Data_** (DAIS 2019) \\
C. Segarra, R. Delgado-Gonzalo, M. Lemay, P-L. Aublin, P. Pietzuch, and V. Schiavoni \\
[[DOI](https://doi.org/10.1007/978-3-030-22496-7_6) | [arXiv](https://arxiv.org/abs/1906.07072) | [Cite]({{ site.url }}/assets/papers/DAIS2019_UsingTEE.bib) | [PDF]({{ site.url }}/assets/papers/DAIS2019_UsingTEE.pdf)]

## Publications

{% for publication in site.publications %}
1. **[{{ publication.venue}} {{ publication.year }}] {{ publication.title }}** \\
{% for author in publication.authors %}
{% assign names = author | split: ' ' %}{% if forloop.index > 1 %}, {% endif %}{{names[0]}} {{names[1]}}{% endfor %}
{% endfor %}

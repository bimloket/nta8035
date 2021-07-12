---
layout: page
title: "NTA 8035"
---

## Semantic modelling of information in the built environment

These pages provide a way to lookup and dereference the concepts of 
<a href='-/downloads#norm' class='link dim underline-hover blue'>
NTA 8035:2020</a>.

NTA 8035:2020 will be superceded by [NEN 2660-2:2021][nen2660], to be published in Q4 of 2021.
New implementations of NTA 8035 are therefore discouraged.

[nen2660]: https://bimloket.github.io/nen2660/

***

{% assign pp = site.pages | sort: "sortkey" %}
{% for p in pp %}

{% unless p.url == page.url %}
{% unless p.dont_render %}
{% if p.title %}
<h3 class='f5 dib mb3'>
<a
  class="link"
  href="{{ site.baseurl }}{{p.url | remove: '.html'}}">
  <span class='db black mb2'>{{p.title}}</span>
  <span class='dim underline-hover brand-dark-color f3'>{{p.excerpt}}</span>
</a>
</h3>

{% endif %}
{% endunless %}
{% endunless %}

{% endfor %}

***

You may discuss implementation and usage on GitHub at 
<a href='{{ site.repo }}/discussions/' class='link'>
bimloket/nen2660</a>.

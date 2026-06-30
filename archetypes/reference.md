---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
type: reference
series: []
tags: []
description: ""
cover:
  image: /assets/images/{{ .Section }}/{{ .Name }}.jpg
  alt: {{ replace .Name "-" " " | title }} series hub
slug: "{{ .Name }}"
---

## TL;DR

- What question this series answers
- Recommended read order (post one → post two → post three)
- Full series index: [/series/{{ .Name }}/](/series/{{ .Name }}/)

------------------------------------------------------------------------

## Start here

1. [First Post](/{{ .Section }}/) - why start here
2. [Second Post](/{{ .Section }}/) - what it adds
3. [Third Post](/{{ .Section }}/) - where it goes next

------------------------------------------------------------------------

## Supporting reading

- [Supporting Post](/{{ .Section }}/) - brief description

------------------------------------------------------------------------

## Related Reading

- [Related Post One](/{{ .Section }}/)
- [Related Post Two](/{{ .Section }}/)

---
title: "Hugo Shortcode Syntax"
date: 2020-01-01T00:00:01+01:00
draft: false
---

# Code
`echo "Hello World"`

# Code Block
```
# some code
echo "Hello World"
```

# Code Block with Highlighting
not working ?
{{< highlight Shell "linenos=table" >}}
# some code
echo "Hello World"
{{< /highlight >}}

# Figure
{{< figure src="https://lh3.googleusercontent.com/d_S5gxu_S1P6NR1gXeMthZeBzkrQMHdI5uvXrpn3nfJuXpCjlqhLQKH_hbOxTHxFhp5WugVOEcl4WDrv9rmKBDOMExhKU5KmmLFQVg" title="Google Logo" >}}

# GitHub Gist
https://gist.github.com/sansmischevia/5148109
{{< gist sansmischevia 5148109 >}}

# Tweet
{{< tweet user="SanDiegoZoo" id="1453110110599868418" >}}

# Vimeo
{{< vimeo 55073825 >}}

# YouTube
{{< youtube w7Ft2ymGmfc >}}

# Instagram
(requires an Access Token)

# Buttons
(not working)

# Columns
(not working)

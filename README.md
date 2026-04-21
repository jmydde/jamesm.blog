# jamesm.blog

A personal blog exploring technology, culture, and creative pursuits through writing and analysis.

**Live:** [jamesm.blog](https://jamesm.blog)

## Overview

This blog covers in-depth articles across diverse topics including artificial intelligence, blockchain technology, data engineering, DevOps infrastructure, retro computing history, music production, personal development, and space exploration.

Built with [Hugo](https://gohugo.io) using the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

## Topics

- **[Artificial Intelligence](/ai)** - LLMs, AI agents, and the future of human expertise
- **[Blockchain](/blockchain)** - Decentralized infrastructure, networks, and ecosystem evolution
- **[Data Engineering](/data-engineering)** - Building data infrastructure that actually scales
- **[Data Science](/data-science)** - Data analysis and scientific exploration
- **[DevOps](/devops)** - Infrastructure, automation, and operational philosophy
- **[General](/general)** - Culture, science, and miscellaneous observations
- **[Retro Computing](/retro-computing)** - The machines and culture that shaped computing
- **[Music Production](/music-production)** - Gear, sound design, and creative workflow
- **[Personal Development](/personal-development)** - Expertise, craft, and the engineering mindset
- **[Space](/space)** - Infrastructure and vision for human expansion beyond Earth

## Project Structure

```
content/
  ├── ai/                    # Artificial intelligence articles
  ├── blockchain/            # Blockchain and cryptocurrency content
  ├── data-engineering/      # Data infrastructure and pipeline design
  ├── data-science/          # Data science and analysis
  ├── devops/                # DevOps, infrastructure, and cloud
  ├── general/               # General-interest articles
  ├── music-production/      # Music production and sound design
  ├── personal-development/  # Career and skill development
  ├── retro-computing/       # Retro computing and computing history
  └── space/                 # Space exploration and infrastructure

config.yaml                   # Hugo configuration
themes/PaperMod/             # Blog theme
```

## Getting Started

### Prerequisites

- [Hugo Extended](https://gohugo.io/getting-started/installing/) (for SASS support)
- Git

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/jmydde/jamesm.blog.git
cd jamesm.blog
```

2. Start the development server:
```bash
hugo server -D
```

The blog will be available at `http://localhost:1313`

**Note:** Use the provided shell script for convenience:
```bash
./hugo.server.dev.sh
```

### Building for Production

```bash
hugo
```

The static site will be generated in the `public/` directory.

## Writing New Posts

Posts are written in Markdown and located in `content/[category]/`. Each post requires YAML frontmatter:

```yaml
---
title: "Post Title"
date: 2026-04-18T12:00:00+01:00
draft: false
tags: ["tag1", "tag2"]
description: "A brief description of the post"
---
```

**Key guidelines:**
- Use ISO 8601 date format with timezone
- Use singular tag names (e.g., `ai` not `ai-tools`)
- Include relevant links to authoritative sources
- Keep content original and copyright-free

### Adding Images

Place images in the category's `images/` subdirectory:
```
content/[category]/images/image-name.png
```

Reference in posts using relative paths or Hugo shortcodes.

## Connect

- **Email:** [jamesmyddelton@gmail.com](mailto:jamesmyddelton@gmail.com)
- **LinkedIn:** [linkedin.com/in/jamesmyddelton](https://uk.linkedin.com/in/jamesmyddelton/)
- **Twitter/X:** [@jamesmyddelton](https://x.com/jamesmyddelton/)
- **GitHub:** [github.com/jmydde](https://github.com/jmydde/jamesm.blog)
- **YouTube:** [@JamesMyddelton](https://www.youtube.com/@JamesMyddelton/playlists/)
- **Ko-fi:** [ko-fi.com/U6U1LGXXV](https://ko-fi.com/U6U1LGXXV/)

## License

Content is original and copyright-protected unless otherwise stated.

## Credits

Built with [Hugo](https://gohugo.io) and [PaperMod Theme](https://github.com/adityatelange/hugo-PaperMod).

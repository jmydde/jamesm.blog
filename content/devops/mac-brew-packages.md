---
title: "Mac Homebrew packages"
date: 2026-04-04T20:59:35+01:00
draft: false
tags: ['brew', 'macos', 'terminal', 'cli', 'kubernetes', 'terraform', 'python', 'syntax highlighting', 'monitoring', 'package management', 'linux']
description: "Comprehensive list of essential Homebrew packages for macOS development, DevOps, cloud tools, and command-line utilities."
---

[Homebrew](https://brew.sh/) is the package manager that makes a Mac genuinely usable as a development machine. The list below is the working set of packages I install on a new laptop, organised by what they do rather than alphabetically. Most can be installed in one command: `brew install <package>`. For graphical applications, see the companion [Mac Applications and Utilities]({{< ref "/devops/mac-apps-utils" >}}) page.

## Essential
* **bat** - Cat alternative with syntax highlighting and Git integration
* **fzf** - Fuzzy finder for CLI (command history, file search, etc.)
* **glow** - Markdown reader in the terminal
* **htop** - Interactive process monitor with colors and mouse support
* **jq** - JSON query and manipulation tool (sed for JSON)
* **pyenv** - Python version manager
* **python** - Python (3.11+)
* **ripgrep (rg)** - Fast, recursive grep alternative
* **terraform** - Infrastructure as code provisioning
* **tfswitch** - Switch Terraform versions easily (warrensbox/tap/tfswitch)
* **tree** - Display directory structure visually
* **wget** - Command-line file downloader
* **yq** - YAML/JSON/XML processor and querying tool

## Cloud & Container Tools
* **awscli** - AWS Command Line Interface
* **docker** - Container platform and runtime
* **gcloud** - Google Cloud CLI
* **helm** - Kubernetes package manager
* **k9s** - Interactive Kubernetes resource viewer and manager
* **kubectl** - Kubernetes command-line tool
* **kubectx** - Switch between Kubernetes clusters and namespaces
* **minikube** - Run Kubernetes locally in a VM

## Development Languages & Frameworks
* **django** - Python web framework
* **go** - Go programming language
* **nvm** - Node.js version manager
* **npm** - Node Package Manager
* **pytorch** - Machine learning framework for deep learning
* **rbenv** - Ruby version manager
* **rust** - Rust programming language
* **tensorflow** - ML library for machine learning and AI

## DevOps & Infrastructure Tools
* **ansible** - Configuration management and automation
* **consul** - Service mesh and service discovery
* **hashicorp/tap/vault** - Secrets management tool
* **packer** - Machine image builder
* **prometheus** - Metrics collection and monitoring

## System & Network Tools
* **bottom** - System monitor (process, memory, disk, network)
* **dust** - Disk usage analyzer (better than du)
* **exa** - Modern ls replacement with colors and icons
* **fd** - Fast find alternative
* **lnav** - Log file analyzer and explorer
* **mtr** - Network diagnostic combining ping and traceroute
* **speedtest-cli** - Test internet upload/download speed
* **tldr** - Simplified man pages with practical examples

## File & Directory Tools
* **midnight-commander** - Full-screen file manager (mc)
* **ncdu** - Disk space usage analyzer
* **ranger** - Terminal file manager with preview support

## Productivity & Utilities
* **direnv** - Load environment variables based on directory
* **httpie** - HTTP CLI client (curl alternative)
* **jupyter** - Interactive notebooks for data science
* **navi** - Interactive cheatsheet and command browser
* **task** - Task management and todo app
* **tmux** - Terminal multiplexer (multiple sessions/panes)

## Database & Data Tools
* **postgresql** - PostgreSQL database client
* **redis-cli** - Redis key-value store client
* **sqlite** - Lightweight embedded database

## Additional Utilities
* **neofetch** - System information display
* **snappy** - Compression library for fast compression/decompression
* **youtube-dl** - Download videos from YouTube and other sites

## Related Pages

- [Mac Applications and Utilities]({{< ref "/devops/mac-apps-utils" >}}) - graphical applications to pair with this CLI toolkit
- [DevOps Best Practices]({{< ref "/devops/best-practices" >}})
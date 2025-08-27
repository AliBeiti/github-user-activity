# GitHub Events CLI

A simple Python CLI tool to fetch and display a GitHub user's latest public activity.

https://roadmap.sh/projects/github-user-activity

## 🚀 Installation

You can install directly from GitHub:

```bash
python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/AliBeiti/github-user-activity.git
```

## Requirements

Python 3.7+

requests module (auto-installed with setup)

## Usage

List all events:

```bash
github-events events <username>
```

List only PushEvents:

```bash
github-events events <username> --sort PushEvent
```

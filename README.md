# Single File Agents (SFA)
> Premise: #1: What if we could pack single purpose, powerful AI Agents into a single python file?
> 
> Premise: #2: What's the best structural pattern for building Agents that can improve in capability as compute and intelligence increases?

![Single File Agents](images/single-file-agents-thumb.png)

## What is this?

A collection of powerful single-file agents built on top of [uv](https://github.com/astral/uv) - the modern Python package installer and resolver. 

These agents aim to do one thing and one thing only. They demonstrate precise prompt engineering and GenAI patterns for practical tasks many of which I share on the [IndyDevDan YouTube channel](https://www.youtube.com/@indydevdan). Watch us walk through the Single File Agent in [this video](https://youtu.be/YAIJV48QlXc).

This repo contains a few agents built across the big 3 GenAI providers (Gemini, OpenAI, Anthropic).

## Quick Start

Export your API keys:

```bash
export GEMINI_API_KEY='your-api-key-here'

export OPENAI_API_KEY='your-api-key-here'

export ANTHROPIC_API_KEY='your-api-key-here'
```

JQ Agent:

```bash
uv run sfa_jq_gemini_v1.py --exe "Filter scores above 80 from data/analytics.json and save to high_scores.json"
```

DuckDB Agent (OpenAI):

```bash
# Tip tier
uv run sfa_duckdb_openai_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"
```

DuckDB Agent (Anthropic):

```bash
# Tip tier
uv run sfa_duckdb_anthropic_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"
```

DuckDB Agent (Gemini):

```bash
# Buggy but usually works
uv run sfa_duckdb_gemini_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"
```

SQLite Agent (OpenAI):

```bash
uv run sfa_sqlite_openai_v2.py -d ./data/analytics.sqlite -p "Show me all users with score above 80"
```

Meta Prompt Generator:

```bash
uv run sfa_meta_prompt_openai_v1.py \
    --purpose "generate mermaid diagrams" \
    --instructions "generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output" \
    --sections "user-prompt" \
    --variables "user-prompt"
```

Python Code to SQLite Agent:

```bash
uv run sfa_sqlite_add_code.py -d ./data/analytics.db -p ./path/to/python/files
```

## Features

- **Self-contained**: Each agent is a single file with embedded dependencies
- **Minimal, Precise Agents**: Carefully crafted prompts for small agents that can do one thing really well
- **Modern Python**: Built on uv for fast, reliable dependency management
- **Run From The Cloud**: With uv, you can run these scripts from your server or right from a gist (see my gists commands)
- **Patternful**: Building effective agents is about setting up the right prompts, tools, and process for your use case. Once you setup a great pattern, you can re-use it over and over. That's part of the magic of these SFA's. 

## Test Data

The project includes a test duckdb database (`data/analytics.db`), a sqlite database (`data/analytics.sqlite`), and a JSON file (`data/analytics.json`) for testing purposes. The database contains sample user data with the following characteristics:

### User Table
- 30 sample users with varied attributes
- Fields: id (UUID), name, age, city, score, is_active, status, created_at
- Test data includes:
  - Names: Alice, Bob, Charlie, Diana, Eric, Fiona, Jane, John
  - Cities: Berlin, London, New York, Paris, Singapore, Sydney, Tokyo, Toronto
  - Status values: active, inactive, pending, archived
  - Age range: 20-65
  - Score range: 3.1-96.18
  - Date range: 2023-2025

Perfect for testing filtering, sorting, and aggregation operations with realistic data variations.

## Agents
> Note: We're using the term 'agent' loosely for some of these SFA's. We have prompts, prompt chains, and a couple are official Agents.

### JQ Command Agent 
> (sfa_jq_gemini_v1.py)

An AI-powered assistant that generates precise jq commands for JSON processing

Example usage:
```bash
# Generate and execute a jq command
uv run sfa_jq_gemini_v1.py --exe "Filter scores above 80 from data/analytics.json and save to high_scores.json"

# Generate command only
uv run sfa_jq_gemini_v1.py "Filter scores above 80 from data/analytics.json and save to high_scores.json"
```

### DuckDB Agents 
> (sfa_duckdb_openai_v2.py, sfa_duckdb_anthropic_v2.py, sfa_duckdb_gemini_v2.py, sfa_duckdb_gemini_v1.py)

We have three DuckDB agents that demonstrate different approaches and capabilities across major AI providers:

#### DuckDB OpenAI Agent (sfa_duckdb_openai_v2.py, sfa_duckdb_openai_v1.py)
An AI-powered assistant that generates and executes DuckDB SQL queries using OpenAI's function calling capabilities.

Example usage:
```bash
# Run DuckDB agent with default compute loops (10)
uv run sfa_duckdb_openai_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"

# Run with custom compute loops 
uv run sfa_duckdb_openai_v2.py -d ./data/analytics.db -p "Show me all users with score above 80" -c 5
```

#### DuckDB Anthropic Agent (sfa_duckdb_anthropic_v2.py)
An AI-powered assistant that generates and executes DuckDB SQL queries using Claude's tool use capabilities.

Example usage:
```bash
# Run DuckDB agent with default compute loops (10)
uv run sfa_duckdb_anthropic_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"

# Run with custom compute loops
uv run sfa_duckdb_anthropic_v2.py -d ./data/analytics.db -p "Show me all users with score above 80" -c 5
```

#### DuckDB Gemini Agent (sfa_duckdb_gemini_v2.py)
An AI-powered assistant that generates and executes DuckDB SQL queries using Gemini's function calling capabilities.

Example usage:
```bash
# Run DuckDB agent with default compute loops (10)
uv run sfa_duckdb_gemini_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"

# Run with custom compute loops
uv run sfa_duckdb_gemini_v2.py -d ./data/analytics.db -p "Show me all users with score above 80" -c 5
```

### Meta Prompt Generator (sfa_meta_prompt_openai_v1.py)
An AI-powered assistant that generates comprehensive, structured prompts for language models.

Example usage:
```bash
# Generate a meta prompt using command-line arguments.
# Optional arguments are marked with a ?.
uv run sfa_meta_prompt_openai_v1.py \
    --purpose "generate mermaid diagrams" \
    --instructions "generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output" \
    --sections "examples, user-prompt" \
    --examples "create examples of 3 basic mermaid charts with <user-chart-request> and <chart-response> blocks" \
    --variables "user-prompt"

# Without optional arguments, the script will enter interactive mode.
uv run sfa_meta_prompt_openai_v1.py \
    --purpose "generate mermaid diagrams" \
    --instructions "generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output"

# Interactive Mode
# Just run the script without any flags to enter interactive mode.
# You'll be prompted step by step for:
# - Purpose (required): The main goal of your prompt
# - Instructions (required): Detailed instructions for the model
# - Sections (optional): Additional sections to include
# - Examples (optional): Example inputs and outputs
# - Variables (optional): Placeholders for dynamic content
uv run sfa_meta_prompt_openai_v1.py
```

### Python Code to SQLite Agent
> (sfa_sqlite_add_code.py)

An AI-powered assistant that adds Python code to a SQLite database table.

Example usage:
```bash
# Add Python code to the SQLite database
uv run sfa_sqlite_add_code.py -d ./data/analytics.db -p ./path/to/python/files
```

### Git Agent
> Up for a challenge?

## Requirements

- Python 3.8+
- uv package manager
- GEMINI_API_KEY (for Gemini-based agents)
- OPENAI_API_KEY (for OpenAI-based agents) 
- ANTHROPIC_API_KEY (for Anthropic-based agents)
- jq command-line JSON processor (for JQ agent)
- DuckDB CLI (for DuckDB agents)

### Installing Required Tools

#### jq Installation

macOS:
```bash
brew install jq
```

Windows:
- Download from [stedolan.github.io/jq/download](https://stedolan.github.io/jq/download/)
- Or install with Chocolatey: `choco install jq`

#### DuckDB Installation

macOS:
```bash
brew install duckdb
```

Windows:
- Download the CLI executable from [duckdb.org/docs/installation](https://duckdb.org/docs/installation)
- Add the executable location to your system PATH

## Installation

1. Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone this repository:
```bash
git clone <repository-url>
```

3. Set your Gemini API key (for JQ generator):
```bash
export GEMINI_API_KEY='your-api-key-here'

# Set your OpenAI API key (for DuckDB agents):
export OPENAI_API_KEY='your-api-key-here'

# Set your Anthropic API key (for DuckDB agents):
export ANTHROPIC_API_KEY='your-api-key-here'
```

## Shout Outs + Resources for you
- [uv](https://github.com/astral/uv) - The engineers creating uv are built different. Thank you for fixing the python ecosystem.
- [Simon Willison](https://simonwillison.net) - Simon introduced me to the fact that you can [use uv to run single file python scripts](https://simonwillison.net/2024/Aug/20/uv-unified-python-packaging/) with dependencies. Massive thanks for all your work. He runs one of the most valuable blogs for engineers in the world.
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) - A proper breakdown of how to build useful units of value built on top of GenAI.
- [Part Time Larry](https://youtu.be/zm0Vo6Di3V8?si=oBetAgc5ifhBmK03) - Larry has a great breakdown on the new Python GenAI library and delivers great hands on, actionable GenAI x Finance information.
- [Aider](https://aider.chat/) - AI Coding done right. Maximum control over your AI Coding Experience. Enough said.

---

- [New Gemini Python SDK](https://github.com/google-gemini/generative-ai-python)
- [Anthropic Agent Chatbot Example](https://github.com/anthropics/courses/blob/master/tool_use/06_chatbot_with_multiple_tools.ipynb)
- [Anthropic Customer Service Agent](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/customer_service_agent.ipynb)

## License

MIT License - feel free to use this code in your own projects.

If you find value from my work: give a shout out and tag my YT channel [IndyDevDan](https://www.youtube.com/@indydevdan).

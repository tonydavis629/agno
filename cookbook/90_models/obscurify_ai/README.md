# Obscurify.ai Cookbook

This cookbook shows how to use [Obscurify.ai](https://obscurify.ai/?utm_source=agno) with the Agno
framework. Obscurify.ai is a privacy-focused service with an OpenAI-compatible API
(`https://obscurify.ai/v1`). Accounts are a random account number with no email, and prompts
and responses are not stored on the server.

> **Prerequisites**: Fork and clone this repository if needed

## Quick Start

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `OBSCURIFY_API_KEY`

Get your key from https://obscurify.ai/account ("Show API Key"). The API works on every plan
with a positive balance.

```shell
export OBSCURIFY_API_KEY=***
```

### 3. Install libraries

```shell
uv pip install -U openai agno
```

### 4. Run basic Agent

```shell
python cookbook/90_models/obscurify_ai/basic.py
```

### 5. Run Agent with Tools

```shell
python cookbook/90_models/obscurify_ai/tool_use.py
```

## Model Ids

Model ids are `vendor/model`. The examples use `deepseek/deepseek-v4-flash` (1,048,576-token
context, tool calling). Other open models include `z-ai/glm-5.3`, `moonshotai/kimi-k2-0905`,
`meta-llama/llama-3.3-70b-instruct` and `qwen/qwen3-coder`. Frontier models such as
`openai/gpt-5.5` and `anthropic/claude-sonnet-5.5` need the Casual or Pro plan.

The full list with context lengths and prices is public at `GET https://obscurify.ai/v1/models`
(no key needed) and at https://obscurify.ai/model_cards.

## Resources

- [Website](https://obscurify.ai/?utm_source=agno)
- [API docs](https://obscurify.ai/api-docs)
- [Models and prices](https://obscurify.ai/model_cards)
- **Base URL**: `https://obscurify.ai/v1`

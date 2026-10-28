"""
Obscurify.ai Basic
==================

Cookbook example for Obscurify.ai, OpenAILike model provider.
"""

import asyncio

from agno.agent import Agent
from agno.models.obscurify_ai import ObscurifyAI

# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------

agent = Agent(model=ObscurifyAI(id="deepseek/deepseek-v4-flash"), markdown=True)

# You can also select the provider by string, which resolves to the same class:
# agent = Agent(model="obscurify-ai:deepseek/deepseek-v4-flash", markdown=True)

# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Sync ---
    agent.print_response("Explain quantum computing in two sentences")

    # --- Sync + Streaming ---
    agent.print_response("Explain quantum computing in two sentences", stream=True)

    # --- Async and Async + Streaming (one event loop, so the async client is reused) ---
    async def main():
        await agent.aprint_response("Share a 2 sentence horror story")
        await agent.aprint_response(
            "Write a four line poem about artificial intelligence", stream=True
        )

    asyncio.run(main())

"""
Obscurify.ai Tool Use
=====================

Cookbook example for `obscurify_ai/tool_use.py`.
"""

import asyncio

from agno.agent import Agent
from agno.models.obscurify_ai import ObscurifyAI


def get_weather(city: str) -> str:
    """Return the current weather for a city."""
    return f"The weather in {city} is sunny and 22 degrees Celsius."


# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------

agent = Agent(
    model=ObscurifyAI(id="deepseek/deepseek-v4-flash"),
    tools=[get_weather],
    markdown=True,
)

# The string syntax works too:
# agent = Agent(model="obscurify-ai:deepseek/deepseek-v4-flash", tools=[get_weather])

# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Sync ---
    agent.print_response("What's the weather in Lisbon?")

    # --- Sync + Streaming ---
    agent.print_response("What's the weather in Tokyo?", stream=True)

    # --- Async and Async + Streaming (one event loop, so the async client is reused) ---
    async def main():
        await agent.aprint_response("What's the weather in Paris?")
        await agent.aprint_response("What's the weather in Oslo?", stream=True)

    asyncio.run(main())

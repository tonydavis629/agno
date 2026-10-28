# Obscurify.ai Tests

### basic.py

**Status:** PASS

**Description:** Basic Obscurify.ai cookbook covering sync, streaming, async, and async streaming agent responses with `deepseek/deepseek-v4-flash`.

**Result:** All four runs returned a response against the live API.

---

### tool_use.py

**Status:** PASS

**Description:** Agent with a local `get_weather` tool covering sync, streaming, async, and async streaming tool calls.

**Result:** All four runs called `get_weather` with the requested city and returned a final answer using the tool result.

---

### String syntax

**Status:** PASS

**Description:** `Agent(model="obscurify-ai:z-ai/glm-5.3")` resolves to `ObscurifyAI` and returns a reply from the live API.

---

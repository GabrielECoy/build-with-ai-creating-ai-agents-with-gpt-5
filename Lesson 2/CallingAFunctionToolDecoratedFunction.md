GabrielECoy: How do I call the function that was decorated with Function_tool without removing the decorator?

GitHub Copilot: Searched text for `class ToolContext`, 2 results

Read [](file:///workspaces/build-with-ai-creating-ai-agents-with-gpt-5/venv/lib64/python3.12/site-packages/agents/tool_context.py)

Read [](file:///workspaces/build-with-ai-creating-ai-agents-with-gpt-5/venv/lib64/python3.12/site-packages/agents/run_context.py)

Read [](file:///workspaces/build-with-ai-creating-ai-agents-with-gpt-5/venv/lib64/python3.12/site-packages/agents/usage.py)

Read [](file:///workspaces/build-with-ai-creating-ai-agents-with-gpt-5/venv/lib64/python3.12/site-packages/agents/__init__.py)

Short answer: you call the decorated function via the FunctionTool's runtime entrypoint — its async on_invoke_tool(...) — because the decorator replaced the name with a FunctionTool object. on_invoke_tool will validate the JSON args, call your original function (sync or async), and return the result.

Why: @function_tool returns a FunctionTool dataclass (see site-packages/agents/tool.py). That object contains:
- .name
- .params_json_schema
- .on_invoke_tool(ctx, input_json_str)  ← the runtime caller that actually runs your original function

Example you can run in your script or REPL

```python
import asyncio
import json

# import helpers
from agents.tool_context import ToolContext
from agents import Usage

# build a minimal ToolContext (tool_name must be provided)
ctx = ToolContext(
    context=None,
    usage=Usage(),
    tool_name=get_weather_forecast.name,   # or "get_weather_forecast"
    tool_call_id="manual-call-1",
)

# JSON string representing the tool arguments (must match params_json_schema)
input_json = json.dumps({"city": "Horizon West, FL"})

# on_invoke_tool is async, so run it with asyncio
result = asyncio.run(get_weather_forecast.on_invoke_tool(ctx, input_json))
print("Tool returned:", result)
```

Notes and tips
- You must pass a JSON string as the second argument; the FunctionTool will parse and validate it against the generated schema.
- on_invoke_tool handles both sync and async original functions and will pass a ToolContext as first arg if the original function expects context.
- By default errors inside your function are caught and converted to a user-friendly string (via the decorator's failure_error_function), so you generally get a string result instead of a crash.
- To learn the expected JSON shape, inspect:
  - print(get_weather_forecast.params_json_schema)
  - or print(json.dumps(get_weather_forecast.params_json_schema, indent=2))

If you need to call the raw original Python function directly
- The decorator returns a FunctionTool and does not attach the original function as __wrapped__ in that implementation, so the original function object is not directly available from the decorated name.
- If you want direct access in future, define the implementation first and then create/register the tool from it, e.g.:

```python
def _get_weather_forecast_impl(city: str):
    ...  # same body

get_weather_tool = function_tool(_get_weather_forecast_impl)
trip_agent = Agent(..., tools=[get_weather_tool])
# You can still call _get_weather_forecast_impl(...) directly for local tests.
```

Would you like me to add a tiny helper in your Lesson 2 script that demonstrates calling the tool manually (and prints the params_json_schema), or show the Agent/Runner wiring where they call on_invoke_tool?
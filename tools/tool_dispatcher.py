import json
import platform


def run_tool(tool_name, arguments):
    if tool_name == "calculator":
        return calculator(arguments)

    elif tool_name == "system_info":
        return system_info()

    else:
        return {
            "success": False,
            "error": f"Unknown tool: {tool_name}"
        }


def calculator(arguments):
    expression = arguments.get("expression")

    if not expression:
        return {
            "success": False,
            "error": "No expression provided"
        }

    try:
        result = eval(expression, {"__builtins__": {}}, {})

        return {
            "success": True,
            "result": result
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def system_info():
    return {
        "success": True,
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine()
    }


if __name__ == "__main__":
    print("Petal Tool Layer started!")

    request = {
        "tool": "system_info",
        "arguments": {}
    }

    response = run_tool(
        request["tool"],
        request["arguments"]
    )

    print(json.dumps(response, indent=2))
class PolicyGuard:
    def __init__(self, allowed, denied):
        self.allowed = set(allowed)
        self.denied = set(denied)

    def check(self, tool_name: str) -> dict:
        if tool_name in self.denied:
            return {"permitted": False, "reason": "Explicitly denied"}
        if tool_name in self.allowed:
            return {"permitted": True, "reason": "Whitelisted"}
        return {"permitted": False, "reason": "Default deny policy"}

if __name__ == "__main__":
    guard = PolicyGuard(allowed=["read_file", "list_dir"], denied=["rm_rf", "exec_shell"])
    for t in ["read_file", "rm_rf", "unknown_tool"]:
        print(t, "->", guard.check(t))

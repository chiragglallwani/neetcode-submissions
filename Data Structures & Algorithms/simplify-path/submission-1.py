class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = [k for k in path.split("/") if len(k) > 0 ]
        stack = []
        print(directory)
        for name in directory:
            if stack and name == "..":
                stack.pop()
            else: 
                if name != ".." and name != ".":
                    stack.append("/" + name)
        return "".join(stack) if len(stack) > 0 else "/"

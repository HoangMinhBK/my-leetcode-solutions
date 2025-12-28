class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_components = path.split("/")
        stack = []
        for component in path_components:
            if component == "..":
                if len(stack) > 0:
                    stack.pop()
            elif component == "" or component == ".":
                continue
            else:
                stack.append(component)
        if len(stack) > 0 and stack[-1] == "":
            stack.pop()
        return "/" + "/".join(stack)

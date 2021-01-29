def getLowestCommonManager(topManager, reportOne, reportTwo):
    parents = {topManager.name: None}
    queue = [topManager]

    while queue:
        current_node = queue.pop(0)
        for adj in current_node.directReports:
            queue.append(adj)
            parents[adj.name] = current_node

    report_one_path = set()
    curr_node = reportOne
    while curr_node is not None:
        report_one_path.add(curr_node.name)
        curr_node = parents.get(curr_node.name, None)

    curr_node = reportTwo
    while curr_node is not None:
        if curr_node in report_one_path:
            return curr_node
        curr_node = parents.get(curr_node.name, None)

    return None

# This is an input class. Do not edit.


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

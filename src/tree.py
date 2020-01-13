import suffix_tree


class SuffixTree(suffix_tree.Tree):
    def __init__(self, d):
        super().__init__(d)

        self.leaf_counts = {}

    def count_leaves(self):
        def on_visit(node):
            if node.is_leaf():
                self.leaf_counts[node] = 1
                return

            self.leaf_counts[node] = sum([self.leaf_counts[c] for c in node.children.values()])

        self.root.post_order(on_visit)

    def longest_repetitive_substring(self, k):
        if not self.leaf_counts:
            self.count_leaves()

        longest_path = None
        for key, value in self.leaf_counts.items():
            if value < k:
                continue

            if not longest_path or len(key.path) > len(longest_path):
                longest_path = key.path

        return str(longest_path).translate(str.maketrans({' ': '', '$': '', '\n': ''}))

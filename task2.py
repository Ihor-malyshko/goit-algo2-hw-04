# Шаблон програми

from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            return 0
        
        count = 0
        
        def dfs(node, current_word):
            nonlocal count
            if node.is_end_of_word and current_word.endswith(pattern):
                count += 1
            for char, child in node.children.items():
                dfs(child, current_word + char)
        
        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            return False
        
        node = self._find_node(prefix)
        return node is not None

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    print("Перевірка кількості слів з суфіксом:")
    result = trie.count_words_with_suffix("e")
    print(f'  count_words_with_suffix("e") = {result}')
    assert result == 1  # apple
    
    result = trie.count_words_with_suffix("ion")
    print(f'  count_words_with_suffix("ion") = {result}')
    assert result == 1  # application
    
    result = trie.count_words_with_suffix("a")
    print(f'  count_words_with_suffix("a") = {result}')
    assert result == 1  # banana
    
    result = trie.count_words_with_suffix("at")
    print(f'  count_words_with_suffix("at") = {result}')
    assert result == 1  # cat

    print("\nПеревірка наявності префікса:")
    result = trie.has_prefix("app")
    print(f'  has_prefix("app") = {result}')
    assert result == True  # apple, application
    
    result = trie.has_prefix("bat")
    print(f'  has_prefix("bat") = {result}')
    assert result == False
    
    result = trie.has_prefix("ban")
    print(f'  has_prefix("ban") = {result}')
    assert result == True  # banana
    
    result = trie.has_prefix("ca")
    print(f'  has_prefix("ca") = {result}')
    assert result == True  # cat
    
    print("\nВсі тести пройдено успішно!")

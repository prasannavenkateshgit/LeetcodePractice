'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei=collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        q=collections.deque()
        seen=set()
        seen.add(beginWord)
        q.append((beginWord,1))
        while q:
            for i in range(len(q)):
                word,steps=q.popleft()
                if word==endWord:
                    return steps
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for nword in nei[pattern]:
                        if nword not in seen:
                            seen.add(nword)
                            q.append((nword,steps+1))
        return 0

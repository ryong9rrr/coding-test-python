/*python
# 80ms // 애너그램을 찾아내는 가장 좋은 방법은 정렬하는 것이다.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        # sorted는 list를 리턴함(sort는 None을 리턴)
        anagrams["".join(sorted(word))].append(word)
    
    return list(anagrams.values())
*/

var groupAnagrams = function (strs) {
  const anagrams = {};

  for (const word of strs) {
    const key = [...word].sort().join("");

    if (!anagrams[key]) anagrams[key] = [];
    anagrams[key].push(word);
  }

  return Object.values(anagrams);
};

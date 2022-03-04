# 정규표현식 + 딕셔너리 사용 // 28ms
def mostCommonWord(self, paragraph, banned):
    dic = defaultdict(int)
    
    # 영문자가 아닌 것들을 " "으로 치환
    paragraph = re.sub("[^\w]", " ", paragraph)
    
    for char in paragraph.split():
        char = char.lower()
        dic[char] += 1
    
    for ban in banned:
        dic[ban] = 0
    
    # 가장 큰 value를 가지는 key를 리턴
    return max(dic, key=dic.get)


# 정규표현식 + 리스트 컴프리헨션 + Counter // 24ms
def mostCommonWord(self, paragraph, banned):

    # 정규표현식, lower 변환 후 banned에 없는 단어만 추출   
    words = [word for word in re.sub("[^\w]", " ", paragraph)
                .lower().split() if word not in banned]
    
    #Counter는 튜플이 원소인 원소들을 가진 배열
    counts = collections.Counter(words)
    
    #가장 많이 등장한 값을 반환하고 이 값은 배열안에 튜플로 들어있음
    return counts.most_common(1)[0][0]


# count 모듈을 사용하지 않고 딕셔너리를 사용
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = defaultdict(int)
        for word in re.sub('[^\w]', ' ', paragraph).lower().split(' '):
            if not word or word in banned:
                continue
            counts[word] += 1
        
        return max(counts, key = counts.get)

"""js
var mostCommonWord = function(paragraph, banned) {
    const regex = /[^\w]/g
    const counts = {};
    
    const words = paragraph.replace(regex, " ").toLowerCase().split(' ');
    
    for (const word of words){
        if (banned.includes(word) || word === '') continue;
        if (!counts[word]) counts[word] = 0;
        counts[word]++;
    }
    
    const _max = Object.entries(counts).sort((a, b) => b[1] - a[1])
    
    return _max[0][0]
};
"""
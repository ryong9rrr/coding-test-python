def solution(s):
    if len(s)%2 == 0 :
        return s[len(s)//2-1:len(s)//2+1]
    else :
        return s[len(s)//2]

"""js
function solution(s) {
    
    
    if (s.length % 2 == 0) {
        return s.slice( s.length/2 - 1, s.length/2 + 1 );
    } else {
        return s.slice( s.length/2, s.length/2 + 1 );
      //return s.slice( Math.floor(s.length/2), Math.floor(s.length/2) + 1 );
    }
}
"""
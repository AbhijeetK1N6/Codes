"""
Sample Input 1 : "aaa"
Sample Output1 : 6
Explanation  1 : {'a','a','a','aa','aa','aaa'}

Sample Input 2 : "abccba"
Sample Output2 : 9
Explanation  2 : {'a','a','b','b','c','c','cc','bccb','abccba'}

Sample Input 3 : "daata"
Sample Output3 : 7
Explanation  3 : {'a','a','a','aa','ata','d','t'}
"""

#Contributed By ~AbhijeetK1N6

class LetsFind:
   def countSubstrings(self, s):
      abhijeet=0
      for i in range(len(s)):
         for j in range(i+1,len(s)+1):
            temp=s[i:j]
            if temp==temp[::-1]:
               abhijeet+=1
      return abhijeet
st1=input()
result=LetsFind()
print(result.countSubstrings(st1))


# coding: utf-8

# In[6]:


# 출처: <삼성 소프트웨어 역량테스트>(김수형 외 지음, 2015) 제1장 초급문제 3절
# 제목: 중복문자열 처리 

#######################
# 문제 : 입력된 2개의 문자열에서 같은 문자열(단, 2개 이상의 영문자)을 찾고, 찾은 무자열이 몇개인지 출력하시오
# 제약사항: 문자열의 구분은 줄바꿈으로 함 

# 입력 예:
# SAQLANGUAGEOFCOMPUTER
# SOFTWAREPROGRAMMING
# 출력 예: 
# OF NG 
# 2
#######################

# 문자열 두 개 입력 받음 
str1 = input()
str2 = input()

# str1의 문자열 길이가 무조건 작거나 같은 것으로 조건 설정 
if len(str1) > len(str2):
    tmp = str1
    str1 = str2
    str2 = tmp

# 모든 str1의 모든 2개 이상의 영문자에 대해, str2에 있는지 확인
word_list = []
for b in range(2, len(str1)+1):
    for a in range(len(str1)-b+1):
        if str2.find(str1[a:a+b]) != -1:
            word_list.append(str1[a:a+b])

# 출력 
for word in word_list:
    print(word,end=' ')
print('\n'+str(len(word_list)))      


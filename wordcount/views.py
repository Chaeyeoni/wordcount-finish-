from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    #원문 글자체를 가지고 와라는 뜻을 text에 담아줌
    words = text.split()
    #split함수는 string을 공백을 기준으로 단어를 리스트화 시켜줌
    # 총 단어 수를 변환 시키는 것은 len
    word_dic = {}

    for word in words:
        if word in word_dic:
            #increase
            word_dic[word]+=1
        else:
            #add to dictionary
            word_dic[word]=1
    return render(request,'result.html', {'full': text, 'total' : len(words), 'dictionary': word_dic.items()})
# Create your views here.
# render 3가지 (1, 요청 2, 이름 3,사전형객체 인자key:인자)

#items 함수 자습

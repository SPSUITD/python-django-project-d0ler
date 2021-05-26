from django.shortcuts import render, redirect
from .models import PublicChat, Message

# Главная страница
def index(request):
  username=request.session.get('username')
  if username is None:
    return redirect('login')

  chats = PublicChat.objects.all()
  return render(request, 'index.html', {'chats': chats})

# Страница чата
def chat(request, pk):
  chat = PublicChat.objects.get(pk=pk)
  username=request.session.get('username')

  if request.method == 'POST':
    message = Message(
      text=request.POST.get('text'),
      author=username,
      chat=chat.title,
    )
    message.save()
    return redirect('chat', chat.pk)
  
  messages = Message.objects.filter(
    chat=chat.title
  ).order_by('date_time')

  return render(request, 'chat.html', {
    'messages': messages,
    'chat': chat,
  })

# Страница получения имени пользователя
def login(request):
  if request.method == 'POST':
    username=request.POST.get('username')
    request.session.update({'username':username})
    return redirect('index')
  
  return render(request, 'login.html')
  

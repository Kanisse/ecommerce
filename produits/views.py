from django.shortcuts import render, redirect
from produits.models import Article

def home (request):
  return render(request, "home.html")

def lister(request):
  articles= Article.objects.all()
  return render(request, "article/articles.html", {'X':articles})
  
def delete(request, id):
  article = Article.objects.get(id=id)
  article.delete()
  return redirect('/produits')

def create (request):
  return render(request, "article/ajouter.html" )

def store(request):
  if request.method=='POST':
    article = Article()
    article.nom= request.POST['Nom']
    article.description=request.POST['Description']
    article.prix= request.POST["prix"]
    article.save()
    return redirect('/produits')    

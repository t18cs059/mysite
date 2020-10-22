from django.shortcuts import render
from .form import numForm

def index(request):
  if request.method == 'POST':
    form = numForm(request.POST)
    if form.is_valid():
      # print(request.POST)
      # print(form.cleaned_data['num1'])
      # print(form.cleaned_data['num2'])
      # return HttpResponseRedirect('/answer/')
      # print([form.cleaned_data['num1'],form.cleaned_data['num2']])
      n1=int(form.cleaned_data['num1'])
      n2=int(form.cleaned_data['num2'])
      ans=str(n1)+" + "+str(n2)+" = "+str(n1+n2)
      # print(ans)
  else:
    form=numForm()
    ans=""
  return render(request,'plus/index.html',{'form':form, 'ans' : ans})
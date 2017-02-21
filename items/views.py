#from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import get_object_or_404, render
from .models import Item
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect


from .forms import ItemForm


def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'items/item_edit.html', {'form': form})

def index(request):
    latest_item_list = Item.objects.order_by('-input_date')[:5]
    context = {'latest_item_list': latest_item_list}
    template = loader.get_template('items/index.html')
    return HttpResponse(template.render(context, request))


# ...
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
#    try:
#        item = Item.objects.get(pk=item_id)
#    except Item.DoesNotExist:
#        raise Http404("Item does not exist")
    return render(request, 'items/detail.html', {'item': item})



def results(request, item_id):
    response = "You're looking at the lists of item %s."
    return HttpResponse(response % item_id)

def stock(request, item_id):
    return HttpResponse("You're adding or removing stock %s." % question_id)

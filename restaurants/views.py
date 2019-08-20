from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {"my_list":[
    	{"restaurant_name":"AlBustan",
    	"food_type":"Cake"},
    	{"restaurant_name":"P.f Changs",
    	"food_type":"Noodles"},
    	{"restaurant_name":"Pizza Hut",
    	"food_type":"Pizza"},
    	
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {"my_object":{"restaurant_name":"AlBustan",
    	"food_type":"Cake"}

    }
    return render(request, 'detail.html', context)

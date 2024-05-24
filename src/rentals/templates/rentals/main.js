{% extends "base.html" %}
{% load static %}
{% load widget_tweaks %}
{% block scripts %}
<script src="{% static 'rentals/main.js' %}" defer ></script>

{% endblock scripts %}


{% block title %} 
| search rentals
{% endblock title %} 



{% block content %}


<div class="flex justify-center items-center g-[500px]">

<form class="w-[400px]" id='search-form' method ="Post" autocomplete="off">
    {% csrf_token %}
    <label for="{{form.search.id_for_label}}" class="block text-center text-3xl text-gray-700 dark:text-white font-bold mb-2">search for books</label>
    {{form.search| add_class:'bg-slate-100 dark:bg-slate-300 text-slate-800 rounded-lg p-3 drop-shadow-xl w-full'}}



    
</form>


</div>



{% endblock content %}
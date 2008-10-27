from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, get_host
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from oxybeles.models import PastedItem
from oxybeles.forms import PastedItemForm

def new(request, form_class=PastedItemForm, template_name="oxybeles/new.html"):
    """
    Form for pasting new items.
    """
    form = form_class()
    if request.method != 'POST':
        return render_to_response(template_name, 
                                  { "form": form, }, 
                                  context_instance=RequestContext(request))
    if request.POST["action"] == "paste":
        form = form_class(request.user, request.POST)
        if form.is_valid():
            item = form.save()
            request.user.message_set.create(
                message=_("Pasted the new item."))
            return HttpResponseRedirect(reverse('oxybeles_view', 
                                        args=(item.id,)))
new = login_required(new)


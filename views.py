from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, get_host
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from oxybeles.models import PastedItem
from oxybeles.forms import PastedItemForm, SendItemForm

def new(request, form_class=PastedItemForm, template_name="oxybeles/new.html"):
    """
    Form for pasting new items.
    """
    form = form_class()
    if request.method == 'POST':
        if request.POST["action"] == "paste":
            form = form_class(request.user, request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                request.user.message_set.create(
                    message=ugettext("The new pasted item was saved."))
                    # some problem with ugettext_lazy here
                return HttpResponseRedirect(reverse('oxybeles_detail',
                                            args=(item.uuid,)))
    return render_to_response(template_name,
                              { "form": form, },
                              context_instance=RequestContext(request))
new = login_required(new)

def detail(request, uuid, form_class=SendItemForm, template_name='oxybeles/pasteditem_detail.html'):
    form = form_class()
    if request.method == 'POST':
        if request.POST["action"] == "send":
            form = form_class(sender=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                request.user.message_set.create(
                    message=ugettext("The pasted item was sent."))
                url = form.pasted_item.get_absolute_url()
                return HttpResponseRedirect(url)
    pasted_item = get_object_or_404(PastedItem, uuid=uuid)
    return render_to_response(template_name,
                              { 'object': pasted_item, 'form': form },
                              context_instance=RequestContext(request))
detail = login_required(detail)

from home.models import Footer


def footer_links(request):
    footer = Footer.objects.first()
    return {'footer': footer}
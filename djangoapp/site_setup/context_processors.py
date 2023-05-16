from site_setup.models import SiteSetup


def context_processor_example(request):
    return {
        'example': 'Veio do context processor (example)'
    }


def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    return {
        'site_setup': setup,
    }

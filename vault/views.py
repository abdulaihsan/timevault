from django.shortcuts import render
from .models import VaultLetter

def submit_vault_letter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        instagram_handle = request.POST.get('instagram_handle', '')
        backup_contact = request.POST.get('backup_contact')
        batch = request.POST.get('batch')
        plan_years = request.POST.get('plan_years')

        VaultLetter.objects.create(
            name=name,
            email=email,
            contact_number=contact_number,
            instagram_handle=instagram_handle,
            backup_contact=backup_contact,
            batch=batch,
            plan_years=plan_years
        )

        return render(request, 'vault/form.html', {'success': True})

    return render(request, 'vault/form.html', {'success': False})
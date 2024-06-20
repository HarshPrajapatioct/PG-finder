def handle_uploaded_file(f):
    with open('pg_admin/static/images/'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
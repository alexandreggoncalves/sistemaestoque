from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from produto.models import Produto
from entradaSaida.models import EntradaSaida
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# INSERIR PRODUTO
@login_required(login_url='/sistema/login/') 
def entradaSaida(request):
    if request.method == 'POST':

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 100, 'Hello World!')
        p.showPage()
        p.save()
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
        #return render(request, 'entradaSaida.html', { 'entradaSaida': request.POST.get('entradaSaida'), 'dataInicio': request.POST.get('dataInicio'), 'dataFim': request.POST.get('dataFim') })
    else:
        return render(request, 'entradaSaida.html')

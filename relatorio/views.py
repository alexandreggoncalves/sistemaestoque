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
        dataInicio          =  request.POST.get('dataInicio')
        dataFim             =  request.POST.get('dataFim')
        filterEntradaSaida  = request.POST.get('entradaSaida')

        if( filterEntradaSaida == 'ES' ):
            entradaSaida = EntradaSaida.objects.filter(created_at__range=(dataInicio, dataFim)).order_by('created_at')
        else:
            entradaSaida = EntradaSaida.objects.filter(entradaSaida=filterEntradaSaida, created_at__range=(dataInicio, dataFim)).order_by('created_at')
            
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.setTitle('Meu Estoque Fácil - Relatório de Entradas e Saídas')

        p.setFont('Helvetica', 20)
        p.drawCentredString(300,800, 'Meu Estoque Fácil - Relatório de Entradas e Saídas' )
        p.line(30, 790, 550, 790)

        data = [ ['Entrada/Saída', 'Quantidade', 'Preço', 'Produto'] ]

        p.setFont('Helvetica', 8)
        y = 760

        p.drawString(32, 750, 'Data')
        p.drawString(100, 750, 'Entrada/Saída')
        p.drawString(160, 750, 'Produto')
        p.drawString(480, 750, 'Qtd.')
        p.drawString(510, 750, 'Preço')
        p.line(30, 745, 550, 745)

        y -= 20
        for es in entradaSaida: 
            y -= 12
            #line = "y: " + str(y) + " | E/S: " + str(es.entradaSaida) + " | Qtd: " + str(es.quantidade) + " | Preço: " + str(es.preco) + " | Produto: " + str(es.idProduto)
            #p.drawString(20, y, Entrada/Saída)
            p.drawString(32, y, str(es.created_at)[8:10]+'/'+str(es.created_at)[5:7]+'/'+str(es.created_at)[0:4]+' '+str(es.created_at)[11:16])
            if str(es.entradaSaida) == 'E':
                p.setFillColorRGB(0,150,0)
                strES = 'Entrada'
            else:
                p.setFillColorRGB(255,0,0)
                strES = 'Saída'
            p.drawString(100, y, strES)
            p.setFillColorRGB(0,0,0)
            p.drawString(160, y, str(es.idProduto)[0:85])
            p.drawString(480, y, str(es.quantidade))
            p.drawString(510, y, str(es.preco))
        
        p.showPage()
        p.save()
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
        #return render(request, 'entradaSaida.html', { 'entradaSaida': request.POST.get('entradaSaida'), 'dataInicio': request.POST.get('dataInicio'), 'dataFim': request.POST.get('dataFim') })
    else:
        return render(request, 'entradaSaida.html')

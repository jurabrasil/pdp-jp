from django.shortcuts import render, redirect, get_object_or_404
from .models import Time, Jogo, Pontuar
from django.contrib import messages
from unidecode import unidecode
<<<<<<< HEAD
# import unicodedata
from django.db.models import Sum, Q

=======
import unicodedata
from django.db.models import Sum, Q


>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
# Create your views here.

def index(request):
    jogos = Jogo.objects.all()
<<<<<<< HEAD

=======
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
    # total_de_gols(jogos)
    for j in jogos:
        unicode_timea = unidecode(str(j.timea)).replace(" ","").replace("'","")
        unicode_timeb = unidecode(str(j.timeb)).replace(" ","").replace("'","")
        j.unicode_timea = unicode_timea
        j.unicode_timeb = unicode_timeb

<<<<<<< HEAD
    gols = Jogo.objects.values('rodada').annotate(Sum('gols_total')).order_by('rodada')

    posicoes = Pontuar.objects.all().order_by("-pg", '-v', '-sg', '-gp')
    gps = Pontuar.objects.all().order_by('-gp', '-pg', '-v', '-sg')[:5]
    defesas = Pontuar.objects.all().order_by('gc', '-pg', '-v', '-sg')[:5]
    proxima_rodada_query = Jogo.objects.filter(placara=None).order_by('rodada')[:1]
    proxima_rodada = proxima_rodada_query[0].rodada
    print(proxima_rodada)
    

    for p in posicoes:
        unicode_time = unidecode(str(p.time.nome)).replace(" ","").replace("'","")
=======
    gols = Jogo.objects.values('rodada').annotate(Sum('gols_total'))

    posicoes = Pontuar.objects.all().order_by("-pg", '-v', '-sg', '-gp')
    gps = Pontuar.objects.all().order_by('-gp', '-pg', '-v', '-sg')

    for p in posicoes:
        unicode_time = unidecode(str(p.time)).replace(" ","").replace("'","")
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
        p.timeUnicode = unicode_time
    #limpa_jogos(jogos)
    #limpa_placar(posicoes)
    
    contexto = {
        'jogos': jogos,
        'posicoes': posicoes,
        'rod': range(1, 14),
        'gols': gols,
<<<<<<< HEAD
        'gps': gps,
        'defesas': defesas,
        'proxima_rodada': proxima_rodada
=======
        'gps': gps
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
    }
    return render(request, 'index.html', contexto)

def jogos(request):
    if not request.user.is_authenticated:
        return redirect('index')
    times = Time.objects.all()
    if request.method == 'POST':
        rodada = request.POST['rodada']
        timea = request.POST['timecasa']
        timeb = request.POST['timefora']
        contexto = {
            'times': times,
            'rodada': rodada,
            'timea': timea,
            'timeb': timeb
        }
        if rodada == '0' or rodada == '':
            messages.error(request, 'A rodada precisa ser preenchida')
            return render(request, 'jogos.html', contexto)
        if timea == "" or timeb == '':
            messages.error(request, 'Os dois times precisam ser preenchidos')
            return render(request, 'jogos.html', contexto)
        if timea == timeb:
            messages.error(
                request, 'Um time devieria enfrentar um adversário diferente não ele próprio.')
            return render(request, 'jogos.html', contexto)
        rodada = int(rodada)
        jogo_atual = Jogo.objects.create(
            rodada=rodada, timea=timea, timeb=timeb)
        jogo_atual.save()
        messages.success(request, 'Jogos cadastrado com sucesso')
        return render(request, 'jogos.html', contexto)
    contexto = {
        'times': times
    }
    return render(request, 'jogos.html', contexto)

def lista(request):
    jogos = Jogo.objects.all()
    for j in jogos:
        if j.placara == None:
            j.placara = ""
            j.placarb = ""
    contexto = {
        'jogos': jogos
    }
<<<<<<< HEAD
    return render(request, 'Lista.html', contexto)
=======
    return render(request, 'lista_jogos.html', contexto)
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0

def placar_jogos(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        chave = int(request.POST['id'])
        placara = request.POST['placara']
        placarb = request.POST['placarb']
        if not placara.isnumeric() or not placarb.isnumeric():
            messages.error(request, 'Colocar valores númericos inteiros no placar')
        placara = int(placara)
        placarb = int(placarb)
        jogo = get_object_or_404(Jogo, pk=chave)
        jogo.placara = placara
        jogo.placarb = placarb
        jogo.gols_total = placara + placarb
        jogo.save()

        id_casa = Time.objects.filter(nome=jogo.timea)[0].pk
        id_fora = Time.objects.filter(nome=jogo.timeb)[0].pk
        timecasa = get_object_or_404(Pontuar, time=id_casa)
        timefora = get_object_or_404(Pontuar, time=id_fora)
        if placara == placarb:
            if placara > 0:
                empate_gols(timecasa, timefora, placara, placarb)
            else:
                empate_zero(timecasa, timefora, placara, placarb)
        elif placara > placarb:
            vitoria_placara(timecasa, timefora, placara, placarb)
        else:
            vitoria_placarb(timecasa, timefora, placara, placarb)
    jogos = Jogo.objects.all()

    contexto = {
        'jogos': jogos
    }
    return render(request, 'placar_jogos.html', contexto)

def limpa_placar(pontuar):
    for t in pontuar:
        t.pg = 0
        t.j = 0
        t.v = 0
        t.e = 0
        t.d = 0
        t.gp = 0
        t.gc = 0
        t.sg = 0
        t.save()

def limpa_jogos(jogo):
    for j in jogo:
        j.placara = None
        j.placarb = None
        j.save()

def empate_gols(timecasa, timefora, placara, placarb):
    timecasa.j += 1
    timecasa.pg += 1
    timecasa.e +=1 
    timecasa.gp += placara
    timecasa.gc += placarb
    timecasa.save()
    # *****
    timefora.j += 1
    timefora.pg += 1
    timefora.e +=1 
    timefora.gp += placarb
    timefora.gc += placara
    timefora.save()

def empate_zero(timecasa, timefora, placara, placarb):
    timecasa.j += 1
    timecasa.pg += 1
    timecasa.e +=1 
    timecasa.save()
    # ****
    timefora.j += 1
    timefora.pg += 1
    timefora.e +=1 
    timefora.save()

def vitoria_placara(timecasa, timefora, placara, placarb):
    timecasa.j +=1
    timecasa.pg +=3
    timecasa.v +=1
    timecasa.gp += placara
    timecasa.gc += placarb
    timecasa.sg += (placara - placarb)
    timecasa.save()
    #******
    timefora.j +=1
    timefora.d +=1
    timefora.gp += placarb
    timefora.gc += placara
    timefora.sg -= (placara - placarb)
    timefora.save()

def vitoria_placarb(timecasa, timefora, placara, placarb):
    timefora.j +=1
    timefora.pg +=3
    timefora.v +=1
    timefora.gp += placarb
    timefora.gc += placara
    timefora.sg += (placarb - placara)
    timefora.save()
    #******
    timecasa.j +=1
    timecasa.d +=1
    timecasa.gp += placara
    timecasa.gc += placarb
    timecasa.sg -= (placarb - placara)
    timecasa.save()

def altera_nome_time(request, time, novo_nome):
    jogos = Jogo.objects.all()
    for j in jogos:
        if j.timea == time:
            j.timea = novo_nome

# def total_de_gols(jogos):
#     print(jogos)
#     for j in jogos:
#         if j.placara != None:
#             j.gols_total = (j.placara + j.placarb)
#         else:
#             j.gols_total = 0
#         j.save()
        
def pagtime(request, time_id):
    posicao = get_object_or_404(Pontuar, pk=time_id)
    time = get_object_or_404(Time, nome=posicao)
<<<<<<< HEAD
    
    time.urlfoto= 'img/'+ unidecode(str(time)).replace(" ","").replace("'","")+'.png'
=======
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
    jogos = Jogo.objects.filter(Q(timea=posicao) | Q(timeb=posicao.time))
    for j in jogos:
        if j.placara == None:
            j.placara = ""
            j.placarb = ""
    contexto = {
        'posicao': posicao,
        'time': time,
        'jogos': jogos
    }
<<<<<<< HEAD
    return render(request, 'pagtime.html', contexto)
=======
    return render(request, 'time.html', contexto)
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0

from django.db import models

# Create your models here.

class Time(models.Model):
    nome = models.CharField(("Nome"), max_length=30)
    nome_abr = models.CharField(("Apelido"), max_length=5)
<<<<<<< HEAD
    #logo = models.ImageField(("foto"), upload_to='fotos_time/%d/%m/%Y/', blank=True, null=True)
=======
    logo = models.ImageField(("foto"), upload_to='fotos_time', blank=True, null=True)
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
    cores =  models.CharField(("Cores"), max_length=30, blank=True)

    class Meta:
        ordering = ('nome',)
    def __str__(self):
        return self.nome

class Jogo(models.Model):
    TIMES = (
<<<<<<< HEAD
        ("Art Elétrica", "Art Elétrica"),
=======
        ("Arte Elétrica", "Arte Elétrica"),
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
        ("Dinos", "Dinos"),
        ("Empório Rebelo", "Empório Rebelo"),
        ("EuroBlack", "EuroBlack"),
        ("Flamengo", "Flamengo"),
        ("Juventude", "Juventude"),
        ("Kosminho", "Kosminho"),
        ("Levis", "Levis"),
        ("Os Pior", "Os Pior"),
        ("Paulista", "Paulista"),
        ("Salgueiro", "Salgueiro"),
        ("São Lucas", "São Lucas"),
        ("Vimec", "Vimec"),
        ("VKT", "VKT"),
    )
    rodada = models.IntegerField()
    num = models.IntegerField(blank=True, null=True)
    num2 = models.IntegerField(blank=True, null=True)
    timea = models.CharField(max_length=30, choices=TIMES)
    placara = models.IntegerField(null=True, blank=True)
    placarb = models.IntegerField(null=True, blank=True)
    timeb = models.CharField(max_length=30, choices=TIMES)
    gols_total = models.IntegerField(blank=True, null=True)
    class Meta:
        ordering= ('rodada',)
    def __str__(self):
        return str(self.rodada) + "ª - " + self.timea + " x " + self.timeb

class Pontuar(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    j = models.IntegerField(default=0)
    pg = models.IntegerField(default=0)
    v =  models.IntegerField(default=0)
    e =  models.IntegerField(default=0)
    d = models.IntegerField(default=0)
    gp = models.IntegerField(default=0)
    gc = models.IntegerField(default=0)
    sg = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Tabelas"
        verbose_name = "Time"
    def __str__(self):
        return self.time.nome



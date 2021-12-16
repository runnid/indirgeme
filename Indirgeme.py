# Verilenleri kullanarak G253H002-P1 noktaları arasında ölçülen eğik mesafeye;
# a) Atmosferik düzeltme getiriniz.
# b) Eğim ve yükseklik indirgemesi getiriniz.
# c) Deniz yüzeyine indirgenen mesafeyi projeksiyon düzlemine aktarınız.

#Atmosferik düzeltme getirme

Em= float(input("Eğik Mesafe Giriniz: "))
p = float(input("Basınç Giriniz: "))
t = float(input("Sıcaklık Giriniz: "))
R = float(input("R giriniz (metre cinsinden): "))
H = float(input("Yükseklik Giriniz: "))
Z = float(input("Düşey Açı Giriniz: "))

a = 0.003661
nGr = 1.0002931
n0 = 1.000290
n = float(1 + ((nGr - 1) / (1 + a * t)) * (p / 760))
N = float(n0 - n)

Kat= float(Em*N)
print("Kat= {}".format(Kat))
DR= float(Em+Kat)
print("DR= {}".format(DR))

#Eğik Mesafe ve Yükseklik İndirgemesi
import math
g=float(Z)
f=float((g*math.pi)/200)
e=float(math.sin(f))

Do = float(DR*e*((1-H/(R))))
print("Do= {}".format(Do))

#Projeksiyon Düzlemine Aktarma

P1Y = float(input("P1 noktasının sağa değerini giriniz: "))
P2Y = float(input("P2 noktasının sağa değerini giriniz: "))

Y1 = float(P1Y-500000)
Y2 = float(P2Y-500000)
YA = float((Y1**2)+(Y1*Y2)+(Y2**2))

Ip = float((YA*Do)/(6*R*R))
print("Ip= {}".format(Ip))
Dp = float(Ip+Do)
print("Dp= {}".format(Dp))




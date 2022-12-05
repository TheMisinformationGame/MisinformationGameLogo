A7=range
t=abs
s=len
r=enumerate
F=int
import math as A,numpy as O
from PIL import Image as P,ImageDraw as V
B=8192
Q=P.new('RGBA',(B,B))
a=V.Draw(Q)
H=F(0.025*B)
b=[H,H,B-1-H,B-1-H]
a.ellipse(b,fill='#FFFFFF')
I=P.new('L',(B,B))
W=V.Draw(I)
W.ellipse(b,fill=255)
C=(B-2*H)/2
c,d=B//2,B//2
R=2.0*A.pi/360.0
E=[(c+C*A.cos(B*R),d+C*A.sin(B*R))for B in A7(0,360,360//8)]
J=F(0.025*B)
for (A8,X) in r(E):
	for (A9,Y) in r(E):u=A.sqrt((X[0]-Y[0])**2+(X[1]-Y[1])**2);v=J+F(0.05*max(0.0,u-1.5*C));a.line([X,Y],fill='#000000',width=v)
w=O.array(Q)
e=O.array(I)
for f in A7(B):
	S=w[f];g=e[f];Z=(S[:,0]==0)&(S[:,1]==0)&(S[:,2]==0)&(S[:,3]==255);h=O.argmax(Z);i=s(Z)-1-O.argmax(Z[::-1])
	if h<i:g[:h]=0;g[i:]=0
I=P.fromarray(e,'L')
W=V.Draw(I)
for (j,x) in r(E):
	K,L=x;M,N=c-K,d-L;k=A.sqrt(M**2+N**2);y,z=M/k,N/k;A0,A1=E[(j-1)%s(E)];A2,A3=E[(j+1)%s(E)];D=A.atan2(A1-L,A0-K);G=A.atan2(A3-L,A2-K);C=0.1*B;l,m=K+C*A.cos(D),L+C*A.sin(D);A4,A5=K+C*A.cos(G),L+C*A.sin(G);D-=A.pi/2;G+=A.pi/2;n=A.sin(G)-A.sin(D);o=A.cos(G)-A.cos(D)
	if t(n)>t(o):T=(m-A5)/n
	else:T=(l-A4)/o
	p=l+A.cos(D)*T;q=m+A.sin(D)*T;U=t(T);J=F(0.02*B);M,N=-1.75*y*J,-1.75*z*J;W.arc([(F(p-U+M),F(q-U+N)),(F(p+U+M),F(q+U+N))],(D/R+540)%360,(G/R+540)%360,fill=0,width=J)
Q.putalpha(I)
A6=Q.resize((1024,1024),resample=P.Resampling.LANCZOS)
A6.save('out.png')
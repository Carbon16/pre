i='Painting & Decorating'
h='Gate'
g='Shop'
f='Expiry'
e='Date'
d=len
Z='n'
Y='Paid'
T='Volunteer'
N='y'
Q='Location'
P=KeyError
O=range
L='Surname'
K='Prename'
I=int
H=input
F=False
E=print
D=True
B='A'
A=str
from datetime import date
from pickle import FALSE
from re import I as j
import os
G={}
R={}
k=D
l=0
J=1
M=1
m=F
n=F
o=0
p=0
q=0
r=F
s=F
S=date.today()
V=S.strftime('%d/%m')
W=I(S.strftime('%y'))
a=W+1
U=D
X=D
t=[]
u=[]
def b(count):
	j='Please enter your surname:';c='Please enter your first name:';C=count;M=D
	while M==D:
		G[B+A(C)]={};J=F;O=F;P=F;R=H(c);S=H(j)
		while d(A(R))==0 or d(A(S))==0:E('Please enter your name.');R=H(c);S=H(j)
		G[B+A(C)][K]=R;G[B+A(C)][L]=S;G[B+A(C)][e]=V;G[B+A(C)][f]=a;b=H('Do you wish to volunteer? (y/n):')
		if b==N:
			while J==F:
				U=I(H('Where do you want to volunteer? \n1. Shop\n2. Gate\n3. Painting & Decorating\nSelect:'))
				if U==1:G[B+A(C)][T]=D;G[B+A(C)][Q]=g;J=D
				if U==2:G[B+A(C)][T]=D;G[B+A(C)][Q]=h;J=D
				if U==3:G[B+A(C)][T]=D;G[B+A(C)][Q]=i;J=D
		while O==F:
			W=H('Has user paid the fee? (y/n):')
			if W==N:G[B+A(C)][Y]=D;O=D
			if W==Z:G[B+A(C)][Y]=F;O=D
		while P==F:
			X=H('Add new member? (y/n):')
			if X==N:M=D;P=D;C=C+1;return C
			if X==Z:M=F;C=C+1;P=D;E('Goodbye');return C
			else:E('Please enter only y or n')
	return G
def U(member):
	R='**End**';N=', ';M='Name: ';G=member;X=D;Z=F;a=F;b=F
	while X==D:
		while Z==F:
			U=I(H('What do you want to search? \n1. Voulenteers\n2. Expired\n3. Not paid\nSelect:'))
			if U==1:
				S=I(H('What do you want to search? \n1. Gate\n2. Shop\n3. Painting\n4. All\nSelect:'))
				if S==1:
					for C in O(1,I(J+5)):
						try:
							if G[B+A(C)][Q]==h:E(M+A(G[B+A(C)][L])+N+A(G[B+A(C)][K]))
						except P:E(R)
				if S==2:
					try:
						for C in O(1,I(J+5)):
							if G[B+A(C)][Q]==g:E(M+A(G[B+A(C)][L])+N+A(G[B+A(C)][K]))
					except P:E(R)
				if S==3:
					try:
						for C in O(1,I(J+5)):
							if G[B+A(C)][Q]==i:E(M+A(G[B+A(C)][L])+N+A(G[B+A(C)][K]))
					except P:E(R)
				if S==4:
					try:
						for C in O(1,I(J+5)):
							if G[B+A(C)][T]==D:E(M+A(G[B+A(C)][L])+N+A(G[B+A(C)][K]))
					except P:E(R)
			if U==2:
				try:
					for C in O(1,I(J+5)):
						if G[B+A(C)][e]>V and G[B+A(C)][f]>W:E(M+A(G[B+A(C)][L])+N+A(G[B+A(C)][K]))
				except P:E(R)
			if U==3:
				try:
					for C in O(1,I(J+5)):
						E(M+A(G[B+A(C)][L])+N+A(G[B+A(C)][K]))
						if G[B+A(C)][Y]==F:E(M+A(G[B+A(C)][L])+N+A(G[B+A(C)][K]))
				except P:E(R)
def c(spons):
	C=spons;G=D;B=F;global M
	while G==D:
		while B==F:
			E('PLEASE BE AWARE THAT THIS SPONSORSHIP WILL COST $200');I=H('Please enter your name:');J=H('Please enter the message you would like:');E('PLEASE CONFIRM THE FOLLOWING DETAILS ARE CORRECT');E('Name:'+I+' | Message:'+J);K=A(H('Please confirm (y/n):'))
			if K==N:C.update({M:[A(I),A(J)]});E('Sponsorship sucess!');G=F;B=D;M=M+1
			if K==Z:E('Please try again');B=F
	return C
while X==D:
	C=I(H('1. Add new member\n2. Get a member\n3. Sponsor\n4. Display sponsors\n5. EXIT\nSELECT: '))
	if C==1:b(J)
	if C==2:U(G)
	if C==3:c(R)
	if C==4:E(R)
	if C==5:X=F;E('Goodbye!')
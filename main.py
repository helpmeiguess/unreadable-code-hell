J=input;G=len;H=open(J(),'r');I=H.read();F=[]
for A in I:F.append(A)
B=0;C=[];D=[];E=0
for A in range(1,100):C.append(0)
while G(F)>E:
	A=F[E];E+=1
	C[B]+=1 if A=='+'else -1 if A=='-'else 0
	B-=1 if A=='<'else -1 if A=='>'else 0
	if A=='.':print(chr(C[B]))
	if A==',':C[B]=ord(J())
	if A=='[':D.append(E)
	if A==']'and C[B]==0:D.pop(G(D)-1)
	elif A==']':E=D[G(D)-1]
